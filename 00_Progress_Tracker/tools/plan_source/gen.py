"""Generate Markdown plan files from track data. Run: python gen.py --force
Safe to re-run: it only (re)writes generated files (Weeks/, ROADMAP.md, 01_Daily_Planner/, 01_MASTER_CALENDAR.md).
WARNING: re-running overwrites ticked checkboxes in 01_Daily_Planner and track Weeks files.
"""
import datetime as dt, importlib.util, json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", "..", ".."))  # Personal_Learning
START = dt.date(2026, 10, 26)
NWEEKS = 30
END = START + dt.timedelta(weeks=NWEEKS, days=-1)
IDX = json.load(open(os.path.join(BASE, "lc_index.json"), encoding="utf-8"))

TRACKS = {
    "dsa":   {"name": "DSA", "folder": "DSA", "emoji": "🧩"},
    "java":  {"name": "Java Backend", "folder": "Java + Spring + Microservices + Kafka + Docker + Kubernetes", "emoji": "☕"},
    "ai":    {"name": "AI Engineering", "folder": "AI Engineering", "emoji": "🤖"},
    "sd":    {"name": "System Design", "folder": "System Design", "emoji": "🏗️"},
    "azure": {"name": "Azure Cloud", "folder": "Azure Cloud", "emoji": "☁️"},
}
SLOTS = {
    "dsa": "Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min",
    "java": "Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min",
    "ai": "Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min",
    "sd": "Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min",
    "azure": "Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min",
}
SEASONS = [(1, 4, "Season 1 — Foundation Forge"), (5, 9, "Season 2 — Concurrency Crucible"),
           (10, 15, "Season 3 — Spring Citadel"), (16, 20, "Season 4 — Distributed Kingdom"),
           (21, 25, "Season 5 — Cloud Ascension"), (26, 30, "Season 6 — Final Boss: The Offer")]
