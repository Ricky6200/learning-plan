# ☕ Java Backend · Week 23 — Azure deployment: TicketVerse live, Season 5 boss

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Deploying your own system to a real cloud with managed data services, identity-based secrets and telemetry is the strongest proof of SDE-2 readiness; it also mirrors your Azure track lab this week.

## 🗓️ Sessions

### Monday 29 Mar · 60 min — Platform choice: AKS vs Container Apps; ACR; budgets and scripts
- 📚 **Learn:** AKS (full Kubernetes, reuse Helm chart, more ops) vs Azure Container Apps (managed, scale to zero, built-in ingress, Dapr optional). **Primary target: Azure Container Apps** (matches the Azure track's W23 Boss; AKS gets its own lab there). Azure Container Registry, resource-group-per-environment, naming, Central India region, budgets and alerts. [Azure Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview), [AKS documentation](https://learn.microsoft.com/en-us/azure/aks/), [Azure: Create budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).
- 🛠️ **Do:** Write ADR-003 (AKS vs ACA for TicketVerse) with a monthly cost estimate from the Azure Pricing Calculator; create `infra/deploy.sh` (az CLI or Bicep) for resource group, ACR, Log Analytics and a budget alert at 50% and 90%; import your GHCR images into ACR. Done when: the script is idempotent (second run makes no changes) and images are listed in ACR.

### Tuesday 30 Mar · 60 min — Managed data: PostgreSQL Flexible Server, Managed Redis, Event Hubs Kafka
- 📚 **Learn:** Azure Database for PostgreSQL Flexible Server (Burstable tier, firewall vs private access, TLS, Flyway against it); Azure Managed Redis (the current Redis offering); Event Hubs Kafka endpoint (Standard tier, SASL_SSL) vs running Kafka in-cluster; connection settings per Spring profile. [Azure PostgreSQL Flexible Server overview](https://learn.microsoft.com/en-us/azure/postgresql/overview), [Azure Managed Redis overview](https://learn.microsoft.com/en-us/azure/redis/overview), [Event Hubs for Apache Kafka](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview).
- 🛠️ **Do:** Extend the script: PostgreSQL Flexible Server (smallest Burstable) with catalog and booking databases, the smallest Azure Managed Redis, and an Event Hubs Standard namespace with your topics as event hubs. Add a `cloud` Spring profile and run booking-service locally against these services (Flyway migrates, the outbox relay publishes to Event Hubs). Done when: one booking saga completes using only Azure data services.

### Wednesday 31 Mar · 60 min — Secrets and identity: Key Vault, managed identity, Workload ID
- 📚 **Learn:** Never ship secrets in images or Git; Azure Key Vault; managed identities; on AKS, Microsoft Entra Workload ID federates a Kubernetes ServiceAccount to an identity; on ACA, assign a managed identity and reference Key Vault secrets; Spring Cloud Azure integration. [Azure Key Vault overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview), [AKS: Workload identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview), [Spring Cloud Azure docs](https://learn.microsoft.com/en-us/azure/developer/java/spring-framework/).
- 🛠️ **Do:** Store DB, Redis and Event Hubs credentials in Key Vault; give each service an identity with `get` permission only on its own secrets; wire secrets into the apps via Key Vault references (ACA) or Workload ID + Spring Cloud Azure (AKS). Grep the repo and image env for secrets. Done when: services start in Azure with zero secrets in Git, images or plain env vars.

### Thursday 01 Apr · 60 min — Deploy all services, public HTTPS entry, CI deploy via OIDC
- 📚 **Learn:** ACA: one container app per service, internal vs external ingress, revisions and traffic split. AKS: Helm chart with Azure values, a Gateway API implementation for public traffic, ACR pull via managed identity. Deploy from GitHub Actions using the OIDC login you set up in W22. [Azure Container Apps: Java overview](https://learn.microsoft.com/en-us/azure/container-apps/java-overview), [AKS: Deploy a cluster with Azure CLI](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli), [GitHub Docs: OIDC in Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure).
- 🛠️ **Do:** Deploy gateway (public HTTPS), catalog, booking, payment-mock, notification and Keycloak (internal where possible); add a `deploy-azure` job to `cd.yml` gated by a `production` environment approval. Run the smoke script against the public URL. Done when: the saga passes over HTTPS on the Azure URL and a redeploy happens from GitHub Actions without any stored Azure secret.

### Friday 02 Apr · 60 min — Application Insights via OpenTelemetry, KQL, cost guardrails, teardown
- 📚 **Learn:** Azure Monitor OpenTelemetry for Java (Application Insights agent or Spring Boot integration): application map, end-to-end transactions, failures; basic KQL over requests/dependencies/traces; cost guardrails: smallest SKUs, scale-to-zero/min replicas, stop dev database at night, delete-by-resource-group teardown. [Enable OpenTelemetry in Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=java), [App Insights for Spring Boot](https://learn.microsoft.com/en-us/azure/azure-monitor/app/java-spring-boot), [AKS cost best practices](https://learn.microsoft.com/en-us/azure/aks/best-practices-cost).
- 🛠️ **Do:** Connect all services to Application Insights; find one booking's end-to-end transaction and the application map; write 3 saved KQL queries (p95 by operation, failed dependencies, bookings per hour from custom metrics); write `infra/teardown.sh` that deletes the resource group and verifies it is gone. Done when: queries are in `docs/kql.md` and teardown is tested on a throwaway resource group.

### Saturday 03 Apr · 60 min — BOSS BATTLE: Live TicketVerse demo URL and verified teardown
- 📚 **Learn:** Rules: 60 minutes; scripts and pipeline only (no portal click-ops except viewing); evidence or it did not happen. Checklist: deploy or verify the deployment, run both saga paths on the public URL, show Application Insights traces and the cost-to-date, record a 5-minute demo video, then tear everything down. [Azure Container Apps docs](https://learn.microsoft.com/en-us/azure/container-apps/), [Azure CLI docs](https://learn.microsoft.com/en-us/cli/azure/).
- 🛠️ **Do:** Run `deploy.sh` (or the CD workflow), wait for health, run the smoke script against the live URL, capture an Application Insights end-to-end trace and the cost analysis view, record the demo, then run `teardown.sh` and show the resource group no longer exists. Done when: all steps complete within 60 minutes, `v5.0.0` is tagged, the video and screenshots are linked in the README, and the bill stays within budget.

## 📦 Deliverable (by Saturday night)
`infra/` scripts (deploy + teardown), ADR-003, TicketVerse running on Azure (managed PostgreSQL, Managed Redis, Event Hubs Kafka, Key Vault + identities, App Insights) deployed via OIDC pipeline; demo video; verified teardown.

## ✅ Self-check (Sunday test preview)
- AKS vs Azure Container Apps: which did you choose for TicketVerse and why?
- How does Workload ID (or managed identity) remove secrets from your deployment?
- What changes when Spring Kafka talks to the Event Hubs Kafka endpoint?
- How did you keep the Azure bill under control, and how do you verify teardown?
- Which Application Insights views or KQL queries help you debug a slow booking?
- Public vs internal ingress: which services should be reachable from the internet?
- What would you change to make this deployment production-grade (HA, backups, private networking)?

## 🚀 Stretch (optional)
Convert `deploy.sh` to Bicep modules and run a what-if deployment before applying ([Bicep overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview)).
