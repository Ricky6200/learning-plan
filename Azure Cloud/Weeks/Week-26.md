# ☁️ Azure Cloud · Week 26 — AI-200 exam week and Season 6 kickoff

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-26.md) · [Week 27 →](Week-27.md)

**Why this week:** This week turns six months of labs into your third credential: AI-200 proves you can build AI back ends on Azure. A light Saturday then sets up the migration toolkit for Season 6 - the 'handle Azure migration' half of your goal.

## 🗓️ Sessions

### Tuesday 20 Apr · 45 min — Final AI-200 revision + exam-day checklist
- 📚 **Learn:** Your `w25/gaps.csv`, flashcards and the AI-200 study guide's skills list, plus the online-exam rules in [About online exams with Pearson VUE](https://learn.microsoft.com/en-us/credentials/certifications/online-exams). Optional: the 120-minute format in [Exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience).
- 🛠️ **Do:** Run a 40-card flashcard sprint across all 4 domains (target 34/40); re-read your traps list; rerun the Pearson VUE system test; write `w26/exam-day.md` with a time plan (about 1 minute per question, flag long case studies, Learn only for exact facts). Done when: the sprint score is logged and the checklist is ticked.

### Wednesday 21 Apr · 45 min — Practice run 3 and weakest-domain repair
- 📚 **Learn:** Final calibration on the AI-200 practice assessment (as in W25), then repair your weakest domain from its module in the [AI-200 course](https://learn.microsoft.com/en-us/training/courses/ai-200t00) - one unit, not the whole module.
- 🛠️ **Do:** Practice run 3 (target 85%+). For each remaining miss, write the correct answer and its doc link in `w25/gaps.csv`, then work through one Learn unit on your weakest domain. Stop studying by 10 pm. Done when: the run-3 score is logged and no objective in `gaps.csv` lacks a fix note.

### Friday 23 Apr · 45 min — EXAM: Sit AI-200 (swap with Saturday if you booked Sat)
- 📚 **Learn:** No new content - 10 minutes on your traps list. Facts: 120 minutes, 700/1000 to pass, Microsoft Learn available in-exam with no extra time, and after a break you can't return to earlier questions ([exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)). Retake after 24 hours if needed (Optional: [retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy)). Exam day borrows time from other blocks - plan for it.
- 🛠️ **Do:** Sit AI-200 (online or at a test centre) following `w26/exam-day.md`: answer what you know first, flag long case studies, use Learn only for exact facts. Save the score report, add the badge to LinkedIn and update the certifications line on your resume. If you don't pass: note the per-domain bars, book the retake and plan two fix sessions inside W27. Done when: the score report is saved in `w26/`.

### Saturday 24 Apr · 60 min — LAB: Exam retro + migration toolkit for Season 6
- 📚 **Learn:** Season 6 migrates a Java + SQL Server app, so set up the tools in your Codespace now: SqlPackage (BACPAC export/import), SQL Server 2022 in a container as the 'on-premises' source, and AppCAT for Java (a code-assessment CLI). Read [Download and install SqlPackage](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-download). Optional: the [AppCAT 7 quickstart](https://learn.microsoft.com/en-us/azure/migrate/appcat/appcat-7-quickstart).
- 🛠️ **Do:** 15 min: retro in `w26/retro.md` - score by domain vs your practice runs, what worked, which labs to reuse in interviews. 25 min, in a 2-core Codespace on `azure-labs`: `dotnet tool install -g microsoft.sqlpackage`; download the AppCAT 7 Linux tarball and add it to PATH; start SQL Server 2022 (`docker run -e ACCEPT_EULA=Y -e MSSQL_SA_PASSWORD=<pwd> -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest`) and run `SELECT @@VERSION` with the container's bundled sqlcmd. Stop the Codespace. Done when: the retro is committed and all three tools respond.

## 📦 Deliverable (by Saturday night)
AI-200 passed (score report + badge) or retake booked; `w26/exam-day.md` and `w26/retro.md`; a Codespace with SqlPackage, AppCAT and SQL Server 2022 ready for Season 6.

## ✅ Self-check (Sunday test preview)
- Which AI-200 domain was weakest on your score report, and which lab would you redo to fix it?
- Why did Microsoft replace AZ-204 with AI-200, and what does AI-200 prove to an employer?
- Walk through a keyless RAG request on Azure: which identity calls which service, with which role?
- What is a BACPAC, and when would SqlPackage export/import be the wrong migration tool?
- What does AppCAT for Java assess, and which Azure targets can it check against?
- Associate certifications expire yearly: how do you renew them, and what does it cost?

## 🚀 Stretch (optional)
Skim the [SQL Server to Azure SQL Database migration guide](https://learn.microsoft.com/en-us/data-migration/sql-server/database/guide) to preview W27's options.
