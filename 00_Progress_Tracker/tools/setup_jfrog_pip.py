"""Connect pip (and later uv) to your company's JFrog Artifactory PyPI repository - without the token ever
appearing on screen or in a chat.

Run it FIRST, in your own terminal - it then waits while you copy the configuration in JFrog:
    py -3.12 "%USERPROFILE%\\Personal_Learning\\00_Progress_Tracker\\tools\\setup_jfrog_pip.py" [--repo NAME]

Then in JFrog: Set Me Up -> PyPI -> repository -> Client: Pip -> Configure -> Generate token ->
Generate Token & Create Instructions -> click the copy icon on the configuration box. The script notices the copy by
itself. (You can also paste the text into its window; nothing is shown while you paste.)

JFrog's instructions mention ~/.pip/pip.conf - the Linux/macOS location. pip on Windows reads %APPDATA%\\pip\\pip.ini
(check with `py -3.12 -m pip config debug`), which is where this script writes.

What it does:
  1. Waits until your clipboard (or a paste) holds the index URL with your token, then clears the clipboard.
  2. Writes %APPDATA%\\pip\\pip.ini with that index URL plus `trusted-host = <that host>` (needed behind a
     TLS-inspecting company proxy; it covers only the repository host). An existing file is backed up first.
     --repo NAME uses repository NAME instead of the one in the copied address (for example the shared repository
     your company docs name). If JFrog refuses NAME, it falls back to the copied repository, so the token isn't wasted.
  3. Proves it works: installs `requests` into a throwaway virtual environment, then deletes it.
  4. Tells you whether `uv` is available through JFrog.

After installing uv later:  py -3.12 setup_jfrog_pip.py --uv
  -> writes %APPDATA%\\uv\\uv.toml with the index URL WITHOUT credentials, then stores your username and token with
     `uv auth login` (token passed via stdin, never shown). No new token needed - it reuses the one in pip.ini.
The token is never printed. Never screenshot or share JFrog's configuration box - it shows the token.
To revoke a token: JFrog -> profile icon -> Edit Profile -> Identity Tokens -> x on the token's row -> Revoke.
"""
import argparse
import configparser
import ctypes
import datetime
import functools
import getpass
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
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
    text = re.sub(r"(https?://[^:/@\s]+:)[^@\s]+@", r"\1****@", text or "")
    if url:
        token = split_credentials(url)[1]
        if token:
            text = text.replace(token, "****")
    return text


REF_TOKEN_RE = re.compile(r"cmVmd[A-Za-z0-9]{59}")  # JFrog reference token: 'cmVmd' + 59 letters/digits

HINTS = {
    "template": "That copy has no token in it. Click 'Generate token', then 'Generate Token & Create Instructions', "
                "and copy again.",
    "no-token": "That address has no username and token. Copy the instructions shown after 'Generate Token & Create "
                "Instructions'.",
    "cut-token": "The token looks cut off (JFrog tokens are 64 characters). Use JFrog's copy icon instead of "
                 "selecting the text.",
    "own-command": "That was this script's own command, not the JFrog text.",
}


def find_index_url(text):
    """-> (url, None) if text holds a complete index URL with username and token, else (None, reason or None)."""
    url = extract_url(text)
    if not url:
        if looks_like_template(text):
            return None, "template"
        if "setup_jfrog_pip" in (text or ""):
            return None, "own-command"
        return None, None
    user, token = split_credentials(url)[:2]
    if not (user and token):
        return None, "no-token"
    if token.startswith("cmVmd") and not REF_TOKEN_RE.fullmatch(token):
        return None, "cut-token"
    return url, None


def repo_of(url):
    m = re.search(r"/api/pypi/([^/]+)/simple/?$", url)
    return m.group(1) if m else "?"


def with_repo(url, repo):
    return re.sub(r"(/api/pypi/)[^/]+(/simple/?)$", lambda m: m.group(1) + repo + m.group(2), url, count=1)


# ---------------------------------------------------------------- clipboard (Windows, stdlib only)
@functools.lru_cache(maxsize=None)
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
    user32.GetClipboardSequenceNumber.restype = wintypes.DWORD
    kernel32.GlobalLock.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalLock.restype = wintypes.LPVOID
    kernel32.GlobalUnlock.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalUnlock.restype = wintypes.BOOL
    return user32, kernel32


def _open_clipboard(user32):
    for _ in range(10):  # another app may hold it for a moment
        if user32.OpenClipboard(None):
            return True
        time.sleep(0.03)
    return False


