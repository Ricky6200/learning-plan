# ☁️ Azure Cloud · Week 25 — AI-200 exam prep: practice, cram, fix gaps

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** A structured final week turns scattered knowledge into exam points: practice assessments, Microsoft's official exam-prep videos and targeted fixes. The same labs become your strongest interview stories.

## 🗓️ Sessions

### Tuesday 13 Apr · 45 min — AI-200 practice assessment run 1 + weighted gap log
- 📚 **Learn:** The free [AI-200 practice assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b) on AI Skills Navigator (sign in first), the skills list in the [AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200) and the [exam sandbox](https://aka.ms/examdemo). The exam is 120 minutes and may contain interactive components.
- 🛠️ **Do:** Take practice run 1 timed. Log every miss in `w25/gaps.csv` (domain, objective, why wrong, doc link); rank by domain weight x misses and choose your top 6 objectives. Confirm (or make) your AI-200 booking for Sat 24 Apr 2027 or another day that week. Done when: the score and top-6 list are committed and the booking is confirmed.

### Wednesday 14 Apr · 45 min — Official AI-200 exam-prep videos 1-2 + fix top-6 gaps
- 📚 **Learn:** Microsoft Learn's AI-200 prep series: [1 - containerized solutions](https://www.youtube.com/watch?v=XHOBLJQZBCU) and [2 - AI solutions with Azure data services](https://www.youtube.com/watch?v=haeOJ2K1UU4) (about 18 minutes together); for each gap, reopen the matching Learn unit from the [AI-200 course](https://learn.microsoft.com/en-us/training/courses/ai-200t00).
- 🛠️ **Do:** Watch both videos. For each top-6 gap, do a 3-minute proof from your repo (re-run a script, re-read a KQL query, re-explain a Bicep or manifest block) and rewrite the gap as two flashcards. Done when: 6 gaps are marked fixed in `gaps.csv` and 12 new flashcards are committed.

### Friday 16 Apr · 45 min — Practice run 2, prep videos 3-4 and Learn lookup drill
- 📚 **Learn:** Second run on the [AI-200 practice assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b), prep videos [3 - connect to and consume Azure services](https://www.youtube.com/watch?v=oIalMs581A0) and [4 - secure, monitor, troubleshoot](https://www.youtube.com/watch?v=K2F1uvc8Cr8); Microsoft Learn is open during associate exams but costs time.
- 🛠️ **Do:** Practice run 2 (target 80%+). Watch videos 3 and 4 (~10 minutes). Then a 10-item lookup race on learn.microsoft.com for facts you missed (SDK method names, KEDA scaler fields, KQL functions), aiming for under 90 seconds each. Done when: the run-2 score and lookup times are logged in `w25/`.

### Saturday 17 Apr · 60 min — LAB: Timed AI-200 build gauntlet (exam simulation)
- 📚 **Learn:** Mixed AI-200 tasks against the clock, using only Microsoft Learn as reference (as in the exam). Start from the [Azure SDK for Python overview](https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview); open your own `py/` folder only after the timer ends.
- 🛠️ **Do:** 45-minute timer, 6 tasks: (1) Cosmos DB vector query with a filter (serverless account); (2) pgvector HNSW index + top-5 query (local `pgvector/pgvector` Docker is fine); (3) cache-aside with TTL (local Redis is fine); (4) a Service Bus message dead-lettered and read back; (5) a Key Vault secret read via DefaultAzureCredential; (6) a KQL p95 query in Application Insights. Then 15 minutes: verify, record times, delete the RG. Done when: 5/6+ done in time, logged in `w25/gauntlet.md`.

## 📦 Deliverable (by Saturday night)
`w25/gaps.csv`, two practice scores (run 2 at 80%+), 6 fixed gaps + 12 flashcards, lookup-race times, gauntlet results and a confirmed AI-200 booking.

## ✅ Self-check (Sunday test preview)
- Which two AI-200 objectives are still weakest, and what is your 48-hour plan for them?
- Walk through a RAG request on Azure from API to Cosmos DB or pgvector to cache, naming the SDK calls.
- How would you make a Functions-based pipeline keyless end to end?
- Explain KEDA scaling for a Service Bus worker in Container Apps in three sentences.
- What would you check first if traces from service B never reach Application Insights?
- Which AI-200 domain carries the most weight, and how did you allocate revision time to it?

## 🚀 Stretch (optional)
Get a second explanation of your weakest topic in Hindi from the [AI-200 Full Course (Hindi) playlist](https://www.youtube.com/playlist?list=PL5TTTZj-297nFs3InPjph4E-07ayWa8mG) - cross-check anything new against the study guide.
