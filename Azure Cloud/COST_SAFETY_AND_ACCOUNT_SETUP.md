# 💸 Cost Safety & Account Setup — learn Azure without surprise bills

> Facts verified on official Microsoft pages on **24–25 Oct 2026**. Prices change and vary by region — always confirm in the
> [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) before creating anything you haven't priced.

## 1. The five rules (memorise these)

1. **Guardrails before resources.** Budget + alerts + MFA exist *before* your first VM. Budgets only **alert** — Microsoft's docs are explicit that resources aren't affected and consumption isn't stopped.
2. **One resource group per lab** (`rg-lab-wNN`), tagged `owner`, `week`, `expires`. Delete the whole group the **same day** — the few planned exceptions (the W17–W21 free-tier Cosmos DB account, W23's registry week, W28's one-day TicketVerse stack) are listed in Section 4.
3. **Smallest SKU that teaches the skill** (tables below). Bigger SKUs teach nothing extra in a lab.
4. **Evidence, then delete.** Screenshot/CLI output into `azure-labs/wNN/`, then `az group delete`. Nothing "for later".
5. **Sunday cost check (10 min)** — every week, no exceptions (ritual in Section 8).

## 2. Choose your account path (decide in W1 Fri)

> [!NOTE]
> **Microsoft Learn sandboxes are no longer available** (official [Learn FAQ](https://learn.microsoft.com/en-us/training/support/faq?pivots=sandbox)):
> module exercises now need your own subscription. That's why this plan gives you two clear paths.

| Path | Who | Lab subscription | When | How W1–W5 labs run |
|---|---|---|---|---|
| **A — Visual Studio subscription** | Your employer gives you a Visual Studio subscription with monthly Azure credits (and its policy allows personal learning) | Monthly dev/test credit: **$150** (VS Enterprise), **$100** (MSDN Platforms), **$50** (VS Professional / Test Professional); no credit card; spending cap stops services until next month unless you remove it | **W1** | Live in Azure from W1 |
| **B — Azure free account (default)** | Everyone else | **$200 credit for 30 days** + **12 months** of free amounts of 20+ popular services (new customers) + **65+ always-free** services | **W6 Tue, 1 Dec 2026** (AZ-104 labs start), on your personal laptop | "Script-first" mode: write and dry-run the scripts in W1–W5 (Azurite — VS Code extension or a Codespace — for the W3 storage lab); run them live from W6 |
| **C — early variant of B** | You'd rather have hands-on from week 2 | Same free account, on your personal laptop (browser + Cloud Shell until the W5 Sat setup) | **W2 Sat, 7 Nov 2026** | Live from W2 — but the $200 credit expires around 7 Dec (start of W7), so most AZ-104 labs run on pay-as-you-go (still small with same-day teardown) |

Why B activates in W6: AZ-900 is conceptual, and the 30-day credit is worth more when hands-on AZ-104 labs start.
**Azure for Students** ($100, no card) needs an academic email, so it usually doesn't apply to you.

**Path B timeline:** activate **Tue 1 Dec 2026** → the $200 credit ends around **31 Dec** → **upgrade to pay-as-you-go in
W9 Tue (22 Dec 2026)** so the W10 labs keep running and the 12-month free services (until about Dec 2027) stay with you.

**Where labs run:** live Azure work happens on your **personal laptop** (set up in W5 Sat: Azure CLI + Bicep, PowerShell 7 +
Az, Git, VS Code with the Azure/Bicep extensions, uv + Python 3.12, JDK 25) or in a **GitHub Codespace**. The company laptop
blocks personal sign-in and the Azure VS Code extensions, so there you only run `az` CLI and `az bicep build`.

### India-specific notes for the free account (Path B/C)

- Sign up through **"Try Azure for free"**, not directly for pay-as-you-go: the Azure free-services page states the
  12-month free services are *not currently available to customers who sign up directly for pay as you go in China and India*.
- During sign-up a **temporary $1 authorization** may appear on your card; it is reversed after verification.
- With the free account your card **isn't charged**; when the credit is used up or the 30 days end, the subscription is
  **disabled** until you upgrade. To keep the **12 months of free services**, **move to pay-as-you-go within 30 days**
  (this plan does it in W9 Tue).
- After upgrading there is **no spending cap** — your budgets and alerts are now your only early warning. Set them first.

## 3. Activation-day checklist (W1 for Path A · W6 Tue for Path B · W2 Sat for Path C)

- [ ] **Secure the account:** MFA on (Entra [security defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults) require MFA registration); never share the login.
- [ ] **Cloud-only admin:** create `labadmin@<tenant>.onmicrosoft.com` (Global Administrator). It starts the Entra ID P2 trial in W6 (the trial is often unavailable to the personal account that created the tenant) and is your Azure SQL Entra admin fallback in W27/W30.
- [ ] **Budget at subscription scope:** small monthly amount (e.g., INR 500); alerts at **50% / 80% / 100% actual** and **100% forecast** to your email ([tutorial](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)).
- [ ] **Action group** (email + Azure mobile app push) attached to the budget.
- [ ] **Cost anomaly alert** on the subscription ([cost alerts](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending)).
- [ ] **CLI defaults:** `az config set defaults.location=centralindia` (Central India has 3 availability zones; its region pair is South India).
- [ ] **Azure Policy:** *Allowed locations* = your lab regions (e.g., Central India, South India). If a Learn exercise needs another region, add it temporarily; before AI W25, exempt the AI resource group if a Foundry model is only offered elsewhere (command prepared in W7 Fri). Use **Audit** (not Deny) for "require tag" policies so exercise scripts don't break (W7 Wed tests Deny once, then removes it).
- [ ] **Lab scripts** (`scripts/new-lab.sh`, `scripts/nuke-lab.sh`, Section 5) committed and tested once.
- [ ] Note in `azure-labs/cost-log.md`: activation date, credit end date (+30 days), pay-as-you-go upgrade date (W9 Tue).

## 4. Cheapest sensible SKUs for every lab in this plan

| Service (week) | Use in labs | Cost traps and facts |
|---|---|---|
| Virtual machines (W2, W10–W14, W29) | B-series (`Standard_B1s` is in the 12-month free hours); auto-shutdown on | **Stopped (allocated) is still billed** — use `az vm deallocate` ([states & billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)). Disks and public IPs bill even when deallocated. |
| Networking (W2, W12–W13, W29) | Standard public IP only when needed | Basic public IPs were retired on 30 Sep 2025. New VNets now default to private subnets, so VMs need an explicit outbound path ([default outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access)). VPN Gateway and ExpressRoute are only **priced** in W29 — never deployed in a lab. |
| Azure Bastion (W12) | **Developer SKU** (free, select regions) | Developer connects one VM in the **same VNet** (no peering), so the W12 lab puts it on the spoke. Basic+ bills hourly ([SKU comparison](https://learn.microsoft.com/en-us/azure/bastion/bastion-sku-comparison)). |
| App Service (W2, W11, W14, W22, W30) | **F1** for basics; **B1** for the W14, W22 and W30 apps; **S1 only for the W11 slot lab** (hours) | Deployment slots need Standard or higher ([slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)). Delete the plan, not just the app. |
| Container Registry (W11, W22–W23, W28) | **Basic** | **ACR Tasks runs are paused on Azure free credits** ([ACR Tasks](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview)) — no problem after your W9 upgrade, and `az acr build` needs no local Docker. |
| Container Apps (W11, W23–W24, W28) | Consumption, **min replicas 0** | Monthly free grant per subscription: 180,000 vCPU-s, 360,000 GiB-s, 2 million requests ([billing](https://learn.microsoft.com/en-us/azure/container-apps/billing)). |
| AKS (W23) | **Free tier**, `--node-count 1`, one 4-vCPU node, created with `--no-wait` | Default node count is **3** if you don't set it; system pools need 4+ vCPUs and don't support B-series ([system pools](https://learn.microsoft.com/en-us/azure/aks/use-system-pools)). Delete the same day ([start/stop](https://learn.microsoft.com/en-us/azure/aks/start-stop-cluster)). |
| Azure Functions (W21) | **Flex Consumption** | Consumption is legacy; Linux Consumption is retired ([hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)). |
| Cosmos DB (W17–W21, W25) | **Free tier** account created in W17 with vector search (`EnableNoSQLVectorSearch`) and kept until W21 Sat; a **serverless** account for the W25 Boss (created W25 Fri) | Free tier: first 1000 RU/s + 25 GB free, one free-tier account per subscription — keep total provisioned throughput at or below 1000 RU/s ([free tier](https://learn.microsoft.com/en-us/azure/cosmos-db/free-tier)). Serverless bills per request; delete it with the Boss RG. |
| PostgreSQL Flexible Server (W14, W18–W19, W28–W29) | **Burstable B1ms** (in the 12-month free hours) | Stop compute when idle, but a stopped server **auto-starts after 7 days** ([stop server](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/how-to-stop-server)); storage still bills. Built-in PgBouncer isn't supported on Burstable. |
| Azure Managed Redis (W19, W28) | Smallest **Balanced** SKU; RediSearch added at creation (Enterprise clustering, NoEviction) | Modules can only be added when you create the cache ([modules](https://learn.microsoft.com/en-us/azure/redis/redis-modules)). Billed hourly: W19 deletes it on Friday and re-creates it on Saturday; in W28 it lives for one day ([pricing](https://azure.microsoft.com/en-us/pricing/details/managed-redis/)). |
| Service Bus (W20–W21, W23, W25) | Basic for queue-only tasks; **Standard** for topics/sessions | Basic supports queues only. Delete the namespace after each lab. |
| Event Hubs (W20 Boss, W28) | **Standard**, 1 throughput unit | The Kafka endpoint isn't available on Basic ([Kafka quickstart](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-quickstart-kafka-enabled-event-hubs)); billed per throughput-unit hour — delete it the same day ([pricing](https://azure.microsoft.com/en-us/pricing/details/event-hubs/)). |
| Key Vault (W22–W23, W25, W28) | Standard, RBAC mode, soft-delete retention **7 days** for labs | Soft delete can't be disabled; deleted vault **names stay reserved** during retention — purge lab vaults without purge protection ([soft delete](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)). |
| App Configuration (W22) | **Free** tier | Max 3 Free stores per region per subscription, 10 MB each. |
| Log Analytics / App Insights (W13, W21, W24–W25, W28, W30) | One small workspace per lab | Billed by ingestion — set a [daily cap](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/daily-cap) in labs and only send the logs you query. |
| Azure Backup (W14) | One small VM, short retention, the vault in its own resource group | Soft delete is now enforced on Recovery Services vaults and **can't be disabled**: stop protection with delete-data and the backup stays soft-deleted **14 days at no extra cost**; delete the vault's resource group after that ([secure by default](https://learn.microsoft.com/en-us/azure/backup/secure-by-default)). |
| Site Recovery (W14) | One small VM, one test failover | Each protected instance is free for its first **31 days**; replica storage still bills ([pricing](https://azure.microsoft.com/en-us/pricing/details/site-recovery/)). Disable replication after the drill. |
| Azure SQL Database (W27, W30) | **Free tier** database (General Purpose serverless, `--use-free-limit true`, AutoPause) | Each month, per database: 100,000 vCore seconds + 32 GB data + 32 GB backup free; up to 10 free databases per subscription; AutoPause stops it when the limit runs out ([free tier](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-tier)). |
| Azure Migrate (W27) | One project: CSV-import assessment + business case | Azure Migrate itself is free; with no appliance and no replication there's nothing to bill. Server Migration and DMS are free for their first 180 days ([pricing](https://azure.microsoft.com/en-us/pricing/details/azure-migrate/)). |
| API Management (W29) | **Consumption** tier | Pay per call after a monthly free grant; never create Developer or Basic+ tiers for a lab — they bill hourly and take long to deploy ([pricing](https://azure.microsoft.com/en-us/pricing/details/api-management/)). |
| Defender for Cloud (W29) | Free foundational CSPM (secure score) | Don't switch on paid Defender plans in the lab subscription. |
| GitHub Codespaces (W3 fallback, W25, W26–W30) | 2-core codespace from `azure-labs` (Azurite fallback, pgvector + Redis, SQL Server 2022, SqlPackage, AppCAT) | Personal accounts get a free monthly quota of core-hours and storage; stop the codespace after every session and delete it when the week ends ([billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)). |

### Week-by-week cost notes for the expensive moments

| When | What runs | How to keep it cheap |
|---|---|---|
| W14 Fri → Sat | Source VM (B1s) + PostgreSQL B1ms, launched Friday | Both inside the 12-month free hours; stop the server Friday, start it at minute 0 Saturday, delete both RGs after the lab (the vault RG waits out soft delete). |
| W19 Fri / Sat | Azure Managed Redis (smallest Balanced) | Hourly — delete it Friday, re-create it Saturday at minute 0, delete it again after the lab. |
| W20 Sat (Boss) | Event Grid topic, Service Bus queue, Event Hubs Standard | One RG for the whole Boss; delete it in the last 10 minutes. |
| W23 Tue → Sat | Basic ACR + Container Apps environment (kept all week), AKS on Friday | Delete the AKS cluster on Friday and `rg-lab-w23` on Saturday. |
| W25 Fri → Sat (Boss) | Serverless Cosmos DB (created Friday, `--no-wait`), a Service Bus namespace, Key Vault, Application Insights; pgvector + Redis in a Codespace | Serverless and Key Vault cost almost nothing idle; delete the Boss RG and stop the Codespace when the timer ends. |
| W27 | Azure SQL free-tier database + an Azure Migrate project; SQL Server 2022 source in a Codespace | Free tier with AutoPause; delete `rg-lab-w27` after the Saturday lab (W30 rebuilds it from code). |
| W28 Sat (one-day stack) | TicketVerse stack: ACR Basic, Container Apps environment, Log Analytics + Application Insights, PostgreSQL B1ms, smallest Managed Redis, Event Hubs Standard, Key Vault, managed identities | Price one day in W28 Fri (`w28/cost.md`) — Redis and Event Hubs dominate. The Azure lab provisions it Saturday morning (before the Java deploy) and the AI block deletes it the same evening: `az stack group delete --name tv --resource-group rg-tv-dev --action-on-unmanage deleteAll`. |
| W29 | API Management Consumption; source VM (B1s) + PostgreSQL B1ms for the online migration | Free grants and free hours; delete each RG after its session. |
| W30 Sat (Final Boss) | B1 App Service + Azure SQL free tier + Application Insights, deployed by the stack and the OIDC workflow | Delete the stack in the last 10 minutes and finish with zero lab resource groups. |

## 5. Lab scripts (bash; run in Cloud Shell or locally)

```bash
#!/usr/bin/env bash
# scripts/new-lab.sh  ->  ./new-lab.sh 12
set -euo pipefail
WEEK=$(printf "%02d" "$1"); RG="rg-lab-w${WEEK}"
az group create -n "$RG" -l "${LOCATION:-centralindia}" \
  --tags owner="$(az account show --query user.name -o tsv)" week="w${WEEK}" expires="$(date +%F)"
echo "Created $RG - delete it today: ./nuke-lab.sh $1"
```

```bash
#!/usr/bin/env bash
# scripts/nuke-lab.sh  ->  ./nuke-lab.sh 12
set -euo pipefail
RG="rg-lab-w$(printf "%02d" "$1")"
az group delete -n "$RG" --yes --no-wait
echo "Deleting $RG. Remaining groups:"; az group list --query "[].{name:name, expires:tags.expires}" -o table
```

## 6. Teardown cheat sheet

| Situation | Command / action |
|---|---|
| Normal lab end | `az group delete -n rg-lab-wNN --yes --no-wait` |
| What's still running? | `az resource list --query "[].{name:name, type:type, rg:resourceGroup}" -o table` |
| Pause a VM (keeps disks) | `az vm deallocate -g <rg> -n <vm>` |
| Pause AKS / PostgreSQL | `az aks stop -g <rg> -n <aks>` · `az postgres flexible-server stop -g <rg> -n <server>` (auto-starts after 7 days!) |
| Key Vault cleanup | `az keyvault list-deleted -o table` → `az keyvault purge -n <vault>` (only if purge protection is off) |
| Backup vault won't delete | `az backup protection disable ... --delete-backup-data true --yes` (the backup stays soft-deleted 14 days, free; soft delete can't be disabled any more), try deleting the vault, else delete its own RG after 14 days |
| Site Recovery | Disable replication first; then delete the target-region resource group |
| AKS node resource group (`MC_...`) | Deleting the cluster's resource group removes it too — don't delete it by hand |
| Deployment stack (W28, W30) | `az stack group delete --name <stack> --resource-group <rg> --action-on-unmanage deleteAll` — removes every managed resource in one go (W28: the AI block runs it the same evening) |
| GitHub Codespace | Stop it after every session; delete it from github.com/codespaces when the week's work is committed |

**Never leave running:** AKS node pools, Azure Managed Redis, Event Hubs Standard namespaces, the W28 TicketVerse stack,
PostgreSQL General Purpose, Bastion Basic/Standard, VPN gateways, App Service B1/S1+ plans, API Management tiers other
than Consumption, NAT gateways and idle public IPs, Service Bus Standard/Premium namespaces, Cosmos DB provisioned
throughput outside the free tier, running Codespaces, and VMs that are "Stopped" but not deallocated.

## 7. Region and quota tips

- Default to **Central India** (`centralindia`, 3 availability zones); its pair is **South India** — used for the W14 Site Recovery drill.
- Your *Allowed locations* policy keeps labs in Central/South India; before AI W25, add a policy exemption for the AI resource group if a Foundry model is only offered in another region (command prepared in W7 Fri).
- Not every SKU exists in every region: check with `az vm list-skus -l centralindia -o table` or the service's region list before a lab.
- New subscriptions can have small vCPU quotas: `az vm list-usage -l centralindia -o table`. Ask for an increase only if a lab truly needs it (AKS is the usual one).

## 8. Weekly cost-check ritual (Sunday, 10 minutes)

- [ ] **Cost analysis** → group by resource group, last 7 days ([quickstart](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)). Anything unexpected? Find and delete it now.
- [ ] `az group list --query "[].{name:name, expires:tags.expires}" -o table` → delete every lab group whose `expires` is in the past (and `az stack group list -g <rg>` for any leftover stack).
- [ ] Budget burn % and forecast vs your monthly amount; free-credit days left (Path B/C, until the W9 upgrade).
- [ ] Soft-deleted Key Vaults and backup items you no longer need.
- [ ] Codespaces: no codespace left running; core-hours used this month vs your free quota.
- [ ] Advisor → Cost tab: act on anything relevant to your lab resources.
- [ ] Append one line to `azure-labs/cost-log.md`: date, month-to-date cost, leftovers found (target: none).

## 9. Security hygiene that also saves money

- Never commit keys, connection strings or `local.settings.json`; add them to `.gitignore`. Prefer **managed identity + DefaultAzureCredential** everywhere (W16 onward) and **GitHub OIDC federated credentials** for pipelines (W22 onward) — no client secrets to leak.
- If a secret leaks: rotate it immediately, then check Cost analysis — leaked credentials are a classic cause of crypto-mining bills.
- Keep employer and personal subscriptions separate; follow your employer's rules for Visual Studio credits.

## 10. Sources

[Azure account options & free account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account) ·
[Free services](https://azure.microsoft.com/en-us/pricing/free-services) ·
[Avoid charges with your free account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/avoid-charges-free-account) ·
[Upgrade your account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/upgrade-azure-subscription) ·
[Spending limit](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit) ·
[Visual Studio subscriber credits](https://azure.microsoft.com/en-us/pricing/member-offers/credit-for-visual-studio-subscribers/) ·
[Budgets](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) ·
[Cost Management overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management) ·
[Delete resource groups](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group) ·
[Deployment stacks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks) ·
[Azure SQL Database free tier](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-tier) ·
[Azure Migrate pricing](https://azure.microsoft.com/en-us/pricing/details/azure-migrate/) ·
[Backup secure by default](https://learn.microsoft.com/en-us/azure/backup/secure-by-default) ·
[Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) ·
[Region pairs](https://learn.microsoft.com/en-us/azure/reliability/regions-paired)
