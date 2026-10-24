# ☁️ Azure Cloud · Week 23 — Containers on Azure: ACR, ACA, AKS + Boss

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Containerized solutions are 20-25% of AI-200 and the way TicketVerse ships: registries, Container Apps with KEDA, AKS manifests and troubleshooting. The Season 5 Boss provisions TicketVerse's Azure infrastructure alongside the Java track's W23 deployment.

## 🗓️ Sessions

### Tuesday 30 Mar · 45 min — ACR images and tasks; containers on App Service
- 📚 **Learn:** Repositories, tags vs digests, versioning (semver + git SHA), ACR Tasks (`az acr build`, triggers, multi-step; task runs are paused on Azure free credits, so use pay-as-you-go or build locally), App Service custom containers with managed-identity pulls, env vars and Key Vault references. Use Learn's [Store and manage containers in ACR](https://learn.microsoft.com/en-us/training/modules/store-manage-containers-azure-container-registry/), [ACR Tasks overview](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview) and [Deploy containers to App Service](https://learn.microsoft.com/en-us/training/modules/deploy-containers-azure-app-service/).
- 🛠️ **Do:** Build the TicketVerse API image with `az acr build` (or `docker build` + `docker push` if Tasks are unavailable), tagging both `1.0.0` and the git SHA; inspect digests with `az acr manifest list-metadata`. Deploy it to a Linux App Service (B1) that pulls via managed identity, with one env var and one Key Vault-referenced secret; check the container log stream. Done when: tags/digest, the running app and a log excerpt are in `w23/`; RG deleted.

### Wednesday 31 Mar · 45 min — Container Apps: environments, revisions, secrets, KEDA scaling
- 📚 **Learn:** Environments (consumption and workload profiles, Log Analytics), revision modes (single vs multiple) and traffic splitting, secrets and env vars, managed-identity registry pulls, health probes, KEDA scale rules (HTTP, azure-servicebus queue length) and scale to zero. Use [Revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions), [Scaling](https://learn.microsoft.com/en-us/azure/container-apps/scale-app) and Learn's [Scale containers in Azure Container Apps](https://learn.microsoft.com/en-us/training/modules/scale-containers-azure-container-apps/).
- 🛠️ **Do:** Deploy your image to Container Apps with a managed-identity ACR pull. Switch to multiple-revision mode, deploy a v2 revision, split traffic 80/20, then roll back to 100/0. Deploy the W20 Service Bus worker as a second app with a KEDA `azure-servicebus` rule (min 0, max 5); send 200 messages and watch replicas scale out and back to zero. Done when: traffic-split and replica-count evidence are in `w23/`.

### Friday 02 Apr · 45 min — AKS with manifests + troubleshooting pods, logs, events, connectivity
- 📚 **Learn:** AKS Free tier, `--node-count 1` (default is 3), system node pools need 4+ vCPUs and no B-series, ACR attach, Deployment/Service/ConfigMap/Secret manifests, probes, `kubectl get/describe/logs/events`, Container Insights; route HTTP with Gateway API, not the retired ingress-nginx. Use the [AKS CLI quickstart](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli), Learn's [Monitor and troubleshoot apps on AKS](https://learn.microsoft.com/en-us/training/modules/monitor-apps-azure-kubernetes-service/) and [Stop/start AKS](https://learn.microsoft.com/en-us/azure/aks/start-stop-cluster).
- 🛠️ **Do:** Create a Free-tier AKS cluster with one 4-vCPU node and `--attach-acr`; apply your Deployment (2 replicas, readiness probe), ConfigMap and LoadBalancer Service manifests from the Java track. Break it twice (wrong image tag -> ImagePullBackOff; wrong port -> failing probe), diagnose with describe, logs and events, then fix. Finally `az aks stop` or delete. Done when: diagnosis notes and the fixed rollout are in `w23/`; cluster stopped or deleted.

### Saturday 03 Apr · 60 min — BOSS BATTLE: Provision TicketVerse on Azure, verify, tear down
- 📚 **Learn:** Season 5 integration with the Java track's W23 deploy: ACR, Container Apps (or AKS), PostgreSQL Flexible, Azure Managed Redis, Key Vault, Application Insights and managed identities. Use [Migrate Spring Boot to Container Apps](https://learn.microsoft.com/en-us/azure/developer/java/migration/migrate-spring-boot-to-azure-container-apps), [Managed-identity image pull](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity-image-pull) and your W19, W22 and W23 scripts.
- 🛠️ **Do:** 60-minute timer. 0-10: assemble `w23/provision.sh` from your W19, W22 and W23 scripts and start Managed Redis + PostgreSQL first in `rg-boss-s5`. 10-35: ACR push, Container Apps app with managed identity, Key Vault secret references, Application Insights connection string. 35-50: hit `/actuator/health` and find the request in Application Insights. 50-60: delete the RG. Done when: health 200 + telemetry screenshot committed and the RG is deleted.

## 📦 Deliverable (by Saturday night)
`w23/` image tags/digest and App Service log, Container Apps traffic-split and KEDA scaling evidence, AKS troubleshooting notes, `provision.sh` and the Boss health/telemetry evidence - with every RG deleted.

## ✅ Self-check (Sunday test preview)
- Tag vs digest: why pin production deployments to a digest?
- What does an ACR Task give you that a local docker build doesn't?
- Single vs multiple revision mode in Container Apps: how do you run a canary release?
- How does KEDA scale a Service Bus worker to zero and back?
- A pod is stuck in ImagePullBackOff: what are your first three troubleshooting commands?
- Container Apps vs AKS for TicketVerse: which would you choose, and why?
- How does a container app pull from ACR without admin credentials?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Deploy cloud-native apps using Azure Container Apps](https://learn.microsoft.com/en-us/credentials/applied-skills/deploy-cloud-native-apps-using-azure-container-apps/) or do the exercise in Learn's [Deploy applications to AKS](https://learn.microsoft.com/en-us/training/modules/deploy-apps-azure-kubernetes-service/).
