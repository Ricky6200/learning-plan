# 🔍 Gap Analysis — what you didn't list, but the market expects (and where it's covered)

> You listed: Java, Microservices, Kafka, Docker, Kubernetes, Azure, AI Engineering, DSA, System Design.
> For a **Java Backend + Cloud + AI** role at SDE-2 level (2026–27 market), these are the gaps I added into the plan.

## ✅ Added to the plan (integrated — no extra time needed)
| # | Missing skill | Why it matters in interviews/jobs | Where it's covered |
|---|---|---|---|
| 1 | **SQL & database depth** (indexes, EXPLAIN, transactions, isolation levels, locking) | Every backend round asks "how would you prevent double booking / slow query?" Your SP experience is a strength — we convert it to ORM + Postgres + concurrency depth | Java W14–W15 · AI W8 · SD W5–W7 · Azure W18–W19 |
| 2 | **Testing** (JUnit 6, Mockito, Testcontainers, contract tests, coverage) | "Complete backend" = tested backend; interviewers ask how you test | Java W3 onward · W10 (Mockito, AssertJ) · W11–W16 (Testcontainers) · W18 (contract tests) · AI W12 (evals) |
| 3 | **Security** (Spring Security, OAuth2/OIDC, JWT, OWASP API & LLM Top 10) | Asked in almost every backend loop; mandatory for real systems | Java W16, W18, W29 · SD W17 · AI W16, W18 |
| 4 | **Observability** (logs, metrics, traces, OpenTelemetry, KQL) | Production debugging is a key SDE-2 signal; also in AI-200 | Java W19, W28 · AI W12, W19 · Azure W13, W24 |
| 5 | **CI/CD & DevSecOps** (GitHub Actions, image scanning, Dependabot, CodeQL) | Teams expect you to ship, not just code | Java W14 (first CI), W26 · AI W19 (eval gate) · Azure W29 |
| 6 | **Infrastructure as Code** (ARM/Bicep, deployment stacks) | AZ-104 requirement + real migrations | Azure W10, W28 (Terraform: stretch only, optional after the plan) |
| 7 | **Networking & HTTP fundamentals, Linux shell** | Needed for Docker/K8s/Azure networking and HLD | SD W1–W2 · Java W22 · Azure W12–W13, W29 |
| 8 | **Python** | AI engineering is Python-first; AI-200 expects Python | AI W1–W3 (then used weekly) |
| 9 | **Caching & Redis** | Classic HLD + performance topic | SD W4 · Java W15 · AI W13 · Azure W19 |
| 10 | **Cloud migration** (Cloud Adoption Framework, Azure Migrate, DMS) | You explicitly want "migration" capability | Azure W14 (basics), W27 (SQL Server + Java apps), W29, W30 (capstone) |
| 11 | **Git workflow & code-review habits** | Daily team skill; PR hygiene shows seniority | Java W7 + every repo |
| 12 | **Writing & explaining** (design docs, READMEs, ADRs, talking aloud) | Interviews grade communication as much as code | SD write-ups · Java W29 docs · AI W28 READMEs + demo · talk-aloud DSA mocks from W15 · Sunday tests |
| 13 | **Interview readiness** (resume, LinkedIn/Naukri, referrals, STAR behavioural, mocks, negotiation) | A job switch fails without this, even with skills | [Career & Interview Prep/](Career%20%26%20Interview%20Prep/) + Sunday career tasks |

## ⏸️ Deliberately NOT in the 30-week plan (and why)
| Topic | Reason | When to consider |
|---|---|---|
| Frontend frameworks (React/Angular) | Not required for backend roles; Swagger UI / simple Streamlit demos are enough | Only if targeting full-stack roles |
| Deep ML math / training models from scratch | AI *engineer* roles focus on building with models; intuition is covered (AI W4 ML fundamentals, W5 how LLMs work, W20–W21 open-source models + LoRA fine-tuning) | After W30 (e.g., fast.ai, Raschka's book) |
| Terraform, CKAD/CKA certifications | Valuable but time-expensive; Bicep + hands-on K8s cover the interview needs | After the plan (months 8–10) |
| Reactive programming (WebFlux) in depth | Awareness only (Java W17, W27); virtual threads cover most needs now | If a target job lists it |
| GraphQL, gRPC deep dives | Awareness in SD W2 and Java W27 | If a target job lists it |
| Extra certifications (AI-103, AZ-305) | Three certs in 7 months is already ambitious | AI-103 after W30 if you target AI roles (AI W25 already covers much of it); AZ-305 for architect roles |

## 🧭 Suggested next steps after Week 30
1. AI-103 (AI Apps & Agents Developer) — reuses ~60% of the AI track.
2. Read *Designing Data-Intensive Applications* fully (deepens HLD).
3. Contribute to one open-source Java/AI project (Spring AI, LangChain4j, Testcontainers modules).
4. Terraform Associate or CKAD if your target roles are platform-heavy.
