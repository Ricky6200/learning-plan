"""Verify URLs. Usage:
    python check_urls.py <url> [<url> ...]
    python check_urls.py --file urls.txt
    python check_urls.py --from-py track_java.py      (extracts all http(s) links from a file)
Prints: STATUS  URL  [youtube title]
YouTube video/playlist URLs are checked through the oEmbed endpoint (returns title if valid).
"""
import json, re, sys, urllib.request, urllib.parse, ssl, concurrent.futures as cf

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9"}
CTX = ssl.create_default_context()

def check(url, hops=0):
    try:
        if re.search(r"youtube\.com/(watch|playlist)|youtu\.be/", url):
            o = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(url, safe="")
            with urllib.request.urlopen(urllib.request.Request(o, headers=UA), timeout=25, context=CTX) as r:
                return (r.status, url, json.loads(r.read().decode("utf-8", "ignore")).get("title", ""))
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
            return (r.status, url, "")
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location") if e.headers else None
        if e.code in (301, 302, 303, 307, 308) and loc and hops < 5:
            nxt = urllib.parse.urljoin(url, loc)
            st, _, extra = check(nxt, hops + 1)
            return (st, url, f"-> redirects to {nxt} {extra}".strip())
        return (e.code, url, "")
    except Exception as e:
        return ("ERR", url, type(e).__name__ + ": " + str(e)[:80])

def main():
    a = sys.argv[1:]
    urls = []
    if a and a[0] == "--file":
        urls = [l.strip() for l in open(a[1], encoding="utf-8") if l.strip().startswith("http")]
    elif a and a[0] == "--from-py":
        txt = open(a[1], encoding="utf-8").read()
        urls = sorted(set(u.rstrip(").,'\"`>") for u in re.findall(r"https?://[^\s)\"'`>\]]+", txt)))
    else:
        urls = a
    with cf.ThreadPoolExecutor(12) as ex:
        for st, u, extra in ex.map(check, urls):
            flag = "OK " if st == 200 else "!! "
            print(f"{flag}{st}  {u}  {extra}")

if __name__ == "__main__":
    main()
