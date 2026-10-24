"""Connect pip (and later uv) to your company's JFrog Artifactory PyPI repository - without the token ever
appearing on screen or in a chat.

Run it in YOUR OWN terminal (it waits for you to press Enter):
    py -3.12 "%USERPROFILE%\\Personal_Learning\\00_Progress_Tracker\\tools\\setup_jfrog_pip.py"

Before running: JFrog -> Set Me Up -> PyPI -> pick the repository your company docs tell you to use -> Client: Pip ->
Configure -> Generate token -> Generate Token & Create Instructions -> click the copy icon next to the configuration.

What it does:
  1. Reads the copied text from your clipboard, finds the index URL, then clears the clipboard.
     (Nothing usable on the clipboard? It asks you to paste the line instead - your typing stays hidden.)
  2. Writes %APPDATA%\\pip\\pip.ini with that index URL plus `trusted-host = <that host>` (needed behind a
     TLS-inspecting company proxy; it covers only the repository host). An existing file is backed up first.
  3. Proves it works: installs `requests` into a throwaway virtual environment, then deletes it.
  4. Tells you whether `uv` is available through JFrog.

After installing uv later:  py -3.12 setup_jfrog_pip.py --uv
  -> writes %APPDATA%\\uv\\uv.toml with the index URL WITHOUT credentials, then stores your username and token with
     `uv auth login` (token passed via stdin, never shown). No new token needed - it reuses the one in pip.ini.
The token is never printed. To revoke a token: JFrog -> your user profile -> Identity Tokens.
"""
import argparse
import configparser
import ctypes
import datetime
import getpass
import os
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit, urlunsplit

URL_RE = re.compile(r"https://[^\s\"'<>`]+/api/pypi/[^\s\"'<>`]+")


def extract_url(text):
    """Return the first JFrog PyPI index URL found in text (normalised to end with /simple), else None."""
    m = URL_RE.search(text or "")
    if not m:
        return None
    url = m.group(0).rstrip(".,;)")
    if not url.rstrip("/").endswith("/simple"):
        url = url.rstrip("/") + "/simple"
    return url


def split_credentials(url):
    """-> (username, token, url_without_credentials, host)."""
    parts = urlsplit(url)
    clean = urlunsplit((parts.scheme, parts.hostname + (":%d" % parts.port if parts.port else ""), parts.path, parts.query, parts.fragment))
    return parts.username, parts.password, clean, parts.hostname


def mask(text, url=None):
    text = re.sub(r"(https://[^:/@\s]+:)[^@\s]+@", r"\1****@", text or "")
    if url:
        token = split_credentials(url)[1]
        if token:
            text = text.replace(token, "****")
    return text


# ---------------------------------------------------------------- clipboard (Windows, stdlib only)
def _clipboard_api():
    if os.name != "nt":
        return None
    from ctypes import wintypes
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    user32.OpenClipboard.argtypes = [wintypes.HWND]
    user32.OpenClipboard.restype = wintypes.BOOL
    user32.GetClipboardData.argtypes = [wintypes.UINT]
    user32.GetClipboardData.restype = wintypes.HANDLE
    user32.EmptyClipboard.restype = wintypes.BOOL
    user32.CloseClipboard.restype = wintypes.BOOL
    kernel32.GlobalLock.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalLock.restype = wintypes.LPVOID
    kernel32.GlobalUnlock.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalUnlock.restype = wintypes.BOOL
    return user32, kernel32


def read_clipboard():
    api = _clipboard_api()
    if not api:
        return ""
    user32, kernel32 = api
    if not user32.OpenClipboard(None):
        return ""
    try:
        handle = user32.GetClipboardData(13)  # CF_UNICODETEXT
        if not handle:
            return ""
        ptr = kernel32.GlobalLock(handle)
        if not ptr:
            return ""
        try:
            return ctypes.wstring_at(ptr)
        finally:
            kernel32.GlobalUnlock(handle)
    finally:
        user32.CloseClipboard()


def clear_clipboard():
    api = _clipboard_api()
    if api and api[0].OpenClipboard(None):
        try:
            api[0].EmptyClipboard()
        finally:
            api[0].CloseClipboard()