BOSS = {4, 9, 15, 20, 25, 30}
MILESTONES = {
    4: "⚔️ Boss S1", 5: "🎓 AZ-900 exam", 9: "⚔️ Boss S2", 13: "🎟️ TicketVerse v0", 15: "⚔️ Boss S3",
    16: "🎓 AZ-104 exam · 🚀 TicketVerse v1.0", 20: "⚔️ Boss S4 · 💼 Start applying", 22: "🐳 Full system in Docker",
    25: "⚔️ Boss S5", 26: "🎓 AI-200 exam", 28: "☁️ TicketVerse live on Azure (with AI)", 30: "👑 FINAL BOSS",
}
CAREER = {
    1: "Create GitHub repos: java-mastery, ai-engineering-lab, system-design-lab, azure-labs; add a GitHub profile README.",
    2: "LinkedIn: headline + About section aimed at 'Java Backend · Azure · AI Engineer'.",
    4: "Optional: LinkedIn post about Season 1 (what you built). Public learning attracts recruiters.",
    6: "STAR story bank: write 2 stories from your current job (see Career & Interview Prep/STAR_STORY_BANK.md).",
    8: "Complete LinkedIn profile (skills, featured repos); follow 30 target companies.",
    10: "Build your target-company list (3 tiers, 30+ companies) in Career & Interview Prep/README.md.",
    12: "STAR stories: add 4 more (conflict, failure, ownership, tight deadline).",
    14: "Draft resume bullets for your projects so far (impact + numbers); Resume v1 goes out in Week 16.",
    16: "Resume v1 (1 page) with TicketVerse v1.0 + AZ-104 (if passed); post the release on LinkedIn; tell 3–5 seniors/friends you'll want referrals from Week 20.",
    18: "Resume v2; update Naukri; LinkedIn 'Open to work' (recruiters only).",
    20: "Start applying: 8–10 targeted applications/week + referrals; track them in the Career tracker.",
    22: "Mock HR/behavioural round with your AI mentor (use STAR bank).",
    24: "Salary research (AmbitionBox, Glassdoor, levels.fyi) + write your negotiation script.",
    26: "Add AI-200 (if passed) to LinkedIn/resume; refresh the pipeline: follow-ups, referrals, next interviews.",
    28: "Resume v3: TicketVerse live on Azure + AI assistant; post a 2-minute demo video on LinkedIn.",
    30: "Pipeline review: interviews scheduled, offers, negotiation, and your next 4-week plan.",
}
DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
FULL = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
ORDER = {  # integrated daily order per day (after DSA + Java)
    "Mon": ["ai", "sd"], "Tue": ["azure", "ai"], "Wed": ["sd", "azure"], "Thu": ["ai", "sd"],
    "Fri": ["azure", "ai"], "Sat": ["ai", "sd", "azure"],
}
XP = {"Easy": 5, "Medium": 10, "Hard": 20}
TARGET = {"Easy": "15m", "Medium": "25m", "Hard": "40m"}
RESOLVE_TARGET = {"Easy": "10m", "Medium": "20m", "Hard": "35m"}
RESOLVE_XP = 5
HOLIDAYS = {  # verified dates; festival days may use the "Lite day" rule (Section 7 of AI_MEMORY.md)
    dt.date(2026, 11, 8): "🪔 **Diwali** — do a *Mini Test* (75 min, see protocol) today, or shift the full test to Mon 9 Nov evening",
    dt.date(2026, 12, 25): "🎄 **Christmas** — Lite day allowed (1 DSA problem + 30 min Java); catch up in Sunday's preview slot",
    dt.date(2027, 1, 1): "🎆 **New Year** — Lite day allowed; catch up on Saturday/Sunday",
    dt.date(2027, 1, 26): "🇮🇳 **Republic Day** — if you're off work, use the extra time to clear your 🔴 re-solves and catch up — next week (Week 15) is a Boss week",
    dt.date(2027, 3, 22): "🎨 **Holi** — Lite day allowed; move today's blocks to Tue–Sat buffers",
}
SETUP_GUIDE = "[03_SETUP_YOUR_LAPTOP.md](../03_SETUP_YOUR_LAPTOP.md)"
ENV_NOTES = {  # environment reminders (company laptop: Company Portal installs, JFrog Artifactory, free AI APIs blocked)
    1: f"⚙️ **Setup week:** finish Section 3 of {SETUP_GUIDE} — and **ask IT this week for Docker + WSL2** (Java needs it from Mon 4 Jan) and to allow the blocked Azure VS Code extensions (texts in Section 9). Java: **Corretto 25** for learning projects from day 1; work stays on JDK 11 (Section 5). Python: `py` + pip/uv through JFrog are ready; add the VS Code **Python + Jupyter** extensions on Monday. Keep every personal repo in `C:\\dev\\personal` so your work email never appears in personal commits.",
    2: f"🐍 Python code that calls an internet API (Thursday's weather lab) needs `pip-system-certs` in that venv on the company laptop — package installs through JFrog already work. ☕ Java calling an internet API and seeing `PKIX path building failed`? See Section 5, step 4 of {SETUP_GUIDE}.",
    3: f"🎓 Run Pearson VUE's **online-exam system test on your personal laptop** this week (webcam + microphone) — you book AZ-900 next Saturday. See Section 7 of {SETUP_GUIDE}. ☁️ Saturday's Azurite lab runs in a Codespace.",
    5: f"🏠 **From next Monday (30 Nov), AI-track coding moves to your personal laptop** (GitHub Codespaces) — free AI APIs are blocked on the company network. This weekend: create your Gemini/Groq keys there (Section 8 of {SETUP_GUIDE}). ☁️ Tue 1 Dec: personal Azure free account on the personal laptop — read `Azure Cloud/COST_SAFETY_AND_ACCOUNT_SETUP.md` first.",
    6: "🏠 **AI-track coding now runs in Codespaces on your personal laptop.** Keep one codespace, stop it after each session, and check your free quota weekly (github.com/settings/billing). ☁️ Tue 1 Dec: create your personal Azure free account.",
    7: "🐳 **Docker approved yet?** Java needs it from Mon 4 Jan (Week 11); next week's AI Docker lessons run inside your Codespace. Not approved? Chase IT this week — the Codespace fallback works for Java too.",
    9: "☁️ **Upgrade your personal Azure account to pay-as-you-go this week** (Azure Tuesday) — the $200 credit ends about 30 days after sign-up; keep the budget alerts on. 🐳 Docker needed from Mon 4 Jan (Java Week 11).",
    10: "🐳 **Next Monday (4 Jan) Java starts Docker essentials.** Docker on the company laptop, or a Codespace on your personal laptop. VisualVM/JMC aren't installed — the JDK's own `jcmd` and `jfr` tools cover the JVM lab.",
    14: "☸️ **Ask IT for kubectl + kind now** — needed from Mon 29 Mar (Java Week 23). Fallback: Azure Cloud Shell / Killercoda / a Codespace.",
    16: "🎓 **AZ-104 exam week** — keep Friday and Saturday lighter in every track; stretch goals can wait.",
    20: "☁️ Next week's Azure Functions labs: run `func` (Functions Core Tools) in a Codespace or on your personal laptop — the Azure VS Code extensions aren't allowed on the company laptop.",
    21: "☸️ **kubectl + kind needed from Mon 29 Mar** (Java Week 23). Not approved? Use a Codespace / Azure Cloud Shell / Killercoda.",
    26: "🎓 **AI-200 exam week** — keep Friday and Saturday lighter in every track. 🧑‍💻 Next week TicketVerse AI needs a 4-core Codespace: check your Codespaces quota now.",
}