def read_clipboard():
    """Clipboard text ("" if none), or None if the clipboard could not be opened."""
    api = _clipboard_api()
    if not api:
        return ""
    user32, kernel32 = api
    if not _open_clipboard(user32):
        return None
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
    if api and _open_clipboard(api[0]):
        try:
            api[0].EmptyClipboard()
        finally:
            api[0].CloseClipboard()


def clipboard_seq():
    """Changes whenever anything is copied (0 if unknown)."""
    api = _clipboard_api()
    return api[0].GetClipboardSequenceNumber() if api else 0


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


def console_keys():
    """(kbhit, getwch) to read pasted text without showing it, or None outside a Windows console."""
    if os.name != "nt":
        return None
    try:
        import msvcrt
        return (msvcrt.kbhit, msvcrt.getwch) if sys.stdin.isatty() else None
    except Exception:
        return None


class HiddenLineReader:
    """Collects typed or pasted characters (never shown) into lines."""

    def __init__(self):
        self.buf, self.skip_next = [], False

    def feed(self, ch):
        if self.skip_next:  # second half of an arrow/function key
            self.skip_next = False
            return None
        if ch in ("\x00", "\xe0"):
            self.skip_next = True
            return None
        if ch == "\x03":
            raise KeyboardInterrupt
        if ch in ("\r", "\n"):
            line, self.buf = "".join(self.buf), []
            return line
        if ch == "\x08":
            if self.buf:
                self.buf.pop()
        elif ch == "\x1b":
            self.buf = []
        else:
            self.buf.append(ch)
        return None


def wait_for_index_url(timeout=900, poll=0.3, keys=None, read_clip=None, clip_seq=None, say=print):
    """Watch the clipboard (and pasted input) until it holds the index URL with a token.
    -> (url, 'clipboard' | 'paste'), or (None, None) after the timeout. keys=False turns pasting off."""
    read_clip = read_clip or read_clipboard
    clip_seq = clip_seq or clipboard_seq
    keys = console_keys() if keys is None else (keys or None)
    reader, said, last_seq = HiddenLineReader(), set(), None
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        seq = clip_seq()
        if not seq or seq != last_seq:
            text = read_clip()
            if text is not None:  # None = clipboard busy; try again next round
                last_seq = seq
                url, reason = find_index_url(text)
                if url:
                    clear_clipboard()
                    return url, "clipboard"
                if reason in ("template", "no-token", "cut-token") and reason not in said:
                    said.add(reason)
                    say(HINTS[reason])
        while keys and keys[0]():
            line = reader.feed(keys[1]())
            if line is None:
                continue
            url, reason = find_index_url(line)
            if url:
                if split_credentials(url)[1] in (read_clip() or ""):
                    clear_clipboard()
                return url, "paste"
            text = line.strip()
            if text and not text.startswith("[") and not text.endswith("="):  # skip the block's other lines
                say(HINTS.get(reason) or "That line had no JFrog address - still waiting for the copy from JFrog.")
        time.sleep(poll)
    return None, None


def paste_with_getpass():
    """Fallback when neither the clipboard nor the console can be watched."""
    for _ in range(6):
        line = getpass.getpass("Paste the line with the index URL (hidden), then press Enter: ")
        url, reason = find_index_url(line)
        if url:
            return url
        if line.strip() and not line.strip().startswith("["):
            print(HINTS.get(reason) or "That line had no JFrog address - try again.")
    sys.exit("Stopped: no index URL received. Nothing was changed.")


def get_url_interactively():
    keys = console_keys()
    if not _clipboard_api() and not keys:
        return paste_with_getpass()
    print("Waiting for the configuration from JFrog... (Ctrl+C cancels)")
    print("  JFrog: Set Me Up -> PyPI -> Client: Pip -> Configure -> Generate token ->")
    print("         'Generate Token & Create Instructions' -> click the copy icon on the configuration box.")
    print("  This window notices the copy by itself%s." % (" (or paste it here - nothing is shown)" if keys else ""))
    print("  Never screenshot or share that box: it shows your token.")
    try:
        url, source = wait_for_index_url(keys=keys or False)
    except KeyboardInterrupt:
        drain_console()
        sys.exit("\nCancelled. Nothing was changed.")
    drain_console()
    if not url:
        sys.exit("Stopped: nothing usable arrived from JFrog within 15 minutes. Nothing was changed.")
    print("Got the JFrog address from your %s." % ("clipboard (clipboard cleared)" if source == "clipboard" else "paste"))
    return url


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


def classify(out):
    """Sort a failed `pip -vv` run: auth / cert / forbidden / notfound / other."""
    low = out.lower()
    codes = set(re.findall(r"\b(40[134]) client error", low)) | set(re.findall(r'http/1\.[01]" (40[134])\b', low))
    if "401" in codes or "credentials not correct" in low:
        return "auth"
    if "certificate_verify_failed" in low or "sslerror" in low:
        return "cert"
    if "403" in codes:
        return "forbidden"
    if "404" in codes or "no matching distribution" in low or "could not find a version" in low:
        return "notfound"
    return "other"


