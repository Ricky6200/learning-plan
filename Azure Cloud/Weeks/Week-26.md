# ☁️ Azure Cloud · Week 26 — AI-200 exam, interviews, cleanup, next steps

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-26.md)

**Why this week:** This is the finish line: the AI-200 credential, sharp interview answers about building and migrating on Azure, a subscription that costs nothing, and a clear plan for what comes next (AI-103 or AZ-305).

## 🗓️ Sessions

### Tuesday 20 Apr · 45 min — Final AI-200 revision + exam-day checklist
- 📚 **Learn:** Your `w25/gaps.csv` and flashcards, the [AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200), online-exam rules in [About online exams with Pearson VUE](https://learn.microsoft.com/en-us/credentials/certifications/online-exams) and the 120-minute format in [Exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience).
- 🛠️ **Do:** Run a 40-card flashcard sprint across all 4 domains (target 34/40); re-read your traps list; rerun the Pearson VUE system test; update `w26/exam-day.md` with a time plan (about 1 minute per question, flag long case studies, Learn only for exact facts). Done when: the sprint score is logged and the checklist is ticked.

### Wednesday 21 Apr · 45 min — Azure interview Q&A: developer and migration scenarios
- 📚 **Learn:** STAR-style answers backed by your own labs: a RAG backend on Azure, keyless auth, messaging choices, containers vs Functions, cost control, and migration (strategy choice, Azure Migrate/AppCAT, database cutover and rollback). Use the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/), your `w14/migration-plan.md` and [Choose an Azure compute service](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree).
- 🛠️ **Do:** Record yourself answering 6 questions, 2 minutes each: (1) migrate a Spring Boot + SQL app to Azure; (2) design TicketVerse's 'Ask' RAG backend; (3) Service Bus vs Event Grid vs Event Hubs; (4) secrets and identity end to end; (5) cut a surprising Azure bill; (6) debug a slow request across services. Replay and fix your weakest answer. Done when: 6 answers are outlined in `w26/interview.md` and one is re-recorded.

### Friday 23 Apr · 45 min — Delete everything, cost audit and next steps
- 📚 **Learn:** Cleanup checks (`az group list`, Cost Management by resource, soft-deleted Key Vaults), renewal (associate certifications renew yearly through a free online assessment) and next options: AI-103 (Azure AI Apps and Agents Developer) or AZ-305 (requires AZ-104). Use [Renew your certification](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification), the [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) and the [AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305).
- 🛠️ **Do:** Delete every lab RG; list soft-deleted vaults (`az keyvault list-deleted`) and purge lab vaults that lack purge protection; confirm Cost Management shows no running cost, and keep budgets on. Polish the `azure-labs` README (labs, diagrams, skills, certifications). Write `w26/next.md`: AI-103 or AZ-305 first, with a 12-week outline and dates. Done when: zero lab RGs, README polished and the next-steps plan committed.

### Saturday 24 Apr · 60 min — BOSS BATTLE: Sit AI-200 (or a final timed mock)
- 📚 **Learn:** Exam facts: 120 minutes, 700/1000 to pass, Microsoft Learn available in-exam with no extra time, breaks allowed but earlier questions lock ([exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)); retake after 24 hours if needed ([retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy)). Exam day borrows time from other blocks - plan for it.
- 🛠️ **Do:** Sit AI-200 (online or at a test centre) following `w26/exam-day.md`. If your exam is on another day, run a 60-minute timed mock instead: 40 practice-assessment questions plus 2 gauntlet tasks. Save the score report, add the badge to LinkedIn and update the certifications line on your resume. Done when: the score report (or mock result) is saved in `w26/` and your Season 6 retro is written.

## 📦 Deliverable (by Saturday night)
AI-200 passed (score report + badge) or retake booked; `w26/interview.md` with 6 answers; zero lab resources running; a polished `azure-labs` README; `w26/next.md` with your AI-103 or AZ-305 plan.

## ✅ Self-check (Sunday test preview)
- In 2 minutes: how would you migrate a Spring Boot + SQL Server app to Azure, and why that strategy?
- Design a keyless, observable RAG backend on Azure: which services, and why each one?
- Why did Microsoft replace AZ-204 with AI-200, and what does AI-200 prove to an employer?
- How do you guarantee nothing is still billing after a project ends?
- AI-103 vs AZ-305: which fits a Java + Azure + AI backend role next, and why?
- Tell the story of a failure you debugged in these labs and what you changed afterwards.

## 🚀 Stretch (optional)
Keep a 30-minute monthly 'Azure updates' habit with [John Savill's channel](https://www.youtube.com/@NTFAQGuy) and the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/).
