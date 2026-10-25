# 🎓 Azure Certification Guide — AZ-900 → AZ-104 → AI-200

> Facts verified on official Microsoft pages on **24–25 Oct 2026**. Exams change — re-check the study guide's
> "Skills measured as of …" date the week you book. Links to every source are at the bottom.

## 1. The path at a glance

| # | Exam | Credential earned | Plan week | Exam window (IST) | Duration | Pass mark | Microsoft Learn open during exam? |
|---|---|---|---|---|---|---|---|
| 1 | **AZ-900** Microsoft Azure Fundamentals | Microsoft Certified: Azure Fundamentals | **W5** | Tue 24 – Sat 28 Nov 2026 (target **Fri 27 Nov**) | 45 min | 700 / 1000 | ❌ No (not on Fundamentals exams) |
| 2 | **AZ-104** Microsoft Azure Administrator | Microsoft Certified: Azure Administrator Associate | **W16** | Tue 9 – Sat 13 Feb 2027 (target **Fri 12 Feb**) | 100 min | 700 / 1000 | ✅ Yes — but the timer keeps running |
| 3 | **AI-200** Developing AI Cloud Solutions on Azure | Microsoft Certified: **Azure AI Cloud Developer Associate** | **W26** | Tue 20 – Sat 24 Apr 2027 (target **Fri 23 Apr**) | 120 min | 700 / 1000 | ✅ Yes — but the timer keeps running |

Scores are scaled (1–1000), so 700 is **not** "70% of questions". There is **no penalty for guessing** — answer everything.

**Vouchers and booking dates in this plan:** request three vouchers from your L&D team in **W1 Fri (30 Oct 2026)** →
book AZ-900 in **W2 Sat (7 Nov)** → AZ-104 in **W10 Tue (29 Dec)** → AI-200 in **W20 Tue (9 Mar 2027)**. AZ-104 has a
go/no-go gate in **W15 Fri (5 Feb)** — details in Section 6. After AI-200, Season 6 (W27–W30) builds migration and
architecture skills that point towards AZ-305 (Section 10).

## 2. Why not AZ-204? (read this once, then stop worrying)

> [!IMPORTANT]
> **AZ-204 "Developing Solutions for Microsoft Azure" was retired on 31 July 2026 (11:59 PM Central Standard Time).**
> Its replacement is **AI-200 "Developing AI Cloud Solutions on Azure"**, which earns the new
> **Microsoft Certified: Azure AI Cloud Developer Associate**. You were told "AZ-900 → AZ-104 → AZ-204";
> the updated, equivalent path is **AZ-900 → AZ-104 → AI-200**.

What the official sources say:

