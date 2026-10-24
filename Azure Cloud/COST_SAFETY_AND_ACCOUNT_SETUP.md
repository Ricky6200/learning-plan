# 💸 Cost Safety & Account Setup — learn Azure without surprise bills

> Facts verified on official Microsoft pages on **24 Oct 2026**. Prices change and vary by region — always confirm in the
> [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) before creating anything you haven't priced.

## 1. The five rules (memorise these)

1. **Guardrails before resources.** Budget + alerts + MFA exist *before* your first VM. Budgets only **alert** — Microsoft's docs are explicit that resources aren't affected and consumption isn't stopped.
2. **One resource group per lab** (`rg-lab-wNN`), tagged `owner`, `week`, `expires`. Delete the whole group the **same day**.
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
| **B — Azure free account (default)** | Everyone else | **$200 credit for 30 days** + **12 months** of free amounts of 20+ popular services (new customers) + **65+ always-free** services | **W6 Tue, 1 Dec 2026** (AZ-104 labs start) | "Script-first" mode: write and dry-run the scripts in W1–W5 (Azurite for the W3 storage lab); run them live from W6 |
| **C — early variant of B** | You'd rather have hands-on from week 2 | Same free account | **W2 Sat, 7 Nov 2026** | Live from W2 — but the $200 credit expires around 7 Dec (start of W7), so most AZ-104 labs run on pay-as-you-go (still small with same-day teardown) |

Why B activates in W6: AZ-900 is conceptual, and the 30-day credit is worth more when hands-on AZ-104 labs start.
**Azure for Students** ($100, no card) needs an academic email, so it usually doesn't apply to you.

### India-specific notes for the free account (Path B/C)

- Sign up through **"Try Azure for free"**, not directly for pay-as-you-go: the Azure free-services page states the
  12-month free services are *not currently available to customers who sign up directly for pay as you go in China and India*.
- During sign-up a **temporary $1 authorization** may appear on your card; it is reversed after verification.
- With the free account your card **isn't charged**; when the credit is used up or the 30 days end, the subscription is
  **disabled** until you upgrade. To keep the **12 months of free services**, **move to pay-as-you-go within 30 days**.
- After upgrading there is **no spending cap** — your budgets and alerts are now your only early warning. Set them first.

## 3. Activation-day checklist (W1 for Path A · W6 Tue for Path B · W2 Sat for Path C)

- [ ] **Secure the account:** MFA on (Entra [security defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults) require MFA registration); never share the login.
- [ ] **Budget at subscription scope:** small monthly amount (e.g., INR 500); alerts at **50% / 80% / 100% actual** and **100% forecast** to your email ([tutorial](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)).
- [ ] **Action group** (email + Azure mobile app push) attached to the budget.
- [ ] **Cost anomaly alert** on the subscription ([cost alerts](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending)).
- [ ] **CLI defaults:** `az config set defaults.location=centralindia` (Central India has 3 availability zones; its region pair is South India).
- [ ] **Azure Policy:** *Allowed locations* = your lab regions (e.g., Central India, South India). If a Learn exercise needs another region, add it temporarily. Use **Audit** (not Deny) for "require tag" policies so exercise scripts don't break.
- [ ] **Lab scripts** (`scripts/new-lab.sh`, `scripts/nuke-lab.sh`, Section 5) committed and tested once.
- [ ] Note in `azure-labs/cost-log.md`: activation date, credit end date (+30 days), upgrade-by date.

## 4. Cheapest sensible SKUs for every lab in this plan

