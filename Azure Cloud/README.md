# ☁️ Azure Cloud Track — build, run and migrate on Azure (AZ-900 → AZ-104 → AI-200)

> **Mission:** in 30 weeks (Mon 26 Oct 2026 → Sun 23 May 2027), become the Java backend engineer who can build, secure,
> operate **and migrate** workloads on Azure — and prove it with three Microsoft certifications and a portfolio of real labs.

> [!IMPORTANT]
> ### Why not AZ-204?
> You were told "AZ-900 → AZ-104 → AZ-204". **AZ-204 was retired on 31 July 2026.** Microsoft's replacement is
> **AI-200 "Developing AI Cloud Solutions on Azure"**, which earns **Microsoft Certified: Azure AI Cloud Developer Associate**.
>
> **Your final path:** **AZ-900** (exam W5, Fri 27 Nov 2026) → **AZ-104** (exam W16, Fri 12 Feb 2027) → **AI-200** (exam W26,
> Fri 23 Apr 2027). Season 6 (W27–W30) then turns the badges into migration skill: Azure SQL, Azure Migrate, TicketVerse
> infrastructure as code, hybrid networking and a timed migrate-and-modernise capstone.
>
> **Vouchers and bookings (employer-paid):** request three vouchers from your L&D team in **W1 Fri (30 Oct)** · book AZ-900
> in **W2 Sat (7 Nov)** · AZ-104 in **W10 Tue (29 Dec)** · AI-200 in **W20 Tue (9 Mar)** · AZ-104 go/no-go gate in **W15 Fri (5 Feb)**.
>
> AI-200 goes last because it expects Python (AI track W1–W3), embeddings, vector databases and RAG (AI track W9–W12) and
> containers (Java track W11 and W22–W24). Official sources and details: [CERTIFICATION_GUIDE.md](CERTIFICATION_GUIDE.md).

## 1. By Week 30 you will…

- [ ] Hold **3 certifications** — AZ-900 (W5), AZ-104 (W16), AI-200 (W26) — or have a dated retake plan for any you miss.
- [ ] Own a public **`azure-labs`** repo with 30 Saturday labs/boss battles: CLI + PowerShell scripts, Bicep, Python, Java, diagrams and evidence.
- [ ] Run apps on **App Service** (slot swap, HTTPS-only, a container pulled with managed identity), **Container Apps** (revisions, KEDA) and **AKS** (manifests) — keyless, via managed identity.
- [ ] Design a **hub-spoke network** with NSGs, Bastion, service and **private endpoints**, plus a **hybrid** design (VPN/ExpressRoute, DNS Private Resolver, Azure Firewall).
- [ ] Migrate three ways, each with a cutover and rollback runbook: **VM → App Service + PostgreSQL** (W14), **SQL Server with stored procedures → Azure SQL** with passwordless JDBC (W27) and **PostgreSQL online** (W29).
- [ ] Assess an estate with **Azure Migrate** (CSV import + business case) and a Java codebase with **AppCAT** (W27).
- [ ] Provision TicketVerse's Azure infrastructure **as code** (Bicep, Azure Verified Modules, a deployment stack) inside a **landing-zone** design, for the Java track's W28 deploy.
- [ ] Build an **AI data layer**: Cosmos DB vector search, PostgreSQL + pgvector (HNSW/IVFFlat tuning) and an Azure Managed Redis cache.
- [ ] Wire **event-driven back ends** with Service Bus, Event Grid, Event Hubs (Kafka endpoint) and Functions, secured with Key Vault, App Configuration and GitHub OIDC federated credentials.
- [ ] Trace a request end to end with **OpenTelemetry + Application Insights** and prove where the time goes with **KQL**.
- [ ] Beat the **Final Boss** (W30): migrate and modernise `legacy-orders` end to end in 60 minutes, and answer 6 Azure interview scenarios in 2 minutes each.
- [ ] Stay inside your budget with **zero orphaned resources** (weekly cost log).

## 2. Your weekly slots

| Day | Minutes | Session type |
|---|---|---|
| Tue | 45 | Learn + small hands-on |
| Wed | 45 | Learn + small hands-on |
| Fri | 45 | Learn + prepare Saturday |
| **Sat** | **60** | **LAB** — or **BOSS BATTLE** in W4, W9, W15, W20, W25, W30 |
| Sun | 20 (inside the 150-min weekly test) | 12 exam-style Azure questions |

