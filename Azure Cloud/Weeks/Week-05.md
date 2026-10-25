# ☁️ Azure Cloud · Week 05 — AZ-900 exam week and AZ-104 kickoff

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** Passing AZ-900 gives you a first credential and momentum for Season 2. Saturday sets up the personal laptop where every live lab runs from now on and starts AZ-104, moving you from 'describe' to 'do' - the CLI, PowerShell and templates administrators use daily.

## 🗓️ Sessions

### Tuesday 24 Nov · 45 min — Practice run 2 and four weak objectives
- 📚 **Learn:** Your `w04/boss.md` miss log and the matching chapters of John Savill's [AZ-900 Study Cram](https://www.youtube.com/watch?v=tQp1YkB2Tgs) at 1.5x speed (jump using the chapter list). Optional: the matching objectives in the [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900).
- 🛠️ **Do:** 0-25 min: practice assessment run 2, timed (target 85%+); add new misses to `w04/boss.md`. Then take your 4 weakest objectives: for each, watch its cram chapter and write a 3-line explanation plus one exam trap (e.g., an availability set is not an availability zone; budgets don't stop spend; Policy is not RBAC). Done when: run 2 is logged and 4 objectives are rewritten (below 85%? repeat the weakest 2 on Wednesday).

### Wednesday 25 Nov · 45 min — Exam logistics rehearsal and flashcard sprint
- 📚 **Learn:** Online proctoring rules: system test, ID/name match, closed room, breaks. Read [About online exams with Pearson VUE](https://learn.microsoft.com/en-us/credentials/certifications/online-exams). Optional: [Exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience).
- 🛠️ **Do:** Run the Pearson VUE system test on the exact laptop and network you'll use; confirm your Microsoft Learn profile name matches your government ID; click through the exam sandbox (aka.ms/examdemo). Do a 20-card rapid-fire from your flashcards. Write `w05/exam-day.md` (time, ID, desk, phone away, flag-and-move rule). Done when: system test passed, checklist committed and flashcards 18/20 or better.

### Friday 27 Nov · 45 min — EXAM: Sit AZ-900 (swap with Saturday if you booked Sat)
- 📚 **Learn:** No new content. Re-read `w05/exam-day.md` and your traps list for 10 minutes. Exam facts: 45 minutes, 700/1000 to pass, no penalty for wrong answers, and Microsoft Learn is not available on Fundamentals exams ([official note](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)). Exam day borrows about 30 minutes from another block - that's fine once.
- 🛠️ **Do:** Check in 30 minutes early (online) with your government ID. Answer every question; flag anything taking over 60 seconds and return to it later. After the exam, save the score report and add the badge to LinkedIn. If you don't pass, book the retake (24-hour minimum wait) and log weak domains from the score report. Done when: the exam is taken and the score report is saved in `w05/`.

### Saturday 28 Nov · 60 min — LAB: Personal-laptop Azure workstation + AZ-104 skills map
- 📚 **Learn:** From W6 every live lab runs on your personal laptop: the company laptop blocks personal sign-in and the Azure VS Code extensions, and cross-track code reaches you through GitHub. AZ-104 domains, weights and expected tools (PowerShell, CLI, portal, ARM/Bicep, Entra ID). Read the [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104). Optional: [Install Azure PowerShell on Windows](https://learn.microsoft.com/en-us/powershell/azure/install-azps-windows).
- 🛠️ **Do:** Personal laptop: install Azure CLI + `az bicep install`, PowerShell 7 + `Install-Module Az -Scope CurrentUser`, Git, VS Code with the Azure and Bicep extensions, uv + Python 3.12 and JDK 25; clone `azure-labs`; print `az version`, `Get-InstalledModule Az` and `java -version`. Fallback: commit `.devcontainer/devcontainer.json` (universal image + `azure-cli` feature) so a 2-core Codespace works too. Then write `w05/az104-map.md`: the 5 domains with weights and every bullet tagged with its plan week (W6-W15). Done when: versions are logged and the map is committed.

## 📦 Deliverable (by Saturday night)
AZ-900 passed (score report + badge saved) or retake booked; `w05/exam-day.md`; the personal laptop ready (Azure CLI + Bicep, PowerShell 7 + Az, Git, VS Code extensions, uv + Python 3.12, JDK 25) with a Codespaces fallback; `w05/az104-map.md`.

## ✅ Self-check (Sunday test preview)
- Which AZ-900 domain was weakest on your score report, and what will you do differently for AZ-104?
- What are the five AZ-104 domains and their weights?
- Why do your live labs run on the personal laptop, and what is your fallback if it is unavailable?
- Azure CLI vs Azure PowerShell: write the command to list resource groups in each.
- What is idempotency in ARM deployments and why does it matter in CI/CD?
- Can you use Microsoft Learn during the AZ-104 exam? What's the catch?

## 🚀 Stretch (optional)
Watch Microsoft Learn's [AZ-104 course introduction](https://www.youtube.com/watch?v=6rs-oGmz3pk) and skim the [AZ-104 lab index](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/) to preview the Saturday labs.
