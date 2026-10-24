# 🏗️ System Design · Week 25 — Mock week: HLD, LLD, revision sheets

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** Mocks convert knowledge into interview performance; this week finds your weakest areas while there is still time to fix them.

## 🗓️ Sessions

### Monday 12 Apr · 45 min — HLD mock #1 (AI mentor or peer, 40 min + score)
- 📚 **Learn:** Mock etiquette: clarify first, think aloud, check in with the interviewer every ~10 minutes, budget time for deep dives. Ask your AI mentor (or a colleague) to run a case you have not presented, e.g., [Design LeetCode](https://www.hellointerview.com/learn/system-design/problem-breakdowns/leetcode) or [FB post search](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-post-search) (Hello Interview; read only afterwards).
- 🛠️ **Do:** 40-minute recorded mock using your framework, then 5 minutes scoring with the 8-line rubric. Done when: `mocks/W25-hld-1.md` has the score, the interviewer's 3 toughest follow-ups and your best answer to each.

### Wednesday 14 Apr · 45 min — LLD mock: machine coding with a peer or AI mentor
- 📚 **Learn:** LLD mock flow: 5 min requirements, 5 min class diagram, 30 min code + tests, 5 min walkthrough of extensibility and concurrency. Unseen-problem suggestion: [Amazon Locker (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/amazon-locker) - read only after the mock.
- 🛠️ **Do:** Do the mock on a problem you have not coded (Amazon Locker, car rental, or one the interviewer picks). Score 0-3 on: requirements, model, patterns, working code, tests, concurrency, communication. Done when: code is committed in `lld/mock-w25/` and the scorecard is in `mocks/W25-lld.md`.

### Thursday 15 Apr · 45 min — HLD mock #2 on your weakest area
- 📚 **Learn:** Choose the case family where your W19/W23/W25 scores were lowest (e.g., storage, streaming, consistency). Refresh with the related breakdown first, e.g., [Design Tinder (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/tinder) for geo + matching or [Design Dropbox](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox) for blobs.
- 🛠️ **Do:** 40-minute recorded mock on a case from your weakest family with a different interviewer if possible, then 5 minutes scoring. Done when: `mocks/W25-hld-2.md` shows the score and whether it improved versus mock #1, with 2 concrete fixes.

### Saturday 17 Apr · 45 min — PRACTICE: Revisit weakest design + one-page summary sheet
- 📚 **Learn:** Spaced revision: one table row per case study (key requirement, scale numbers, core components, the one big trade-off, a failure mode). Reuse your write-ups in `hld/`; cross-check with the [Hello Interview core concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts).
- 🛠️ **Do:** 20 min: rewrite the weakest design's deep-dive section using the mock feedback. 25 min: build `hld/SUMMARY.md` - one row per case study (all 18) plus a list of 15 LLD problems with their key patterns. Done when: the summary has no empty cells and you can recite any row's trade-off in 30 seconds.

## 📦 Deliverable (by Saturday night)
Three mock scorecards in `mocks/`, an improved weakest design, and `hld/SUMMARY.md` covering every case study and LLD problem.

## ✅ Self-check (Sunday test preview)
- Which part of the framework do you rush or skip under time pressure?
- Name your three weakest case studies and the fix for each.
- Give a 60-second summary of the URL shortener including its key trade-off.
- What follow-up questions did your interviewers ask that you could not answer well?
- Which LLD patterns do you reach for first, and are they always justified?

## 🚀 Stretch (optional)
Do a fourth mock with a different peer and compare their feedback with your AI mentor's.
