# ☕ Java Backend · Week 28 — Azure deployment: TicketVerse live with AI

> 📅 **Mon 03 May 2027 → Sun 09 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 27](Week-27.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-28.md) · [Week 29 →](Week-29.md)

**Why this week:** Deploying your own system to a real cloud with managed data services, identity-based secrets and telemetry is the strongest proof of SDE-2 readiness. It is a joint week: Azure W28 writes and provisions the infrastructure as code, you deploy and prove the application on it. Personal-account Azure work happens on your personal laptop or in a Codespace.

## 🗓️ Sessions

### Monday 03 May · 60 min — Platform choice: Container Apps vs AKS; the infra contract
- 📚 **Learn:** AKS (full Kubernetes, reuses your Helm chart, more operations) vs Azure Container Apps (managed, scale to zero, built-in ingress, revisions; Dapr optional); the primary target is Container Apps, matching the infrastructure Azure W28 provisions with Bicep. Azure Container Registry, resource group per environment, naming, Central India region, budgets and alerts. Read: [Azure Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview). Optional: [Azure: Create budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).
- 🛠️ **Do:** Write ADR-003 (Container Apps vs AKS for TicketVerse) with a monthly cost estimate from the Azure Pricing Calculator, and `docs/azure-contract.md`: every output you need from Azure W28's Bicep (ACR login server, Container Apps environment, PostgreSQL host, Managed Redis host, Event Hubs namespace, Key Vault URI, App Insights connection string) and every env var or secret each service expects. Done when: the ADR is committed and every service setting maps to exactly one infra output or Key Vault secret.

