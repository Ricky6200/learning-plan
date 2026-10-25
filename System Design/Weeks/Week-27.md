# 🏗️ System Design · Week 27 — Mock week: HLD, LLD, revision sheets

> 📅 **Mon 26 Apr 2027 → Sun 02 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 26](Week-26.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-27.md) · [Week 28 →](Week-28.md)

**Why this week:** Mocks convert knowledge into interview performance; this week finds your weakest areas while there is still time to fix them, and polishes the `system-design-lab` portfolio recruiters will open.

## 🗓️ Sessions

### Monday 26 Apr · 45 min — HLD mock #1 (AI mentor or peer, 40 min + score)
- 📚 **Learn:** Mock etiquette: clarify first, think aloud, check in with the interviewer every ~10 minutes, budget time for deep dives. Ask your AI mentor (or a colleague) to run a case you have not designed: FB post search, Strava, or the LLM chat/RAG platform from your W26 stretch. Optional: read [FB post search (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-post-search) only afterwards.
- 🛠️ **Do:** 40-minute recorded mock using your framework, then 5 minutes scoring with the 8-line rubric. Done when: `mocks/W27-hld-1.md` has the score, the interviewer's 3 toughest follow-ups and your best answer to each.

### Wednesday 28 Apr · 45 min — LLD mock: 45-min machine coding with a peer or AI mentor
- 📚 **Learn:** LLD mock flow: 5 min requirements, 5 min class diagram, 30 min code + tests, 5 min walkthrough of extensibility and concurrency. Unseen-problem suggestion: Amazon Locker - read [Amazon Locker (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/amazon-locker) only after the mock.
- 🛠️ **Do:** Do the mock on a problem you have not coded (Amazon Locker, or one the interviewer picks). Score 0-3 on: requirements, model, patterns, working code, tests, concurrency, communication. Done when: code is committed in `lld/mock-w27/` and the scorecard is in `mocks/W27-lld.md`.

### Thursday 29 Apr · 45 min — HLD mock #2 on your weakest area
- 📚 **Learn:** Choose the case family where your W20, W21, W25 and Monday scores were lowest (e.g., storage, streaming, consistency). Refresh with the related breakdown first, e.g., [Design Tinder (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/tinder) for geo + matching. Optional: [Design Dropbox (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox) for blobs.
- 🛠️ **Do:** 40-minute recorded mock on a case from your weakest family with a different interviewer if possible, then 5 minutes scoring. Done when: `mocks/W27-hld-2.md` shows the score and whether it improved versus mock #1, with 2 concrete fixes.

### Saturday 01 May · 45 min — PRACTICE: One-page summary sheet + portfolio polish
- 📚 **Learn:** Spaced revision: one table row per case study (key requirement, scale numbers, core components, the one big trade-off, a failure mode). Portfolio polish: a CI badge proves your tests run (reuse the `ci.yml` you wrote in Java W14 Sat, running `mvn -B test`) and a README index lets reviewers jump to diagrams. Read [Building and testing Java with Maven (GitHub Docs)](https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-maven). Optional: [Adding a workflow status badge (GitHub Docs)](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge).
- 🛠️ **Do:** 15 min: build `hld/SUMMARY.md` - one row per case study in `hld/`, a list of your LLD problems with their key patterns, and a 'Related AI designs' row linking your AI-track design docs. 10 min: add `.github/workflows/ci.yml` (`mvn -B test`), the status badge and a README index with diagram thumbnails. Done when: CI is green on GitHub, the badge shows 'passing' and the summary has no empty cells.

## 📦 Deliverable (by Saturday night)
Three mock scorecards in `mocks/`, `hld/SUMMARY.md` covering every case study and LLD problem, and a `system-design-lab` README with a green CI badge and a diagram index.

## ✅ Self-check (Sunday test preview)
- Which part of the framework do you rush or skip under time pressure?
- Name your three weakest case studies and the fix for each.
- Give a 60-second summary of the URL shortener including its key trade-off.
- What follow-up questions did your interviewers ask that you could not answer well?
- Which LLD patterns do you reach for first, and are they always justified?

## 🚀 Stretch (optional)
Rewrite the weakest design's deep-dive section using the mock feedback, and do a fourth mock with a different peer to compare their feedback with your AI mentor's. Cross-check your summary against the [Hello Interview core concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts).