That's 3 h 15 min of Azure per week. Exam days (Fridays of W5, W16, W26) borrow extra time from another block once — that's expected.

**Where you work:** W1–W5 on the company laptop (Azure CLI, `az bicep build`, and the Bicep, Azure Resources, Azure Functions and
Azurite VS Code extensions; personal Microsoft sign-in is blocked there). W5 Sat sets up your **personal laptop**; from W6 (personal free account activated
**Tue 1 Dec 2026**) every live lab runs there or in a GitHub Codespace, and cross-track code arrives through GitHub.

## 3. How to run one session — Predict → Type → Verify → Explain

Built for "I understand code but freeze when I have to write it": you always **write it yourself**, in small steps.

| Minute (45-min session) | Step | What you actually do |
|---|---|---|
| 0–3 | **Aim** | Read the session's **Done when** — that's the finish line. |
| 3–18 | **Learn actively** | Work through the session's **one main resource** (≤ 15 min; the "Optional" link only if time remains); write 3 bullets + 1 tiny diagram in `wNN/notes.md` (no pasted paragraphs). |
| 18–40 | **Predict → Type → Verify** | ≤ 25 min hands-on: before each command/code block, write what you expect; type it yourself (no copy-paste); compare; fix; repeat. |
| 40–45 | **Explain + log** | Explain it aloud in 60 seconds, add 2 flashcards to `flashcards.md`, commit with a meaningful message. |

**Saturday LAB (60 min, ≤ 45 min hands-on):** 0–5 plan the resources → 5–45 build in `rg-lab-wNN` (`scripts/new-lab.sh`) → 45–55 save evidence
(CLI output, screenshots) to `wNN/` → 55–60 `scripts/nuke-lab.sh` and confirm the group is gone. Slow resources (AKS, a Flexible
Server, a source VM, a vector-enabled Cosmos DB account) are launched on Friday with `--no-wait` when a lab needs them.
**BOSS BATTLE:** visible timer, notes only where the task allows, score yourself honestly, log every miss.

Writing-confidence tips: start from a 5-line script and grow it; lean on `--help` and `az find`; use GitHub Copilot to
*explain* errors, not to write the whole lab; keep reusable snippets in `azure-labs/snippets.md`.

## 4. Phase map

| Season | Weeks | Focus | Milestone |
|---|---|---|---|
| S1 Foundation Forge | W1–W4 | Cloud concepts, Azure architecture, storage + identity, governance; Azure CLI, cost guardrails, exam vouchers | **Boss W4:** timed AZ-900 practice run (85%+) + speed round; AZ-900 already booked in W2 |
| S2 Concurrency Crucible | W5–W9 | **AZ-900 exam (W5 Fri)**; personal-laptop setup (W5 Sat); free account (W6 Tue); AZ-104 identity, RBAC, Policy, storage; pay-as-you-go upgrade (W9 Tue) | **Boss W9:** timed identity + storage admin challenge (CLI + PowerShell) |
| S3 Spring Citadel | W10–W15 | ARM/Bicep, VMs, App Service, containers, networking, monitoring, backup/DR, migration basics; AZ-104 prep | **Boss W15:** timed AZ-104 gauntlet, after the W15 Fri go/no-go gate |
| S4 Distributed Kingdom | W16–W20 | **AZ-104 exam (W16 Fri)**; AI-200: keyless SDK, Cosmos DB, PostgreSQL + pgvector, Managed Redis; Service Bus, Event Grid, Event Hubs | **Boss W20:** timed messaging lab incl. the Event Hubs Kafka endpoint |
| S5 Cloud Ascension | W21–W25 | Functions, Key Vault, App Configuration, workload identity, ACR Tasks / Container Apps / AKS, OpenTelemetry + KQL, AI-200 prep | **Boss W25:** timed AI-200 build gauntlet |
| S6 Final Boss: The Offer | W26–W30 | **AI-200 exam (W26 Fri)**; Migration I, TicketVerse IaC + landing zones, Migration II + DevOps & APIs, capstone | **Final Boss W30:** migrate and modernise `legacy-orders` end to end (timed runbook) |

### Week by week