| Source | What it states |
|---|---|
| [AZ-204 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204) | Banner: "This exam was retired on July 31, 2026, at 11:59 PM Central Standard Time." |
| [Azure Developer Associate certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/) | Banner: "This certification and the renewal assessment are retired", linking to the Microsoft Tech Community [Skills Hub blog post](https://techcommunity.microsoft.com/blog/skills-hub-blog/the-ai-job-boom-is-here-are-you-ready-to-showcase-your-skills/4494128). |
| [Microsoft Q&A — "Will AI-200 replace AZ-204?"](https://learn.microsoft.com/en-us/answers/questions/5955907/will-ai-200-replace-az-204-after-its-retirement) | Accepted answer: AI-200 is the replacement for AZ-204; existing Azure Developer Associate holders can't renew and the certification moves to "Historical" when it expires; prepare for AI-200. |
| [AI-200 certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/) + [course AI-200T00](https://learn.microsoft.com/en-us/training/courses/ai-200t00) | The new associate credential, its exam (120 minutes, proctored, may include interactive components) and the official course. |

**What actually changed for you:** AI-200 keeps the developer core (containers, messaging, Functions, Key Vault,
App Configuration, monitoring) and adds an AI-backend focus: **Cosmos DB vector search, PostgreSQL + pgvector,
Azure Managed Redis, Python SDKs, OpenTelemetry and KQL**. AZ-204-era topics such as API Management,
Microsoft Graph/MSAL and Blob Storage SDK work are not listed in AI-200's skills measured.

**Why AI-200 is last in this plan (W26):** its audience profile expects proficiency in **Python**, **vector
databases** and **containerized apps**. You get those from the AI track (Python in W1–W3, embeddings, pgvector and RAG in
W9–W12) and the Java track (Docker in W11 and W22, Kubernetes in W23–W24). AZ-104 comes first because it is the admin
foundation every developer/migration role leans on, and it's the prerequisite for AZ-305 later.

## 3. AZ-900 — Microsoft Azure Fundamentals (exam in W5)

**Proves:** you can explain cloud concepts and Azure's core services, security and governance to anyone —
a good warm-up and a common first badge. **Fundamentals certifications do not expire.**
**Format:** 45 minutes, no Microsoft Learn access. **Official self-paced path:** ~5 hours of Learn modules
(3 learning paths in [course AZ-900T00](https://learn.microsoft.com/en-us/training/courses/az-900t00)).

Skills measured as of **20 Jul 2026** ([study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)) mapped to weeks:

| Domain (weight) | Objective group (all bullets) | Week |
|---|---|---|
| Cloud concepts (25–30%) | Cloud computing; shared responsibility; public/private/hybrid + use cases; consumption-based model; pricing models; serverless | W1 Tue (serverless again W2 Wed) |
| | Benefits: high availability, scalability, reliability, predictability, security, governance, manageability | W1 Wed |
| | Service types: IaaS, PaaS, SaaS + use cases | W1 Wed |
| Architecture & services (35–40%) | Regions, region pairs, sovereign regions, availability zones, datacenters, resources & resource groups, subscriptions, management groups, hierarchy | W2 Tue |
| | Compute types (containers, VMs, functions); VM options (VMs, VM Scale Sets, availability sets, Azure Virtual Desktop); VM resources; app hosting options | W2 Wed + W2 Sat lab |
| | Virtual networks, subnets, peering, Azure DNS, VPN Gateway, ExpressRoute; public and private endpoints | W2 Fri |
| | Storage services, tiers, redundancy, account options; AzCopy, Storage Explorer, Azure File Sync; Azure Migrate, Data Box | W3 Tue + W3 Sat lab |
| | Entra ID & Entra Domain Services; SSO, MFA, passwordless; external identities; Conditional Access; Azure RBAC; Zero Trust; defense in depth; Defender for Cloud | W3 Wed, W3 Fri, W3 Sat |
| Management & governance (30–35%) | Cost factors, pricing calculator, cost management, tags | W4 Tue (budgets first set W1 Fri) |
| | Microsoft Purview, Azure Policy, resource locks | W4 Wed |
| | Portal, Cloud Shell, Azure CLI, Azure PowerShell, Azure Arc, infrastructure as code, ARM & ARM templates | W4 Fri, W1 Sat |
| | Azure Advisor, Service Health, Azure Monitor (Log Analytics, alerts, Application Insights) | W4 Fri |

**Practice:** free [AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) —
run 1 is the timed W4 Boss, run 2 waits until W5 Tue (so it measures learning, not memory); aim for **85%+** before you sit the exam.

## 4. AZ-104 — Microsoft Azure Administrator (exam in W16)

**Proves:** you can implement, manage and monitor identity, governance, storage, compute and networking in a real
Azure environment — the admin foundation for developer, DevOps and migration roles. No prerequisite certification
is listed on the [certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) (AZ-900 is optional, but you'll already have it).
**Format:** 100 minutes; case studies and multi-part items; Microsoft Learn available inside the exam (no extra time).
**Official self-paced path:** ~18 hours of Learn modules ([course AZ-104T00](https://learn.microsoft.com/en-us/training/courses/az-104t00)) plus the
[official hands-on labs](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/).

Skills measured as of **17 Apr 2026** ([study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)) mapped to weeks:

| Domain (weight) | Objective group (all bullets) | Week |
|---|---|---|
| Identities & governance (20–25%) | Entra users and groups: create, properties, licenses, external users, SSPR | W6 (Lab 01 on Sat) |
| | Built-in roles, role assignments at scopes, interpreting access | W7 Tue + Sat |
| | Azure Policy, resource locks, tags, resource groups, subscriptions, costs via alerts/budgets/Advisor, management groups | W7 Wed, Fri, Sat |
| Storage (15–20%) | Firewalls and virtual networks, SAS tokens, stored access policies, access keys, identity-based access for Azure Files | W8 Wed + Sat, W9 Tue (service-endpoint network rule W12 Sat) |
| | Create/configure accounts, redundancy, object replication, encryption, Storage Explorer & AzCopy | W8 Tue, Fri, Sat |
| | File shares, blob containers, tiers, soft delete (blobs, containers), Files snapshots + soft delete, lifecycle management, versioning | W9 Tue, Wed, Fri |
| Compute (20–25%) | Interpret/modify ARM templates and Bicep, deploy, export a deployment / convert ARM to Bicep | W10 Tue, Wed |
| | Create VMs, encryption at host, move VMs (RG/subscription/region), resize, disks, availability zones & sets, VM Scale Sets | W10 Fri + Sat, W11 Tue |
| | Containers in the portal: ACR, Container Instances, Container Apps, sizing and scaling | W11 Wed |
| | App Service: plan, scaling, create, TLS/certificates (HTTPS-only, minimum TLS), custom DNS, backup, networking (access restrictions), deployment slots | W11 Fri + Sat |
| Virtual networking (15–20%) | VNets and subnets, peering, public IPs, user-defined routes, troubleshoot connectivity | W12 Tue, Fri |
| | NSGs and ASGs, effective security rules, Azure Bastion, service endpoints, private endpoints | W12 Wed, Fri, Sat |
| | Azure DNS (public + private zones), internal/public load balancer, troubleshoot load balancing | W13 Tue + Sat |
| Monitor & maintain (10–15%) | Metrics, log settings, log queries (KQL), alert rules + action groups + processing rules, Insights, Network Watcher + Connection monitor | W13 Wed, Fri |
| | Recovery Services vault, Backup vault, backup policy, backup/restore (file-level restore), Site Recovery + failover, backup reports and alerts | W14 Tue, Wed |

**PowerShell:** AZ-104 expects Azure PowerShell as well as the CLI, so every Saturday from W6 to W14 (except W12)
repeats one step with Az PowerShell in Cloud Shell.
**Exam prep:** W15 (practice run 1 Tue, Study Cram on gaps Wed, run 2 + go/no-go gate Fri, timed gauntlet **Boss** Sat);
final revision and run 3 in W16 Tue–Wed. **Practice:** free
[AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21).
**Bonus:** the W14 Saturday lab is a hands-on **migration** (VM-hosted Spring Boot + Postgres → App Service + Flexible
Server) with a written runbook — not on the exam, but exactly the "migration" skill you want to sell in interviews.
Season 6 (W27–W30) takes it much further.

## 5. AI-200 — Developing AI Cloud Solutions on Azure (exam in W26)

**Proves:** you can build the back end of AI solutions on Azure — containers, AI-ready data services, messaging,
serverless, security and observability — across the full development lifecycle.
**Audience profile** (from the study guide): proficient in Azure SDKs, data management services, monitoring and
troubleshooting, messaging and eventing, **vector databases, Python** and **containerized applications**.
**Format:** 120 minutes, proctored, "may have interactive components"; Microsoft Learn available (timer runs).
**Official self-paced path:** 9 learning paths (~36 hours of modules, each with a ~30-minute exercise) in
[course AI-200T00](https://learn.microsoft.com/en-us/training/courses/ai-200t00). Exercises need your own subscription,
VS Code, the latest Azure CLI and **Python 3.12+** (you'll use Python 3.12 via uv on your personal laptop, the same version as the AI track).

Skills measured as of **7 Oct 2026** ([study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)) mapped to weeks:

| Domain (weight) | Objective (all bullets) | Week |
|---|---|---|
| Containerized solutions (20–25%) | ACR: build, store, version and manage images; ACR Tasks | W23 Tue (registry basics W11 Wed) |
| | Deploy containers to App Service with env vars and secrets | W22 Sat (managed-identity pull + Key Vault reference) |
| | Container Apps: environment configuration and revision management; KEDA event-driven scaling | W23 Tue, Wed, Sat |
| | Deploy and manage apps on AKS with manifests; monitor/troubleshoot AKS and Container Apps (logs, events, connectivity) | W23 Fri, W24 Sat |
| AI solutions with data services (30–35%)\* | Cosmos DB for NoSQL: SDK + queries; RU optimization via indexing policies and consistency levels | W17 (all week) |
| | Cosmos DB: embeddings + vector similarity search; change feed processor | W18 Tue, Wed (vector capability enabled at creation in W17 Wed) |
| | PostgreSQL: SDK connect/query; schema design, data types, indexing | W18 Fri |
| | PostgreSQL: indexing to cut latency and pgvector overhead; compute/memory/storage for vector workloads; vector search + RAG with metadata filters; connection optimization | W19 Tue, Wed (pooling W18 Sat) |
| | Azure Managed Redis: caching, expiration, invalidation; vector indexing for similarity search | W19 Fri + Sat lab |
| Connect to and consume Azure services (20–25%) | Service Bus: messages, queues, topics, subscriptions, dead-letter handling | W20 Tue, Wed + Boss Sat |
| | Event Grid: filters, custom events, retries | W20 Fri + Boss Sat |
| | Azure Functions: serverless APIs with triggers and bindings; configure and deploy function apps | W21 (all week) |
| Secure, monitor, troubleshoot (20–25%) | Key Vault secrets incl. rotation and retrieval | W22 Tue (rotation design), Sat (Key Vault reference) |
| | App Configuration: store and retrieve settings | W22 Fri |
| | Trace distributed systems with OpenTelemetry SDKs | W24 Tue, Wed (Application Insights intro W21 Sat) |
| | KQL queries for logs and metrics | W24 Fri (foundation W13 Wed) |

\* The study guide's "Skills at a glance" and change log list data services at **30–35%** ("% of exam increased"),
while one section heading still shows 25–30%. Treat it as the heaviest domain either way.

**Kickoff:** W16 Sat (study-guide map + keyless Python SDK). **Exam prep:** W25 (run 1 Tue, prep videos Wed, run 2 Fri,
timed build gauntlet **Boss** Sat); final revision and run 3 in W26 Tue–Wed, exam W26 Fri.
**Practice assessment:** lives on **AI Skills Navigator** (sign-in required) —
[AI-200 practice assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b).
**Official prep videos (Microsoft Learn, Oct 2026):** [1 containers](https://www.youtube.com/watch?v=XHOBLJQZBCU) ·
[2 data services](https://www.youtube.com/watch?v=haeOJ2K1UU4) · [3 connect & consume](https://www.youtube.com/watch?v=oIalMs581A0) ·
[4 secure, monitor, troubleshoot](https://www.youtube.com/watch?v=K2F1uvc8Cr8).

## 6. How to book (Pearson VUE) — same steps for all three exams

1. **Use a personal Microsoft account (MSA).** Microsoft "strongly recommends" it: exam records registered with a
   work/school account are lost if you leave that organization.
2. **Fix your certification profile name** so it matches your government ID *exactly* (online proctoring rejects mismatches).
3. Open the certification page → **Schedule exam** → you're handed to **Pearson VUE** → choose **online (OnVUE)** or a **test centre** → pick a slot in IST → pay.
4. **Online?** Run the Pearson VUE **system test** on the same laptop, network and room you'll use (personal laptop with admin rights is safest; corporate laptops often block the secure browser).
5. Save the confirmation to `azure-labs/certs/` and add the date to your calendar with a 2-day reminder.

| | Online (OnVUE) | Test centre |
|---|---|---|
| Best when | You have a quiet private room, stable wired internet, personal laptop | Home is noisy/shared or internet is flaky |
| Watch out for | Walled room, closed door, nobody may enter; clear desk; extra monitors unplugged; phone out of reach but audible | Travel time; centre slot availability in your city |

**Booking deadlines in this plan (employer-paid vouchers):** request the three vouchers from your L&D team in **W1 Fri**
(30 Oct 2026) · book AZ-900 in **W2 Sat** (7 Nov) for Fri 27 Nov · AZ-104 in **W10 Tue** (29 Dec) for Fri 12 Feb 2027 ·
AI-200 in **W20 Tue** (9 Mar 2027) for Fri 23 Apr 2027. A voucher that hasn't arrived by the deadline is worth chasing the same day.

**AZ-104 go/no-go gate (W15 Fri, 5 Feb 2027):** practice run 2 at **80%+** → go; **75–79%** → go only if no domain is
weak; **below 75%** → reschedule. Rescheduling or cancelling is free if you do it at least **24 hours** before the
appointment ([reschedule and cancellation policy](https://learn.microsoft.com/en-us/credentials/support/reschedule-and-cancellation-policy)).

**Price:** each certification page says the price is *"based on the country or region in which the exam is
proctored"* — the exact INR amount appears at checkout (this guide deliberately doesn't quote amounts). Your exams are
employer-paid through vouchers; if you ever pay yourself, Microsoft's [Exam Replay](https://learn.microsoft.com/en-us/credentials/certifications/deals)
offer bundles one exam + one retake (both used within 12 months; the retake only after a fail).

## 7. Using Microsoft Learn during the exam (associate exams only)

From [Exam duration and exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience):

- Available on **associate/expert role-based exams** (AZ-104, AI-200) — **not** on Fundamentals (AZ-900).
- Everything on `learn.microsoft.com` **except Q&A, practice assessments and your profile**; other domains are blocked.
- **No extra time** — it opens in a split screen and the clock keeps running. Use Ctrl+F on a page.
- Strategy: answer from memory first; open Learn only for **precise facts** (CLI parameter names, SKU limits, tier
  features). The W15 Fri "lookup race" drill trains exactly this.

Also: you may take unscheduled breaks (the clock runs), but **after a break you can't return to questions you've already seen.**

## 8. Practice, renewal and retakes

| Topic | Rule (official) | What you do in this plan |
|---|---|---|
| Practice assessments | Free on Microsoft Learn (AZ-900, AZ-104) and on AI Skills Navigator (AI-200); style and difficulty, not the real questions | AZ-900: run 1 W4 Boss, run 2 W5 Tue (85%+); AZ-104: runs W15 Tue/Fri (80%+ gate), run 3 W16 Wed; AI-200: runs W25 Tue/Fri, run 3 W26 Wed |
| Exam sandbox | [aka.ms/examdemo](https://aka.ms/examdemo) shows the real exam UI and question types | Click through it in W5 Wed; repeat before AZ-104/AI-200 if the UI still feels new |
| Score report | Results usually within minutes (lab exams ~30 min); bar chart per skill area; Microsoft doesn't reveal which questions you missed | Copy the bars into your gap log immediately |
| Retake policy | Fail → wait **24 hours** for attempt 2; then **14 days** between later attempts; max 5 attempts in 12 months; retakes are paid ([policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy)) | If you fail, book the retake 2–3 weeks out and fix weak domains next to the current track work |
| Renewal | Associate certifications expire **annually**; renew **free** via an online assessment on Learn in the **6-month window** before expiry; passing extends one year; Fundamentals don't expire ([renewal](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification)) | Calendar reminders: AZ-104 ~Aug 2027, AI-200 ~Oct 2027 (6 months before expiry) |

## 9. Exam-day checklist (print it)

- [ ] **T-2 days:** system test passed on the exam laptop + network; Windows updates done; VPN/proxy off.
- [ ] **T-1 day:** traps list re-read; no new topics; sleep by 11 pm.
- [ ] **ID:** valid government photo ID; name identical to your Learn certification profile.
- [ ] **Room (online):** walled room, door closed, nobody enters; desk clear; extra monitors unplugged and turned away; phone out of reach but audible.
- [ ] **Check-in:** start early — ID photos, headshot and a room scan take time (follow the greeter's instructions in the chat window).
- [ ] **During:** answer everything (no negative marking); flag anything >60–90 s; use Learn only for exact facts (associate exams); watch the clock at the halfway mark.
- [ ] **After:** save the score report to `azure-labs/certs/`; claim and share the badge; log weak domains even if you passed.

## 10. After AI-200 — Season 6 and the next certification

Season 6 (W27–W30) isn't tied to an exam, but it rehearses most of the design thinking in **AZ-305**
(skills measured as of 17 Apr 2026, [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)):

| Week | What you build | AZ-305 area it rehearses |
|---|---|---|
| W27 Migration I | Azure SQL target choice (SQL Database vs Managed Instance vs SQL on VM), Azure Migrate CSV assessment + business case, AppCAT, BACPAC migration with passwordless JDBC | Design data storage (relational); design migrations (evaluate servers, data and apps; migrate databases) |
| W28 TicketVerse IaC + landing zones | Bicep modules, Azure Verified Modules, a deployment stack; landing-zone design areas, subscription vending, policy-driven governance | Design governance (management groups, subscriptions, tagging, compliance); automated deployment |
| W29 Migration II + DevOps & APIs | Hybrid networking (VPN/ExpressRoute, DNS Private Resolver, Azure Firewall, Front Door), Well-Architected review + secure score + PIM, API Management, PostgreSQL online migration | Design network solutions; API integration; identity governance; migrations with cutover and rollback |
| W30 Capstone | Migrate and modernise `legacy-orders`: Bicep target, OIDC pipeline, managed identity to Azure SQL, Application Insights, timed runbook | Design infrastructure (compute, application architecture, migrations) and monitoring |

| Next step | Why it fits you | Notes (verified) |
|---|---|---|
| **AI-103** Developing AI Apps and Agents on Azure → *Azure AI Apps and Agents Developer Associate* | Natural continuation of your AI track (agents, generative AI, Microsoft Foundry, Python) | Replaced **AI-102**, which retired on **30 Jun 2026**. Skills: plan/manage an Azure AI solution 25–30%, generative AI + agentic solutions 30–35%, computer vision 10–15%, text analysis 10–15%, information extraction 10–15%. [Study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) · [Certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/) |
| **AZ-305** Designing Microsoft Azure Infrastructure Solutions → *Azure Solutions Architect Expert* | Best if you aim for tech-lead, architect or migration-lead roles — Season 6 already covered much of it | Requires the **Azure Administrator Associate** (your AZ-104). Domains: identity, governance and monitoring 25–30%, data storage 20–25%, business continuity 15–20%, infrastructure 30–35%. [Study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) · [Certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/) |
| **Microsoft Applied Skills** (hosted, lab-based) | Small, practical credentials you can earn between exams | e.g. [Deploy cloud-native apps using Azure Container Apps](https://learn.microsoft.com/en-us/credentials/applied-skills/deploy-cloud-native-apps-using-azure-container-apps/), [Build AI-powered solutions with Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/credentials/applied-skills/build-ai-powered-solutions-by-using-microsoft-azure-database-for-postgresql/); 72-hour wait between attempts |

**Recommendation:** decide in W30 Fri (`w30/next.md`). For a Java backend + Azure + AI-engineering role, take **AI-103**
next (≈8–10 weeks); if you're aiming at migration-lead or architect roles, take **AZ-305** first while Season 6 is fresh.

## 11. Sources (all checked 24–25 Oct 2026)

- Study guides: [AZ-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) ·
  [AZ-104](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) ·
  [AI-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200) ·
  [AZ-204 (retired)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204) ·
  [AI-102 (retired)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-102)
- Certification pages: [Azure Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/) ·
  [Azure Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) ·
  [Azure AI Cloud Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/) ·
  [Azure Developer Associate (retired)](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/)
- Retirement context: [Microsoft Tech Community Skills Hub blog](https://techcommunity.microsoft.com/blog/skills-hub-blog/the-ai-job-boom-is-here-are-you-ready-to-showcase-your-skills/4494128) ·
  [Microsoft Q&A answer](https://learn.microsoft.com/en-us/answers/questions/5955907/will-ai-200-replace-az-204-after-its-retirement)
- Policies: [Exam duration & experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience) ·
  [Retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy) ·
  [Reschedule and cancellation policy](https://learn.microsoft.com/en-us/credentials/support/reschedule-and-cancellation-policy) ·
  [Renewal](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification) ·
  [Online exams with Pearson VUE](https://learn.microsoft.com/en-us/credentials/certifications/online-exams) ·
  [Scoring & score reports](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports) ·
  [Pearson VUE for Microsoft](https://home.pearsonvue.com/microsoft)
