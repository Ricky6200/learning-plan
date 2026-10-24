# ☁️ Azure Cloud · Week 14 — Backup, disaster recovery and migration + Boss

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Backup and DR complete AZ-104's last domain, and migration is exactly what you want to own on Azure: strategy vocabulary, Azure Migrate, database migration and a hands-on VM-to-PaaS move prove you can lead a real migration.

## 🗓️ Sessions

### Tuesday 26 Jan · 45 min — Recovery Services vault, Backup vault, policies and restore
- 📚 **Learn:** Recovery Services vault vs Backup vault (which workloads each protects), backup policies (schedule, retention, instant restore), backup and restore, backup reports and alerts, secure-by-default soft delete (14 days at no extra cost). Use [Introduction to Azure Backup](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-backup/), [Backup vault overview](https://learn.microsoft.com/en-us/azure/backup/backup-vault-overview) and [Back up a VM with CLI](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-cli).
- 🛠️ **Do:** Create a Recovery Services vault, protect a small VM with a custom daily policy (7-day retention) and run an on-demand backup. Create a Backup vault and configure operational backup for blobs. Add a backup alert to your email. Cleanup: `az backup protection disable --delete-backup-data true`, then delete the vaults and RG. Done when: backup job status, the blob backup instance and the alert rule are in `w14/backup.md`.

### Wednesday 27 Jan · 45 min — Site Recovery: replicate, test failover, fail over
- 📚 **Learn:** Azure Site Recovery for Azure VMs: replication policy, RPO, recovery plans, test failover vs failover, commit and re-protect; billing (each protected instance is free for its first 31 days, replica storage is still charged). Use [Introduction to Azure Site Recovery](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-site-recovery/), [Enable Azure VM replication](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-enable-replication) and [Run a DR drill](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-dr-drill).
- 🛠️ **Do:** Enable replication for a small VM from Central India to South India. While it syncs, write `w14/dr-runbook.md`: RPO/RTO targets, test-failover steps into an isolated VNet, validation checks and cleanup. If replication shows Protected in time, run the test failover and clean it up; otherwise finish on Sunday. Disable replication and delete target resources afterwards. Done when: replication status and the runbook are committed.

### Friday 29 Jan · 45 min — Migration: strategies, Azure Migrate, DMS, landing zones
- 📚 **Learn:** Cloud Adoption Framework migrate phases (plan, prepare, execute, decommission), strategies (rehost, refactor, rearchitect, rebuild, replace, retain, retire), Azure Migrate discovery, assessment and server migration, AppCAT for Java, Database Migration Service, landing zones. Use [Select migration strategies](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/select-cloud-migration-strategy), [About Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) and [AppCAT for Java](https://learn.microsoft.com/en-us/azure/migrate/appcat/java).
- 🛠️ **Do:** For your company's Spring Boot + SQL app write `w14/migration-plan.md`: inventory, a strategy per component with reasons, target services (App Service, Container Apps or AKS; Azure SQL or PostgreSQL Flexible), tools (Azure Migrate, AppCAT, DMS or pg_dump), cutover and rollback, landing-zone prerequisites. Then write Saturday's `w14/source-vm.sh` (VM + Docker Compose running Spring Boot + Postgres). Done when: plan and script are committed.

### Saturday 30 Jan · 60 min — BOSS BATTLE: Migration Lab - VM-hosted app to PaaS + runbook
- 📚 **Learn:** Season 3 integration: VMs, networking, App Service or Container Apps, PostgreSQL Flexible Server, CAF phases. Use [Dump and restore to PostgreSQL Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/migrate/how-to-migrate-using-dump-and-restore), [Migrate Spring Boot to Azure Container Apps](https://learn.microsoft.com/en-us/azure/developer/java/migration/migrate-spring-boot-to-azure-container-apps) and your `w14/migration-plan.md`.
- 🛠️ **Do:** 60-minute timer. 0-10: run `source-vm.sh` and start a PostgreSQL Flexible (Burstable B1ms) server in parallel. 10-30: `pg_dump` on the VM, `pg_restore` into Flexible Server; deploy the app (JAR to App Service or image to Container Apps) with the new JDBC URL as a secret/setting. 30-40: smoke test + row-count check. 40-55: finish the runbook (validate, cutover, rollback, decommission). 55-60: delete everything. Done when: the app serves migrated data and the runbook is committed.

## 📦 Deliverable (by Saturday night)
`w14/` backup evidence, DR runbook, `migration-plan.md`, Boss migration runbook with evidence, and `az group list -o table` showing no lab RGs left.

## ✅ Self-check (Sunday test preview)
- Recovery Services vault vs Backup vault: where do VM backups vs blob or disk backups live?
- RPO vs RTO: which does replication frequency affect, and which does a recovery plan affect?
- Test failover vs failover: what must you clean up after a test?
- Moving a Spring Boot JAR from a VM to App Service: is that rehost, refactor or rearchitect, and why?
- What does Azure Migrate need on-premises for discovery, and what does an assessment give you?
- Offline vs online database migration: when is downtime unavoidable?
- What is an Azure landing zone, and why should it exist before you migrate workloads?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Configure and migrate to Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/credentials/applied-skills/configure-and-migrate-to-azure-database-for-postgresql/) or watch Savill's [Overview of Migrating to Azure](https://www.youtube.com/watch?v=Hf7ZTa_PlGU).
