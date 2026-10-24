"""Connect pip (and later uv) to your company's JFrog Artifactory PyPI repository - without the token ever
appearing on screen or in a chat.

Run it in YOUR OWN terminal (it waits for you to press Enter):
    py -3.12 "%USERPROFILE%\\Personal_Learning\\00_Progress_Tracker\\tools\\setup_jfrog_pip.py"

Before running: JFrog -> Set Me Up -> PyPI -> Client: Pip -> Configure -> Generate Token & Create Instructions,
then click the copy icon next to the configuration (or select the line with the index URL and press Ctrl+C).

What it does:
  1. Reads the copied text from your clipboard, finds the index URL, then clears the clipboard.
     (Nothing usable on the clipboard? It asks you to paste the line instead - your typing stays hidden.)
  2. Saves it in %APPDATA%\\pip\\pip.ini (an existing file is backed up first).
  3. Proves it works: installs `requests` into a throwaway virtual environment, then deletes it.
  4. Tells you whether `uv` is available through JFrog.

After installing uv later:  py -3.12 setup_jfrog_pip.py --uv   -> writes %APPDATA%\\uv\\uv.toml from pip.ini (no new token).
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


def token_of(url):
    m = re.match(r"https://[^:/@]+:([^@]+)@", url or "")
    return m.group(1) if m else None


def mask(text, url=None):
    text = re.sub(r"(https://[^:/@\s]+:)[^@\s]+@", r"\1****@", text or "")
    tok = token_of(url)
    if tok:
        text = text.replace(tok, "****")
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


def get_url_interactively():
    input("In JFrog, copy the configuration (Client: Pip), then press Enter here... ")
    url = extract_url(read_clipboard())
    if url:
        clear_clipboard()
        print("Found the index URL on your clipboard. (Clipboard cleared.)")
        return url
    print("No JFrog PyPI address found on the clipboard.")
    for _ in range(3):
        line = getpass.getpass("Paste the line that contains the index URL (it stays hidden), then press Enter: ")
        url = extract_url(line)
        drain_console()
        if url:
            return url
        print("That line had no address like https://<user>:<token>@<host>/artifactory/api/pypi/<repo>/simple - try again.")
    sys.exit("Stopped: no index URL received. Nothing was changed.")


# ---------------------------------------------------------------- pip config + test
def write_pip_ini(url, path, truststore=False, backup=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if backup and os.path.exists(path):
        saved = path + ".bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(path, saved)
        print("Backed up your existing pip.ini to", saved)
    lines = ["[global]", "index-url = " + url]
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
                "blocked by JFrog Curation. Ask your team which PyPI repository to use.")
    if "no matching distribution" in low or "could not find a version" in low:
        return "The repository answered, but had no 'requests' package. Ask your team which PyPI repository to use."
    if "certificate_verify_failed" in low or "sslerror" in low:
        return "Certificate error even with the Windows certificate store. Ask your team for the company CA bundle."
    return "Unexpected error - the last lines are shown above (token hidden)."


def setup_pip(url, pip_ini):
    if "@" not in url.split("/api/pypi/")[0]:
        print("Warning: this address has no 'user:token@' part, so JFrog will probably refuse it.")
    print("Repository address:", mask(url, url))
    write_pip_ini(url, pip_ini)
    print("Saved", pip_ini)

    env = dict(os.environ, PIP_CONFIG_FILE=pip_ini, PIP_DISABLE_PIP_VERSION_CHECK="1", PIP_NO_INPUT="1")
    tmp = tempfile.mkdtemp(prefix="jfrog-pip-check-")
    try:
        print("Testing: creating a throwaway virtual environment and installing 'requests' through JFrog...")
        subprocess.run([sys.executable, "-m", "venv", os.path.join(tmp, "venv")], check=True)
        vpy = venv_python(os.path.join(tmp, "venv"))
        args = ["install", "--timeout", "30", "--retries", "1", "requests"]
        code, out = pip_run(vpy, args, env)
        if code != 0 and ("CERTIFICATE_VERIFY_FAILED" in out or "SSLError" in out):
            print("Certificate problem - switching pip to the Windows certificate store and retrying...")
            write_pip_ini(url, pip_ini, truststore=True, backup=False)
            code, out = pip_run(vpy, args, env)
        if code != 0:
            print("\n".join(mask(out, url).strip().splitlines()[-12:]))
            print("\n[FAILED] " + explain_failure(out))
            print("Your pip.ini was kept so you can see it; re-running this script replaces it.")
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


# ---------------------------------------------------------------- uv config
def setup_uv(pip_ini, uv_toml):
    cp = configparser.ConfigParser(interpolation=None)
    cp.read(pip_ini, encoding="utf-8")
    url = cp.get("global", "index-url", fallback=None)
    if not url:
        sys.exit("No index-url found in %s - run this script without --uv first." % pip_ini)
    if "'" in url:
        sys.exit("The index URL contains a quote character; please set up uv manually.")
    os.makedirs(os.path.dirname(uv_toml), exist_ok=True)
    if os.path.exists(uv_toml):
        saved = uv_toml + ".bak-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(uv_toml, saved)
        print("Backed up your existing uv.toml to", saved)
    with open(uv_toml, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Written by setup_jfrog_pip.py: uv uses your company's JFrog PyPI repository and Company Portal Python\n")
        fh.write("native-tls = true\n")
        fh.write('python-preference = "only-system"\n')
        fh.write('python-downloads = "never"\n\n')
        fh.write("[[index]]\n")
        fh.write("url = '%s'\n" % url)
        fh.write("default = true\n")
    print("Saved", uv_toml, "->", mask(url, url))
    print("Test it:  uv venv C:\\dev\\uv-check  then  uv pip install --python C:\\dev\\uv-check requests")


def main():
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~")
    p = argparse.ArgumentParser(description="Connect pip (and uv) to your company's JFrog PyPI repository.")
    p.add_argument("--uv", action="store_true", help="write %%APPDATA%%\\uv\\uv.toml from your pip.ini (after installing uv)")
    p.add_argument("--test-url", help=argparse.SUPPRESS)
    p.add_argument("--pip-ini", default=os.path.join(appdata, "pip", "pip.ini"), help=argparse.SUPPRESS)
    p.add_argument("--uv-toml", default=os.path.join(appdata, "uv", "uv.toml"), help=argparse.SUPPRESS)
    a = p.parse_args()
    if a.uv:
        setup_uv(a.pip_ini, a.uv_toml)
        return
    url = a.test_url or get_url_interactively()
    ok = setup_pip(url, a.pip_ini)
    print("\nDone. Tell your AI mentor 'N4 done'." if ok else "\nNot done yet - see the message above.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
