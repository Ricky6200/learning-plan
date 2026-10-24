# ☁️ Azure Cloud · Week 12 — Virtual networking I: VNets, routing, secure access

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** Networking is 15-20% of AZ-104 and where migrations usually break: overlapping address spaces, missing routes, open NSGs or public PaaS endpoints. Hub-spoke, Bastion and private endpoints are the patterns interviewers expect you to draw and defend.

## 🗓️ Sessions

### Tuesday 12 Jan · 45 min — VNets, subnets, peering and public IP addresses
- 📚 **Learn:** CIDR planning without overlaps, subnets (Azure reserves 5 IPs in each), VNet peering (non-transitive, gateway transit), Standard public IPs (Basic SKU retired on 30 Sep 2025), default outbound access changes. Use [Configure virtual networks](https://learn.microsoft.com/en-us/training/modules/configure-virtual-networks/), [Configure VNet peering](https://learn.microsoft.com/en-us/training/modules/configure-vnet-peering/) and [Public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses).
- 🛠️ **Do:** Write `w12/ipam.md`: hub 10.0.0.0/16 (AzureBastionSubnet /26, shared /24), spoke1 10.1.0.0/16 (app /24, data /24), spoke2 10.2.0.0/16; prove there are no overlaps and count usable IPs per subnet. Create the hub and spoke1 with CLI and peer them in both directions. Done when: the IP plan and `az network vnet peering list -o table` (both Connected) are committed.

### Wednesday 13 Jan · 45 min — NSGs, ASGs, effective rules and user-defined routes
- 📚 **Learn:** NSG processing (priority, default rules, inbound/outbound, subnet vs NIC), application security groups, effective security rules, route tables, next-hop types and system routes. Use [Configure network security groups](https://learn.microsoft.com/en-us/training/modules/configure-network-security-groups/), [Application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups) and [Control traffic flow with routes](https://learn.microsoft.com/en-us/training/modules/control-network-traffic-flow-with-routes/).
- 🛠️ **Do:** In spoke1 create NSG rules: allow 443 from Internet to ASG `asg-web`, allow 5432 from `asg-web` to `asg-db`, deny other inbound. Predict 4 packets (pass/fail), then check with effective rules and IP flow verify on a tiny VM without a public IP. Add a route table sending 0.0.0.0/0 to 10.0.1.4 (virtual appliance) and inspect effective routes. Done when: a prediction-vs-result table is in `w12/`.

### Friday 15 Jan · 45 min — Bastion, service endpoints and private endpoints
- 📚 **Learn:** Bastion SKUs (Developer is free in select regions but connects one VM in the same VNet - no peering; Basic and above support peered VNets), service vs private endpoints, private DNS zones such as `privatelink.blob.core.windows.net`, disabling public access. Use [Bastion SKU comparison](https://learn.microsoft.com/en-us/azure/bastion/bastion-sku-comparison), [Private endpoint overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) and [Private endpoint DNS values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns).
- 🛠️ **Do:** Draw both flows (service endpoint vs private endpoint) for a VM reaching storage: the route taken, the IP the VM resolves, and what the storage firewall sees. Write Saturday's `w12/hubspoke.sh` (VNets, peering, NSG, Bastion, storage + private endpoint + private DNS zone and link) and syntax-check it with `bash -n`. Done when: the diagram and script are committed.

### Saturday 16 Jan · 60 min — LAB: Hub-spoke, NSG, Bastion and a private endpoint to storage
- 📚 **Learn:** Hands-on with [Connect to storage using a private endpoint](https://learn.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-storage-portal), [AZ-104 Lab 04 - virtual networking](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_04-Implement_Virtual_Networking.html) and [Deploy Bastion](https://learn.microsoft.com/en-us/azure/bastion/quickstart-host-portal).
- 🛠️ **Do:** Run `hubspoke.sh`: hub + spoke peered; a VM with no public IP in the spoke app subnet; Bastion Developer on the spoke VNet (free) or Basic in the hub to test peered access (billed hourly - delete promptly); storage with public access disabled, a private endpoint and the private DNS zone linked. Via Bastion, `nslookup` returns a 10.x address and `curl -I` gets an HTTP reply; from your laptop you get 403. Done when: evidence committed, RG deleted.

## 📦 Deliverable (by Saturday night)
`w12/` IP plan, NSG/ASG prediction table, endpoint diagram, `hubspoke.sh` and private-endpoint DNS evidence.

## ✅ Self-check (Sunday test preview)
- Why is VNet peering non-transitive, and how do hub-spoke designs work around it?
- The subnet NSG allows 443 but the NIC NSG denies it: what happens to the traffic?
- What does a user-defined route with next hop 'Virtual appliance' do to internet-bound traffic?
- Service endpoint vs private endpoint: which gives the PaaS resource a private IP in your VNet?
- Why does private endpoint access fail without the right private DNS zone link?
- Which Bastion SKU is free, and which SKUs support VNet peering?
- Why might a brand-new VM fail to reach the internet in 2026, and how do you fix it?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Configure secure access to your workloads using Azure networking](https://learn.microsoft.com/en-us/credentials/applied-skills/configure-secure-workloads-use-azure-virtual-networking/).
