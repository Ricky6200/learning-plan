# ☁️ Azure Cloud Track — build, run and migrate on Azure (AZ-900 → AZ-104 → AI-200)

> **Mission:** in 26 weeks, become the Java backend engineer who can build, secure, operate **and migrate** workloads
> on Azure — and prove it with three Microsoft certifications and a portfolio of real labs.

> [!IMPORTANT]
> ### Why not AZ-204?
> You were told "AZ-900 → AZ-104 → AZ-204". **AZ-204 was retired on 31 July 2026.** Microsoft's replacement is
> **AI-200 "Developing AI Cloud Solutions on Azure"**, which earns **Microsoft Certified: Azure AI Cloud Developer Associate**.
>
> **Your final path:** **AZ-900** (exam W5, ~27 Nov 2026) → **AZ-104** (exam W16, ~12 Feb 2027) → **AI-200** (exam W26, ~24 Apr 2027).
>
> AI-200 goes last because it expects Python (AI track W1–W2), vector databases/RAG (AI track W6–W10) and containers
> (Java track W19–W21). Official sources and details: [CERTIFICATION_GUIDE.md](CERTIFICATION_GUIDE.md).

## 1. By Week 26 you will…

- [ ] Hold **3 certifications** — AZ-900 (W5), AZ-104 (W16), AI-200 (W26) — or have a dated retake plan for any you miss.
- [ ] Own a public **`azure-labs`** repo with 26 Saturday labs/boss battles: CLI scripts, Bicep, Python, diagrams and evidence.
- [ ] Deploy a Spring Boot app to **App Service (slot swap)**, **Container Apps (revisions, KEDA)** and **AKS (manifests)** — keyless, via managed identity.
- [ ] Design a **hub-spoke network** with NSGs, Bastion and **private endpoints**, and troubleshoot it with Network Watcher.
- [ ] Execute and document a **VM → PaaS migration** (Spring Boot + Postgres) with a cutover and rollback runbook (W14 Boss).
- [ ] Build an **AI data layer**: Cosmos DB vector search, PostgreSQL + pgvector (HNSW/IVFFlat tuning) and an Azure Managed Redis cache.
- [ ] Wire **event-driven back ends** with Service Bus, Event Grid and Functions, secured with Key Vault + App Configuration.
- [ ] Trace a request end to end with **OpenTelemetry + Application Insights** and prove where the time goes with **KQL**.
- [ ] Answer 6 core Azure interview scenarios (developer + migration) in 2 minutes each, using stories from your own labs.
- [ ] Stay inside your budget with **zero orphaned resources** (weekly cost log).

## 2. Your weekly slots

| Day | Minutes | Session type |
|---|---|---|
| Tue | 45 | Learn + small hands-on |
| Wed | 45 | Learn + small hands-on |
| Fri | 45 | Learn + prepare Saturday |
| **Sat** | **60** | **LAB** — or **BOSS BATTLE** in W4, W9, W14, W19, W23, W26 |
| Sun | 20 (inside the 150-min weekly test) | 12 exam-style Azure questions |

That's 3 h 15 min of Azure per week. Exam days (W5, W16, W26) borrow extra time from another block once — that's expected.

## 3. How to run one session — Predict → Type → Verify → Explain

Built for "I understand code but freeze when I have to write it": you always **write it yourself**, in small steps.

| Minute (45-min session) | Step | What you actually do |
|---|---|---|
| 0–3 | **Aim** | Read the session's **Done when** — that's the finish line. |
| 3–20 | **Learn actively** | Work through the linked module/doc/video; write 3 bullets + 1 tiny diagram in `wNN/notes.md` (no pasted paragraphs). |
| 20–40 | **Predict → Type → Verify** | Before each command/code block, write what you expect; type it yourself (no copy-paste); compare; fix; repeat. |
| 40–45 | **Explain + log** | Explain it aloud in 60 seconds, add 2 flashcards to `flashcards.md`, commit with a meaningful message. |

