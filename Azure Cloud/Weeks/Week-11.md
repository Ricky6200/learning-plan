# ☁️ Azure Cloud · Week 11 — VMs II, containers and App Service

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** AZ-104 expects you to choose and run the right compute: VM availability, scale sets, containers and App Service. Java teams usually land a Spring Boot app on App Service or containers first, so this week mirrors a real first deployment.

## 🗓️ Sessions

### Tuesday 05 Jan · 45 min — Availability sets, zones, scale sets and moving VMs
- 📚 **Learn:** Availability sets (fault and update domains) vs availability zones, Virtual Machine Scale Sets (Flexible vs Uniform, autoscale), moving resources across RGs, subscriptions and regions (Resource Mover). Use [Configure virtual machine availability](https://learn.microsoft.com/en-us/training/modules/configure-virtual-machine-availability/), [Scale sets overview](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview) and [Move resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).
- 🛠️ **Do:** Create a Flexible scale set with 2 small instances across zones 1 and 2, add an autoscale rule (CPU above 70% adds 1, max 3), list instances with their zones, then scale to 0. Create an empty managed disk in one RG and `az resource move` it to another; note what a VM move must bring along (NIC, disks, IP). Done when: the instance/zone list and move output are in `w11/` and RGs are deleted.

### Wednesday 06 Jan · 45 min — Containers in the portal: ACR, Container Instances, Container Apps
- 📚 **Learn:** Azure Container Registry (SKUs, Entra auth vs admin user), Container Instances (container groups, restart policy, CPU/memory sizing), Container Apps (environment, ingress, min/max replicas, scale rules). Use [Configure Azure Container Instances](https://learn.microsoft.com/en-us/training/modules/configure-azure-container-instances/), the [Container Apps portal quickstart](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-portal) and [AZ-104 Lab 09c - Container Apps](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09c-Implement-Azure-Container-Apps.html).
- 🛠️ **Do:** Create a Basic ACR and `az acr import` the public image `mcr.microsoft.com/azuredocs/aci-helloworld`. Run it on Container Instances with 0.5 vCPU and 1 GiB, then deploy the same image in the portal to Container Apps with external ingress, min 0 / max 3 replicas and an HTTP scale rule. Curl both and compare startup, scaling and billing. Done when: both URLs answered and a 5-line comparison is committed; RG deleted.

### Friday 08 Jan · 45 min — App Service plans, scaling, TLS, custom domains, backup, networking
- 📚 **Learn:** Plan tiers and what they unlock (slots, autoscale, backups, VNet integration), scale up vs out, managed TLS certificates, custom domains (CNAME/A + TXT verification), backups, access restrictions, VNet integration and private endpoints. Use [Configure App Service plans](https://learn.microsoft.com/en-us/training/modules/configure-app-service-plans/), [Configure Azure App Service](https://learn.microsoft.com/en-us/training/modules/configure-azure-app-services/) and [Networking features](https://learn.microsoft.com/en-us/azure/app-service/networking-features).
- 🛠️ **Do:** Build `w11/appservice-matrix.md` comparing Free, Basic, Standard and Premium: deployment slots, autoscale, backups, VNet integration, custom domain + TLS. Answer 5 scenarios (e.g., the cheapest tier with a staging slot and autoscale). Write the DNS records you would add to map `api.ticketverse.in` and bind a managed certificate. Done when: matrix, 5 answers and the DNS plan are committed.

### Saturday 09 Jan · 60 min — LAB: Spring Boot on App Service with a staging slot swap
- 📚 **Learn:** Java SE on App Service (Java 21 or 25), `az webapp deploy` for JARs, app settings, deployment slots (Standard tier or higher), slot-sticky settings, swap with preview. Use the [Java on App Service quickstart](https://learn.microsoft.com/en-us/azure/app-service/quickstart-java), [Set up staging environments](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots) and [AZ-104 Lab 09a - web apps](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09a-Implement_Web_Apps.html).
- 🛠️ **Do:** Build a Spring Boot JAR (TicketVerse v0 if ready, else Spring Initializr with a `/version` endpoint). Create a Linux S1 plan and a Java SE web app (check `az webapp list-runtimes --os linux`); deploy v1 to production and v2 to a `staging` slot; make one setting slot-sticky; swap, verify the version flip, swap back. Delete the RG immediately after. Done when: both versions served, swap evidence in `w11/`, RG deleted.

## 📦 Deliverable (by Saturday night)
`w11/` scale set + move evidence, ACR/ACI/Container Apps comparison, App Service tier matrix with DNS plan, and Spring Boot slot-swap evidence.

## ✅ Self-check (Sunday test preview)
- Availability set vs availability zone vs scale set: what failure scope and SLA does each address?
- Flexible vs Uniform scale set orchestration: which would you choose for a mixed fleet, and why?
- Container Instances vs Container Apps vs AKS: pick one for a one-off batch job, a scale-to-zero API and a 20-service platform.
- Which App Service tier is the minimum for deployment slots and autoscale?
- What is a slot-sticky setting and when do you need one?
- How do you map a custom domain to App Service and bind a free managed certificate?
- Scale up vs scale out in App Service: what changes, and which one affects running instances?

## 🚀 Stretch (optional)
Do the Learn module [Deploy a Spring Boot app to Azure Container Apps](https://learn.microsoft.com/en-us/training/modules/java-spring-on-azure-container-apps/) and compare cold start and cost with App Service.
