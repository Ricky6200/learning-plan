"""Final QA: verify every external link in all Markdown files under Personal_Learning.
Usage: python check_all.py [--exclude "Azure Cloud"] [--only "Azure Cloud"]
Skips generated LeetCode problem URLs (built from the official catalog). Retries 429/5xx sequentially.
"""
import collections, concurrent.futures as cf, glob, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_urls import check  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
args = sys.argv[1:]
excl = args[args.index("--exclude") + 1] if "--exclude" in args else None
only = args[args.index("--only") + 1] if "--only" in args else None

where = collections.defaultdict(set)
for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    rel = os.path.relpath(f, ROOT)
    if excl and rel.startswith(excl):
        continue
    if only and not rel.startswith(only):
        continue
    txt = open(f, encoding="utf-8").read()
    for u in re.findall(r"\]\((https?://[^)\s]+)\)", txt):
        u = u.rstrip(".,;")
        if re.match(r"https://leetcode\.com/problems/[a-z0-9-]+/$", u):
            continue
        where[u].add(rel)

urls = sorted(where)
print(f"unique external links: {len(urls)}")
res = {}
with cf.ThreadPoolExecutor(8) as ex:
    for st, u, extra in ex.map(check, urls):
        res[u] = (st, extra)
retry = [u for u, (st, _) in res.items() if st in (429, 500, 502, 503, 504, "ERR")]
for u in retry:
    time.sleep(2)
    st, _, extra = check(u)
    res[u] = (st, extra)
bad = {u: v for u, v in res.items() if v[0] != 200}
print(f"OK: {len(res) - len(bad)}  NOT-OK: {len(bad)}")
for u, (st, extra) in sorted(bad.items(), key=lambda x: str(x[1][0])):
    print(f"{st}  {u}  {extra}  <- {', '.join(sorted(where[u]))[:160]}")
