# ☁️ Azure Cloud · Week 11 — VMs II, containers and App Service

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** AZ-104 expects you to choose and run the right compute: VM availability, scale sets, containers and App Service. Java teams usually land a Spring Boot app on App Service or containers first, so this week mirrors a real first deployment - including HTTPS-only and TLS settings that security reviews check.

## 🗓️ Sessions

### Tuesday 05 Jan · 45 min — Availability sets, zones, scale sets and moving VMs
- 📚 **Learn:** Availability sets (fault and update domains) vs availability zones, Virtual Machine Scale Sets (Flexible vs Uniform, autoscale), moving resources across RGs, subscriptions and regions (Resource Mover). Read [Configure virtual machine availability](https://learn.microsoft.com/en-us/training/modules/configure-virtual-machine-availability/). Optional: [Move resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription).
- 🛠️ **Do:** Create a Flexible scale set with 2 small instances across zones 1 and 2, add an autoscale rule (CPU above 70% adds 1, max 3), list instances with their zones, then scale to 0. Create an availability set (`az vm availability-set create`, 2 fault domains) and note why an existing VM can't join it. Create an empty managed disk in one RG and `az resource move` it to another; note what a VM move must bring along (NIC, disks, IP). Done when: the instance/zone list, availability set and move output are in `w11/` and RGs are deleted.

### Wednesday 06 Jan · 45 min — Containers: ACR, Container Instances and Container Apps basics
- 📚 **Learn:** Azure Container Registry (SKUs, Entra auth vs admin user, import), Container Instances (container groups, restart policy, CPU/memory sizing), Container Apps (environment, ingress, min/max replicas, scale rules) - building on your Java W11 Docker basics. Read [Configure Azure Container Instances](https://learn.microsoft.com/en-us/training/modules/configure-azure-container-instances/). Optional: the [Container Apps portal quickstart](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-portal).
- 🛠️ **Do:** Create a Basic ACR, `az acr import` the public image `mcr.microsoft.com/azuredocs/aci-helloworld` and list it with `az acr repository list`. Run the same public image on Container Instances (0.5 vCPU, 1 GiB, public IP), then deploy it in the portal to Container Apps with external ingress, min 0 / max 3 replicas and an HTTP scale rule. Curl both and compare startup, scaling and billing. Done when: both URLs answered and a 5-line comparison is committed; RG deleted.

### Friday 08 Jan · 45 min — App Service plans, scaling, TLS, custom domains, backup, networking
- 📚 **Learn:** Plan tiers and what they unlock (slots, autoscale, backups, VNet integration), scale up vs out, managed TLS certificates, custom domains (CNAME/A + TXT verification), backups, access restrictions, VNet integration and private endpoints. Read [Configure App Service plans](https://learn.microsoft.com/en-us/training/modules/configure-app-service-plans/). Optional: [App Service networking features](https://learn.microsoft.com/en-us/azure/app-service/networking-features).
- 🛠️ **Do:** Build `w11/appservice-matrix.md` comparing Free, Basic, Standard and Premium: deployment slots, autoscale, backups, VNet integration, custom domain + TLS. Answer 5 scenarios (e.g., the cheapest tier with a staging slot and autoscale). Write the DNS records you would add to map `api.ticketverse.in` and bind a managed certificate. Done when: matrix, 5 answers and the DNS plan are committed.

### Saturday 09 Jan · 60 min — LAB: Java app on App Service: slot swap, HTTPS-only, TLS
- 📚 **Learn:** Java SE on App Service (Java 21 or 25), `az webapp deploy` for JARs, deployment slots (Standard tier or higher), slot-sticky settings, swap, HTTPS-only, minimum TLS version and access restrictions. Read [Set up staging environments](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots). Optional: the [Java SE quickstart](https://learn.microsoft.com/en-us/azure/app-service/quickstart-java?pivots=java-javase) - its sample Spring Boot app is today's JAR (Spring Boot comes in Java W13; treat it as a black box).
- 🛠️ **Do:** In Cloud Shell (JDK + Maven included) clone the quickstart's Spring Boot sample and package it twice, changing the greeting to v1, then v2. Create a Linux S1 plan and a Java SE web app; deploy v1 to production and v2 to a `staging` slot; make one setting slot-sticky; swap and verify, then swap back in Az PowerShell (`Switch-AzWebAppSlot`). Set `az webapp update --https-only true`, `az webapp config set --min-tls-version 1.2` and an access restriction allowing only your laptop's IP (Cloud Shell curl gets 403). Delete the RG. Done when: swap, TLS and 403 evidence are in `w11/`.

## 📦 Deliverable (by Saturday night)
`w11/` scale set, availability set + move evidence, ACR/ACI/Container Apps comparison, App Service tier matrix with DNS plan, and slot-swap (CLI + PowerShell), HTTPS-only, TLS and access-restriction evidence.

## ✅ Self-check (Sunday test preview)
- Availability set vs availability zone vs scale set: what failure scope and SLA does each address?
- Flexible vs Uniform scale set orchestration: which would you choose for a mixed fleet, and why?
- Container Instances vs Container Apps vs AKS: pick one for a one-off batch job, a scale-to-zero API and a 20-service platform.
- Which App Service tier is the minimum for deployment slots and autoscale?
- What is a slot-sticky setting and when do you need one?
- How do you map a custom domain to App Service, bind a free managed certificate and force HTTPS with TLS 1.2+?
- Scale up vs scale out in App Service: what changes, and which one affects running instances?

## 🚀 Stretch (optional)
Do the Learn module [Deploy a Spring Boot app to Azure Container Apps](https://learn.microsoft.com/en-us/training/modules/java-spring-on-azure-container-apps/) and compare cold start and cost with App Service; the official [AZ-104 Lab 09a - web apps](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09a-Implement_Web_Apps.html) and [Lab 09c - Container Apps](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_09c-Implement-Azure-Container-Apps.html) cover the same portal tasks.