def drain_console():
    """Discard leftover pasted lines so they don't run as commands after the script exits."""
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getwch()
    except Exception:
        pass


def looks_like_template(text):
    return "api/pypi" in (text or "") and re.search(r"<\s*(user|username|token|password)\s*>", text, re.I) is not None


def get_url_interactively():
    input("In JFrog, copy the configuration (Client: Pip, after 'Generate Token & Create Instructions'), then press Enter here... ")
    clip = read_clipboard()
    url = extract_url(clip)
    if url and split_credentials(url)[1]:
        clear_clipboard()
        print("Found the index URL on your clipboard. (Clipboard cleared.)")
        return url
    if looks_like_template(clip):
        print("The clipboard has the template WITHOUT your token. In JFrog choose 'Generate token', click "
              "'Generate Token & Create Instructions', copy again, and re-run this script.")
        sys.exit(1)
    print("No JFrog PyPI address with a token found on the clipboard.")
    for _ in range(3):
        line = getpass.getpass("Paste the line that contains the index URL (it stays hidden), then press Enter: ")
        url = extract_url(line)
        drain_console()
        if url and split_credentials(url)[1]:
            return url
        print("That line had no address like https://<user>:<token>@<host>/artifactory/api/pypi/<repo>/simple - try again.")
    sys.exit("Stopped: no index URL received. Nothing was changed.")


# ---------------------------------------------------------------- pip config + test
def backup(path):
    if os.path.exists(path):
        saved = path + ".bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(path, saved)
        print("Backed up your existing", os.path.basename(path), "to", saved)


