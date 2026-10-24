# ☁️ Azure Cloud · Week 13 — Networking II: DNS, load balancing, Azure Monitor

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** Name resolution and load balancing finish AZ-104 networking, and monitoring (10-15%) is how you prove a system is healthy. KQL and alerting come back in AI-200 and in every on-call rotation you will join.

## 🗓️ Sessions

### Tuesday 19 Jan · 45 min — Azure DNS public/private zones and Azure Load Balancer
- 📚 **Learn:** Public zones, record sets (A, CNAME, TXT, alias), delegation; private DNS zones, VNet links and auto-registration; Load Balancer (public vs internal, Standard SKU, frontend, backend pool, health probe, rules, outbound rules). Use [Host your domain on Azure DNS](https://learn.microsoft.com/en-us/training/modules/host-domain-azure-dns/), [Private DNS overview](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview) and [Introduction to Azure Load Balancer](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-load-balancer/).
- 🛠️ **Do:** Create private zone `ticketverse.internal`, link it to a VNet with auto-registration and add an A record `api`. Use `az vm run-command invoke` on a small VM to `nslookup api.ticketverse.internal` and the VM's own auto-registered name. Sketch an internal load balancer for 2 API VMs (frontend IP, pool, `/health` probe, rule 80 -> 8080). Done when: run-command output and the LB sketch are committed; RG deleted.

### Wednesday 20 Jan · 45 min — Azure Monitor: metrics, diagnostic settings, Log Analytics, KQL
- 📚 **Learn:** Metrics vs logs, the Activity log, resource logs via diagnostic settings, Log Analytics workspaces, KQL basics (where, project, summarize, bin, render). Use [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview), [Diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/diagnostic-settings) and the [Log Analytics tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial).
- 🛠️ **Do:** Create a Log Analytics workspace; send a storage account's blob logs and the subscription Activity log to it. Generate some traffic, then write 3 KQL queries: operations per hour (`summarize count() by bin(TimeGenerated, 1h)`), failed requests by status code, and who deleted what (AzureActivity). Done when: 3 queries + result screenshots are in `w13/kql.md`.

### Friday 22 Jan · 45 min — Alerts, action groups, processing rules, Insights, Network Watcher
- 📚 **Learn:** Alert types (metric, log search, activity log), action groups, alert processing rules (suppress during maintenance), VM/storage/network Insights, Network Watcher (IP flow verify, next hop, connection troubleshoot, Connection monitor). Use [Alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview), [Alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules) and [Connection monitor overview](https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview).
- 🛠️ **Do:** Create an email action group and a metric alert (VM CPU above 80% for 5 minutes); trigger it with a busy loop via `az vm run-command invoke`. Add an alert processing rule that suppresses notifications for the next 30 minutes and confirm the second firing sends no email. Run Network Watcher next hop and IP flow verify for the VM. Done when: alert email, suppression evidence and both outputs are in `w13/`.

### Saturday 23 Jan · 60 min — LAB: Public load balancer break/fix + monitoring
- 📚 **Learn:** Use [Create a public load balancer with CLI](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-cli), [AZ-104 Lab 06 - network traffic management](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_06-Implement_Network_Traffic_Management.html) and [Troubleshoot Azure Load Balancer](https://learn.microsoft.com/en-us/troubleshoot/azure/load-balancer/troubleshoot-common-problems/load-balancer-troubleshoot) as references.
- 🛠️ **Do:** Script a Standard public load balancer with 2 small VMs running nginx (cloud-init prints the hostname); curl the frontend and watch responses alternate. Break it: add an NSG rule that blocks the probe (deny the AzureLoadBalancer service tag) and watch the health probe status metric drop; fix it. Add a metric alert on probe health. Finish with `nuke-lab.sh 13`. Done when: alternating responses and broken/fixed metric screenshots are committed; RG deleted.

## 📦 Deliverable (by Saturday night)
`w13/` private DNS evidence, load balancer sketch and break/fix evidence, 3 KQL queries, alert + processing-rule evidence and Network Watcher outputs.

## ✅ Self-check (Sunday test preview)
- CNAME vs alias record: why can't you put a CNAME at the zone apex?
- Public vs internal load balancer: where do health probes come from, and what happens when a probe fails?
- Metrics vs logs in Azure Monitor: which is near real-time, and which needs a diagnostic setting?
- Write KQL that counts failed requests per 5 minutes and renders a timechart.
- Action group vs alert processing rule: what does each control?
- Which Network Watcher tool tells you which NSG rule blocked a packet?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Deploy and configure Azure Monitor](https://learn.microsoft.com/en-us/credentials/applied-skills/deploy-and-configure-azure-monitor/) or complete [AZ-104 Lab 11 - monitoring](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_11-Implement_Monitoring.html).
