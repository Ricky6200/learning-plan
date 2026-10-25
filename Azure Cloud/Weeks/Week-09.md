# ☁️ Azure Cloud · Week 09 — Storage II: Files, blob protection + Boss

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Azure Files and blob data protection (snapshots, soft delete, versioning, lifecycle) are how teams avoid data loss and cut storage bills. Upgrading before the free credit ends keeps your labs alive, and the Season 2 Boss proves you can run identity and storage like an administrator under time pressure.

## 🗓️ Sessions

### Tuesday 22 Dec · 45 min — Pay-as-you-go upgrade + Azure Files snapshots and soft delete
- 📚 **Learn:** Your free credit ends around 31 Dec and the subscription is then disabled - upgrade now so W10 labs keep running and the 12-month free services stay. Azure Files: shares (SMB/NFS, tiers), share snapshots, share soft delete, identity-based access (AD DS, Entra Domain Services, Entra Kerberos; share-level RBAC + NTFS ACLs). Read [Configure Azure Files](https://learn.microsoft.com/en-us/training/modules/configure-azure-files-file-sync/). Optional: [Upgrade your Azure free account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription).
- 🛠️ **Do:** 0-8 min: upgrade to pay-as-you-go; recheck the budget and add a cost anomaly alert; list in `w09/notes.md` the 12-month free services you'll use (B1s VM hours, PostgreSQL Flexible B1ms hours, 5 GB of blob). 8-30: create a file share; upload a file with `az storage file upload`; take a snapshot; change the file and restore the old version from the snapshot; enable share soft delete, delete the share and undelete it. Done when: the upgrade is confirmed, the free-services list is committed and restore + undelete evidence are in `w09/`.

### Wednesday 23 Dec · 45 min — Blob containers, tiers, soft delete and versioning
- 📚 **Learn:** Container access levels, per-blob tiers and the default tier, archive rehydration (standard vs high priority), blob and container soft delete, versioning vs snapshots. Read [Configure Azure Blob Storage](https://learn.microsoft.com/en-us/training/modules/configure-blob-storage/). Optional: [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview).
- 🛠️ **Do:** Enable blob soft delete (7 days), container soft delete and versioning. Overwrite a blob 3 times, list versions and promote an old one; delete a blob and undelete it; delete a container and restore it. Archive one blob and start a rehydrate to Hot (observe the pending status). Done when: CLI outputs for versions, undelete, restore and rehydrate are in `w09/blob-protection.md`.

### Friday 25 Dec · 45 min — Blob lifecycle management + Boss prep cheat sheet
- 📚 **Learn:** Lifecycle rules (prefix and blob-index filters; tierToCool, tierToCold, tierToArchive, delete; days since modification, creation or last access; version and snapshot actions), then skim your W6-W8 notes. Read the [Lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview). Optional: [Configure a lifecycle policy](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure). (25 Dec is a holiday - shift this session if needed.)
- 🛠️ **Do:** Write `w09/lifecycle.json`: `logs/` -> Cool after 30 days, Archive after 90, delete after 365; previous versions older than 30 days -> delete. Apply it with `az storage account management-policy create` and read it back. Then build a one-page cheat sheet of 15 identity + storage CLI commands (plus `New-AzStorageAccount`) for tomorrow's Boss. Done when: the policy is applied and read back, and the cheat sheet is committed.

### Saturday 26 Dec · 60 min — BOSS BATTLE: Identity + storage admin challenge (timed, CLI + PowerShell)
- 📚 **Learn:** Season 2 skills: Entra groups, RBAC scopes, Policy and tags, storage redundancy, SAS with stored access policies, firewalls, Files snapshots, blob protection. Reference only your cheat sheet during the build, then use the free [AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21).
- 🛠️ **Do:** 40 minutes, CLI except task 3: (1) group `ops-admins` with Contributor on `rg-boss-s2`; (2) policy requiring tag costCenter on that RG; (3) a ZRS StorageV2 account in Az PowerShell (`New-AzStorageAccount -SkuName Standard_ZRS -Kind StorageV2`), then versioning, soft delete and a firewall allowing only your IP; (4) a SAS tied to a stored access policy, then revoke it; (5) file share + snapshot. Then 20 minutes of AZ-104 practice questions, logging domain 1-2 misses. Done when: 5/5 tasks verified, score logged, RG deleted.

## 📦 Deliverable (by Saturday night)
Pay-as-you-go upgrade confirmed with the 12-month free-services list; `w09/` Files restore evidence, blob-protection log, `lifecycle.json`, and Boss script `boss-s2.sh` (+ the PowerShell step) with 5/5 verified tasks and the practice-question score.

## ✅ Self-check (Sunday test preview)
- Share snapshot vs blob snapshot vs blob version: which one is created automatically?
- What is the difference between blob soft delete and container soft delete?
- How long can archive rehydration take, and how can you speed it up?
- Describe a lifecycle rule that archives blobs 90 days after last modification and deletes them after a year.
- Which identity sources can Azure Files use for SMB, and what do share-level RBAC and NTFS permissions each control?
- A developer deleted a container yesterday: which settings must have been enabled to recover it?
- Why must a free account be upgraded before its 30-day credit ends, and what keeps protecting you afterwards?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Secure storage for Azure Files and Azure Blob Storage](https://learn.microsoft.com/en-us/credentials/applied-skills/secure-storage-azure-files-azure-blob-storage/) (72-hour wait between attempts).