def load(key):
    p = os.path.join(BASE, "data", f"track_{key}.py")
    if not os.path.exists(p):
        return None
    try:
        s = importlib.util.spec_from_file_location(key, p)
        m = importlib.util.module_from_spec(s)
        s.loader.exec_module(m)
    except Exception as e:  # file still being written by an author
        print(f"skip {key}: {type(e).__name__}")
        return None
    if len(getattr(m, "WEEKS", [])) != NWEEKS:
        print(f"skip {key}: {len(getattr(m, 'WEEKS', []))}/{NWEEKS} weeks")
        return None
    return m


def season(w):
    for a, b, n in SEASONS:
        if a <= w <= b:
            return n


def wdates(w):
    s = START + dt.timedelta(weeks=w - 1)
    return s, s + dt.timedelta(days=6)


def fmt(d):
    return d.strftime("%a %d %b %Y")


def day_date(w, dn):
    return START + dt.timedelta(weeks=w - 1, days=DAY_NAMES.index(dn))


def lc(i, short=False, nodiff=False):
    p = IDX[str(i)]
    url = f"https://leetcode.com/problems/{p['slug']}/"
    d = p["difficulty"][0]
    if nodiff:
        return f"[{i}. {p['title']}]({url})"
    return f"[LC {i} · {p['title']}]({url}) ({d})" if not short else f"[{i}. {p['title']}]({url}) ({d})"


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip() + "\n")


def header(key, w, title):
    s, e = wdates(w)
    t = TRACKS[key]
    boss = " · ⚔️ **BOSS WEEK**" if w in BOSS else ""
    nav_prev = f"[← Week {w-1:02d}](Week-{w-1:02d}.md)" if w > 1 else ""
    nav_next = f"[Week {w+1:02d} →](Week-{w+1:02d}.md)" if w < NWEEKS else ""
    nav = " · ".join(x for x in [nav_prev, "[Roadmap](../ROADMAP.md)", f"[Today's planner](../../01_Daily_Planner/Week-{w:02d}.md)", nav_next] if x)
    return (f"# {t['emoji']} {t['name']} · Week {w:02d} — {title}\n\n"
            f"> 📅 **{fmt(s)} → {fmt(e)}** · {season(w)}{boss}  \n"
            f"> ⏱️ Slots: {SLOTS[key]}\n\n{nav}\n\n")


# ----------------------------------------------------------------- DSA
def core_week(weeks, n):
    """The nearest week <= n that introduced new problems (skips re-solve weeks)."""
    while n >= 1 and weeks.get(n, {}).get("resolve_week"):
        n -= 1
    return n if n >= 1 else None


_RESOLVE_PLANS = {}


