# ☁️ Azure Cloud · Week 01 — Cloud concepts and a safe Azure setup

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Cloud concepts are 25-30% of AZ-900 and the opening of almost every Azure interview (IaaS/PaaS/SaaS, shared responsibility). Building cost guardrails before you create anything is the habit that separates professionals from people who get surprise bills.

## 🗓️ Sessions

### Tuesday 27 Oct · 45 min — Cloud computing, shared responsibility and cloud models
- 📚 **Learn:** Cloud computing, the shared responsibility model, public/private/hybrid models and their use cases, the consumption-based model, pricing models and serverless. Use the Learn module [Describe cloud computing](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/), John Savill's [CapEx, OpEx and consumption](https://www.youtube.com/watch?v=WiwV9wb0GMo) and skim the skills list in the [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900).
- 🛠️ **Do:** Create the `azure-labs` repo with `w01/notes.md`. Draw the shared-responsibility table (rows: on-prem, IaaS, PaaS, SaaS; columns: OS patching, runtime, app code, data, identity). Predict first, then check the module: who patches the OS for App Service? Write 3 real use cases each for public, private and hybrid cloud using your company's Java + SQL stack. Done when: table + 9 use cases are committed and you can explain each model aloud in 60 seconds.

### Wednesday 28 Oct · 45 min — Cloud benefits and IaaS vs PaaS vs SaaS
- 📚 **Learn:** High availability vs scalability (vertical/horizontal) vs elasticity, reliability, predictability, security, governance and manageability; IaaS, PaaS and SaaS with use cases. Use [Describe the benefits of using cloud services](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/), [Describe cloud service types](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/) and Savill's [HA and scalability](https://www.youtube.com/watch?v=JRbhGzGzoOA).
- 🛠️ **Do:** In `w01/service-types.md` classify 12 offerings as IaaS, PaaS, SaaS or serverless with a one-line reason: VM running Tomcat, App Service, Azure SQL Database, Microsoft 365, AKS, Azure Functions, Container Apps, Cosmos DB, Dynamics 365, GitHub, Azure Virtual Desktop, on-prem Oracle (trick item). Add one elasticity example from your Spring Boot app. Done when: 12/12 classified and both module assessments passed.

### Friday 30 Oct · 45 min — Account strategy, budgets and alerts before anything else
- 📚 **Learn:** Azure free account ($200 credit for 30 days, 12-month free services, always-free services), spending limit, budgets (they alert, they never stop resources), action groups, tags. Read [Avoid charges with your free account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/avoid-charges-free-account), [Create and manage budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) and this track's COST_SAFETY_AND_ACCOUNT_SETUP.md.
- 🛠️ **Do:** Choose your path in COST_SAFETY_AND_ACCOUNT_SETUP.md: A = employer Visual Studio subscription now, B = Azure free account on W6 Tue. Path A: create a small monthly budget (e.g., INR 500) with 50/80/100% actual and 100% forecast alerts to your email. Path B: write `w01/guardrails.md` with the exact clicks + CLI you will run first on activation day. Done when: the budget shows in Cost Management (A) or the guardrails runbook is reviewed line by line (B).

### Saturday 31 Oct · 60 min — LAB: Azure CLI, Cloud Shell and your lab guardrail kit
- 📚 **Learn:** Azure CLI install and login, `az account show`, output formats (`-o table`) and JMESPath `--query`, Cloud Shell ephemeral sessions (no storage account needed), one resource group per lab + teardown. Use [Get started with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli), [Query Azure CLI results](https://learn.microsoft.com/en-us/cli/azure/use-azure-cli-successfully-query) and [Cloud Shell ephemeral sessions](https://learn.microsoft.com/en-us/azure/cloud-shell/get-started/ephemeral).
- 🛠️ **Do:** Run `az bicep install` (Azure CLI is installed; the Bicep VS Code extension is blocked on your company laptop, so check `.bicep` files with `az bicep build`). Write `scripts/new-lab.sh` (creates `rg-lab-wNN` tagged owner/week/expires) and `scripts/nuke-lab.sh` (`az group delete --yes --no-wait`). Path A: run both in Cloud Shell and confirm with `az group list -o table`. Path B: run `az version` and read `az group create --help`. Done when: both scripts are committed and either executed (A) or dry-run explained in comments (B).

## 📦 Deliverable (by Saturday night)
`azure-labs` repo with `w01/` notes (shared-responsibility table, 12 service-type classifications), `scripts/new-lab.sh` + `scripts/nuke-lab.sh`, and your account path decided (A: budget + alerts live; B: guardrails runbook ready for W6 Tue).

## ✅ Self-check (Sunday test preview)
- Explain the shared responsibility model for IaaS vs PaaS vs SaaS: who patches the OS and who always owns the data?
- Scalability vs elasticity vs high availability: give a Spring Boot example of each.
- When would a bank choose hybrid cloud, and what is the main benefit of the consumption-based model?
- Why is serverless not 'no servers'? Name two Azure serverless services.
- Does an Azure budget stop resources when it is exceeded? What actually protects a free account?
- Which Azure CLI flag returns only selected JSON fields, and how do you print a table?

## 🚀 Stretch (optional)
Watch the first 30 minutes of Savill's [Azure Master Class v3 Part 1](https://www.youtube.com/watch?v=BqNbzeuxTaE) or, in Hindi, the opening videos of [AZ-900 Full Course in Hindi](https://www.youtube.com/playlist?list=PLks8W396lro4RpDs-teA87oaGH6nRU5Zf).
