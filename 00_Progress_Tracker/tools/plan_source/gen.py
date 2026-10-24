"""Generate Markdown plan files from track data. Run: python gen.py
Safe to re-run: it only (re)writes generated files (Weeks/, ROADMAP_26_WEEKS.md, 01_Daily_Planner/, 01_MASTER_CALENDAR.md).
WARNING: re-running overwrites ticked checkboxes in 01_Daily_Planner and track Weeks files.
"""
import datetime as dt, importlib.util, json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", "..", ".."))  # Personal_Learning
START = dt.date(2026, 10, 26)
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
           (10, 14, "Season 3 — Spring Citadel"), (15, 19, "Season 4 — Distributed Kingdom"),
           (20, 23, "Season 5 — Cloud Ascension"), (24, 26, "Season 6 — Final Boss: The Offer")]
BOSS = {4, 9, 14, 19, 23, 26}
MILESTONES = {
    4: "⚔️ Boss S1", 5: "🎓 AZ-900 exam", 9: "⚔️ Boss S2", 14: "⚔️ Boss S3 · 🚀 TicketVerse v1.0",
    16: "🎓 AZ-104 exam", 19: "⚔️ Boss S4 · 🐳 full system in Docker", 20: "💼 Start applying",
    23: "⚔️ Boss S5 · ☁️ TicketVerse on Azure", 26: "🎓 AI-200 exam · 👑 FINAL BOSS",
}
CAREER = {
    1: "Create GitHub repos: java-mastery, ai-engineering-lab, system-design-lab, azure-labs; add a GitHub profile README.",
    2: "LinkedIn: headline + About section aimed at 'Java Backend · Azure · AI Engineer'.",
    4: "Optional: LinkedIn post about Season 1 (what you built). Public learning attracts recruiters.",
    6: "STAR story bank: write 2 stories from your current job (see Career & Interview Prep/STAR_STORY_BANK.md).",
    8: "Complete LinkedIn profile (skills, featured repos); follow 30 target companies.",
    10: "Build your target-company list (3 tiers, 30+ companies) in Career & Interview Prep/README.md.",
    12: "STAR stories: add 4 more (conflict, failure, ownership, tight deadline).",
    14: "Resume v1 (1 page) with TicketVerse v1.0 + post the release on LinkedIn.",
    16: "Add AZ-104 to LinkedIn/resume; tell 3–5 seniors/friends you'll want referrals from Week 20.",
    18: "Resume v2; update Naukri; LinkedIn 'Open to work' (recruiters only).",
    20: "Start applying: 8–10 targeted applications/week + referrals; track them in the Career tracker.",
    22: "Mock HR/behavioural round with your AI mentor (use STAR bank).",
    24: "Salary research (AmbitionBox, Glassdoor, levels.fyi) + write your negotiation script.",
    26: "Pipeline review: interviews scheduled, offers, next 4-week plan.",
}
DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
FULL = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday", "Thu": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
ORDER = {  # integrated daily order per day (after DSA + Java)
    "Mon": ["ai", "sd"], "Tue": ["azure", "ai"], "Wed": ["sd", "azure"], "Thu": ["ai", "sd"],
    "Fri": ["azure", "ai"], "Sat": ["ai", "sd", "azure"],
}
XP = {"Easy": 5, "Medium": 10, "Hard": 20}
TARGET = {"Easy": "15m", "Medium": "25m", "Hard": "40m"}
HOLIDAYS = {  # verified dates; festival days may use the "Lite day" rule (Section 7 of AI_MEMORY.md)
    dt.date(2026, 11, 8): "🪔 **Diwali** — do a *Mini Test* (75 min, see protocol) today, or shift the full test to Mon 9 Nov evening",
    dt.date(2026, 12, 25): "🎄 **Christmas** — Lite day allowed (1 DSA problem + 30 min Java); catch up in Sunday's preview slot",
    dt.date(2027, 1, 1): "🎆 **New Year** — Lite day allowed; catch up on Saturday/Sunday",
    dt.date(2027, 1, 26): "🇮🇳 **Republic Day** — if you're off work, use the extra time to prepare for Saturday's Boss Battle",
    dt.date(2027, 3, 22): "🎨 **Holi** — Lite day allowed; move today's blocks to Tue–Sat buffers",
}
SETUP_GUIDE = "[03_SETUP_YOUR_LAPTOP.md](../03_SETUP_YOUR_LAPTOP.md)"
ENV_NOTES = {  # environment reminders (company laptop: Company Portal installs, JFrog Artifactory, free AI APIs blocked)
    1: f"⚙️ **Setup week:** finish the open items in Section 3 of {SETUP_GUIDE}. Java: **Corretto 25 is installed** — make it the SDK of your learning projects from day 1 (Section 5); work stays on JDK 11. Python: start it with `py`; pip and uv already work through JFrog. Keep every personal repo in `C:\\dev\\personal` so your work email never appears in personal commits.",
    2: f"🐍 AI blocks now use pip packages — already working through JFrog. ☕ A `PKIX path building failed` error when your Java code calls an internet API? See Section 5, step 4 of {SETUP_GUIDE}.",
    3: f"🎓 Run Pearson VUE's **online-exam system test on your personal laptop** this week (webcam + microphone) — you book AZ-900 next Saturday. See Section 7 of {SETUP_GUIDE}.",
    4: f"🏠 **From this week, AI-track coding happens on your personal laptop** (GitHub Codespaces in the browser) — the free AI APIs are blocked on the company network. Create your Gemini/Groq keys there. See Section 8 of {SETUP_GUIDE}.",
    5: "☁️ Next week (Tue 1 Dec) you create your **personal Azure free account on the personal laptop** — personal Microsoft sign-in is blocked on the office laptop, so the Azure W6–W7 identity labs run there. Read `Azure Cloud/COST_SAFETY_AND_ACCOUNT_SETUP.md` first.",
    9: "🐳 **Docker needed from Mon 28 Dec** (Java Week 10). Not approved on the company laptop yet? Run the Java container weeks in a Codespace on your personal GitHub account.",
    18: "☸️ **kubectl + kind needed from Mon 8 Mar** (Java Week 20) — request them now, or use Azure Cloud Shell / Killercoda / a Codespace.",
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
    if len(getattr(m, "WEEKS", [])) != 26:
        print(f"skip {key}: {len(getattr(m, 'WEEKS', []))}/26 weeks")
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
    nav_next = f"[Week {w+1:02d} →](Week-{w+1:02d}.md)" if w < 26 else ""
    nav = " · ".join(x for x in [nav_prev, "[Roadmap](../ROADMAP_26_WEEKS.md)", f"[Today's planner](../../01_Daily_Planner/Week-{w:02d}.md)", nav_next] if x)
    return (f"# {t['emoji']} {t['name']} · Week {w:02d} — {title}\n\n"
            f"> 📅 **{fmt(s)} → {fmt(e)}** · {season(w)}{boss}  \n"
            f"> ⏱️ Slots: {SLOTS[key]}\n\n{nav}\n\n")


# ----------------------------------------------------------------- DSA
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
        title = "🔁 Re-solve speed-run (no new problems — beat the target time)" if rs else f"🗓️ Daily problems — Core ({sum(len(v) for v in w['days'].values())})"
        out += f"## {title}\n\n| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |\n|---|---|---|---|---|---|\n"
        for dn, ids in w["days"].items():
            for j, i in enumerate(ids):
                p = IDX[str(i)]
                challenge = " 🔥 *weekend challenge — finish Sunday if needed*" if (dn == "Sat" and j == 2 and not rs) else ""
                out += f"| {dn if j == 0 else ''} | {day_date(n, dn).strftime('%d %b') if j == 0 else ''} | {lc(i, nodiff=True)}{challenge} | {p['difficulty']} | {TARGET[p['difficulty']]} | ☐ |\n"
        out += "\n"
        if w["bonus"]:
            out += "## ➕ Bonus (only after Core is done — great for weekends/holidays)\n" + "".join(f"- {lc(i, True)}\n" for i in w["bonus"]) + "\n"
        if not rs and n > 1:
            prev = [i for d in weeks[n - 1]["days"].values() for i in d]
            prev = sorted(prev, key=lambda i: -XP[IDX[str(i)]["difficulty"]])[:2]
            rev = prev[:]
            if n > 3:
                older = [i for d in weeks[n - 3]["days"].values() for i in d]
                rev += sorted(older, key=lambda i: -XP[IDX[str(i)]["difficulty"]])[:1]
            out += ("## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)\n"
                    + "".join(f"- {lc(i, True)}\n" for i in rev)
                    + "- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)\n\n")
        out += ("## ⏱️ The 60-minute routine\n"
                "1. **5 min** — re-read yesterday's notes (pattern + insight).\n"
                "2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.\n"
                "3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.\n\n")
        out += "## ✅ Self-check (Sunday test preview)\n" + "".join(f"- {q}\n" for q in w["self_check"]) + "\n"
        out += f"## 💡 Tip\n{w['tip']}\n"
        write(os.path.join(folder, "Weeks", f"Week-{n:02d}.md"), out)
    # roadmap
    out = ("# 🧩 DSA · 26-Week Roadmap\n\n> Java · pattern-by-pattern · 13 core problems/week (+ bonus) · spaced repetition.  \n"
           "> All problems are **free** on LeetCode (no Premium needed). Totals: **325 core + 118 bonus**.\n\n"
           "| Week | Dates | Season | Pattern focus | Core | Milestone |\n|---|---|---|---|---|---|\n")
    for w in m.WEEKS:
        n = w["week"]; s, e = wdates(n)
        cnt = "re-solve" if w.get("resolve_week") else sum(len(v) for v in w["days"].values())
        out += f"| [W{n:02d}](Weeks/Week-{n:02d}.md) | {s:%d %b}–{e:%d %b} | {season(n).split(' — ')[0]} | {w['title']} | {cnt} | {MILESTONES.get(n, '')} |\n"
    write(os.path.join(folder, "ROADMAP_26_WEEKS.md"), out)


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
    out = (f"# {t['emoji']} {t['name']} · 26-Week Roadmap\n\n> Slots: {SLOTS[key]}  \n"
           f"> Click a week for the day-by-day sessions.\n\n| Week | Dates | Season | Theme | Saturday | Milestone |\n|---|---|---|---|---|---|\n")
    for w in m.WEEKS:
        n = w["week"]; s, e = wdates(n)
        sat = w["sessions"][-1]["topic"].replace("|", "/")
        out += f"| [W{n:02d}](Weeks/Week-{n:02d}.md) | {s:%d %b}–{e:%d %b} | {season(n).split(' — ')[0]} | {w['title']} | {sat} | {MILESTONES.get(n, '')} |\n"
    write(os.path.join(folder, "ROADMAP_26_WEEKS.md"), out)


# ------------------------------------------------- integrated planner
def rel(key, n):
    return f"../{TRACKS[key]['folder'].replace(' ', '%20').replace('+', '%2B').replace('&', '%26')}/Weeks/Week-{n:02d}.md"


def gen_planner(mods):
    dsa = {w["week"]: w for w in mods["dsa"].WEEKS}
    other = {k: {w["week"]: w for w in mods[k].WEEKS} for k in ("java", "ai", "sd", "azure") if mods.get(k)}
    for n in range(1, 27):
        s, e = wdates(n)
        dw = dsa[n]
        boss = n in BOSS
        xp_dsa = 0 if dw.get("resolve_week") else sum(XP[IDX[str(i)]["difficulty"]] for d in dw["days"].values() for i in d)
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
            probs = " · ".join(lc(i) + (" 🔥 weekend challenge" if dn == "Sat" and j == 2 and not dw.get("resolve_week") else "") for j, i in enumerate(dw["days"][dn]))
            verb = "Re-solve" if dw.get("resolve_week") else "Solve"
            out += f"- [ ] 🧩 **DSA · 60m** — {verb}: {probs}\n"
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
        out += (f"## Sunday · {sun:%d %b} · 3.5 h — {'⚔️ BOSS BATTLE TEST' if boss else 'Weekly Test Day'}{' · 🎉' if sun in HOLIDAYS else ''}\n"
                + (f"> {HOLIDAYS[sun]}\n\n" if sun in HOLIDAYS else "") +
                f"- [ ] (Optional, 8:00 AM IST) [LeetCode Weekly Contest](https://leetcode.com/contest/) — great practice from Week 8 onward\n"
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
        if n < 26: nav.append(f"[Week {n+1:02d} →](Week-{n+1:02d}.md)")
        out += "\n" + " · ".join(nav) + "\n"
        write(os.path.join(ROOT, "01_Daily_Planner", f"Week-{n:02d}.md"), out)


def gen_calendar(mods):
    out = ("# 📆 Master Calendar — 26 Weeks (Mon 26 Oct 2026 → Sun 25 Apr 2027)\n\n"
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
    for n in range(1, 27):
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
