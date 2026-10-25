# ☁️ Azure Cloud · Week 04 — Governance, cost, monitoring tools + AZ-900 Boss

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Management and governance is 30-35% of AZ-900 and what managers ask about first: cost control, Policy, locks, infrastructure as code and monitoring. Season 1 ends with a timed Boss Battle that proves you are exam-ready.

## 🗓️ Sessions

### Tuesday 17 Nov · 45 min — Cost factors, pricing calculator, Cost Management and tags
- 📚 **Learn:** What drives cost (resource type, consumption, region, bandwidth, reservations, Azure Hybrid Benefit), the pricing calculator, Cost Management and budgets, tags for cost allocation. Read [Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/). Optional: the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/).
- 🛠️ **Do:** Estimate TicketVerse v1 in the pricing calculator (Central India): App Service B1, PostgreSQL Flexible Server Burstable B1ms, the smallest Azure Managed Redis SKU and 50 GB of Hot LRS blob. Export the estimate, then change the region and add a 1-year reservation and record the deltas. Write a 4-tag standard (owner, env, costCenter, week). Done when: estimate + 3 cost levers + tag standard committed.

### Wednesday 18 Nov · 45 min — Microsoft Purview, Azure Policy and resource locks
- 📚 **Learn:** Microsoft Purview (data governance and compliance), Azure Policy (definitions, initiatives, effects such as deny, audit and modify), resource locks (CanNotDelete vs ReadOnly) and how they differ from RBAC. Read [Describe features and tools for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/). Optional: Savill's [Azure Policy](https://www.youtube.com/watch?v=z7WMqHE3R8g).
- 🛠️ **Do:** In `w04/governance.md` answer 4 scenarios with tool + scope + effect: (1) block resources outside India regions, (2) stop accidental deletion of the prod database, (3) every resource must carry costCenter, (4) find where customer PII lives across data stores. Path A: put a CanNotDelete lock on a test RG, try `az group delete`, read the error, remove the lock. Done when: 4 answers (+ lock evidence for Path A) committed.

### Friday 20 Nov · 45 min — Management tools, Azure Arc, ARM/IaC and monitoring tools
- 📚 **Learn:** Portal, Cloud Shell, Azure CLI vs Azure PowerShell, Azure Arc, infrastructure as code, ARM and ARM templates; Azure Advisor, Service Health, Azure Monitor (Log Analytics, alerts, Application Insights). Read [Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/). Optional (the monitoring half): [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/).
- 🛠️ **Do:** Write a 10-row 'which tool?' quiz with answers (e.g., regional outage notice -> Service Health; idle VM -> Advisor; govern on-prem Linux servers -> Arc; repeatable deployment -> ARM/Bicep; slow API trace -> Application Insights). Then write the same resource-group command in CLI (`az group create`) and PowerShell (`New-AzResourceGroup`). Done when: quiz + both commands committed and the module assessment passed.

### Saturday 21 Nov · 60 min — BOSS BATTLE: AZ-900 readiness - timed practice run and speed round
- 📚 **Learn:** All three AZ-900 domains under time pressure, plus exam logistics (45-minute exam, 700/1000 to pass, the name on your ID must match your profile). Use the free [AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23). Optional, after the timer: John Savill's [AZ-900 Study Cram](https://www.youtube.com/watch?v=tQp1YkB2Tgs).
- 🛠️ **Do:** Timer on. 0-25 min: practice assessment run 1 (target 85%+). 25-35: log every miss by domain in `w04/boss.md`. 35-55: speed round - answer your W1-W4 flashcards and the 'which tool?' quiz aloud, 30 seconds each, marking misses. 55-60: confirm the AZ-900 booking (Fri 27 Nov) and set reminders. Run 2 waits until W5 Tue so it measures learning, not memory. Done when: the run-1 score, miss log and speed-round misses are saved (below 85%? keep the date and fix weak domains in W5).

## 📦 Deliverable (by Saturday night)
`w04/` cost estimate + tag standard, governance answers, tool quiz, and `boss.md` with the run-1 score, a miss log by domain and speed-round results; AZ-900 booking for 27 Nov 2026 confirmed.

## ✅ Self-check (Sunday test preview)
- Name five factors that change an Azure bill and one lever to reduce each.
- Azure Policy vs RBAC vs resource locks: which one stops a Contributor from deleting a resource?
- What does Microsoft Purview do that Azure Policy does not?
- What is Azure Arc and when would a company with on-prem servers use it?
- ARM template vs Bicep vs CLI script: what do 'declarative' and 'idempotent' mean here?
- Azure Advisor vs Service Health vs Azure Monitor: which tells you about a regional outage?
- What is Application Insights and how is it related to Log Analytics?

## 🚀 Stretch (optional)
Watch Microsoft Learn's [AZ-900 management and governance video](https://www.youtube.com/watch?v=dHdvHqKCPHw) and turn 5 surprises into flashcards.
