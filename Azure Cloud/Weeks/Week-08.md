# ☁️ Azure Cloud · Week 08 — Storage I: accounts, replication, security, data tools

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Storage is 15-20% of AZ-104 and the first thing you configure in any migration; wrong redundancy, open firewalls or leaked keys and SAS tokens are classic production incidents that interviewers love to discuss.

## 🗓️ Sessions

### Tuesday 15 Dec · 45 min — Storage accounts, redundancy, object replication and encryption
- 📚 **Learn:** Account settings (performance, kind, redundancy, default tier), changing redundancy, object replication (versioning on both accounts, change feed on the source), encryption at rest (Microsoft-managed vs customer-managed keys, infrastructure encryption). Read [Configure storage accounts](https://learn.microsoft.com/en-us/training/modules/configure-storage-accounts/). Optional: [Object replication overview](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-overview).
- 🛠️ **Do:** In `rg-lab-w08` create a source and a destination StorageV2 account (LRS); enable versioning on both and change feed on the source; add an object replication policy for container `posters`; upload 3 blobs and confirm they arrive (it is asynchronous). Change the source from LRS to GRS with `az storage account update --sku`. Done when: replication and SKU-change outputs are committed and the RG is deleted.

### Wednesday 16 Dec · 45 min — Storage access: user-delegation SAS, stored policies, keys
- 📚 **Learn:** Access keys and rotation, SAS types (a user delegation SAS is signed with Entra credentials - the most secure), stored access policies (revoke a SAS without rotating keys), disabling shared key access. Read [Configure Azure Storage security](https://learn.microsoft.com/en-us/training/modules/configure-storage-security/). Optional: [Create a user delegation SAS with Azure CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli).
- 🛠️ **Do:** On a fresh account: (1) curl a 5-minute read-only user-delegation SAS (`az storage blob generate-sas --as-user --auth-mode login --full-uri`) - the live version of W3's Azurite gap; (2) create stored access policy `read-1h` on a container, issue a service SAS bound to it, curl a blob, delete the policy and show the same SAS now returns 403; (3) rotate key1 and prove an old connection string fails. Done when: 3 before/after results are in `w08/access.md`.

### Friday 18 Dec · 45 min — Moving data with AzCopy and Azure Storage Explorer
- 📚 **Learn:** AzCopy v10 (Entra login vs SAS, `copy`, `sync`, `--recursive`, job logs and resume), Storage Explorer connections (Entra ID, SAS, keys), choosing AzCopy vs Storage Explorer vs Data Box. Read the [AzCopy v10 guide](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10). Optional: [Get started with Storage Explorer](https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer).
- 🛠️ **Do:** Install AzCopy and Storage Explorer on the personal laptop. Generate 200 small files with a script, `azcopy copy` them recursively to a container, edit 5 files locally and run `azcopy sync` (count what transferred). Browse and download one file in Storage Explorer using Entra ID sign-in. Done when: the AzCopy job summary, sync delta and an Explorer screenshot are in `w08/`.

### Saturday 19 Dec · 60 min — LAB: AZ-104 Lab 07 - manage Azure Storage (blob + firewall)
- 📚 **Learn:** The official [Lab 07 - Manage Azure Storage](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_07-Manage_Azure_Storage.html) plus storage firewall rules: default action, IP rules, virtual network rules, trusted Microsoft services. Optional: [Storage firewall rules](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security).
- 🛠️ **Do:** Complete the Lab 07 tasks for the storage account, blob container, SAS access and network restriction (leave Azure Files for W9). Script the account, container and network-rule creation in `w08/storage.sh` as you go: allow only your laptop's IP and retry from Cloud Shell (expect 403). Then repeat one step in Az PowerShell in Cloud Shell: add a second rule (`Add-AzStorageAccountNetworkRule ... -IPAddressOrRange 203.0.113.0/24`) and list the rules with `Get-AzStorageAccountNetworkRuleSet`. Finish with `nuke-lab.sh 08`. Done when: lab tasks, `storage.sh`, the 403 and the rule list are committed and the RG deletion is confirmed.

## 📦 Deliverable (by Saturday night)
`w08/` object replication evidence, access experiments (user-delegation SAS, stored-policy revoke, key rotation), AzCopy and Storage Explorer evidence, firewall 403 evidence with one Az PowerShell step (rule added + listed), and `storage.sh`.

## ✅ Self-check (Sunday test preview)
- Which features must be enabled for object replication, and is replication synchronous?
- How do you revoke a SAS token without rotating the account keys?
- What is the blast radius if an account SAS signed with key1 leaks, and how do you contain it?
- Storage firewall: what does allowing trusted Microsoft services actually permit?
- AzCopy copy vs sync: which can delete destination files, and when?
- Microsoft-managed keys vs customer-managed keys: what changes operationally?

## 🚀 Stretch (optional)
Disable shared key access on a test account and fix your scripts so they only use `--auth-mode login`.
