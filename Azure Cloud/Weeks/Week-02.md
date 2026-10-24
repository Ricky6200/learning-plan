# ☁️ Azure Cloud · Week 02 — Azure architecture, compute and networking services

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** Regions, availability zones and the management group > subscription > resource group hierarchy appear in every Azure design discussion, and picking the right compute and network service for a Java backend is the core of AZ-900's biggest domain (35-40%).

## 🗓️ Sessions

### Tuesday 03 Nov · 45 min — Regions, availability zones and the resource hierarchy
- 📚 **Learn:** Regions, region pairs and sovereign regions, availability zones, datacenters; resources, resource groups, subscriptions, management groups and how they nest. Use [Describe the core architectural components of Azure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/), Savill's [Regions and region pairs](https://www.youtube.com/watch?v=4RjPOAN54AE) and [Azure region pairs](https://learn.microsoft.com/en-us/azure/reliability/regions-paired).
- 🛠️ **Do:** Draw (Excalidraw or draw.io) a TicketVerse hierarchy: tenant -> management group -> dev and prod subscriptions -> one resource group per workload -> resources, plus a zone-redundant API across 3 zones in Central India. Look up (don't guess) Central India's paired region and two services that support zone redundancy. Done when: diagram + 5 annotated facts committed and the module assessment passed.

### Wednesday 04 Nov · 45 min — Compute options: VMs, scale sets, containers, functions, AVD
- 📚 **Learn:** Compare VMs, containers and functions; VM options (Virtual Machine Scale Sets, availability sets, Azure Virtual Desktop); resources a VM needs (disk, NIC, VNet, IP); app hosting choices (App Service, containers, VMs). Use [Describe Azure compute services](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/), Savill's [Resources required for VMs](https://www.youtube.com/watch?v=PP5BWZ0cAJo) and [Serverless technologies](https://www.youtube.com/watch?v=-xeJGiMw5OE).
- 🛠️ **Do:** Make `w02/compute.md` with 6 workloads: Spring Boot REST API, nightly batch job, legacy Windows app, image resize on upload, 2,000 call-centre desktops, Kafka consumer. For each choose VM, VMSS, App Service, Container Apps, AKS, Functions or AVD, plus its scaling model and a one-line reason. Done when: 6 rows are filled and you can defend each choice in one sentence.

### Friday 06 Nov · 45 min — Networking: VNets, peering, DNS, VPN Gateway, ExpressRoute, endpoints
- 📚 **Learn:** Virtual networks and subnets, peering, Azure DNS, VPN Gateway vs ExpressRoute, public vs private endpoints. Use [Describe Azure networking services](https://learn.microsoft.com/en-us/training/modules/describe-azure-networking-services/), Savill's [Core network resources](https://www.youtube.com/watch?v=aNK0C9Oj2sg) and [Public and private endpoints](https://www.youtube.com/watch?v=bPNkXwRFsek).
- 🛠️ **Do:** Sketch: office -> VPN Gateway (or ExpressRoute) -> hub VNet -> peered spoke VNet with app and DB subnets; App Service reaching a storage account through a private endpoint. Mark which hops cross the public internet. Write 5 flashcards: VPN vs ExpressRoute, peering vs VPN, public vs private endpoint, DNS zone vs record, VNet vs subnet. Done when: sketch + flashcards committed.

### Saturday 07 Nov · 60 min — LAB: VM + App Service via CLI, then delete
- 📚 **Learn:** CLI flow for a VM (B-series size, SSH key, cloud-init, auto-shutdown) and a web app (`az webapp up --html` on the Free tier), then teardown by resource group. New VNets now default to private subnets, so VMs need an explicit outbound path such as a public IP ([default outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access)). Use [Create a Linux VM with CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli).
- 🛠️ **Do:** Path A: run `new-lab.sh 02`; create a `Standard_B1s` Ubuntu VM with `--generate-ssh-keys` and `--custom-data` cloud-init that installs nginx; `az vm open-port --port 80`; set auto-shutdown; deploy a hello page with `az webapp up --html --sku F1`; curl both URLs; run `nuke-lab.sh 02`. Path B: write the same `w02/deploy.sh`, read each command's `--help` and price it in the pricing calculator. Done when: script + curl output (or estimate) committed and the RG is gone.

## 📦 Deliverable (by Saturday night)
`w02/` hierarchy diagram, compute decision table, network sketch + flashcards, and `deploy.sh` with curl evidence and RG deletion (Path B: pricing-calculator estimate).

## ✅ Self-check (Sunday test preview)
- Region vs availability zone vs region pair: what failure does each protect against?
- Describe the hierarchy from management group to resource. Where do Azure Policy and RBAC assignments inherit?
- Virtual Machine Scale Sets vs availability sets: when would you use each?
- VPN Gateway vs ExpressRoute: how do path, bandwidth and cost model differ?
- Public endpoint vs private endpoint for a storage account: what changes for an app inside a VNet?
- Which resources does `az vm create` create implicitly when you only pass a name and an image?

## 🚀 Stretch (optional)
Watch Adam Marczak's [Compute Services episode](https://www.youtube.com/watch?v=inaXkN2UrFE) and add three differences between Container Instances and Container Apps to your notes.
