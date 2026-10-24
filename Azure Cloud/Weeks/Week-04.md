# ☁️ Azure Cloud · Week 04 — Governance, cost, monitoring tools + AZ-900 Boss

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Management and governance is 30-35% of AZ-900 and what managers ask about first: cost control, Policy, locks, infrastructure as code and monitoring. Season 1 ends with a timed Boss Battle that proves you are exam-ready.

## 🗓️ Sessions

### Tuesday 17 Nov · 45 min — Cost factors, pricing calculator, Cost Management and tags
- 📚 **Learn:** What drives cost (resource type, consumption, region, bandwidth, reservations, Azure Hybrid Benefit), the pricing calculator, Cost Management and budgets, tags for cost allocation. Use [Describe cost management in Azure](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/), the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) and Savill's [Factors that affect costs](https://www.youtube.com/watch?v=fMShW_RGcxY).
- 🛠️ **Do:** Estimate TicketVerse v1 in the pricing calculator (Central India): App Service B1, PostgreSQL Flexible Server Burstable B1ms, the smallest Azure Managed Redis SKU and 50 GB of Hot LRS blob. Export the estimate, then change the region and add a 1-year reservation and record the deltas. Write a 4-tag standard (owner, env, costCenter, week). Done when: estimate + 3 cost levers + tag standard committed.

### Wednesday 18 Nov · 45 min — Microsoft Purview, Azure Policy and resource locks
- 📚 **Learn:** Microsoft Purview (data governance and compliance), Azure Policy (definitions, initiatives, effects such as deny, audit and modify), resource locks (CanNotDelete vs ReadOnly) and how they differ from RBAC. Use [Describe features and tools for governance and compliance](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/), Savill's [Azure Policy](https://www.youtube.com/watch?v=z7WMqHE3R8g) and [Resource locks](https://www.youtube.com/watch?v=eF_KilJRxbE).
- 🛠️ **Do:** In `w04/governance.md` answer 4 scenarios with tool + scope + effect: (1) block resources outside India regions, (2) stop accidental deletion of the prod database, (3) every resource must carry costCenter, (4) find where customer PII lives across data stores. Path A: put a CanNotDelete lock on a test RG, try `az group delete`, read the error, remove the lock. Done when: 4 answers (+ lock evidence for Path A) committed.

### Friday 20 Nov · 45 min — Management tools, Azure Arc, ARM/IaC and monitoring tools
- 📚 **Learn:** Portal, Cloud Shell, Azure CLI vs Azure PowerShell, Azure Arc, infrastructure as code, ARM and ARM templates; Azure Advisor, Service Health, Azure Monitor (Log Analytics, alerts, Application Insights). Use [Describe features and tools for managing and deploying Azure resources](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/) and [Describe monitoring tools in Azure](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/).
- 🛠️ **Do:** Write a 10-row 'which tool?' quiz with answers (e.g., regional outage notice -> Service Health; idle VM -> Advisor; govern on-prem Linux servers -> Arc; repeatable deployment -> ARM/Bicep; slow API trace -> Application Insights). Then write the same resource-group command in CLI (`az group create`) and PowerShell (`New-AzResourceGroup`). Done when: quiz + both commands committed and both module assessments passed.

### Saturday 21 Nov · 60 min — BOSS BATTLE: AZ-900 readiness - two timed practice runs, book exam
- 📚 **Learn:** All three AZ-900 domains under time pressure, plus exam logistics (45-minute exam, 700/1000 to pass, the name on your ID must match your profile). Use the free [AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23), the [exam sandbox](https://aka.ms/examdemo) and John Savill's [AZ-900 Study Cram](https://www.youtube.com/watch?v=tQp1YkB2Tgs) for review.
- 🛠️ **Do:** Timer on. 0-25 min: practice assessment run 1 (target 85%+). 25-30: log every miss by domain in `w04/boss.md`. 30-55: run 2 (target 85%+). 55-60: book AZ-900 on Pearson VUE for Fri 27 Nov (or Sat 28 Nov) 2026. Misses feed W5 Tue/Wed cram review. Done when: two scores of 85%+ and the booking confirmation are saved (below 85%? book anyway and fix weak domains in W5).

## 📦 Deliverable (by Saturday night)
`w04/` cost estimate + tag standard, governance answers, tool quiz, `boss.md` with two practice scores and a miss log by domain, and the AZ-900 booking confirmation for 27/28 Nov 2026.

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