| Week | Dates | Theme | Saturday | Key dates |
|---|---|---|---|---|
| W1 | 26 Oct–1 Nov | Cloud concepts and a safe Azure setup | LAB: CLI, Cloud Shell, guardrail kit | Fri: request exam vouchers |
| W2 | 2–8 Nov | Architecture, compute and networking services | LAB: VM + App Service via CLI | Sat: book AZ-900 |
| W3 | 9–15 Nov | Storage, identity and security fundamentals | LAB: storage tiers, SAS, RBAC (Path B: Azurite via the VS Code extension, or in a Codespace) | |
| W4 | 16–22 Nov | Governance, cost, monitoring tools | ⚔️ BOSS: AZ-900 practice run + speed round | |
| W5 | 23–29 Nov | AZ-900 exam week + AZ-104 kickoff | LAB: personal-laptop workstation + AZ-104 skills map | 🎓 Fri 27 Nov: AZ-900 |
| W6 | 30 Nov–6 Dec | Entra ID users, groups, licenses, SSPR | LAB: AZ-104 Lab 01 | Tue 1 Dec: free account + P2 trial via `labadmin` |
| W7 | 7–13 Dec | RBAC, subscriptions, governance at scale | LAB: AZ-104 Lab 02a (custom roles) | |
| W8 | 14–20 Dec | Storage I: accounts, replication, security, data tools | LAB: AZ-104 Lab 07 (blob + firewall) | |
| W9 | 21–27 Dec | Storage II: Files, blob protection | ⚔️ BOSS: identity + storage admin challenge | Tue 22 Dec: pay-as-you-go upgrade · Fri 25 Dec holiday |
| W10 | 28 Dec–3 Jan | ARM templates, Bicep, VMs I | LAB: Linux VM with Bicep (data disk, encryption at host, resize) | Tue 29 Dec: book AZ-104 · Fri 1 Jan holiday |
| W11 | 4–10 Jan | VMs II, containers, App Service | LAB: Java app on App Service (slot swap, HTTPS-only, TLS) | |
| W12 | 11–17 Jan | Virtual networking I: VNets, routing, secure access | LAB: hub-spoke, Bastion, private + service endpoints | |
| W13 | 18–24 Jan | Networking II: DNS, load balancing, Azure Monitor | LAB: load balancer design and break/fix | |
| W14 | 25–31 Jan | Backup, disaster recovery and migration basics | LAB: VM-hosted app → App Service + runbook | Tue 26 Jan holiday |
| W15 | 1–7 Feb | AZ-104 exam prep | ⚔️ BOSS: timed AZ-104 gauntlet | Fri 5 Feb: go/no-go gate |
| W16 | 8–14 Feb | AZ-104 exam + AI-200 kickoff | LAB: AI-200 map + keyless Python SDK | 🎓 Fri 12 Feb: AZ-104 |
| W17 | 15–21 Feb | Cosmos DB for NoSQL I | LAB: Cosmos DB RAG document store | |
| W18 | 22–28 Feb | Cosmos DB vectors, change feed, PostgreSQL basics | LAB: PostgreSQL agent-tool backend + pooling | |
| W19 | 1–7 Mar | pgvector, Managed Redis and a RAG data layer | LAB: RAG data layer (pgvector + Redis) | |
| W20 | 8–14 Mar | Service Bus, Event Grid, Event Hubs | ⚔️ BOSS: timed messaging lab (Event Hubs Kafka) | Tue 9 Mar: book AI-200 |
| W21 | 15–21 Mar | Azure Functions | LAB: MCP server on Functions + Application Insights | |
| W22 | 22–28 Mar | Key Vault, App Configuration, workload identity | LAB: container on App Service via managed identity + Key Vault | |
| W23 | 29 Mar–4 Apr | ACR Tasks, Container Apps, AKS | LAB: ship an AI-track container (DocuMind) to Container Apps | |
| W24 | 5–11 Apr | OpenTelemetry, Application Insights, KQL | LAB: troubleshoot Container Apps from logs and KQL | |
| W25 | 12–18 Apr | AI-200 exam prep | ⚔️ BOSS: timed AI-200 build gauntlet | |
| W26 | 19–25 Apr | AI-200 exam week + Season 6 kickoff | LAB: exam retro + migration toolkit (Codespace) | 🎓 Fri 23 Apr: AI-200 |
| W27 | 26 Apr–2 May | Migration I: SQL Server and Java apps | LAB: `legacy-orders` → Azure SQL with passwordless JDBC | |
| W28 | 3–9 May | TicketVerse infrastructure as code + landing zones | LAB: provision TicketVerse with a deployment stack (one-day stack) | ☁️ TicketVerse live on Azure (with Java W28) |
| W29 | 10–16 May | Migration II: hybrid networks, WAF, APIs, PostgreSQL | LAB: PostgreSQL online migration with cutover/rollback | |
| W30 | 17–23 May | Capstone: migrate and modernise | 👑 FINAL BOSS: `legacy-orders` end to end (timed) | Plan ends Sun 23 May 2027 |

