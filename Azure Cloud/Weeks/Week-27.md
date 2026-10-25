# ☁️ Azure Cloud · Week 27 — Migration I: SQL Server and Java apps

> 📅 **Mon 26 Apr 2027 → Sun 02 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 26](Week-26.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-27.md) · [Week 28 →](Week-28.md)

**Why this week:** Most enterprise Java apps sit on SQL Server with stored procedures. Choosing the right Azure SQL target, assessing servers and code, moving the database and switching the app to passwordless access is exactly the 'handle Azure migration' skill you set out to build - and a strong interview story.

## 🗓️ Sessions

### Tuesday 27 Apr · 45 min — Azure SQL targets: SQL Database vs Managed Instance vs SQL VM
- 📚 **Learn:** Azure SQL Database (single database, elastic pools, serverless, Hyperscale), Managed Instance (near-100% SQL Server compatibility: SQL Agent, cross-database queries, CLR, linked servers) and SQL Server on Azure VMs (full OS access); vCore vs DTU; migration paths (BACPAC with SqlPackage, DMS offline, Managed Instance link for near-zero downtime). Read [What is Azure SQL?](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview). Optional: the [Azure SQL Database free tier](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-tier).
- 🛠️ **Do:** In `w27/sql-target.md` pick SQL Database, Managed Instance or SQL Server on VM for 5 workloads with one reason each: 40 stored procedures; SQL Agent jobs + cross-database queries; a vendor app needing OS access; 200 small tenant databases; a 10 TB OLTP database. Then create the target: `az sql server create --enable-ad-only-auth` with you as Entra admin (`--external-admin-name`, `--external-admin-sid`; or W6's `labadmin` if your personal account can't sign in), and `az sql db create ... --use-free-limit true --free-limit-exhaustion-behavior AutoPause`. Done when: 5 choices are committed and `az sql db show` reports `useFreeLimit: true`.

### Wednesday 28 Apr · 45 min — Assess: Azure Migrate CSV import, business case, AppCAT
- 📚 **Learn:** Azure Migrate discovers servers with an appliance or - with no appliance - from an imported CSV; assessments give readiness, right-sized targets and monthly cost; a business case adds TCO, savings and Azure Hybrid Benefit. AppCAT for Java checks code against a target (App Service, AKS, Container Apps). Read [Build a business case or assess servers using an imported CSV file](https://learn.microsoft.com/en-us/azure/migrate/tutorial-discover-import). Optional: [Build a business case](https://learn.microsoft.com/en-us/azure/migrate/how-to-build-a-business-case).
- 🛠️ **Do:** Create an Azure Migrate project (free) and import a 5-server CSV from the portal template - 2 app VMs, 1 SQL Server, 1 file server, 1 batch server, invented values only. Create an Azure VM assessment and a business case; record readiness, sizes and monthly cost. Then, in your Codespace, run `appcat analyze --input <ticketverse-clone> --target azure-container-apps --output w27/appcat` and list the top 3 findings with a fix each. Done when: assessment, business-case numbers and AppCAT findings are in `w27/assess.md`.

### Friday 30 Apr · 45 min — Database migration methods + the legacy source app
- 📚 **Learn:** Offline vs online: BACPAC export/import with SqlPackage (simple; downtime = export + import time), Azure Database Migration Service (offline to SQL Database with a self-hosted integration runtime; online to Managed Instance), cutover, validation and rollback. Read the [SQL Server to Azure SQL Database migration guide](https://learn.microsoft.com/en-us/data-migration/sql-server/database/guide) (migration options). Optional: [Migrate with DMS](https://learn.microsoft.com/en-us/data-migration/sql-server/database/database-migration-service).
- 🛠️ **Do:** In your Codespace start SQL Server 2022 and run `w27/source/orders.sql`: tables `customers` and `orders`, procedures `usp_PlaceOrder` and `usp_GetOrdersByCustomer`, 1,000 seed rows - your day job, so write it yourself. Generate a Spring Boot app `legacy-orders` (Spring Initializr: Web, JDBC, MS SQL Server Driver) whose `GET /orders/{customerId}` calls the procedure through `JdbcTemplate`, using SQL auth from an environment variable. Done when: curl returns orders from the source database.

### Saturday 01 May · 60 min — LAB: Migrate legacy-orders to Azure SQL with passwordless JDBC
- 📚 **Learn:** Passwordless JDBC: add `azure-identity`, drop user and password, set `authentication=ActiveDirectoryDefault` (mssql-jdbc 12.2+). DefaultAzureCredential uses your `az login` locally and the app's managed identity in Azure, where you create its database user with `CREATE USER [app-name] FROM EXTERNAL PROVIDER`. Read [Connect using Microsoft Entra authentication](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-using-azure-active-directory-authentication) (ActiveDirectoryDefault). Optional: [SqlPackage Import](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-import).
- 🛠️ **Do:** 45-minute timer. 0-10: `sqlpackage /Action:Export` the source to `orders.bacpac`. 10-20: allow the Codespace's IP on the server firewall; `sqlpackage /Action:Import` into your empty free-tier database with `/AccessToken:` from `az account get-access-token --resource https://database.windows.net/`. 20-30: compare row counts and `EXEC usp_GetOrdersByCustomer 42` on both sides (portal Query editor for Azure). 30-40: switch `legacy-orders` to the passwordless URL and smoke test. 40-45: write `w27/runbook.md` (cutover, rollback, decommission); delete `rg-lab-w27`. Done when: the app serves migrated data with no password.

## 📦 Deliverable (by Saturday night)
`w27/sql-target.md` (5 justified targets), `assess.md` (Azure Migrate assessment, business case, AppCAT top findings), `source/orders.sql` + the `legacy-orders` app, and `runbook.md` with row-count and stored-procedure evidence from Azure SQL - with `rg-lab-w27` deleted (W30 rebuilds it from code).

## ✅ Self-check (Sunday test preview)
- SQL Database vs Managed Instance vs SQL Server on VM: which fits an app using SQL Agent jobs and cross-database queries, and why?
- What does the Azure SQL Database free tier give you, and what happens when the monthly limits run out?
- How does Azure Migrate assess servers without an appliance, and what can't you do with CSV-imported servers?
- What does a business case add on top of an assessment?
- Name three AppCAT findings you'd expect in a Spring Boot app and how you'd fix each.
- BACPAC export/import vs DMS: which gives less downtime, and what limits BACPAC?
- How does `authentication=ActiveDirectoryDefault` work locally vs on App Service, and which SQL statement grants a managed identity access?

## 🚀 Stretch (optional)
Repeat the move with Azure Database Migration Service (offline), or read how [Managed Instance link](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/managed-instance-link-feature-overview) enables near-zero-downtime SQL Server migrations.
