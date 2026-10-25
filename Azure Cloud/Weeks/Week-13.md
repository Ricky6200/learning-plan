# ☁️ Azure Cloud · Week 13 — Networking II: DNS, load balancing, Azure Monitor

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** Name resolution and load balancing finish AZ-104 networking, and monitoring (10-15%) is how you prove a system is healthy. KQL and alerting come back in AI-200 and in every on-call rotation you will join.

## 🗓️ Sessions

### Tuesday 19 Jan · 45 min — Azure DNS: public and private zones
- 📚 **Learn:** Public zones, record sets (A, CNAME, TXT, alias), delegation and the zone's Azure name servers; private DNS zones, VNet links and auto-registration. Read [Host your domain on Azure DNS](https://learn.microsoft.com/en-us/training/modules/host-domain-azure-dns/). Optional: [Private DNS overview](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview).
- 🛠️ **Do:** Create public zone `<yourname>-lab.in` (you needn't own the domain), add an A record `www` and query it straight from one of the zone's Azure name servers (`nslookup www.<zone> <ns1-xx.azure-dns.com>`). Then create private zone `ticketverse.internal`, link it to a VNet with auto-registration, add an A record `api`, and use `az vm run-command invoke` on a small VM to resolve `api.ticketverse.internal` and the VM's own auto-registered name. Done when: both lookups are committed and the RG is deleted.

### Wednesday 20 Jan · 45 min — Azure Monitor: metrics, diagnostic settings, Log Analytics, KQL
- 📚 **Learn:** Metrics vs logs, the Activity log, resource logs via diagnostic settings, Log Analytics workspaces, KQL basics (where, project, summarize, bin, render). Read the [Log Analytics tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial). Optional: [Diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/diagnostic-settings).
- 🛠️ **Do:** Create a Log Analytics workspace; send a storage account's blob logs and the subscription Activity log to it. Generate some traffic, then write 3 KQL queries: operations per hour (`summarize count() by bin(TimeGenerated, 1h)`), failed requests by status code, and who deleted what (AzureActivity). Done when: 3 queries + result screenshots are in `w13/kql.md`.

### Friday 22 Jan · 45 min — Alerts, action groups, processing rules, Insights, Network Watcher
- 📚 **Learn:** Alert types (metric, log search, activity log), action groups, alert processing rules (suppress during maintenance), VM/storage/network Insights, Network Watcher (IP flow verify, next hop, connection troubleshoot, Connection monitor). Read the [Alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview). Optional: [Alert processing rules](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-processing-rules).
- 🛠️ **Do:** Create an email action group and a metric alert (VM CPU above 80% for 5 minutes); trigger it with a busy loop via `az vm run-command invoke`. Add an alert processing rule that suppresses notifications for the next 30 minutes and confirm the second firing sends no email. Run Network Watcher next hop and IP flow verify for the VM. Done when: alert email, suppression evidence and both outputs are in `w13/`.

### Saturday 23 Jan · 60 min — LAB: Load balancer design and break/fix
- 📚 **Learn:** Standard Load Balancer parts (frontend IP, backend pool, health probe, load-balancing rules, outbound rules), public vs internal, and the AzureLoadBalancer service tag that health probes come from. Read [Create a public load balancer with CLI](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-cli). Optional: [Troubleshoot Azure Load Balancer](https://learn.microsoft.com/en-us/troubleshoot/azure/load-balancer/troubleshoot-common-problems/load-balancer-troubleshoot).
- 🛠️ **Do:** First sketch an internal load balancer for 2 TicketVerse API VMs (frontend IP, pool, `/health` probe, rule 80 -> 8080) in `w13/lb.md`. Then script a Standard public load balancer with 2 small VMs running nginx (cloud-init prints the hostname); curl the frontend and watch responses alternate. Break it with an NSG rule denying the AzureLoadBalancer service tag, watch the health-probe metric drop, fix it. Read the probe config in Az PowerShell in Cloud Shell (`Get-AzLoadBalancer | Get-AzLoadBalancerProbeConfig`). `nuke-lab.sh 13`. Done when: sketch, alternating responses and broken/fixed metric evidence are committed.

## 📦 Deliverable (by Saturday night)
`w13/` public + private DNS evidence, internal load balancer sketch, public load balancer break/fix evidence (+ PowerShell probe config), 3 KQL queries, alert + processing-rule evidence and Network Watcher outputs.

## ✅ Self-check (Sunday test preview)
- CNAME vs alias record: why can't you put a CNAME at the zone apex?
- How can you test records in an Azure public DNS zone before delegating the domain to it?
- Public vs internal load balancer: where do health probes come from, and what happens when a probe fails?
- Metrics vs logs in Azure Monitor: which is near real-time, and which needs a diagnostic setting?
- Write KQL that counts failed requests per 5 minutes and renders a timechart.
- Action group vs alert processing rule: what does each control?
- Which Network Watcher tool tells you which NSG rule blocked a packet?

## 🚀 Stretch (optional)
Add a metric alert on the load balancer's health-probe status, then do [AZ-104 Lab 06 - network traffic management](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_06-Implement_Network_Traffic_Management.html) or [AZ-104 Lab 11 - monitoring](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_11-Implement_Monitoring.html), or the hosted Applied Skills lab [Deploy and configure Azure Monitor](https://learn.microsoft.com/en-us/credentials/applied-skills/deploy-and-configure-azure-monitor/).
