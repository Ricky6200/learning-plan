# ☁️ Azure Cloud · Week 23 — Containers on Azure: ACR Tasks, Container Apps, AKS

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Containerized solutions are 20-25% of AI-200 and the way TicketVerse and DocuMind ship: ACR Tasks builds, Container Apps revisions and KEDA scaling, and AKS manifests with troubleshooting. TicketVerse's own Azure infrastructure comes later, as code, in W28 alongside the Java track's deploy.

## 🗓️ Sessions

### Tuesday 30 Mar · 45 min — ACR Tasks and a Container Apps environment
- 📚 **Learn:** Repositories, tags vs digests, versioning (semver + git SHA), ACR Tasks quick builds (`az acr build` runs in Azure - no local Docker; Tasks are paused on free credits, which you left in W9), Container Apps environments (Consumption, Log Analytics) and managed-identity registry pulls. Read the [ACR Tasks overview](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview). Optional: Learn's [Store and manage containers in ACR](https://learn.microsoft.com/en-us/training/modules/store-manage-containers-azure-container-registry/).
- 🛠️ **Do:** In `rg-lab-w23` (keep it all week) create a Basic ACR. Write a 10-line FastAPI `hello-api` (`/health`, `/version`) with a Dockerfile in `w23/`, then `az acr build` it tagged `1.0.0` and the git SHA; inspect digests with `az acr manifest list-metadata`. Create a Container Apps environment (`az containerapp env create`) and deploy the image with `--registry-identity system` and external ingress. Done when: tags/digest and a 200 from `/health` are in `w23/`.

### Wednesday 31 Mar · 45 min — Container Apps: revisions, traffic splitting and KEDA scaling
- 📚 **Learn:** Revision modes (single vs multiple) and traffic splitting, secrets and environment variables, health probes, KEDA scale rules (HTTP, `azure-servicebus` queue length) and scale to zero. Read [Revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions). Optional: [Scaling](https://learn.microsoft.com/en-us/azure/container-apps/scale-app).
- 🛠️ **Do:** Switch `hello-api` to multiple-revision mode, deploy a v2 revision, split traffic 80/20, then roll back to 100/0. Build your W20 Service Bus worker with `az acr build`, create a queue in a new Standard namespace and deploy the worker as a second app with a KEDA `azure-servicebus` rule (min 0, max 5; connection string as a secret); send 200 messages and watch replicas scale out and back to zero. Delete the namespace. Done when: traffic-split and replica-count evidence are in `w23/`.

### Friday 02 Apr · 45 min — AKS: deploy with manifests, troubleshoot one failure
- 📚 **Learn:** AKS Free tier, `--node-count 1` (default is 3), system node pools need 4+ vCPUs and no B-series, `--attach-acr`, Deployment/Service/ConfigMap manifests, probes, `kubectl get/describe/logs/events`; route HTTP with Gateway API, not the retired ingress-nginx. Microsoft Entra Workload ID lets pods use a managed identity without secrets - Java's Azure deploy relies on it. Read the [AKS CLI quickstart](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli). Optional: [Workload ID overview](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview).
- 🛠️ **Do:** Minute 0: `az aks create` (Free tier, one 4-vCPU node, `--attach-acr` to your W23 registry, `--no-wait`) and read the Workload ID overview while it builds. Then `az aks get-credentials` (kubectl via Cloud Shell or `az aks install-cli`) and apply a Deployment (2 replicas, readiness probe), ConfigMap and LoadBalancer Service for `hello-api` (or your Java W23 manifests). Break it once (wrong image tag -> ImagePullBackOff), diagnose with describe, logs and events, fix it. Delete the cluster. Done when: diagnosis notes and the fixed rollout are in `w23/`.

### Saturday 03 Apr · 60 min — LAB: Ship an AI-track container to Container Apps
- 📚 **Learn:** Deploy what the AI track built: ACR Tasks can build straight from a GitHub repo, a user-assigned identity pulls the image and reads Key Vault, and secrets use `keyvaultref:<secret-uri>,identityref:<identity-id>`, surfaced to the app with `secretref:`. Read [Manage secrets in Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets). Optional: [Health probes](https://learn.microsoft.com/en-us/azure/container-apps/health-probes).
- 🛠️ **Do:** 0-10: `az acr build` DocuMind's image (AI W13) from your GitHub repo (`https://github.com/<you>/<repo>.git#main:<folder>`); if it can't start without its database, use `mcr.microsoft.com/k8se/quickstart:latest` - the platform steps are identical. 10-30: create a user-assigned identity (AcrPull + Key Vault Secrets User), store the LLM key in Key Vault and create the app in your W23 environment with that identity, the Key Vault secret reference, ingress on the app port, min 0 / max 2 replicas and a readiness probe. 30-40: curl it, read log stream and system logs. 40-45: delete `rg-lab-w23`. Done when: a 200 response and logs are in `w23/`.

## 📦 Deliverable (by Saturday night)
`w23/` `hello-api` tags/digest, Container Apps traffic-split and KEDA scaling evidence, AKS troubleshooting notes, and an AI-track container (or the sample image) running on Container Apps with a Key Vault-backed secret - with `rg-lab-w23` deleted.

## ✅ Self-check (Sunday test preview)
- Tag vs digest: why pin production deployments to a digest?
- What does an ACR Task give you that a local docker build doesn't, and how does a container app then pull the image without admin credentials?
- Single vs multiple revision mode in Container Apps: how do you run a canary release?
- How does KEDA scale a Service Bus worker to zero and back?
- A pod is stuck in ImagePullBackOff: what are your first three troubleshooting commands?
- What does AKS Workload ID give a pod, and why is it better than mounting a client secret?
- Container Apps vs AKS for TicketVerse: which would you choose, and why?

## 🚀 Stretch (optional)
Work through the official AI-200 modules [Deploy applications to AKS](https://learn.microsoft.com/en-us/training/modules/deploy-apps-azure-kubernetes-service/), [Monitor and troubleshoot apps on AKS](https://learn.microsoft.com/en-us/training/modules/monitor-apps-azure-kubernetes-service/) and [Scale containers in Azure Container Apps](https://learn.microsoft.com/en-us/training/modules/scale-containers-azure-container-apps/), or attempt the hosted Applied Skills lab [Deploy cloud-native apps using Azure Container Apps](https://learn.microsoft.com/en-us/credentials/applied-skills/deploy-cloud-native-apps-using-azure-container-apps/).