**Cross-track hooks:** W11 deploys the App Service quickstart's Spring Boot sample (Spring Boot arrives in Java W13) ·
W14 migrates TicketVerse v0 (Java W13) from a VM to App Service · W17–W19 reuse your AI-track embeddings (AI W9) and
DocuMind data (AI W10–W13) · W20's Event Hubs Kafka endpoint is where Java W20–W21 Kafka code can run · W21 extends the
MCP work from AI W16 on Functions · W22's GitHub federated credential is the pattern Java W26 CI/CD uses · W23 ships
DocuMind (AI W13) to Container Apps and applies Java W23 manifests on AKS · W28 provisions the stack Java W28 deploys
TicketVerse onto — that Saturday runs DSA → Azure lab → Java deploy → AI live check + teardown → SD · W30 reuses W27's
`legacy-orders` app and W28's Bicep modules.

## 5. Navigation

| File | What's inside |
|---|---|
| [ROADMAP.md](ROADMAP.md) | All 30 weeks on one page |
| [Weeks/](Weeks/) | `Week-01.md` … `Week-30.md`: every session's topic, learn, do, Done when, self-check and stretch |
| [RESOURCES.md](RESOURCES.md) | Study guides, learning paths, docs (incl. Season 6 migration and IaC), YouTube (English + Hindi), practice, tools with versions |
| [CERTIFICATION_GUIDE.md](CERTIFICATION_GUIDE.md) | Why AI-200 replaced AZ-204, skills-measured → week maps, vouchers and booking dates, go/no-go gate, Learn-in-exam rules, retakes, renewal, what's next |
| [COST_SAFETY_AND_ACCOUNT_SETUP.md](COST_SAFETY_AND_ACCOUNT_SETUP.md) | Account paths (Visual Studio credits vs personal free account on W6 Tue), pay-as-you-go upgrade (W9 Tue), budgets, cheapest SKUs per lab, teardown, Sunday cost ritual |

