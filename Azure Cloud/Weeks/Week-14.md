# ☁️ Azure Cloud · Week 14 — Backup, disaster recovery and migration basics

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Backup and DR complete AZ-104's last domain, and migration is exactly what you want to own on Azure: strategy vocabulary, Azure Migrate, database target options and a hands-on VM-to-PaaS move are your first migration story (Season 6 goes deeper).

## 🗓️ Sessions

### Tuesday 26 Jan · 45 min — Backup: Recovery Services vault, policies and a file restore
- 📚 **Learn:** Recovery Services vault vs Backup vault (which workloads each protects), backup policies (schedule, retention, instant restore), file-level restore, backup reports, and secure-by-default soft delete: it can no longer be disabled, deleted backup data stays 14 days at no extra cost and a deleted vault can move to a soft-deleted state. Read [Back up a VM with CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli). Optional: [Recover files from a VM backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-restore-files-from-vm). (26 Jan is Republic Day - shift this session if needed.)
- 🛠️ **Do:** Minute 0: create a B1s VM holding a test file, plus a Recovery Services vault in its own RG `rg-w14-vault`; protect the VM with a custom daily policy (7-day retention) and run `az backup protection backup-now`. When the snapshot recovery point appears (~15 min), use File Recovery: run its script on the VM, copy the file back from the mounted recovery point, unmount. Cleanup: `az backup protection disable --delete-backup-data true --yes`, delete the VM's RG, try deleting the vault (else delete `rg-w14-vault` after 14 days). Done when: job, restored file and cleanup notes are in `w14/backup.md`.

### Wednesday 27 Jan · 45 min — Site Recovery: replicate, test failover, fail over
- 📚 **Learn:** Azure Site Recovery for Azure VMs: replication policy, RPO, recovery plans, test failover vs failover, commit and re-protect; billing (each protected instance is free for its first 31 days, replica storage is still charged). Read [Enable Azure VM replication](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-enable-replication). Optional: [Run a DR drill](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill).
- 🛠️ **Do:** Enable replication for a small VM from Central India to South India. While it syncs, write `w14/dr-runbook.md`: RPO/RTO targets, test-failover steps into an isolated VNet, validation checks and cleanup. If replication shows Protected in time, run the test failover and clean it up; otherwise finish on Sunday. Disable replication and delete target resources afterwards. Done when: replication status and the runbook are committed.

### Friday 29 Jan · 45 min — Migration strategies, Azure Migrate and database targets
- 📚 **Learn:** CAF strategies (retire, rehost, replatform, refactor, rearchitect, replace, rebuild, retain), Azure Migrate discovery and assessment, AppCAT for Java, landing zones; database targets - Azure SQL Database vs Managed Instance vs SQL Server on VM - and DMS offline vs online (the full treatment comes in W27). Read [Select migration strategies](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/select-cloud-migration-strategy). Optional: [What is Azure SQL?](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview).
- 🛠️ **Do:** Write a one-page `w14/migration-plan.md` for a company-style Spring Boot + SQL Server app: inventory, a strategy per component with reasons, targets (App Service or Container Apps; Azure SQL Database or Managed Instance), tools (Azure Migrate, AppCAT, DMS), cutover and rollback. Then launch Saturday's slow resources: a B1s source VM whose cloud-init installs `openjdk-25-jre-headless` and Docker and runs `docker run -d -p 5432:5432 postgres:17`, plus a PostgreSQL Flexible Server (Burstable B1ms) that you `stop` once created. Done when: the plan is committed, the VM runs and the server is stopped.

### Saturday 30 Jan · 60 min — LAB: Migration lab - VM-hosted app to App Service + runbook
- 📚 **Learn:** Lift the data and replatform the app: `pg_dump`/`pg_restore` into Flexible Server, the JAR on App Service with the new JDBC URL as an app setting, then a runbook with validation, cutover and rollback. Read [Dump and restore to PostgreSQL Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/migrate/how-to-migrate-using-dump-and-restore). Optional: [Migrate Spring Boot apps to App Service](https://learn.microsoft.com/en-us/azure/developer/java/migration/migrate-spring-boot-to-app-service).
- 🛠️ **Do:** Minute 0: `az postgres flexible-server start`. 0-10: copy the TicketVerse v0 JAR to the source VM, run it with `java -jar` against the local Postgres and smoke-test it. 10-25: `pg_dump` on the VM, `pg_restore` into Flexible Server. 25-35: deploy the JAR to a Linux B1 App Service (Java SE) with the new JDBC URL and credentials as app settings; smoke test + row counts; check the app with Az PowerShell (`Get-AzWebApp`). 35-45: finish `w14/runbook.md` (validate, cutover, rollback, decommission), delete the RGs. Done when: the app serves migrated data and the runbook is committed.

## 📦 Deliverable (by Saturday night)
`w14/` backup + file-restore evidence and cleanup notes, DR runbook, `migration-plan.md`, the VM-to-App Service migration runbook with evidence (+ one PowerShell step), and `az group list -o table` showing no lab RGs left except the vault RG waiting out soft delete.

## ✅ Self-check (Sunday test preview)
- Recovery Services vault vs Backup vault: where do VM backups vs blob or disk backups live?
- RPO vs RTO: which does replication frequency affect, and which does a recovery plan affect?
- Test failover vs failover: what must you clean up after a test?
- Moving a Spring Boot JAR from a VM to App Service: is that rehost, replatform or refactor, and why?
- SQL Database vs Managed Instance vs SQL Server on VM: which fits an app that uses SQL Agent jobs and cross-database queries?
- Offline vs online database migration: when is downtime unavoidable?
- Soft delete can't be disabled on a Recovery Services vault any more: how do you clean up a lab vault safely?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Configure and migrate to Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/credentials/applied-skills/configure-and-migrate-to-azure-database-for-postgresql/) or watch Savill's [Overview of Migrating to Azure](https://www.youtube.com/watch?v=Hf7ZTa_PlGU).
