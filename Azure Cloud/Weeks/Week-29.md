# ☁️ Azure Cloud · Week 29 — Migration II: hybrid networks, WAF, APIs, PostgreSQL

> 📅 **Mon 10 May 2027 → Sun 16 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 28](Week-28.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-29.md) · [Week 30 →](Week-30.md)

**Why this week:** Real migrations connect to on-premises networks, get reviewed against the Well-Architected Framework, put an API gateway in front of legacy services and move databases with minimal downtime. These are the architect-level questions that separate a cloud admin from a migration engineer.

## 🗓️ Sessions

### Tuesday 11 May · 45 min — Hybrid networking design: VPN, ExpressRoute, DNS, firewall
- 📚 **Learn:** Site-to-site and point-to-site VPN vs ExpressRoute (private, SLA-backed, not encrypted by default), hub-spoke with Azure Firewall, DNS Private Resolver so on-premises clients can resolve private endpoints, and Application Gateway (regional, WAF) vs Front Door (global edge). Read [Connect an on-premises network to Azure](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/). Optional: [Azure DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview).
- 🛠️ **Do:** Design - don't deploy (gateways take 30+ minutes and bill hourly) - `w29/hybrid.md` for a company moving TicketVerse while its SQL Server stays on-premises for 6 months: S2S VPN now, ExpressRoute later; a hub with Azure Firewall and a DNS Private Resolver; prod and dev spokes; Front Door + WAF in front. Draw it, price VPN Gateway vs a 50 Mbps ExpressRoute circuit in the calculator, and write how `<server>.database.windows.net` resolves from on-premises to a private endpoint. Done when: diagram, prices and DNS flow are committed.

### Wednesday 12 May · 45 min — Well-Architected review, Defender secure score and PIM
- 📚 **Learn:** The Well-Architected Framework's five pillars (reliability, security, cost optimization, operational excellence, performance efficiency) and its free review assessment, Defender for Cloud's free CSPM secure score and recommendations, and Privileged Identity Management (just-in-time admin roles; needs Entra ID P2). Read the [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) overview. Optional: [Secure score](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls).
- 🛠️ **Do:** Run the Azure Well-Architected Review assessment (linked from the overview) for TicketVerse on Azure, using your W28 design, and export the top 10 recommendations. Open Defender for Cloud, record the secure score and remediate two recommendations on a lab resource (scores refresh within hours - recheck on Sunday). Write how PIM would make your Owner access just-in-time. Done when: the review export, secure-score evidence and the PIM note are in `w29/`.

### Friday 14 May · 45 min — API Management basics: import, products, rate limits
- 📚 **Learn:** API Management as the gateway in front of legacy and new APIs (strangler-fig migrations): APIs, operations, products, subscription keys, policies (inbound, backend, outbound) and tiers - Consumption is serverless with a monthly free grant and supports `rate-limit` but not `rate-limit-by-key`. Read [Import and publish your first API](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish). Optional: the [rate-limit policy](https://learn.microsoft.com/en-us/azure/api-management/rate-limit-policy).
- 🛠️ **Do:** Create a Consumption instance (`az apim create --sku-name Consumption`, a few minutes), import the tutorial's Petstore OpenAPI, add it to a product that requires a subscription key, and add an inbound `<rate-limit calls="5" renewal-period="60" />` policy plus a `set-header` on responses. Call it 6 times with curl and your key. Done when: calls 1-5 return 200, call 6 returns 429 with Retry-After, and the RG is deleted.

### Saturday 15 May · 60 min — LAB: PostgreSQL online migration with cutover and rollback
- 📚 **Learn:** Online migration keeps the source live: the migration service copies the data, then streams changes through logical replication (`wal_level=logical`, a primary key on every table) until you cut over; rollback means pointing the app back to the source before you decommission it. Burstable targets work, just slower. Read [Migrate online from an Azure VM or on-premises PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/migrate/migration-service/tutorial-migration-service-iaas-online). Optional: [Known issues](https://learn.microsoft.com/en-us/azure/postgresql/migrate/migration-service/concepts-known-issues-migration-service).
- 🛠️ **Do:** Minute 0: a B1s source VM (cloud-init: Docker running `postgres:17` with `-c wal_level=logical -c max_replication_slots=4 -c max_wal_senders=4`; NSG allows 5432 only from service tag `AzureCloud.CentralIndia`) and a B1ms Flexible Server target. Load TicketVerse-like data (3 tables with primary keys, 10,000 rows). Create an online migration in the portal (Validate and migrate). While it syncs, insert 50 source rows and confirm they arrive; cut over. Write `w29/pg-runbook.md` (pre-checks, cutover, validation, rollback trigger and steps). Delete the RG. Done when: row counts match after cutover and the runbook is committed.

## 📦 Deliverable (by Saturday night)
`w29/hybrid.md` with diagram, prices and DNS flow; the Well-Architected Review export, secure-score evidence and PIM note; the API Management 200/429 test; and `pg-runbook.md` with matching row counts after an online cutover - every lab RG deleted.

## ✅ Self-check (Sunday test preview)
- Site-to-site VPN vs ExpressRoute: compare path, bandwidth, SLA and encryption.
- Why do on-premises clients fail to resolve private endpoints without DNS Private Resolver (or conditional forwarders)?
- Application Gateway vs Front Door: when do you need each, and where does WAF sit?
- Name the five Well-Architected pillars and one TicketVerse trade-off between two of them.
- What does API Management add in a strangler-fig migration, and why can't the Consumption tier use rate-limit-by-key?
- Offline vs online PostgreSQL migration: what must be true on the source for online, and what is your rollback trigger?
- What is PIM, and why is just-in-time access better than a permanent Owner assignment?

## 🚀 Stretch (optional)
GitHub Actions OIDC deep dive: add an environment-scoped federated credential (`repo:<you>/<repo>:environment:prod`) with a required reviewer; then read [Terraform on Azure](https://learn.microsoft.com/en-us/azure/developer/terraform/overview) and compare it with your W28 Bicep.
