# ☁️ Azure Cloud · Week 15 — AZ-104 exam prep: practice, go/no-go + Boss

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** AZ-104 is a hands-on administrator exam (100 minutes; Microsoft Learn is open but the clock keeps running). Practice runs, cram review and a go/no-go gate decide whether you sit next week, and Season 3 ends with a timed Boss that simulates the exam.

## 🗓️ Sessions

### Tuesday 02 Feb · 45 min — Practice assessment run 1 and a weighted gap log
- 📚 **Learn:** Exam reality: case studies, multi-part items, possibly labs; Microsoft Learn is allowed on associate exams but no extra time is added. Use the free [AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21). Optional: the [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104).
- 🛠️ **Do:** Take the practice assessment timed (stop at 40 minutes if needed). Log every miss in `w15/gaps.csv` (domain, objective, why wrong, doc link). Rank objectives by domain weight x misses and pick your top 5 focus objectives. Confirm your AZ-104 booking for Fri 12 Feb 2027 (made in W10). Done when: score recorded, top-5 list committed and the booking confirmed.

### Wednesday 03 Feb · 45 min — AZ-104 Study Cram v2 on your top-5 gaps
- 📚 **Learn:** John Savill's [AZ-104 Study Cram v2](https://www.youtube.com/watch?v=0Knf9nub4-k) - jump via chapters to your top-5 objectives at 1.5x speed. Optional: Microsoft Learn's [AZ-104 exam prep session](https://www.youtube.com/watch?v=w_G1Rufop-s) for exam-taking tips.
- 🛠️ **Do:** For each top-5 objective: watch its cram chapter, then prove it with a 5-minute CLI or portal micro-task (e.g., stored access policy, effective NSG rules, slot swap, budget + action group, lifecycle rule). Done when: 5 micro-tasks are evidenced in `w15/` and each gap is marked fixed in `gaps.csv`.

### Friday 05 Feb · 45 min — Practice run 2, go/no-go gate and Learn lookup drill
- 📚 **Learn:** Second practice run, then the gate: run 2 at 80%+ means go; 75-79% means go only if no domain is weak; below 75% means reschedule - free if done at least 24 hours before the appointment. Use the [AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21). Optional: the [reschedule and cancellation policy](https://learn.microsoft.com/en-us/credentials/support/reschedule-and-cancellation-policy).
- 🛠️ **Do:** Practice run 2 (target 80%+). Apply the gate and write the decision in `w15/go-no-go.md`; if it's no-go, reschedule today and plan the extra week. Then a 10-item 'Learn lookup race' for facts you missed (under 90 seconds each) and note which doc pages to open first during the exam. Done when: the run-2 score, the go/no-go decision and lookup times are logged in `w15/`.

### Saturday 06 Feb · 60 min — BOSS BATTLE: Timed AZ-104 gauntlet - exam simulation
- 📚 **Learn:** Season 3 integration: mixed AZ-104 tasks against the clock. References for after the timer only: the [AZ-104 lab index](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/) and your own `scripts/` folder.
- 🛠️ **Do:** 45-minute timer, no notes, 6 tasks: (1) custom role + assignment; (2) Allowed locations policy; (3) storage account with SAS and firewall; (4) VM with a data disk; (5) NSG rule allowing 443 from an ASG + effective rules check; (6) metric alert with an action group. Then 15 minutes: verify each task, record time per task and delete everything. Done when: 5/6 or more completed in time and results are logged in `w15/boss.md`.

## 📦 Deliverable (by Saturday night)
`w15/gaps.csv`, two practice scores, the go/no-go decision (and new date if rescheduled), 5 fixed micro-tasks, lookup-race times, Boss gauntlet results in `w15/boss.md` and the confirmed AZ-104 booking.

## ✅ Self-check (Sunday test preview)
- Which three AZ-104 objectives are still weakest for you, and what is your 48-hour fix?
- When should you use Microsoft Learn during the exam, and when should you just flag and move on?
- Walk through troubleshooting 'VM can't reach storage over a private endpoint' in 5 steps.
- How do you let a user manage only VMs in one RG without touching networking?
- How do you recover a deleted blob, a deleted container and a deleted file share?
- What is the minimum App Service tier for slots, autoscale and backups?
- What is your go/no-go rule, and what does rescheduling cost if you do it at least 24 hours ahead?

## 🚀 Stretch (optional)
Watch Microsoft Learn's exam-readiness episode [Preparing for AZ-104 (1 of 5)](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-az-104-manage-azure-identities-and-governance-1-of-5) and continue with the rest of that series.