def write_pip_ini(url, path, truststore=False, make_backup=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if make_backup:
        backup(path)
    host = split_credentials(url)[3]
    lines = ["[global]", "index-url = " + url, "trusted-host = " + host]
    if truststore:
        lines.append("use-feature = truststore")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


def venv_python(venv_dir):
    if os.name == "nt":
        return os.path.join(venv_dir, "Scripts", "python.exe")
    return os.path.join(venv_dir, "bin", "python")


def pip_run(vpy, args, env):
    r = subprocess.run([vpy, "-m", "pip", *args], capture_output=True, text=True, env=env)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def explain_failure(out):
    low = out.lower()
    if "401" in out or "unauthorized" in low or "user for" in low:
        return ("JFrog refused the login (401). Generate the instructions again with 'Generate Token & Create "
                "Instructions' (Client: Pip), copy them, and re-run this script.")
    if "403" in out or "forbidden" in low:
        return ("Access denied (403). Your account may not have read access to this repository, or the package is "
                "blocked by JFrog Curation. Check your company docs for which PyPI repository to use.")
    if "no matching distribution" in low or "could not find a version" in low:
        return "The repository answered, but had no 'requests' package. Check which PyPI repository you selected."
    if "certificate_verify_failed" in low or "sslerror" in low:
        return "Certificate error. Follow your company's guide for trusting the proxy certificate."
    return "Unexpected error - the last lines are shown above (token hidden)."


def setup_pip(url, pip_ini):
    print("Repository address:", mask(url, url))
    write_pip_ini(url, pip_ini)
    print("Saved", pip_ini, "(index-url + trusted-host for the repository host)")

    env = dict(os.environ, PIP_CONFIG_FILE=pip_ini, PIP_DISABLE_PIP_VERSION_CHECK="1", PIP_NO_INPUT="1")
    tmp = tempfile.mkdtemp(prefix="jfrog-pip-check-")
    try:
        print("Testing: creating a throwaway virtual environment and installing 'requests' through JFrog...")
        subprocess.run([sys.executable, "-m", "venv", os.path.join(tmp, "venv")], check=True)
        vpy = venv_python(os.path.join(tmp, "venv"))
        args = ["install", "--timeout", "30", "--retries", "1", "requests"]
        code, out = pip_run(vpy, args, env)
        if code != 0 and ("CERTIFICATE_VERIFY_FAILED" in out or "SSLError" in out):
            print("Certificate problem - letting pip also trust the Windows certificate store and retrying...")
            write_pip_ini(url, pip_ini, truststore=True, make_backup=False)
            code, out = pip_run(vpy, args, env)
        if code != 0:
            print("\n".join(mask(out, url).strip().splitlines()[-12:]))
            print("\n[FAILED] " + explain_failure(out))
            print("Your pip.ini was kept so you can inspect it; re-running this script replaces it.")
            return False
        print("[OK] pip works through JFrog: 'requests' installed successfully.")

        code, out = pip_run(vpy, ["index", "versions", "uv"], env)
        m = re.search(r"^uv \(([^)]+)\)", out, re.M)
        if code == 0 and m:
            print("[OK] uv is available through JFrog (latest %s). To install it for your user:" % m.group(1))
            print("     py -3.12 -m pip install --user uv")
            print("     then add the folder pip prints to your user PATH, open a new terminal, and run:")
            print('     py -3.12 "%s" --uv' % os.path.abspath(__file__))
        else:
            print("[INFO] uv was not found through JFrog - keep using pip + venv (or request uv from IT).")
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------- uv config (index without credentials + uv auth login)
def setup_uv(pip_ini, uv_toml, uv_exe=None):
    cp = configparser.ConfigParser(interpolation=None)
    cp.read(pip_ini, encoding="utf-8")
    url = cp.get("global", "index-url", fallback=None)
    if not url:
        sys.exit("No index-url found in %s - run this script without --uv first." % pip_ini)
    user, token, clean_url, host = split_credentials(url)
    if "'" in clean_url:
        sys.exit("The index URL contains a quote character; please set up uv manually.")
    os.makedirs(os.path.dirname(uv_toml), exist_ok=True)
    backup(uv_toml)
    with open(uv_toml, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Written by setup_jfrog_pip.py: uv uses your company's JFrog PyPI repository and Company Portal Python.\n")
        fh.write("# Credentials are NOT stored here - they were saved with `uv auth login`.\n")
        fh.write("native-tls = true\n")
        fh.write('python-preference = "only-system"\n')
        fh.write('python-downloads = "never"\n\n')
        fh.write("[[index]]\n")
        fh.write('name = "artifactory"\n')
        fh.write("url = '%s'\n" % clean_url)
        fh.write("default = true\n")
    print("Saved", uv_toml, "->", clean_url, "(no credentials in this file)")

    uv = uv_exe or shutil.which("uv")
    if not uv:
        print("[INFO] 'uv' is not on your PATH yet. After installing it, run this command again.")
        return False
    if not (user and token):
        print("[INFO] pip.ini has no username/token, so nothing to store. Run: uv auth login %s" % host)
        return False
    r = subprocess.run([uv, "auth", "login", host, "--username", user, "--password", "-"],
                       input=token, capture_output=True, text=True)
    if r.returncode != 0:
        print(mask((r.stdout or "") + (r.stderr or ""), url))
        print("[FAILED] 'uv auth login' did not work - see the message above.")
        return False
    print("[OK] Credentials stored with 'uv auth login' for", host)
    print("Test it:  uv venv --python 3.12 C:\\dev\\uv-check  then  uv pip install --python C:\\dev\\uv-check requests")
    return True


def main():
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~")
    p = argparse.ArgumentParser(description="Connect pip (and uv) to your company's JFrog PyPI repository.")
    p.add_argument("--uv", action="store_true", help="configure uv from your pip.ini (after installing uv)")
    p.add_argument("--test-url", help=argparse.SUPPRESS)
    p.add_argument("--pip-ini", default=os.path.join(appdata, "pip", "pip.ini"), help=argparse.SUPPRESS)
    p.add_argument("--uv-toml", default=os.path.join(appdata, "uv", "uv.toml"), help=argparse.SUPPRESS)
    p.add_argument("--uv-exe", help=argparse.SUPPRESS)
    a = p.parse_args()
    if a.uv:
        ok = setup_uv(a.pip_ini, a.uv_toml, a.uv_exe)
        sys.exit(0 if ok else 1)
    url = a.test_url or get_url_interactively()
    ok = setup_pip(url, a.pip_ini)
    print("\nDone. Tell your AI mentor 'N4 done'." if ok else "\nNot done yet - see the message above.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
