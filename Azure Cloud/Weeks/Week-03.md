# ☁️ Azure Cloud · Week 03 — Storage, identity and security fundamentals

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Every backend stores files and needs secure access: storage tiers and redundancy plus Entra ID, RBAC and Zero Trust are classic AZ-900 questions and the first things you configure when a Spring Boot app moves to Azure.

## 🗓️ Sessions

### Tuesday 10 Nov · 45 min — Storage services, tiers, redundancy and data movement
- 📚 **Learn:** Blob, Files, Queue, Table and Disk; access tiers (hot, cool, cold, archive); redundancy (LRS, ZRS, GRS, GZRS and read-access variants); storage account types; moving files (AzCopy, Storage Explorer, File Sync) and migration (Azure Migrate, Data Box). Use [Describe Azure storage services](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/) and Savill's [Storage account resources](https://www.youtube.com/watch?v=AI2XoRFwqYE).
- 🛠️ **Do:** Build `w03/storage-cheatsheet.md`: a redundancy table (copies, zones, regions, readable secondary?) and a tier table (early-deletion period, storage vs access cost, archive rehydration). Then choose tier + redundancy for (a) daily invoices, (b) 7-year audit logs, (c) TicketVerse event posters, and pick a tool to move 50 TB over a slow link. Done when: both tables + 4 justified choices committed.

### Wednesday 11 Nov · 45 min — Entra ID, authentication methods, external identities, Conditional Access
- 📚 **Learn:** Microsoft Entra ID vs Entra Domain Services, single sign-on, MFA, passwordless, external identities (B2B guests, customer identities), Conditional Access signals and decisions. Use the first five units of [Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/) and Savill's [Conditional Access, MFA and SSO](https://www.youtube.com/watch?v=DFwERh9Xxk0).
- 🛠️ **Do:** In `w03/identity.md` map your company's login flow to SSO, MFA and Conditional Access terms. Write 3 Conditional Access policies in plain English (block legacy authentication; require MFA outside India; require a compliant device for admins) and note that Conditional Access needs Entra ID P1. Explain when a lift-and-shift app needs Entra Domain Services. Done when: 3 policies + the Domain Services note are committed.

### Friday 13 Nov · 45 min — RBAC, Zero Trust, defense in depth, Defender for Cloud
- 📚 **Learn:** Azure RBAC (security principal, role definition, scope, assignment), Zero Trust (verify explicitly, least privilege, assume breach), defense-in-depth layers, Microsoft Defender for Cloud (posture + workload protection). Use the remaining units of [Describe Azure identity, access, and security](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/), Savill's [RBAC](https://www.youtube.com/watch?v=0iVyJBG06fM) and [Zero Trust](https://www.youtube.com/watch?v=JX3w4to-qgo).
- 🛠️ **Do:** Design least-privilege access for a 4-person TicketVerse team: who gets Owner, Contributor, Reader or Storage Blob Data Reader, and at which scope (management group, subscription, resource group, resource). Then map 7 defense-in-depth layers to one concrete control each for your app. Done when: RBAC matrix + 7-layer table committed and the module assessment passed.

### Saturday 14 Nov · 60 min — LAB: Storage tiers, a user-delegation SAS and an RBAC assignment
- 📚 **Learn:** Storage account basics, blob upload with Entra auth, tier changes, SAS types (prefer user delegation SAS), data-plane RBAC roles. Use [Grant limited access with SAS](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview), [Blob quickstart with CLI](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli) and [Assign roles with Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli).
- 🛠️ **Do:** Path A: `new-lab.sh 03`; create a StorageV2 LRS account; assign yourself Storage Blob Data Contributor on it (wait ~2 min); upload two blobs with `--auth-mode login`; set one to Archive and read its tier; create a 5-minute read-only user-delegation SAS for the other and curl it before and after expiry; `nuke-lab.sh 03`. Path B: do the blob + SAS steps on Azurite (Docker). Done when: tier output, SAS 200/403 evidence and RG deletion are committed.

## 📦 Deliverable (by Saturday night)
`w03/` storage cheat sheet, identity notes, RBAC matrix, defense-in-depth table, and SAS/RBAC lab evidence (Path B: Azurite evidence).

## ✅ Self-check (Sunday test preview)
- LRS vs ZRS vs GRS vs GZRS: which survives a zone outage, which a region outage, and which lets you read the secondary?
- Hot vs cool vs cold vs archive: what is the trade-off, and what is rehydration?
- Account SAS vs service SAS vs user delegation SAS: which is most secure and why?
- What are the four parts of an Azure RBAC role assignment, and how does scope inheritance work?
- Explain Zero Trust's three principles with one Azure feature for each.
- Entra ID vs Entra Domain Services: when does a lift-and-shift legacy app need the latter?
- AzCopy vs Storage Explorer vs Azure File Sync vs Data Box: which would you use for 50 TB over a slow link?

## 🚀 Stretch (optional)
Watch Savill's [Data movement and migration options](https://www.youtube.com/watch?v=jNBcXnMTo9s) and write five lines comparing Azure Migrate and Data Box.
