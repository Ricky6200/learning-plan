# ☁️ Azure Cloud · Week 25 — AI-200 exam prep: practice, gaps + Boss

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** A structured final week turns scattered knowledge into exam points: practice assessments, Microsoft's official exam-prep videos, targeted fixes and a timed Boss that simulates the exam's hands-on feel. The same labs become your strongest interview stories.

## 🗓️ Sessions

### Tuesday 13 Apr · 45 min — AI-200 practice assessment run 1 + weighted gap log
- 📚 **Learn:** The exam is 120 minutes and may contain interactive components. Use the free [AI-200 practice assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b) on AI Skills Navigator (sign in first). Optional: the skills list in the [AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200).
- 🛠️ **Do:** Take practice run 1 timed. Log every miss in `w25/gaps.csv` (domain, objective, why wrong, doc link); rank by domain weight x misses and choose your top 6 objectives. Confirm your AI-200 booking for Fri 23 Apr 2027 (made in W20). Done when: the score and top-6 list are committed and the booking is confirmed.

### Wednesday 14 Apr · 45 min — Official AI-200 exam-prep videos + fix top-6 gaps
- 📚 **Learn:** Microsoft Learn's AI-200 prep series, starting with the heaviest domain: [2 - AI solutions with Azure data services](https://www.youtube.com/watch?v=haeOJ2K1UU4) (~9 min). Optional: [1 - containerized solutions](https://www.youtube.com/watch?v=XHOBLJQZBCU). For each gap, reopen the matching Learn unit of the AI-200 course.
- 🛠️ **Do:** Watch video 2 (and 1 if time). For each top-6 gap, do a 3-minute proof from your repo (re-run a script, re-read a KQL query, re-explain a Bicep or manifest block) and rewrite the gap as two flashcards. Done when: 6 gaps are marked fixed in `gaps.csv` and 12 new flashcards are committed.

### Friday 16 Apr · 45 min — Practice run 2, prep videos 3-4 and Boss setup
- 📚 **Learn:** Second run on the practice assessment from Tuesday, then the official prep videos for the last two domains: [3 - connect to and consume Azure services](https://www.youtube.com/watch?v=oIalMs581A0). Optional: [4 - secure, monitor, troubleshoot](https://www.youtube.com/watch?v=K2F1uvc8Cr8). Microsoft Learn is open during associate exams but costs time.
- 🛠️ **Do:** Practice run 2 (target 80%+); watch video 3 (and 4 if time). Then launch tomorrow's slow resource: a serverless Cosmos DB account with `--capabilities EnableServerless EnableNoSQLVectorSearch --no-wait` (vector search takes ~15 minutes to activate). Done when: the run-2 score is logged in `w25/` and the account is provisioning.

### Saturday 17 Apr · 60 min — BOSS BATTLE: Timed AI-200 build gauntlet (exam simulation)
- 📚 **Learn:** Season 5 integration: mixed AI-200 tasks against the clock, using only Microsoft Learn as reference (as in the exam). Start from the [Azure SDK for Python overview](https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview); open your own `py/` folder only after the timer ends.
- 🛠️ **Do:** 45-minute timer, 6 tasks: (1) Cosmos DB vector query with a filter on Friday's serverless account; (2) pgvector HNSW index + top-5 query (a `pgvector/pgvector` container in a Codespace is fine); (3) cache-aside with TTL (Redis in the same Codespace is fine); (4) a Service Bus message dead-lettered and read back; (5) a Key Vault secret read via DefaultAzureCredential; (6) a KQL p95 query in Application Insights. Then 15 minutes: verify, record times, delete the RG and stop the Codespace. Done when: 5/6+ done in time, logged in `w25/boss.md`.

## 📦 Deliverable (by Saturday night)
`w25/gaps.csv`, two practice scores (run 2 at 80%+), 6 fixed gaps + 12 flashcards, the Boss gauntlet results in `w25/boss.md` and a confirmed AI-200 booking.

## ✅ Self-check (Sunday test preview)
- Which two AI-200 objectives are still weakest, and what is your 48-hour plan for them?
- Walk through a RAG request on Azure from API to Cosmos DB or pgvector to cache, naming the SDK calls.
- How would you make a Functions-based pipeline keyless end to end?
- Explain KEDA scaling for a Service Bus worker in Container Apps in three sentences.
- What would you check first if traces from service B never reach Application Insights?
- Which AI-200 domain carries the most weight, and how did you allocate revision time to it?

## 🚀 Stretch (optional)
Get a second explanation of your weakest topic in Hindi from the [AI-200 Full Course (Hindi) playlist](https://www.youtube.com/playlist?list=PL5TTTZj-297nFs3InPjph4E-07ayWa8mG) - cross-check anything new against the study guide.
