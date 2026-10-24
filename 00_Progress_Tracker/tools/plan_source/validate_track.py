"""Validate a track data file. Usage: python validate_track.py <path_to_track_file.py>"""
import importlib.util, sys

DAYS = {
    "java":  (["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], [60, 60, 60, 60, 60, 60]),
    "ai":    (["Mon", "Tue", "Thu", "Fri", "Sat"], [45, 45, 45, 45, 45]),
    "sd":    (["Mon", "Wed", "Thu", "Sat"], [45, 45, 45, 45]),
    "azure": (["Tue", "Wed", "Fri", "Sat"], [45, 45, 45, 60]),
}

def main(p):
    s = importlib.util.spec_from_file_location("t", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    days, mins = DAYS[m.TRACK_KEY]
    errs = []
    if len(m.WEEKS) != 26:
        errs.append(f"expected 26 weeks, got {len(m.WEEKS)}")
    for i, w in enumerate(m.WEEKS, 1):
        if w.get("week") != i:
            errs.append(f"week index mismatch at position {i}")
        for k in ("title", "why", "sessions", "deliverable", "self_check", "stretch"):
            if not w.get(k):
                errs.append(f"W{i}: missing {k}")
        ss = w.get("sessions", [])
        if [x.get("day") for x in ss] != days:
            errs.append(f"W{i}: days {[x.get('day') for x in ss]} != {days}")
        if [x.get("mins") for x in ss] != mins:
            errs.append(f"W{i}: mins {[x.get('mins') for x in ss]} != {mins}")
        for x in ss:
            for k in ("topic", "learn", "do"):
                v = x.get(k, "")
                if not v:
                    errs.append(f"W{i} {x.get('day')}: empty {k}")
                if "\n" in v:
                    errs.append(f"W{i} {x.get('day')}: newline in {k}")
                if "```" in v:
                    errs.append(f"W{i} {x.get('day')}: triple backticks in {k}")
            if len(x.get("learn", "").split()) > 90:
                errs.append(f"W{i} {x.get('day')}: learn too long ({len(x['learn'].split())} words)")
            if len(x.get("do", "").split()) > 100:
                errs.append(f"W{i} {x.get('day')}: do too long ({len(x['do'].split())} words)")
        if len(w.get("self_check", [])) < 5:
            errs.append(f"W{i}: self_check < 5")
    if errs:
        print("FAIL")
        print("\n".join(errs))
        sys.exit(1)
    print(f"OK  {m.TRACK_KEY}: 26 weeks, {sum(len(w['sessions']) for w in m.WEEKS)} sessions")

if __name__ == "__main__":
    main(sys.argv[1])
