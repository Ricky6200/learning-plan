# 📝 WEEKLY TEST PROTOCOL (the AI mentor follows this exactly)

> Trigger: the learner says **"Run my Week N test"** (normally Sunday). Total ≈ **150 minutes**, 5 sections.
> Goal: measure real skill on *this week's* content (+ spaced repetition), find weak spots, and turn them into concrete fixes.

---

## 1) Before the test — read these (in this order)
1. `00_Progress_Tracker/AI_MEMORY.md` (rules) and `PROGRESS_DASHBOARD.md` (actual position).
2. `01_Daily_Planner/Week-NN.md` → which items were actually ticked ✅ (test what was covered; note what was skipped).
3. Week files for N: `DSA/Weeks/Week-NN.md`, `Java …/Weeks/Week-NN.md`, `System Design/Weeks/Week-NN.md`,
   `AI Engineering/Weeks/Week-NN.md`, `Azure Cloud/Weeks/Week-NN.md` (topics, deliverables, self-check seeds).
4. `WEAKNESS_TRACKER.md` → items whose re-test week = N (must be included).
5. `DSA/REVISION_TRACKER.md` → 🔴 problems (candidates for the spaced-repetition question).

## 2) Rules to announce at the start
- Closed book: no web search, no AI help, no notes. An IDE is allowed **only** for the DSA/Java coding tasks (like a LeetCode editor).
- Answer each section in **one message**. Timers are honour-based; the learner reports time taken.
- If the learner only has limited time: run a **Mini Test (75 min)** = half the questions per section; mark it "mini" in the log.
- If a section's topics were skipped this week, test what *was* done and log the gap (do not silently skip the track).

## 3) Sections, timing & scoring (each section scored /100)

| # | Section | Time | Composition | Scoring |
|---|---|---|---|---|
| 1 | 🧩 DSA | 45 min | 2 coding problems in Java on the week's pattern (1 Easy/Medium + 1 Medium; from W9 the 2nd may be a Hard-lite) — **not** from the week's list (use similar LeetCode problems the learner hasn't solved; check the plan's lists to avoid repeats) + 5 "which pattern & why" one-liners | 2 × 40 (correctness 20 · optimal complexity 8 · edge cases 6 · code clarity 6) + 5 × 4 |
| 2 | ☕ Java | 30 min | 8 questions: mix of MCQ, short answer, **output prediction** (give a code snippet), **spot-the-bug**, "explain like an interviewer" + 1 small coding task (≤ 15 min) | 8 × 8 + task 36 (correct 20 · idiomatic/modern Java 8 · edge cases/tests 8) |
| 3 | 🏗️ System Design | 30 min | 5 concept questions + 1 mini design: LLD (classes, relationships, key methods, pattern used — in text) **or** HLD (requirements, components, data flow, 2 trade-offs — in text) | 5 × 10 + design 50 (requirements 10 · structure/components 15 · trade-offs/patterns 15 · clarity 10) |
| 4 | 🤖 AI | 25 min | 6 questions (concepts + 1 Python code-reading/debug) + 1 scenario ("design/choose/fix") | 6 × 10 + scenario 40 |
| 5 | ☁️ Azure | 20 min | 12 exam-style questions for the **current cert** (AZ-900 W1–W5, AZ-104 W5–W16, AI-200 W16–W26): single-choice, multi-select, scenario, "which service" | % correct (each ≈ 8.33) |

**Difficulty mix per section:** ~40% recall · ~40% application · ~20% interview-tricky (edge cases, trade-offs).
**Spaced repetition (from Week 3):** each section includes 1–2 questions from earlier weeks — prioritise WEAKNESS_TRACKER items due now.
**Question quality rules:** don't reuse self-check questions verbatim (use them as seeds); vary formats; Azure questions must map to the
official "skills measured" in `Azure Cloud/CERTIFICATION_GUIDE.md`; never test content from future weeks.

## 4) Grading behaviour
- Strict but fair, partial credit allowed. For every deduction write **one line why**.
- For code: mentally run 3–5 test cases incl. edge cases (empty, single element, duplicates, negatives, overflow, null). State complexity.
- Status per section: 🟢 ≥ 80 · 🟡 60–79 · 🔴 < 60. Overall = DSA 25% · Java 25% · SD 20% · AI 15% · Azure 15%.
- A **topic** (not just a section) is "weak" if the learner lost ≥ 50% of the marks of the questions on that topic.

## 5) Boss weeks (W4, W9, W14, W19, W23, W26)
- Same 5 sections, slightly harder, plus **one integrated Boss question** inside the most relevant section (e.g., W14: "design + code the seat-hold logic and explain its transaction isolation").
- **Boss defeated** if overall ≥ 70 and no section < 50 → +300 XP and the Season badge. Otherwise schedule a **30-min Rematch** (only failed sections) next Sunday.
- W26 Final Boss = full mock interview loop: DSA (2 problems) · Java/Spring deep-dive · LLD · HLD · AI · behavioural (STAR).

## 6) After grading — write & update (all mandatory)
1. Create `Weekly_Tests/Week-NN-Test.md` using the template in Section 8 (questions, learner answers — keep code verbatim, model answers, marks, feedback).
2. `TEST_SCOREBOARD.md` → add the row.
3. `WEAKNESS_TRACKER.md` → add new weak topics (with evidence, exact remediation tasks, re-test weeks N+1 and N+3); update re-tested items (close if ≥ 80).
4. `01_Daily_Planner/Week-(N+1).md` → replace the "Fix-it items" placeholder with ≤ 5 concrete items (15–20 min each, assign a day).
5. `PROGRESS_DASHBOARD.md` → scores, XP (+overall % ; boss +300), level, streak, badges, position.
6. `DAILY_LOG.md` → Sunday entry. 7. `AI_SESSION_LOG.md` → handoff entry.
8. Every 4th week (W4, W8, W12, …): write 2–3 trend lines in `TEST_SCOREBOARD.md` and "patterns noticed" in `WEAKNESS_TRACKER.md`.

## 7) Message to the learner at the end (keep it short)
1. Score table (5 sections + overall, with 🟢🟡🔴).
2. ✅ 3 strengths · ⚠️ 3 weaknesses (topic-level, specific).
3. 🎯 Focus plan for next week (the Fix-it items) + whether any plan adjustment is recommended.
4. XP gained, new level/badges, streak. One honest, motivating line.

## 8) Test file template (`Weekly_Tests/Week-NN-Test.md`)
```markdown
# Week NN Test — <date> (<normal | mini | BOSS>)
Duration: <reported> · Covered this week: <ticked %> · Skipped: <items>

## 1. DSA (/100)
### Q1 <title / LC-like statement>   — Learner code: ```java …``` — Verdict, complexity, marks, feedback
### Q2 …
### Pattern one-liners — answers, marks
**Section score:** xx/100 🟢/🟡/🔴

## 2. Java (/100) … ## 3. System Design (/100) … ## 4. AI (/100) … ## 5. Azure (/100) …

## Summary
| Section | Score | Status | Weak topics |
| Overall (weighted) | | | |
### Remediation added to Week NN+1
- [ ] …
### XP: +xx (total xxxx · Level …)
```