def resolve_plan(weeks):
    """Spaced re-solves for every normal week, planned once in calendar order:
    Mon–Fri 1 problem from the same weekday of the previous problem week (D+7; Week 1: yesterday's, D+1);
    Saturday 1–2 timed re-solves from three weeks earlier (D+21), Easy/Medium first; only 1 when Saturday's new
    problems already need more than 50 min, so the 60-min block stays realistic.
    Least-re-solved problems go first, so no problem is repeated while others from the same week wait."""
    sig = tuple((n, bool(w.get("resolve_week")), tuple(tuple(v) for v in w["days"].values())) for n, w in sorted(weeks.items()))
    if sig in _RESOLVE_PLANS:
        return _RESOLVE_PLANS[sig]
    days, times, plan = DAY_NAMES[:6], {}, {}

    def take(pool, k, avoid_hard):
        pool = list(dict.fromkeys(pool))
        diff = lambda i: IDX[str(i)]["difficulty"]
        got = sorted(pool, key=lambda i: (times.get(i, 0), avoid_hard and diff(i) == "Hard", -XP[diff(i)]))[:k]  # stable: day order on ties
        for i in got:
            times[i] = times.get(i, 0) + 1
        return got

    for n in sorted(weeks):
        if weeks[n].get("resolve_week"):
            continue
        for dn in days[:5]:
            if n == 1:
                pool = weeks[1]["days"][days[days.index(dn) - 1]] if dn != "Mon" else []
            else:
                src = core_week(weeks, n - 1)
                pool = weeks[src]["days"][dn] if src else []
            plan[(n, dn)] = take(pool, 1, False)
        weekday_picks = {i for d in days[:5] for i in plan[(n, d)]}
        src = 1 if n == 1 else core_week(weeks, n - 3 if n > 3 else n - 1)
        src_days = days[:5] if n == 1 else days
        pool = [i for d in src_days for i in weeks[src]["days"][d]] if src else []
        sat_new = sum(int(TARGET[IDX[str(i)]["difficulty"]][:-1]) for i in weeks[n]["days"]["Sat"])
        plan[(n, "Sat")] = take([i for i in pool if i not in weekday_picks] or pool, 1 if sat_new > 50 else 2, True)
    _RESOLVE_PLANS[sig] = plan
    return plan


def daily_resolves(weeks, n, dn):
    return resolve_plan(weeks).get((n, dn), [])


def challenge(dn, i, rs):
    return " 🔥 *weekend challenge — finish Sunday if needed*" if (dn == "Sat" and not rs and IDX[str(i)]["difficulty"] == "Hard") else ""


def gen_dsa(m):
    L = m.L
    weeks = {w["week"]: w for w in m.WEEKS}
    folder = os.path.join(ROOT, TRACKS["dsa"]["folder"])
    for w in m.WEEKS:
        n = w["week"]
        rs = w.get("resolve_week", False)
        out = header("dsa", n, w["title"])
        out += f"**Why this week:** {w['why']}\n\n"
        out += "## 🧠 Concepts to master\n" + "".join(f"- {c}\n" for c in w["concepts"]) + "\n"
        out += "## 🎥 Learn from (pick ONE per topic — don't binge)\n" + "".join(f"- [{L[k][0]}]({L[k][1]})\n" for k in w["learn"]) + "\n"
        out += "Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)\n\n"
        title = "🔁 Re-solve speed-run (no new problems — beat the target time)" if rs else f"🗓️ Daily problems — Core ({sum(len(v) for v in w['days'].values())} new)"
        col = "Re-solve target" if rs else "First-attempt time-box"
        out += f"## {title}\n\n| Day | Date | Problem | Difficulty | {col} | Done (☐→✅) |\n|---|---|---|---|---|---|\n"
        for dn, ids in w["days"].items():
            for j, i in enumerate(ids):
                p = IDX[str(i)]
                tb = (RESOLVE_TARGET if rs else TARGET)[p["difficulty"]]
                out += f"| {dn if j == 0 else ''} | {day_date(n, dn).strftime('%d %b') if j == 0 else ''} | {lc(i, nodiff=True)}{challenge(dn, i, rs)} | {p['difficulty']} | {tb} | ☐ |\n"
        out += "\n"
        if not rs:
            out += ("## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)\n"
                    "Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago "
                    "(one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. "
                    "Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.\n\n"
                    "| Day | Re-solve | Target |\n|---|---|---|\n")
            for dn in w["days"]:
                rv = daily_resolves(weeks, n, dn)
                out += f"| {dn} | {' · '.join(lc(i, True) for i in rv) if rv else '— (first day)'} | {' / '.join(RESOLVE_TARGET[IDX[str(i)]['difficulty']] for i in rv) if rv else ''} |\n"
            out += "\n"
        if w["bonus"]:
            out += "## ➕ Bonus (only after Core is done — great for weekends/holidays)\n" + "".join(f"- {lc(i, True)}\n" for i in w["bonus"]) + "\n"
        out += ("## ⏱️ The 60-minute routine\n"
                + ("1. **10–20 min** — re-solve today's problem(s) above from memory, timed.\n"
                   "2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.\n"
                   if not rs else
                   "1. **~50 min** — re-solve today's problems from memory, one at a time, against the target time.\n")
                + "3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.\n\n"
                "**Sunday:** re-solve everything you marked 🔴 this week (preview slot).\n\n")
        out += "## ✅ Self-check (Sunday test preview)\n" + "".join(f"- {q}\n" for q in w["self_check"]) + "\n"
        out += f"## 💡 Tip\n{w['tip']}\n"
        write(os.path.join(folder, "Weeks", f"Week-{n:02d}.md"), out)
    # roadmap
    core = sum(len(v) for w in m.WEEKS if not w.get("resolve_week") for v in w["days"].values())
    bonus = len({i for w in m.WEEKS for i in w["bonus"]})
    out = (f"# 🧩 DSA · {NWEEKS}-Week Roadmap\n\n> Java · pattern-by-pattern · up to 2 new problems a day + a daily spaced re-solve.  \n"
           f"> All problems are **free** on LeetCode (no Premium needed). Totals: **{core} core + {bonus} bonus**.\n\n"
           "| Week | Dates | Season | Pattern focus | New core | Milestone |\n|---|---|---|---|---|---|\n")
    for w in m.WEEKS:
        n = w["week"]; s, e = wdates(n)
        cnt = "re-solve" if w.get("resolve_week") else sum(len(v) for v in w["days"].values())
        out += f"| [W{n:02d}](Weeks/Week-{n:02d}.md) | {s:%d %b}–{e:%d %b} | {season(n).split(' — ')[0]} | {w['title']} | {cnt} | {MILESTONES.get(n, '')} |\n"
    write(os.path.join(folder, "ROADMAP.md"), out)