EXPLAIN = {
    "auth": "JFrog refused the token (401): it is wrong, revoked or expired. Run this script again and generate a new "
            "token in JFrog while it waits.",
    "cert": "Certificate error. Follow your company's guide for trusting the proxy certificate.",
    "forbidden": "Access denied (403): no read access to this repository, or the package is blocked by JFrog Curation. "
                 "Check your company docs for which PyPI repository to use.",
    "notfound": "The repository doesn't exist or has no 'requests' package. Check the repository name.",
    "other": "Unexpected error - see the lines above (token hidden).",
}


def key_lines(out, url, limit=8):
    keep = [ln for ln in out.splitlines() if re.search(r"error|could not fetch|ssl|timed out|retrying", ln, re.I)]
    return "\n".join(mask(ln, url)[:220] for ln in (keep[-limit:] or out.strip().splitlines()[-limit:]))


def try_install(vpy, url, pip_ini, env, make_backup):
    """Write pip.ini for url, then install 'requests' through it. -> (ok, kind, pip output)."""
    write_pip_ini(url, pip_ini, make_backup=make_backup)
    args = ["install", "-vv", "--no-cache-dir", "--timeout", "30", "--retries", "1", "requests"]
    code, out = pip_run(vpy, args, env)
    if code != 0 and ("CERTIFICATE_VERIFY_FAILED" in out or "SSLError" in out):
        print("Certificate problem - letting pip also trust the Windows certificate store and retrying...")
        write_pip_ini(url, pip_ini, truststore=True, make_backup=False)
        code, out = pip_run(vpy, args, env)
    return code == 0, (None if code == 0 else classify(out)), out


def setup_pip(url, pip_ini, prefer_repo=None):
    candidates = [with_repo(url, prefer_repo)] if prefer_repo else []
    if url not in candidates:
        candidates.append(url)
    env = dict(os.environ, PIP_CONFIG_FILE=pip_ini, PIP_DISABLE_PIP_VERSION_CHECK="1", PIP_NO_INPUT="1")
    tmp = tempfile.mkdtemp(prefix="jfrog-pip-check-")
    try:
        print("Testing: creating a throwaway virtual environment and installing 'requests' through JFrog...")
        subprocess.run([sys.executable, "-m", "venv", os.path.join(tmp, "venv")], check=True)
        vpy = venv_python(os.path.join(tmp, "venv"))
        for i, cand in enumerate(candidates):
            print("Repository '%s': %s" % (repo_of(cand), mask(cand, cand)))
            ok, kind, out = try_install(vpy, cand, pip_ini, env, make_backup=(i == 0))
            if ok:
                break
            if kind not in ("auth", "cert") and i + 1 < len(candidates):
                print("[INFO] '%s' didn't work (%s) - trying '%s', the repository you copied..."
                      % (repo_of(cand), kind, repo_of(candidates[i + 1])))
                continue
            print(key_lines(out, cand))
            print("\n[FAILED] " + EXPLAIN[kind])
            print("Your pip.ini was kept so you can inspect it; re-running this script replaces it.")
            return False
        print("Saved", pip_ini, "(index-url + trusted-host for the repository host)")
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
    p.add_argument("--repo", help="use this repository instead of the one in the copied address "
                                  "(falls back to the copied one if JFrog refuses it)")
    p.add_argument("--test-url", help=argparse.SUPPRESS)
    p.add_argument("--pip-ini", default=os.path.join(appdata, "pip", "pip.ini"), help=argparse.SUPPRESS)
    p.add_argument("--uv-toml", default=os.path.join(appdata, "uv", "uv.toml"), help=argparse.SUPPRESS)
    p.add_argument("--uv-exe", help=argparse.SUPPRESS)
    a = p.parse_args()
    if a.repo and not re.fullmatch(r"[A-Za-z0-9._-]+", a.repo):
        p.error("--repo takes a repository name, like my-python-virtual")
    if a.uv:
        ok = setup_uv(a.pip_ini, a.uv_toml, a.uv_exe)
        sys.exit(0 if ok else 1)
    if a.repo:
        print("Preferred repository: %s (falls back to the one you copy if JFrog refuses it)" % a.repo)
    url = a.test_url or get_url_interactively()
    ok = setup_pip(url, a.pip_ini, a.repo)
    print("\nDone. Tell your AI mentor 'N4 done'." if ok else "\nNot done yet - see the message above.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