**Saturday LAB (60 min):** 0–5 plan the resources → 5–45 build in `rg-lab-wNN` (`scripts/new-lab.sh`) → 45–55 save evidence
(CLI output, screenshots) to `wNN/` → 55–60 `scripts/nuke-lab.sh` and confirm the group is gone.
**BOSS BATTLE:** visible timer, notes only where the task allows, score yourself honestly, log every miss.

Writing-confidence tips: start from a 5-line script and grow it; lean on `--help` and `az find`; use GitHub Copilot to
*explain* errors, not to write the whole lab; keep reusable snippets in `azure-labs/snippets.md`.

## 4. Phase map

| Season | Weeks | Focus | Milestone |
|---|---|---|---|
| S1 Foundation Forge | W1–W4 | Cloud concepts, Azure architecture, storage + identity, governance; Azure CLI + cost guardrails | **Boss W4:** two AZ-900 practice runs at 85%+ and exam booked |
| S2 Concurrency Crucible | W5–W9 | **AZ-900 exam (W5)**; AZ-104 identity, RBAC, Policy, storage | **Boss W9:** timed identity + storage admin challenge (CLI only) |
| S3 Spring Citadel | W10–W14 | ARM/Bicep, VMs, App Service, containers, networking, monitoring, backup/DR, **migration** | **Boss W14:** Migration Lab — VM-hosted Spring Boot + DB → PaaS + runbook |
| S4 Distributed Kingdom | W15–W19 | AZ-104 prep + **exam (W16)**; AI-200: keyless SDK, Cosmos DB, PostgreSQL + pgvector, Managed Redis | **Boss W19:** RAG data layer on Azure (pgvector + Redis) + practice questions |
| S5 Cloud Ascension | W20–W23 | Service Bus, Event Grid, Functions, Key Vault, App Configuration, ACR / Container Apps / AKS | **Boss W23:** provision TicketVerse on Azure, verify, tear down (pairs with Java W23) |
| S6 Final Boss: The Offer | W24–W26 | OpenTelemetry + KQL, AI-200 prep, interview Q&A, cleanup, next steps | **Boss W26:** **AI-200 exam** |

**Cross-track hooks:** W11 deploys the Java track's TicketVerse v0 to App Service · W14 migrates a Spring Boot + Postgres
app · W17–W19 reuse your AI-track embeddings and DocuMind chunks · W21 extends the AI track's MCP work on Functions ·
W23 provisions the infrastructure the Java track deploys to · W24 adds Application Insights to TicketVerse.

## 5. Navigation

| File | What's inside |
|---|---|
| [ROADMAP_26_WEEKS.md](ROADMAP_26_WEEKS.md) | All 26 weeks on one page |
| [Weeks/](Weeks/) | `Week-01.md` … `Week-26.md`: every session's topic, learn, do, Done when, self-check and stretch |
| [RESOURCES.md](RESOURCES.md) | Study guides, learning paths, docs, YouTube (English + Hindi), practice, tools with versions |
| [CERTIFICATION_GUIDE.md](CERTIFICATION_GUIDE.md) | Why AI-200 replaced AZ-204, skills-measured → week maps, booking, Learn-in-exam rules, retakes, renewal |
| [COST_SAFETY_AND_ACCOUNT_SETUP.md](COST_SAFETY_AND_ACCOUNT_SETUP.md) | Account paths (Visual Studio credits vs free account on W6), budgets, cheapest SKUs, teardown, Sunday cost ritual |

Suggested repo layout: `azure-labs/` → `scripts/`, `w01/` … `w26/`, `py/`, `certs/`, `flashcards.md`, `cost-log.md`, `stories.md`.

## 6. Rules, pitfalls & tips