# --------------------------------------------------------- other tracks
def gen_track(key, m):
    folder = os.path.join(ROOT, TRACKS[key]["folder"])
    for w in m.WEEKS:
        n = w["week"]
        out = header(key, n, w["title"])
        out += f"**Why this week:** {w['why']}\n\n## 🗓️ Sessions\n\n"
        for s in w["sessions"]:
            dd = day_date(n, s["day"])
            out += f"### {FULL[s['day']]} {dd:%d %b} · {s['mins']} min — {s['topic']}\n"
            out += f"- 📚 **Learn:** {s['learn']}\n- 🛠️ **Do:** {s['do']}\n\n"
        out += f"## 📦 Deliverable (by Saturday night)\n{w['deliverable']}\n\n"
        out += "## ✅ Self-check (Sunday test preview)\n" + "".join(f"- {q}\n" for q in w["self_check"]) + "\n"
        out += f"## 🚀 Stretch (optional)\n{w['stretch']}\n"
        write(os.path.join(folder, "Weeks", f"Week-{n:02d}.md"), out)
    t = TRACKS[key]
    out = (f"# {t['emoji']} {t['name']} · {NWEEKS}-Week Roadmap\n\n> Slots: {SLOTS[key]}  \n"
           f"> Click a week for the day-by-day sessions.\n\n| Week | Dates | Season | Theme | Saturday | Milestone |\n|---|---|---|---|---|---|\n")
    for w in m.WEEKS:
        n = w["week"]; s, e = wdates(n)
        sat = w["sessions"][-1]["topic"].replace("|", "/")
        out += f"| [W{n:02d}](Weeks/Week-{n:02d}.md) | {s:%d %b}–{e:%d %b} | {season(n).split(' — ')[0]} | {w['title']} | {sat} | {MILESTONES.get(n, '')} |\n"
    write(os.path.join(folder, "ROADMAP.md"), out)


# ------------------------------------------------- integrated planner
def rel(key, n):
    return f"../{TRACKS[key]['folder'].replace(' ', '%20').replace('+', '%2B').replace('&', '%26')}/Weeks/Week-{n:02d}.md"


