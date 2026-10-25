"""Validate a track data file against the 30-week plan rules.
Usage: python validate_track.py <path_to_track_file.py> [more files...]
Checks: 30 weeks, schema, fixed day slots and minutes, word limits, "Done when", global boss Saturdays,
company-neutral wording (tracked files are backed up to a public-facing GitHub account) and, for DSA,
LeetCode ids (exist, free, no duplicate core problems, at most 2 new problems per day)."""
import importlib.util, json, os, re, sys

NWEEKS = 30
BOSS = {4, 9, 15, 20, 25, 30}
DAYS = {
    "java":  (["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], [60, 60, 60, 60, 60, 60]),
    "ai":    (["Mon", "Tue", "Thu", "Fri", "Sat"], [45, 45, 45, 45, 45]),
    "sd":    (["Mon", "Wed", "Thu", "Sat"], [45, 45, 45, 45]),
    "azure": (["Tue", "Wed", "Fri", "Sat"], [45, 45, 45, 60]),
}
DSA_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# Company-specific words must stay out of tracked files. Generic patterns live here; the employer-specific list lives in the
# git-ignored forbidden_words.local.md next to this script (one regex per line, '#' = comment), so it never reaches GitHub.
_HERE = os.path.dirname(os.path.abspath(__file__))
_LOCAL_WORDS = os.path.join(_HERE, "forbidden_words.local.md")
_PATTERNS = [r"artifactory\.[a-z0-9-]+\.com"]
if os.path.exists(_LOCAL_WORDS):
    with open(_LOCAL_WORDS, encoding="utf-8") as f:
        _PATTERNS += [ln.strip() for ln in f if ln.strip() and not ln.lstrip().startswith("#")]
else:
    print(f"note: {os.path.basename(_LOCAL_WORDS)} not found - only generic company-word checks run", file=sys.stderr)
FORBIDDEN = re.compile("|".join(_PATTERNS), re.I)
IDX_PATH = os.path.join(_HERE, "lc_index.json")


def text_of(x):
    if isinstance(x, str):
        return x
    if isinstance(x, dict):
        return " ".join(text_of(v) for v in x.values())
    if isinstance(x, (list, tuple)):
        return " ".join(text_of(v) for v in x)
    return ""


def common_checks(m, errs):
    if len(m.WEEKS) != NWEEKS:
        errs.append(f"expected {NWEEKS} weeks, got {len(m.WEEKS)}")
    for i, w in enumerate(m.WEEKS, 1):
        if w.get("week") != i:
            errs.append(f"week index mismatch at position {i} (found {w.get('week')})")
        title = w.get("title", "")
        if i in BOSS and "boss" not in title.lower():
            errs.append(f"W{i}: boss week title must mention Boss")
        if i not in BOSS and "boss" in title.lower():
            errs.append(f"W{i}: title mentions Boss but W{i} is not a boss week {sorted(BOSS)}")
        hit = FORBIDDEN.search(text_of(w))
        if hit:
            errs.append(f"W{i}: company-specific word '{hit.group(0)}' - use generic wording (company JFrog, corporate proxy)")


def check_sessions(m, errs):
    days, mins = DAYS[m.TRACK_KEY]
    for i, w in enumerate(m.WEEKS, 1):
        for k in ("title", "why", "sessions", "deliverable", "self_check", "stretch"):
            if not w.get(k):
                errs.append(f"W{i}: missing {k}")
        ss = w.get("sessions", [])
        if [x.get("day") for x in ss] != days:
            errs.append(f"W{i}: days {[x.get('day') for x in ss]} != {days}")
        if [x.get("mins") for x in ss] != mins:
            errs.append(f"W{i}: mins {[x.get('mins') for x in ss]} != {mins}")
        for x in ss:
            d = x.get("day")
            for k in ("topic", "learn", "do"):
                v = x.get(k, "")
                if not v:
                    errs.append(f"W{i} {d}: empty {k}")
                if "\n" in v:
                    errs.append(f"W{i} {d}: newline in {k}")
                if "```" in v:
                    errs.append(f"W{i} {d}: triple backticks in {k}")
            if len(x.get("learn", "").split()) > 90:
                errs.append(f"W{i} {d}: learn too long ({len(x['learn'].split())} words, max 90)")
            if len(x.get("do", "").split()) > 100:
                errs.append(f"W{i} {d}: do too long ({len(x['do'].split())} words, max 100)")
            if "done when" not in x.get("do", "").lower():
                errs.append(f"W{i} {d}: 'do' must end with a verifiable 'Done when: ...'")
            is_boss_topic = "BOSS" in x.get("topic", "")
            if i in BOSS and d == "Sat" and not x.get("topic", "").startswith("BOSS BATTLE"):
                errs.append(f"W{i} Sat: boss week - topic must start with 'BOSS BATTLE'")
            if is_boss_topic and not (i in BOSS and d == "Sat"):
                errs.append(f"W{i} {d}: 'BOSS' only allowed in boss-week Saturday topics {sorted(BOSS)}")
        if len(w.get("self_check", [])) < 5:
            errs.append(f"W{i}: self_check < 5")
    return sum(len(w.get("sessions", [])) for w in m.WEEKS)


def check_dsa(m, errs):
    idx = json.load(open(IDX_PATH, encoding="utf-8"))
    L = getattr(m, "L", {})
    seen = {}
    core = 0
    for i, w in enumerate(m.WEEKS, 1):
        for k in ("title", "why", "concepts", "learn", "days", "self_check", "tip"):
            if not w.get(k):
                errs.append(f"W{i}: missing {k}")
        if "bonus" not in w:
            errs.append(f"W{i}: missing bonus (use [] if none)")
        for key in w.get("learn", []):
            if key not in L:
                errs.append(f"W{i}: learn key '{key}' not in L")
        if len(w.get("self_check", [])) < 5:
            errs.append(f"W{i}: self_check < 5")
        days = w.get("days", {})
        if list(days.keys()) != DSA_DAYS:
            errs.append(f"W{i}: days {list(days.keys())} != {DSA_DAYS}")
        rs = w.get("resolve_week", False)
        for d, ids in days.items():
            if not ids:
                errs.append(f"W{i} {d}: no problems")
            if not rs and len(ids) > 2:
                errs.append(f"W{i} {d}: {len(ids)} new problems (max 2/day; the generator adds the daily re-solve)")
            for pid in ids:
                p = idx.get(str(pid))
                if not p:
                    errs.append(f"W{i} {d}: LC {pid} not in lc_index.json")
                    continue
                if p.get("paid"):
                    errs.append(f"W{i} {d}: LC {pid} is Premium (paid)")
                if rs:
                    if pid not in seen:
                        errs.append(f"W{i} {d}: re-solve LC {pid} was never a core problem earlier")
                else:
                    if pid in seen:
                        errs.append(f"W{i} {d}: LC {pid} duplicates core problem from W{seen[pid]}")
                    seen[pid] = i
                    core += 1
        for pid in w.get("bonus", []):
            p = idx.get(str(pid))
            if not p:
                errs.append(f"W{i} bonus: LC {pid} not in lc_index.json")
            elif p.get("paid"):
                errs.append(f"W{i} bonus: LC {pid} is Premium (paid)")
    bonus_ids = {pid for w in m.WEEKS for pid in w.get("bonus", [])}
    overlap = sorted(bonus_ids & set(seen))
    if overlap:
        errs.append(f"bonus problems that are also core: {overlap[:12]}{'...' if len(overlap) > 12 else ''}")
    return core, len(bonus_ids)


def main(p):
    s = importlib.util.spec_from_file_location("t", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    errs = []
    common_checks(m, errs)
    if m.TRACK_KEY == "dsa":
        core, bonus = check_dsa(m, errs)
        summary = f"{core} core problems, {bonus} bonus"
    else:
        summary = f"{check_sessions(m, errs)} sessions"
    if errs:
        print(f"FAIL {m.TRACK_KEY} ({len(errs)} problems)")
        print("\n".join(errs))
        return False
    print(f"OK  {m.TRACK_KEY}: {NWEEKS} weeks, {summary}")
    return True


if __name__ == "__main__":
    ok = all([main(p) for p in sys.argv[1:]]) if len(sys.argv) > 1 else False
    sys.exit(0 if ok else 1)