Suggested repo layout: `azure-labs/` → `scripts/`, `w01/` … `w30/`, `py/`, `certs/`, `.devcontainer/`, `flashcards.md`, `cost-log.md`, `stories.md`
(TicketVerse's Bicep lives in `ticketverse/infra/azure/` from W28).

## 6. Rules, pitfalls & tips

**Rules**
1. **Guardrails before resources** — budget + alerts + MFA first. Budgets *alert*; they never stop spending.
2. **One resource group per lab; delete it the same day.** Check `az group list` every Sunday.
3. **No secrets in git** — managed identity + `DefaultAzureCredential` from W16 on, GitHub Actions log in through a federated credential (W22); `.gitignore` your local settings.
4. **Type, don't paste.** Predict every output before you run it.
5. **Evidence or it didn't happen** — outputs/screenshots in `wNN/`, one STAR story per lab in `stories.md`.

**Pitfalls this plan already handles (all verified Oct 2026)**

| Pitfall | Bites in | What to do |
|---|---|---|
| Microsoft Learn sandboxes no longer exist — exercises need your own subscription | W1–W5 | Choose Path A/B in [COST_SAFETY_AND_ACCOUNT_SETUP.md](COST_SAFETY_AND_ACCOUNT_SETUP.md) |
| Personal Microsoft sign-in is blocked on the company laptop | W1–W5, then always | Company laptop: `az` CLI, `az bicep build` and the Bicep/Azurite VS Code extensions; live labs on the personal laptop (set up W5 Sat) or a Codespace |
| New VNets default to private subnets, so a VM may have no internet | W2, W10, W12 | Give it an explicit outbound path (public IP, NAT gateway or load balancer) |
| Dynamic groups and SSPR need Entra ID P1+; the P2 trial is often unavailable to the personal account that created the tenant | W6 | Create cloud-only `labadmin` and start the trial as that user; fallback: the Applied Skills lab |
| The $200 credit ends 30 days after activation and the subscription is disabled | W9 | Upgrade to pay-as-you-go on W9 Tue (22 Dec), recheck budgets + anomaly alert |
| Allowed-locations policy blocks Foundry models offered only outside India | W7 → AI W25 | Add a policy exemption for that one resource group (command written in W7 Fri) |
| Deployment slots need Standard tier or higher | W11 | Use S1 only for the slot lab, delete right after |
| Bastion Developer is free but one VM, same VNet, no peering | W12 | Put Bastion Developer on the spoke VNet; Basic+ bills hourly |
| Recovery Services vault soft delete can no longer be disabled | W14 | Stop protection with delete-data (14 days soft-deleted at no cost); keep the vault in its own resource group |
| A "Stopped" VM is still billed unless deallocated | Any | `az vm deallocate` or delete |
| Cosmos DB vector search needs the `EnableNoSQLVectorSearch` capability (~15 min to activate) | W17, W25 | Enable it at account creation (W17 Wed, W25 Fri) |
| Built-in PgBouncer isn't supported on Burstable PostgreSQL | W18 | Client-side pooling (`psycopg_pool`) |
| RediSearch can only be added at creation and needs Enterprise clustering + NoEviction | W19 | Tick it in the create wizard |
| ACR Tasks runs are paused on Azure free credits | W23 | Fine after your W9 upgrade (`az acr build` needs no local Docker) |
| AKS defaults to 3 nodes; system pools need 4+ vCPUs (no B-series) | W23 | `--node-count 1 --no-wait`, then delete the same day |
| Deleted Key Vault names stay reserved during soft-delete retention | W22 | Unique names; purge lab vaults (no purge protection) |
| Python OpenTelemetry distro is now `microsoft-opentelemetry` | W24 | Older `azure-monitor-opentelemetry` still works |
| A personal Microsoft account may fail as the Azure SQL Entra admin | W27, W30 | Make `labadmin` the admin |

**Tips**
- Exams are employer-paid: request vouchers in **W1 Fri**, book each exam on its deadline (W2 Sat, W10 Tue, W20 Tue) with a
  **personal** Microsoft account, and make your profile name match your ID exactly. Rescheduling is free up to 24 hours before.
- Holidays: W9 Fri = 25 Dec, W10 Fri = 1 Jan, W14 Tue = 26 Jan — move those sessions to Sunday after the weekly test.
- **Behind schedule?** Minimum viable week = Tuesday session + Saturday lab + teardown. Skip stretch goals, never skip teardown.
- Every Sunday retro: pick **one** thing to do better next week (e.g., "type every command", "commit after each step").

## 7. How you're tested on Sundays

The Azure block of the 150-minute weekly test is **20 minutes: 12 exam-style questions for the current certification.**

| Weeks | Question pool |
|---|---|
| W1–W4 | AZ-900 (this week's topics + earlier weeks) |
| W5 | AZ-900 retro + AZ-104 kickoff (skills map, CLI vs PowerShell, where labs run) |
| W6–W15 | AZ-104 — about 8 questions on this week, 4 on earlier weeks |
| W16 | AZ-104 retro + AI-200 kickoff (keyless SDK auth, managed identities) |
| W17–W25 | AI-200 — about 8 on this week, 4 on earlier weeks |
| W26 | Exam week: use the slot for the season retro (or a mini-mock if your exam is later) |
| W27–W30 | Migration and architecture scenarios (Azure SQL targets, Azure Migrate/AppCAT, landing zones, hybrid networking, Well-Architected, cutover/rollback) in AZ-305 style, plus a retake topic if one is pending |

**Formats:** single/multiple choice, "put these CLI steps in order", "spot the bug" in a CLI/Bicep/KQL/Python snippet,
and a 2–3 question mini case study.
**Scoring:** /100 → **≥80 green**, **60–79 amber**, **<60 red**. Amber/red topics become remediation tasks in the first
10 minutes of next Tuesday's and Wednesday's sessions (re-do the micro-task, 10 flashcards, or re-run one lab step).
Track every score in `azure-labs/scores.csv` — the trend line is your best predictor of exam readiness.