def gen_planner(mods):
    dsa = {w["week"]: w for w in mods["dsa"].WEEKS}
    other = {k: {w["week"]: w for w in mods[k].WEEKS} for k in ("java", "ai", "sd", "azure") if mods.get(k)}
    for n in range(1, NWEEKS + 1):
        s, e = wdates(n)
        dw = dsa[n]
        boss = n in BOSS
        rs = dw.get("resolve_week", False)
        n_resolves = sum(len(daily_resolves(dsa, n, d)) for d in DAY_NAMES[:6])
        xp_dsa = (sum(RESOLVE_XP for d in dw["days"].values() for i in d) if rs
                  else sum(XP[IDX[str(i)]["difficulty"]] for d in dw["days"].values() for i in d) + RESOLVE_XP * n_resolves)
        xp_blocks = 25 * 10
        out = f"# 🗓️ Week {n:02d} · {s:%d %b} → {e:%d %b %Y} · {season(n)}\n\n"
        flags = []
        if boss: flags.append("⚔️ **BOSS WEEK** — Saturday blocks are timed Boss Battles; beat the boss on Sunday for +300 XP")
        if n in MILESTONES: flags.append(f"🏁 Milestone: {MILESTONES[n]}")
        if n in ENV_NOTES: flags.append(ENV_NOTES[n])
        for hd, note in HOLIDAYS.items():
            if s <= hd <= e:
                flags.append(f"🎉 {hd:%a %d %b}: {note}")
        flags.append(f"⭐ XP available: ~{xp_blocks + xp_dsa + 100 + (300 if boss else 0)} (blocks {xp_blocks} · DSA {xp_dsa} · test 100{' · boss 300' if boss else ''})")
        out += "".join(f"> {f}  \n" for f in flags) + "\n"
        links = [f"[{TRACKS['dsa']['emoji']} DSA]({rel('dsa', n)})"] + [f"[{TRACKS[k]['emoji']} {TRACKS[k]['name']}]({rel(k, n)})" for k in ("java", "ai", "sd", "azure")]
        out += "**Open the details:** " + " · ".join(links) + "  \n"
        out += "**Tracker:** [Dashboard](../00_Progress_Tracker/PROGRESS_DASHBOARD.md) · [Daily log](../00_Progress_Tracker/DAILY_LOG.md) · [Weakness tracker](../00_Progress_Tracker/WEAKNESS_TRACKER.md)\n\n"
        out += "## 🎯 This week's mission\n| Track | Theme |\n|---|---|\n"
        out += f"| 🧩 DSA | {dw['title']} |\n"
        for k in ("java", "ai", "sd", "azure"):
            if k in other:
                out += f"| {TRACKS[k]['emoji']} {TRACKS[k]['name']} | {other[k][n]['title']} |\n"
        out += "\n## 🔧 Fix-it items (added by your AI mentor after last Sunday's test)\n- [ ] _none yet — the mentor fills this in after each test_\n\n"
        for dn in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
            dd = day_date(n, dn)
            hrs = "4.5 h" if dn == "Sat" else "3.5 h"
            out += f"## {FULL[dn]} · {dd:%d %b} · {hrs}{' · 🎉' if dd in HOLIDAYS else ''}\n"
            if dd in HOLIDAYS:
                out += f"> {HOLIDAYS[dd]}\n\n"
            probs = " · ".join(lc(i) + (" 🔥 weekend challenge" if challenge(dn, i, rs) else "") for i in dw["days"][dn])
            rv = daily_resolves(dsa, n, dn)
            if rs:
                out += f"- [ ] 🧩 **DSA · 60m** — 🔁 Re-solve (timed, from memory): {probs}\n"
            elif rv:
                label = "2 timed re-solves" if len(rv) > 1 else "Re-solve"
                out += f"- [ ] 🧩 **DSA · 60m** — 🔁 {label}: {' · '.join(lc(i, True) for i in rv)} → Solve: {probs}\n"
            else:
                out += f"- [ ] 🧩 **DSA · 60m** — Solve: {probs}\n"
            if "java" in other:
                ses = next(x for x in other["java"][n]["sessions"] if x["day"] == dn)
                out += f"- [ ] ☕ **Java · {ses['mins']}m** — {ses['topic']}\n"
            for k in ORDER[dn]:
                if k in other:
                    ses = next((x for x in other[k][n]["sessions"] if x["day"] == dn), None)
                    if ses:
                        out += f"- [ ] {TRACKS[k]['emoji']} **{TRACKS[k]['name']} · {ses['mins']}m** — {ses['topic']}\n"
            out += "\n"
        sun = day_date(n, "Sun")
        contest = (f"- [ ] 🏆 **LeetCode Weekly Contest · 8:00 AM IST · 90m** — on alternate Sundays from Week 10 it replaces the DSA part (45 min) of today's test; take the rest of the test afterwards\n"
                   if n >= 10 and n % 2 == 0 else
                   f"- [ ] (Optional, 8:00 AM IST) [LeetCode Weekly Contest](https://leetcode.com/contest/) — timed practice on unseen problems\n")
        out += (f"## Sunday · {sun:%d %b} · 3.5 h — {'⚔️ BOSS BATTLE TEST' if boss else 'Weekly Test Day'}{' · 🎉' if sun in HOLIDAYS else ''}\n"
                + (f"> {HOLIDAYS[sun]}\n\n" if sun in HOLIDAYS else "") +
                contest +
                f"- [ ] 📝 **Weekly test · 150m** — start a session and paste: `Read 00_Progress_Tracker\\AI_MEMORY.md and WEEKLY_TEST_PROTOCOL.md. Run my Week {n} test now.`\n"
                f"- [ ] 🔍 **Retro · 30m** — mentor updates scoreboard, weak areas, XP; you note 1 win + 1 fix\n"
                f"- [ ] 👀 **Preview & revise · 30m** — finish the 🔥 weekend challenge if pending · DSA spaced revision (in the DSA week file) · skim next week\n")
        if n in CAREER:
            out += f"- [ ] 💼 **Career · 15m** — {CAREER[n]}\n"
        out += ("\n## 📊 Scorecard (filled after the test)\n| Track | Score /100 | Status | Weak topics |\n|---|---|---|---|\n"
                + "".join(f"| {t} | | | |\n" for t in ["DSA", "Java", "System Design", "AI", "Azure"]) + "| **Overall** | | | |\n")
        nav = []
        if n > 1: nav.append(f"[← Week {n-1:02d}](Week-{n-1:02d}.md)")
        nav.append("[Master calendar](../01_MASTER_CALENDAR.md)")
        if n < NWEEKS: nav.append(f"[Week {n+1:02d} →](Week-{n+1:02d}.md)")
        out += "\n" + " · ".join(nav) + "\n"
        write(os.path.join(ROOT, "01_Daily_Planner", f"Week-{n:02d}.md"), out)


