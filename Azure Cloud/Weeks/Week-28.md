# ☁️ Azure Cloud · Week 28 — TicketVerse infrastructure as code + landing zones

> 📅 **Mon 03 May 2027 → Sun 09 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 27](Week-27.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-28.md) · [Week 29 →](Week-29.md)

**Why this week:** Production teams never click resources into existence: Bicep modules, Azure Verified Modules and deployment stacks make TicketVerse's infrastructure repeatable, reviewable and removable in one command, and landing-zone thinking (CAF Ready) is what architects ask about first. Saturday provisions the real infrastructure the Java track deploys onto in its W28.

## 🗓️ Sessions

### Tuesday 04 May · 45 min — Bicep modules and Azure Verified Modules
- 📚 **Learn:** Modules (`module x './file.bicep'`), `.bicepparam` files, outputs passed between modules, and Azure Verified Modules: Microsoft-maintained registry modules (`br/public:avm/res/<provider>/<type>:<version>`) with secure defaults - pin the version. Terraform is the main alternative (a state file, AzureRM/AzAPI providers; AVM ships Terraform modules too). Read [Bicep modules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules). Optional: the [AVM Bicep quickstart](https://azure.github.io/Azure-Verified-Modules/usage/quickstart/bicep/).
- 🛠️ **Do:** On the personal laptop (VS Code + Bicep extension), write `ticketverse/infra/azure/platform.bicep` from AVM modules: Log Analytics workspace, workspace-based Application Insights, Basic ACR, Container Apps environment, and one user-assigned identity per TicketVerse service (a `for` loop over a `services` array). Add `main.bicep` calling it plus `main.bicepparam`. Run `az bicep build` and `az deployment group what-if` against an empty `rg-tv-dev`. Done when: what-if lists only creates and no errors.

### Wednesday 05 May · 45 min — Landing zones: CAF Ready, design areas, subscription vending
- 📚 **Learn:** The CAF Ready phase prepares an Azure landing zone: platform landing zones (identity, management, connectivity) plus application landing zones, designed across 8 areas (billing and tenant, identity and access, resource organization, network, security, management, governance, platform automation), subscription vending (a request becomes a governed subscription) and policy-driven governance. Read [Azure landing zone design areas](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas). Optional: [Subscription vending](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending).
- 🛠️ **Do:** Write `w28/landing-zone.md` for a company running TicketVerse: a management-group tree (Platform, Landing zones -> Corp/Online, Sandbox, Decommissioned), subscriptions (connectivity, management, identity, ticketverse-prod, ticketverse-dev), one decision per design area, 5 policies with their scope (e.g., allowed locations, deny public IPs in Corp, deploy diagnostic settings, require tags, Defender plans) and a subscription-vending request as 10 lines of YAML. Done when: the design and a diagram are committed.

### Friday 07 May · 45 min — Deployment stacks and the TicketVerse data tier
- 📚 **Learn:** Deployment stacks manage a template's resources as one unit: deny settings (`denyDelete`) block out-of-band deletes, `--action-on-unmanage` decides whether removed resources are detached or deleted, and one command tears everything down. Stacks also have their own what-if. Read [Create and deploy deployment stacks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks). Optional: [Preview stack changes with what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks-what-if).
- 🛠️ **Do:** Add `data.bicep` from AVM modules: Key Vault (RBAC), PostgreSQL Flexible Server (Burstable B1ms; `catalog` and `booking` databases; admin password as a `@secure()` parameter, never committed), the smallest Azure Managed Redis, and an Event Hubs Standard namespace with one hub per TicketVerse Kafka topic. Add role assignments: AcrPull and Key Vault Secrets User for every service identity, Event Hubs Data Sender/Receiver only where needed. Run what-if on the full `main.bicep` and price one day of the stack in `w28/cost.md`. Done when: what-if is clean and the daily cost is estimated.

### Saturday 08 May · 60 min — LAB: Provision TicketVerse on Azure with a deployment stack
- 📚 **Learn:** One stack, outputs handed to the app team as JSON, a cost check and a one-command teardown. Today's order: this lab runs first, Java W28 then deploys TicketVerse onto the stack, and the AI block checks it live and tears it down. Read the [deployment stacks quickstart](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/quickstart-create-deployment-stacks).
- 🛠️ **Do:** Today this lab runs right after DSA, before Java deploys. Minute 0: `az stack group create -n tv -g rg-tv-dev -f main.bicep -p main.bicepparam --deny-settings-mode denyDelete --action-on-unmanage deleteAll` (Redis and PostgreSQL take longest). Meanwhile write `w28/handoff.md`: what each service needs (ACR login server, environment ID, identity client IDs, Key Vault URI, Event Hubs bootstrap server). Then verify: try deleting one resource (denied), save the stack outputs to `infra/azure/outputs.json` and check Cost Management's forecast; the AI block tears the stack down tonight. Done when: the stack succeeded, outputs are committed and the Java track has its handoff.

## 📦 Deliverable (by Saturday night)
`ticketverse/infra/azure/` (platform + data Bicep from Azure Verified Modules, `main.bicepparam`, `outputs.json`), `w28/landing-zone.md` with a diagram, `w28/cost.md`, `w28/handoff.md`, and the TicketVerse stack running for the Java W28 deploy - deleted with one command the same evening, once the AI block's live check is done.

## ✅ Self-check (Sunday test preview)
- Bicep module vs Azure Verified Module: what does AVM give you, and why pin its version?
- Bicep vs Terraform: name two practical differences (state, providers, tooling).
- What is a deployment stack, and how do deny settings and actionOnUnmanage protect and clean up resources?
- Name the eight landing-zone design areas; which two would you settle first for TicketVerse?
- What is subscription vending, and why does policy-driven governance scale better than manual reviews?
- Platform landing zone vs application landing zone: what lives in each?
- How do you hand infrastructure outputs to an application team without sharing any secret?

## 🚀 Stretch (optional)
Deploy the same stack from a GitHub Actions workflow using your W22 federated credential, then skim the [CAF Ready overview](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/) to see where landing zones fit in the adoption journey.