| Service (week) | Use in labs | Cost traps and facts |
|---|---|---|
| Virtual machines (W2, W10–W14) | B-series (e.g., `Standard_B1s`); auto-shutdown on | **Stopped (allocated) is still billed** — use `az vm deallocate` ([states & billing](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing)). Disks and public IPs bill even when deallocated. |
| Networking (W2, W12–W13) | Standard public IP only when needed | Basic public IPs were retired on 30 Sep 2025. New VNets now default to private subnets, so VMs need an explicit outbound path ([default outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access)). |
| Azure Bastion (W12) | **Developer SKU** (free, select regions) | Developer connects one VM in the **same VNet** (no peering). Basic+ bills hourly — delete right after the lab ([SKU comparison](https://learn.microsoft.com/en-us/azure/bastion/bastion-sku-comparison)). |
| App Service (W2, W11, W23) | **F1** for basics; **S1 only for the slot lab** (hours) | Deployment slots need Standard or higher ([slots](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)). Delete the plan, not just the app. |
| Container Apps (W11, W22–W24) | Consumption, **min replicas 0** | Monthly free grant per subscription: 180,000 vCPU-s, 360,000 GiB-s, 2 million requests ([billing](https://learn.microsoft.com/en-us/azure/container-apps/billing)). |
| Azure Functions (W21) | **Flex Consumption** | Consumption is legacy; Linux Consumption is retired ([hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)). |
| Cosmos DB (W17–W18, W25) | **Free tier** (opt in at creation) or serverless | Free tier: first 1000 RU/s + 25 GB free, one free-tier account per subscription ([free tier](https://learn.microsoft.com/en-us/azure/cosmos-db/free-tier)). |
| PostgreSQL Flexible Server (W14, W18–W19, W23) | **Burstable B1ms** | Stop compute when idle, but a stopped server **auto-starts after 7 days** ([stop server](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/how-to-stop-server)); storage still bills. Built-in PgBouncer isn't supported on Burstable. |
| Azure Managed Redis (W19, W23) | Smallest **Balanced** SKU; add RediSearch at creation | Modules can only be added when you create the cache ([modules](https://learn.microsoft.com/en-us/azure/redis/redis-modules)). Create, use, delete the same day ([pricing](https://azure.microsoft.com/en-us/pricing/details/managed-redis/)). |
| Service Bus (W20–W21) | Basic for queue-only labs; **Standard** for topics/sessions | Basic supports queues only. Delete the namespace after the lab. |
| Key Vault (W22–W23) | Standard, RBAC mode, soft-delete retention **7 days** for labs | Soft delete can't be disabled; deleted vault **names stay reserved** during retention — purge lab vaults without purge protection ([soft delete](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview)). |
| App Configuration (W22) | **Free** tier | Max 3 Free stores per region per subscription, 10 MB each. |
| Container Registry (W11, W23) | **Basic** | **ACR Tasks runs are paused on Azure free credits** ([ACR Tasks](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview)) — build locally and `docker push`, or run Tasks after upgrading. |
| AKS (W23) | **Free tier**, `--node-count 1`, one 4-vCPU node | Default node count is **3** if you don't set it; system pools need 4+ vCPUs and don't support B-series ([system pools](https://learn.microsoft.com/en-us/azure/aks/use-system-pools)). `az aks stop` or delete the same day ([start/stop](https://learn.microsoft.com/en-us/azure/aks/start-stop-cluster)). |
| Log Analytics / App Insights (W13, W24) | One small workspace per lab | Billed by ingestion — set a [daily cap](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/daily-cap) in labs and only send the logs you query. |
| Azure Backup (W14) | One small VM, short retention | Secure-by-default soft delete keeps deleted backups **14 days at no extra cost**; stop protection and delete data **before** deleting the vault ([secure by default](https://learn.microsoft.com/en-us/azure/backup/secure-by-default)). |
| Site Recovery (W14) | One small VM, one test failover | Each protected instance is free for its first **31 days**; replica storage still bills ([pricing](https://azure.microsoft.com/en-us/pricing/details/site-recovery/)). Disable replication after the drill. |

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
| Backup vault won't delete | `az backup protection disable ... --delete-backup-data true --yes`, then delete the vault, then the RG |
| Site Recovery | Disable replication first; then delete the target-region resource group |
| AKS node resource group (`MC_...`) | Deleting the cluster's resource group removes it too — don't delete it by hand |

**Never leave running:** AKS node pools, Azure Managed Redis, PostgreSQL General Purpose, Bastion Basic/Standard,
VPN gateways, App Service S1+ plans, NAT gateways and idle public IPs, Service Bus Standard/Premium namespaces,
Cosmos DB provisioned throughput outside the free tier, and VMs that are "Stopped" but not deallocated.

## 7. Region and quota tips

- Default to **Central India** (`centralindia`, 3 availability zones); its pair is **South India** — used for the W14 Site Recovery drill.
- Not every SKU exists in every region: check with `az vm list-skus -l centralindia -o table` or the service's region list before a lab.
- New subscriptions can have small vCPU quotas: `az vm list-usage -l centralindia -o table`. Ask for an increase only if a lab truly needs it (AKS is the usual one).

## 8. Weekly cost-check ritual (Sunday, 10 minutes)

- [ ] **Cost analysis** → group by resource group, last 7 days ([quickstart](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis)). Anything unexpected? Find and delete it now.
- [ ] `az group list --query "[].{name:name, expires:tags.expires}" -o table` → delete every lab group whose `expires` is in the past.
- [ ] Budget burn % and forecast vs your monthly amount; free-credit days left (Path B/C).
- [ ] Soft-deleted Key Vaults and backup items you no longer need.
- [ ] Advisor → Cost tab: act on anything relevant to your lab resources.
- [ ] Append one line to `azure-labs/cost-log.md`: date, month-to-date cost, leftovers found (target: none).

## 9. Security hygiene that also saves money

- Never commit keys, connection strings or `local.settings.json`; add them to `.gitignore`. Prefer **managed identity + DefaultAzureCredential** everywhere (W16 onward).
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
[Region pairs](https://learn.microsoft.com/en-us/azure/reliability/regions-paired)
