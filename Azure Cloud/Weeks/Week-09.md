# ☁️ Azure Cloud · Week 09 — Storage II: Files, blob protection + Boss

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Azure Files and blob data protection (snapshots, soft delete, versioning, lifecycle) are how teams avoid data loss and cut storage bills. The Season 2 Boss proves you can run identity and storage like an administrator under time pressure.

## 🗓️ Sessions

### Tuesday 22 Dec · 45 min — Azure Files: shares, snapshots, soft delete, identity-based access
- 📚 **Learn:** File shares (SMB/NFS, tiers), share snapshots, share soft delete, identity-based access (AD DS, Entra Domain Services, Entra Kerberos; share-level RBAC + NTFS ACLs), File Sync recap. Use [Configure Azure Files](https://learn.microsoft.com/en-us/training/modules/configure-azure-files-file-sync/), [Identity-based authentication overview](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview) and [Share snapshots](https://learn.microsoft.com/en-us/azure/storage/files/storage-snapshots-files).
- 🛠️ **Do:** Create a file share; upload a file with `az storage file upload` (or mount it if port 445 is open on your network); take a snapshot; change the file and restore the old version from the snapshot. Enable share soft delete, delete the share and undelete it. Write 6 lines on which identity option you'd pick for a company with on-prem AD. Done when: restore + undelete evidence and the note are in `w09/`.

### Wednesday 23 Dec · 45 min — Blob containers, tiers, soft delete and versioning
- 📚 **Learn:** Container access levels, per-blob tiers and the default tier, archive rehydration (standard vs high priority), blob and container soft delete, versioning vs snapshots. Use [Configure Azure Blob Storage](https://learn.microsoft.com/en-us/training/modules/configure-blob-storage/), [Blob soft delete](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) and [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview).
- 🛠️ **Do:** Enable blob soft delete (7 days), container soft delete and versioning. Overwrite a blob 3 times, list versions and promote an old one; delete a blob and undelete it; delete a container and restore it. Archive one blob and start a rehydrate to Hot (observe the pending status). Done when: CLI outputs for versions, undelete, restore and rehydrate are in `w09/blob-protection.md`.

### Friday 25 Dec · 45 min — Blob lifecycle management + Boss prep cheat sheet
- 📚 **Learn:** Lifecycle rules (prefix and blob-index filters; tierToCool, tierToCold, tierToArchive, delete; days since modification, creation or last access; version and snapshot actions). Use [Lifecycle management overview](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview) and [Configure a lifecycle policy](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure), then skim your W6-W8 notes. (25 Dec is a holiday - shift this session if needed.)
- 🛠️ **Do:** Write `w09/lifecycle.json`: `logs/` -> Cool after 30 days, Archive after 90, delete after 365; previous versions older than 30 days -> delete. Apply it with `az storage account management-policy create` and read it back. Then build a one-page cheat sheet of 15 identity + storage CLI commands for tomorrow's Boss. Done when: the policy is applied and read back, and the cheat sheet is committed.

### Saturday 26 Dec · 60 min — BOSS BATTLE: Identity + storage admin challenge (timed, CLI only)
- 📚 **Learn:** Season 2 skills: Entra groups, RBAC scopes, Policy and tags, storage redundancy, SAS with stored access policies, firewalls, Files snapshots, blob protection. Reference only your cheat sheet during the build, then use the free [AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21).
- 🛠️ **Do:** 40 minutes, CLI only: (1) group `ops-admins` with Contributor on `rg-boss-s2`; (2) policy requiring tag costCenter on that RG; (3) ZRS StorageV2 account with versioning, soft delete and a firewall allowing only your IP; (4) a SAS tied to a stored access policy, then revoke it; (5) file share + snapshot. Then 20 minutes of AZ-104 practice questions, logging domain 1-2 misses. Done when: 5/5 tasks verified, score logged, RG deleted.

## 📦 Deliverable (by Saturday night)
`w09/` Files restore evidence, blob-protection log, `lifecycle.json`, and Boss script `boss-s2.sh` with 5/5 verified tasks and the practice-question score.

## ✅ Self-check (Sunday test preview)
- Share snapshot vs blob snapshot vs blob version: which one is created automatically?
- What is the difference between blob soft delete and container soft delete?
- How long can archive rehydration take, and how can you speed it up?
- Describe a lifecycle rule that archives blobs 90 days after last modification and deletes them after a year.
- Which identity sources can Azure Files use for SMB, and what do share-level RBAC and NTFS permissions each control?
- A developer deleted a container yesterday: which settings must have been enabled to recover it?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Secure storage for Azure Files and Azure Blob Storage](https://learn.microsoft.com/en-us/credentials/applied-skills/secure-storage-azure-files-azure-blob-storage/) (72-hour wait between attempts).