def gen_calendar(mods):
    out = (f"# 📆 Master Calendar — {NWEEKS} Weeks (Mon {START:%d %b %Y} → Sun {END:%d %b %Y})\n\n"
           "> Every week: Mon–Sat learn (3.5 h weekdays, 4.5 h Saturday) · **Sunday = weekly test (150 min) + retro**.  \n"
           "> Click a week number to open that week's **daily checklist**.\n\n")
    out += "## 🗺️ Seasons\n| Season | Weeks | Boss battle |\n|---|---|---|\n"
    for a, b, nm in SEASONS:
        out += f"| {nm} | W{a}–W{b} | W{b} |\n"
    out += "\n## 🎓 Certification anchors\n| Exam | Target week | Window |\n|---|---|---|\n"
    for ex, wk in [("AZ-900 Azure Fundamentals", 5), ("AZ-104 Azure Administrator", 16), ("AI-200 Azure AI Cloud Developer", 26)]:
        s, e = wdates(wk)
        out += f"| {ex} | W{wk} | {s:%d %b %Y} – {e:%d %b %Y} |\n"
    out += "\n## 📅 Week-by-week\n| Week | Dates | 🧩 DSA | ☕ Java | 🤖 AI | 🏗️ System Design | ☁️ Azure | 🏁 Milestone |\n|---|---|---|---|---|---|---|---|\n"
    for n in range(1, NWEEKS + 1):
        s, e = wdates(n)
        row = [f"[W{n:02d}](01_Daily_Planner/Week-{n:02d}.md)", f"{s:%d %b}–{e:%d %b}"]
        for k in ("dsa", "java", "ai", "sd", "azure"):
            m = mods.get(k)
            row.append(m.WEEKS[n - 1]["title"].replace("|", "/") if m else "_(pending)_")
        row.append(MILESTONES.get(n, ""))
        out += "| " + " | ".join(row) + " |\n"
    write(os.path.join(ROOT, "01_MASTER_CALENDAR.md"), out)


if __name__ == "__main__":
    if "--force" not in sys.argv:
        sys.exit("Refusing to run: regenerating OVERWRITES ticked checkboxes in 01_Daily_Planner/ and every track's Weeks/ files.\n"
                 "Use only for a deliberate re-plan the user approved (log it in Section 10 of AI_MEMORY.md). Then: python gen.py --force")
    mods = {k: load(k) for k in TRACKS}
    gen_dsa(mods["dsa"])
    for k in ("java", "ai", "sd", "azure"):
        if mods[k]:
            gen_track(k, mods[k])
    gen_planner(mods)
    gen_calendar(mods)
    print("Generated. Tracks with data:", [k for k, v in mods.items() if v])
