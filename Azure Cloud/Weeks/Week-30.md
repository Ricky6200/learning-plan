# ☁️ Azure Cloud · Week 30 — Capstone: migrate and modernise + Final Boss

> 📅 **Mon 17 May 2027 → Sun 23 May 2027** · Season 6 — Final Boss: The Offer · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 29](Week-29.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-30.md)

**Why this week:** The finish line: one timed, end-to-end migration proves the whole journey - move the data, modernise the app with managed identity and infrastructure as code, ship it through CI/CD and observe it - plus sharp interview answers, a subscription that costs nothing and a clear next step (AZ-305 or AI-103).

## 🗓️ Sessions

### Tuesday 18 May · 45 min — Azure interview Q&A: developer and migration scenarios
- 📚 **Learn:** STAR-style answers backed by your own labs: a RAG backend on Azure, keyless auth, messaging choices, containers vs Functions, cost control, and migration (strategy choice, Azure Migrate and AppCAT, the Azure SQL target, database cutover and rollback, landing zones). Read [Choose an Azure compute service](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree). Optional: the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/).
- 🛠️ **Do:** Record yourself answering 6 questions, 2 minutes each: (1) migrate a Spring Boot + SQL Server app with stored procedures to Azure; (2) design TicketVerse's 'Ask' RAG backend; (3) Service Bus vs Event Grid vs Event Hubs; (4) secrets and identity end to end; (5) cut a surprising Azure bill; (6) debug a slow request across services. Replay and fix your weakest answer. Done when: 6 answers are outlined in `w30/interview.md` and one is re-recorded.

### Wednesday 19 May · 45 min — Capstone prep: target Bicep, OIDC pipeline and timed runbook
- 📚 **Learn:** Saturday migrates `legacy-orders` end to end against the clock, so script it now: a Bicep target (Linux B1 App Service, Java SE, system-assigned identity; Azure SQL free-tier database with Entra-only auth; Application Insights wired in with the connection string and `ApplicationInsightsAgent_EXTENSION_VERSION=~3` app settings), a GitHub Actions workflow that builds the JAR and deploys with `azure/login` (your W22 identity) and `azure/webapps-deploy`, and a minute-by-minute runbook. Read [Deploy to App Service using GitHub Actions](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions). Optional: [Passwordless connections with Azure SQL for Java](https://learn.microsoft.com/en-us/azure/developer/java/spring-framework/migrate-sql-database-to-passwordless-connection).
- 🛠️ **Do:** Create an empty `rg-capstone`, write `w30/target.bicep` (reuse W27 Tue's settings and W28's modules) and run `az deployment group what-if`. Add `.github/workflows/legacy-orders.yml` to `azure-labs` (`workflow_dispatch`, `permissions: id-token: write`, Maven build, `azure/login@v2`, `azure/webapps-deploy`) and give your W22 identity Website Contributor on `rg-capstone`. Draft `w30/runbook.md` with timed steps and a rollback point. Done when: what-if is clean, the workflow's build job passes and the runbook is committed.

### Friday 21 May · 45 min — Delete everything else, cost audit and next steps
- 📚 **Learn:** Cleanup checks (`az group list`, Cost Management by resource, soft-deleted Key Vaults, leftover deployment stacks), renewal (associate certifications renew yearly through a free online assessment on Learn) and next options: AZ-305 (Azure Solutions Architect Expert; requires AZ-104) or AI-103 (Azure AI Apps and Agents Developer). Read the [AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305). Optional: the [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103).
- 🛠️ **Do:** Delete every lab RG except `rg-capstone` (and the TicketVerse stack once Java is done: `az stack group delete --action-on-unmanage deleteAll`); list soft-deleted vaults (`az keyvault list-deleted`) and purge lab vaults without purge protection; confirm Cost Management shows no running cost and keep the budgets on. Polish the `azure-labs` README (labs, diagrams, skills, certifications). Write `w30/next.md`: AZ-305 or AI-103 first, with a 12-week outline and dates. Done when: only `rg-capstone` remains, the README is polished and the plan is committed.

### Saturday 22 May · 60 min — BOSS BATTLE: Migrate and modernise legacy-orders end to end (timed)
- 📚 **Learn:** Final Boss rules: 60 minutes, follow `w30/runbook.md`, scripts and pipeline only (the portal for viewing and the SQL Query editor), evidence or it didn't happen. The app reaches Azure SQL as its managed identity: as Entra admin run `CREATE USER [<app>] FROM EXTERNAL PROVIDER`, add it to db_datareader and db_datawriter and `GRANT EXECUTE`. Reference: [Connect App Service to Azure SQL with a managed identity](https://learn.microsoft.com/en-us/azure/app-service/tutorial-connect-msi-azure-database).
- 🛠️ **Do:** 0-5: `az stack group create` the target from `target.bicep`. 5-20: export the source with SqlPackage in your Codespace; import it into the new database (access token). 20-30: create the app's database user and grants in the Query editor; set the passwordless JDBC URL as an app setting. 30-40: run the deploy workflow (`gh workflow run`), smoke-test `/orders/42`, find the request in Application Insights. 40-50: compare row counts and procedure output, record step times, declare cutover. 50-60: delete the stack, stop the Codespace, prove no lab RGs remain. Done when: every step is evidenced in `w30/boss.md` within 60 minutes.

## 📦 Deliverable (by Saturday night)
`w30/interview.md` (6 answers), `target.bicep` + the OIDC `legacy-orders.yml` workflow, `runbook.md` and `boss.md` with timed evidence, `w30/next.md`, a polished `azure-labs` README, and zero lab resources running (budgets kept).

## ✅ Self-check (Sunday test preview)
- In 2 minutes: how would you migrate a Spring Boot + SQL Server app with stored procedures to Azure, and why that strategy?
- Design a keyless, observable RAG backend on Azure: which services, and why each one?
- Walk through your capstone runbook: where is the point of no return, and how do you roll back before it?
- How does the app's managed identity get access to Azure SQL, and why is that safer than a SQL login?
- How do you guarantee nothing is still billing after a project ends?
- AZ-305 vs AI-103: which fits a Java + Azure + AI backend role next, and why?
- Tell the story of a failure you debugged in these labs and what you changed afterwards.

## 🚀 Stretch (optional)
Keep a 30-minute monthly 'Azure updates' habit with [John Savill's channel](https://www.youtube.com/@NTFAQGuy) and the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/).