### Tuesday 04 May · 60 min — Cloud profile: PostgreSQL Flexible Server, Managed Redis, Event Hubs Kafka
- 📚 **Learn:** Azure Database for PostgreSQL Flexible Server (Burstable tier, firewall vs private access, TLS required, Flyway runs against it); Azure Managed Redis (TLS; the current Redis offering); the Event Hubs Kafka endpoint (Standard tier, port 9093, SASL_SSL with a connection string or Entra ID) instead of running Kafka yourself; connection settings per Spring profile, all from env vars. Read: [Event Hubs for Apache Kafka](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview). Optional: [Azure PostgreSQL Flexible Server overview](https://learn.microsoft.com/en-us/azure/postgresql/overview).
- 🛠️ **Do:** Give each service an `application-cloud.yaml` containing only `${ENV}` placeholders (JDBC URL with `sslmode=require`, Redis TLS flag, Kafka security protocol and JAAS config) plus a value-free `.env.cloud.example`; start every service with the `cloud` profile against your local compose infra by setting env vars only (PLAINTEXT and TLS off locally). Done when: all services start with `--spring.profiles.active=cloud` and a grep finds no host, password or connection string in the repo.

### Wednesday 05 May · 60 min — Secrets and identity: Key Vault, managed identity, Workload ID
- 📚 **Learn:** Never ship secrets in images or Git; Azure Key Vault; managed identities; on Container Apps, assign a user-assigned identity and reference Key Vault secrets (`keyvaultref:` + `identityref:`), then map them to env vars with `secretref:`; on AKS, Microsoft Entra Workload ID federates a Kubernetes ServiceAccount to an identity; Spring Cloud Azure can also read Key Vault and enables passwordless database connections. Read: [Azure Container Apps: Manage secrets](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets). Optional: [AKS: Workload identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview).
- 🛠️ **Do:** Complete `docs/azure-contract.md`: for each service, its user-assigned identity, the Key Vault secrets it may read (get only), and the exact `az containerapp secret set --secrets name=keyvaultref:...,identityref:...` and `az containerapp update --set-env-vars NAME=secretref:name` commands your CD job will run on Saturday; add a gitleaks step to `ci.yml` that fails on committed secrets. Done when: every secret has one Key Vault name and one consuming identity, and CI goes red when you commit a fake key on a test branch.

### Thursday 06 May · 60 min — CD to Azure: OIDC login, ACR import, Container Apps update
- 📚 **Learn:** Container Apps: one app per service, internal vs external ingress, revisions and traffic split. Deploy from GitHub Actions with the OIDC login from W26 (no stored secret): import images from GHCR into ACR, then `az containerapp update --image` per service; a `production` environment with a required reviewer gates the job. Read: [Azure Container Apps: Java overview](https://learn.microsoft.com/en-us/azure/container-apps/java-overview). Optional: [GitHub Docs: OIDC in Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure).
- 🛠️ **Do:** Add a `deploy-azure` job to `cd.yml` (manual trigger + `production` approval): `azure/login` via OIDC, `az acr import` for the 5 images and ticketverse-ai, then `az containerapp update --image` per service, with resource names read from repository variables that you fill from Azure W28's Bicep outputs on Saturday; until then a dry-run step only lists your resource groups. Done when: the job runs green in dry-run mode with no stored Azure secret.

### Friday 07 May · 60 min — Application Insights via OpenTelemetry, KQL queries, teardown script
- 📚 **Learn:** Azure Monitor OpenTelemetry for Java (the Application Insights Java agent or the Spring Boot integration): application map, end-to-end transactions, failures; KQL over `requests`, `dependencies` and `traces`; cost guardrails: smallest SKUs, min replicas 0-1, stop the dev database at night, delete by resource group. Read: [Enable OpenTelemetry in Application Insights (Java)](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=java). Optional: [App Insights for Spring Boot](https://learn.microsoft.com/en-us/azure/azure-monitor/app/java-spring-boot).
- 🛠️ **Do:** Copy the Application Insights Java agent (`com.microsoft.azure:applicationinsights-agent`) into your images and attach it only via `JAVA_TOOL_OPTIONS` in the cloud environment; check that services still start locally without it. Save 3 KQL queries for Saturday in `docs/kql.md` (p95 by operation, failed dependencies, bookings per hour) and write `infra/teardown`: `az stack group delete --action-on-unmanage deleteAll` (the stack's deny settings block a plain group delete), then delete the group and check `az group exists` returns false. Done when: the queries are saved and teardown is proven on a throwaway group.

### Saturday 08 May · 60 min — BUILD: TicketVerse live on Azure (joint deploy with Azure W28)
- 📚 **Learn:** Joint run with today's Azure lab, which provisions the TicketVerse infrastructure with Bicep, so do this block after the Azure lab today (swap the order once). Checklist: copy the Bicep outputs into repository variables and Key Vault, run `deploy-azure`, verify health, run both sagas and the AI e2e script on the public HTTPS URL, capture an App Insights trace and the cost to date, record the demo, tear down once. Reference: [Azure Container Apps docs](https://learn.microsoft.com/en-us/azure/container-apps/). Optional: [Azure CLI docs](https://learn.microsoft.com/en-us/cli/azure/).
- 🛠️ **Do:** Today Azure's lab runs first and provisions the stack. Then, from your personal laptop or a Codespace: run the deploy job, wait for health, run the smoke script (both sagas) and `scripts/e2e-ai` against the live URL, capture an Application Insights end-to-end transaction and the cost analysis view, and record a 5-minute demo video. Leave the stack running: the AI block uses it, then runs `infra/teardown`. Done when: both sagas pass on the live URL, `v2.2.0` is tagged, the video is linked in the README and spend stays within budget.

## 📦 Deliverable (by Saturday night)
ADR-003, `docs/azure-contract.md`, cloud profiles with zero hard-coded settings, Key Vault + identity mapping, a `deploy-azure` OIDC job, App Insights agent + saved KQL, `infra/teardown`; TicketVerse (with ticketverse-ai) live on Azure Container Apps on infrastructure provisioned by Azure W28, demo video, verified teardown, tag `v2.2.0`.

## ✅ Self-check (Sunday test preview)
- Container Apps vs AKS: which did you choose for TicketVerse and why?
- How do managed identities and Key Vault references remove secrets from your deployment?
- What changes when Spring Kafka talks to the Event Hubs Kafka endpoint?
- How did the Java and Azure tracks split the work, and what was in your infra contract?
- How did you keep the Azure bill under control, and how do you verify teardown?
- Which Application Insights views or KQL queries help you debug a slow booking?
- What would you change to make this deployment production-grade (HA, backups, private networking)?

## 🚀 Stretch (optional)
Add revision-based traffic splitting (90/10) for booking-service on Container Apps before teardown. Extra: deploy the Helm chart to a small AKS cluster with Workload ID on a separate evening, then tear it down the same day.