**Rules**
1. **Guardrails before resources** — budget + alerts + MFA first. Budgets *alert*; they never stop spending.
2. **One resource group per lab; delete it the same day.** Check `az group list` every Sunday.
3. **No secrets in git** — managed identity + `DefaultAzureCredential` from W16 on; `.gitignore` your local settings.
4. **Type, don't paste.** Predict every output before you run it.
5. **Evidence or it didn't happen** — outputs/screenshots in `wNN/`, one STAR story per lab in `stories.md`.

**Pitfalls this plan already handles (all verified Oct 2026)**

| Pitfall | Bites in | What to do |
|---|---|---|
| Microsoft Learn sandboxes no longer exist — exercises need your own subscription | W1–W5 | Choose Path A/B in [COST_SAFETY_AND_ACCOUNT_SETUP.md](COST_SAFETY_AND_ACCOUNT_SETUP.md) |
| New VNets default to private subnets, so a VM may have no internet | W2, W10, W12 | Give it an explicit outbound path (public IP, NAT gateway or load balancer) |
| Dynamic groups and SSPR need Entra ID P1+ | W6 | Start the Entra ID P2 trial on activation day |
| Deployment slots need Standard tier or higher | W11 | Use S1 only for the slot lab, delete right after |
| Bastion Developer is free but one VM, same VNet, no peering | W12 | Basic SKU for peered tests — delete within the hour |
| A "Stopped" VM is still billed unless deallocated | Any | `az vm deallocate` or delete |
| Built-in PgBouncer isn't supported on Burstable PostgreSQL | W18 | Client-side pooling (`psycopg_pool`) |
| Managed Redis modules (RediSearch) can only be added at creation | W19 | Tick RediSearch when you create the cache |
| ACR Tasks runs are paused on Azure free credits | W23 | `docker build` + `docker push`, or run Tasks after upgrading |
| AKS defaults to 3 nodes; system pools need 4+ vCPUs (no B-series) | W23 | `--node-count 1`, then stop or delete the same day |
| Deleted Key Vault names stay reserved during soft-delete retention | W22 | Unique names; purge lab vaults (no purge protection) |
| Python OpenTelemetry distro is now `microsoft-opentelemetry` | W24 | Older `azure-monitor-opentelemetry` still works |

**Tips**
- Book each exam early with a **personal** Microsoft account, and make your profile name match your ID exactly.
- Holidays: W9 Fri = 25 Dec, W10 Fri = 1 Jan — move those sessions to Sunday after the weekly test.
- **Behind schedule?** Minimum viable week = Tuesday session + Saturday lab + teardown. Skip stretch goals, never skip teardown.
- Every Sunday retro: pick **one** thing to do better next week (e.g., "type every command", "commit after each step").

## 7. How you're tested on Sundays

The Azure block of the 150-minute weekly test is **20 minutes: 12 exam-style questions for the current certification.**

| Weeks | Question pool |
|---|---|
| W1–W4 | AZ-900 (this week's topics + earlier weeks) |
| W5 | AZ-900 retro + AZ-104 kickoff (skills map, CLI vs PowerShell, ARM template sections) |
| W6–W15 | AZ-104 — about 8 questions on this week, 4 on earlier weeks |
| W16 | AZ-104 retro + AI-200 kickoff (keyless SDK auth, managed identities) |
| W17–W25 | AI-200 — about 8 on this week, 4 on earlier weeks |
| W26 | Exam week: use the slot for the season retro (or a mini-mock if your exam is later) |

**Formats:** single/multiple choice, "put these CLI steps in order", "spot the bug" in a CLI/Bicep/KQL/Python snippet,
and a 2–3 question mini case study.
**Scoring:** /100 → **≥80 green**, **60–79 amber**, **<60 red**. Amber/red topics become remediation tasks in the first
10 minutes of next Tuesday's and Wednesday's sessions (re-do the micro-task, 10 flashcards, or re-run one lab step).
Track every score in `azure-labs/scores.csv` — the trend line is your best predictor of exam readiness.
