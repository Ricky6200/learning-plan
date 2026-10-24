# ☕ Java Backend Track — Core Java → Spring → Microservices → Kafka → Docker → Kubernetes → Azure

> **Mission:** in 26 weeks, go from "I can read Java" to "I can **write**, test, ship and defend a production-grade Java backend" — proven by the **TicketVerse** capstone running on Azure and a 60-minute mock interview you pass.

Week 1 starts **Mon 26 Oct 2026** · Week 26 ends **Sun 25 Apr 2027** · Stack: **JDK 25 LTS · Spring Boot 4.1.x (or newest stable) · Spring AI 2.0.x · Kafka 4.x (KRaft) · Kubernetes + Gateway API · Azure**

---

## 1. By Week 26 you will…

| # | Outcome (measurable) | Proof |
|---|---|---|
| 1 | Write Core Java from a blank file: OOP, constructors, equals/hashCode, immutability, generics, collections, streams | `java-mastery` repo, 10 weekly packages, 150+ JUnit tests |
| 2 | Explain and build collection internals | Your own `MyArrayList`, `MyHashMap`, O(1) LRU cache, `MinHeap` |
| 3 | Write correct concurrent code and debug it | Producer–consumer ×3, deadlock found with `jstack`, Lock/Condition queue, CompletableFuture + virtual threads gauntlet |
| 4 | Diagnose the JVM | GC comparison table, heap-dump leak hunt, JFR + async-profiler flame graphs |
| 5 | Explain Spring internals (IoC, bean lifecycle, auto-config, proxies, `@Transactional`) | Spring-without-Boot lab + TicketVerse code |
| 6 | Guarantee **zero double booking** under concurrency | 100-thread test: optimistic/pessimistic locking + Redis holds + DB constraints |
| 7 | Secure APIs with OAuth2/OIDC + JWT | Keycloak + resource server + method security, OWASP API Top 10 audit |
| 8 | Build event-driven microservices | 5 services + gateway, Kafka saga, transactional outbox, idempotent consumers, DLT |
| 9 | Run it anywhere | Docker Compose (one command), Helm chart on Kubernetes with Gateway API, GitHub Actions CI/CD |
| 10 | Deploy and operate on Azure | Live demo URL, Key Vault + managed identity, App Insights traces, teardown script |
| 11 | Add AI to a Java backend | Spring AI assistant: tool calling, RAG on pgvector, MCP server |
| 12 | Interview-ready | 239-question bank answered aloud, 5 STAR stories, mock interview score ≥ 75/100 |

---

## 2. Your weekly slots

| Day | Java slot | What happens |
|---|---|---|
| Mon | 60 min | New concept + coding kata |
| Tue | 60 min | Concept + coding kata |
| Wed | 60 min | Concept + coding kata |
| Thu | 60 min | Concept + coding kata |
| Fri | 60 min | Concept + coding kata |
| Sat | 60 min | **BUILD** (mini-project / TicketVerse milestone) — or a timed **BOSS BATTLE** in W4, W9, W14, W19, W23, W26 |
| Sun | 30 min (inside the 150-min weekly test) | Java test: 8 questions + 1 coding task |

Total ≈ **6.5 h/week** for this track. Repos: **`java-mastery`** (W1–W10, one package per week, JUnit tests from W3) → **`ticketverse`** (W11–W26).

---

## 3. How to run one session (built for "I understand code but freeze when writing it")

```text
10 min  RECAP + PREDICT   Re-type yesterday's key snippet from memory. Read today's topic and
                          PREDICT outputs/behaviour on paper before running anything.
25 min  LEARN             Read/watch the linked resource with a question in mind.
                          Write 3 bullet notes in your own words (notes/<week>.md).
25 min  CODE              1) TYPE the example (never paste)   2) MODIFY it (break it, extend it)
                          3) WRITE IT FROM SCRATCH in a new file without looking.
                          Finish with the "Done when:" check, then commit.
```

**Session rules**
- ✍️ **No copy-paste, no AI-generated code** for katas and boss battles. AI may *review* your code or give a **hint** after you have been stuck 10 minutes.
- 🔮 **Predict → run → explain.** Every surprise gets one sentence in your notes — that sentence is tomorrow's recap.
- ✅ **"Done when:" is binary.** If it is not met, the session is not done; carry it to the next slot (catch-up rules are in `../00_Progress_Tracker/AI_MEMORY.md`).
- 🧪 **Tests prove it.** From W3 every exercise gets at least one JUnit test (JUnit 6 — Jupiter, same API as JUnit 5).
- 📦 **Commit every session**: `git commit -m "W05-Tue: MinHeap with siftUp/siftDown, 5 tests green"`.
- 🗣️ **Say it aloud.** End each session by explaining the concept in 60 seconds as if in an interview.

**Saturday BUILD protocol:** 5 min plan (classes/endpoints/tests list) → 45 min build → 10 min README + commit + tag if it is a milestone.
**Boss Battle rules:** 60-minute timer, fresh package/branch, docs allowed, no AI code, pass = acceptance tests green. Cleared = **+300 XP**; shipped TicketVerse milestone = **+200 XP**.

---

## 4. Phase map

| Season | Weeks | Dates | Focus | Milestone / Boss |
|---|---|---|---|---|
| S1 "Foundation Forge" | W1–W4 | 26 Oct – 22 Nov 2026 | JVM basics, methods, OOP (constructors, init order, equals/hashCode, immutability), inheritance/interfaces, Strings, JUnit, exceptions, generics, collections | **Boss W4 (Sat 21 Nov):** timed Library Management System |
| S2 "Concurrency Crucible" | W5–W9 | 23 Nov – 27 Dec 2026 | Collections internals, streams (40 drills), Java 9→25, Maven/Git, multithreading, JMM, executors, locks, atomics, CompletableFuture, virtual threads | **Boss W9 (Sat 26 Dec):** concurrency gauntlet |
| S3 "Spring Citadel" | W10–W14 | 28 Dec 2026 – 31 Jan 2027 | JVM/GC, Spring Core, Boot internals, REST, JPA/Hibernate, transactions & locking, Redis, Spring Security + OAuth2, testing | **Boss W14 (Sat 30 Jan):** TicketVerse **v1.0.0** release |
| S4 "Distributed Kingdom" | W15–W19 | 1 Feb – 7 Mar 2027 | Microservices + DDD, gateway, resilience, observability, Kafka, Spring Kafka, outbox, saga, Docker, Linux | **Boss W19 (Sat 6 Mar):** whole system via `docker compose up` (**v3.1.0**) |
| S5 "Cloud Ascension" | W20–W23 | 8 Mar – 4 Apr 2027 | Kubernetes, Gateway API, HPA, Helm, GitHub Actions CI/CD, DevSecOps, Azure (AKS/Container Apps, managed data, Key Vault, App Insights) | **Boss W23 (Sat 3 Apr):** live Azure demo URL + verified teardown (**v5.0.0**) |
| S6 "Final Boss: The Offer" | W24–W26 | 5 Apr – 25 Apr 2027 | Spring AI assistant (tools, RAG, MCP), performance & hardening, interview mode | **Boss W26 (Sat 24 Apr):** 60-min mock technical interview |

TicketVerse versions: v0 (W11) → v1.0 (W14) → v2 (W16) → v3 (W18–W19) → v4 (W22) → v5 (W23) → v6 (W24) → v7 (W25). Details: [PROJECT_SPEC](Project_TicketVerse/PROJECT_SPEC.md).

---

## 5. Navigation

| File / folder | Use it for |
|---|---|
| [ROADMAP_26_WEEKS.md](ROADMAP_26_WEEKS.md) | One-page view of all 26 weeks |
| [Weeks/](Weeks/) | Daily sessions (`Week-01.md` … `Week-26.md`): topic, learn, do, "Done when", self-check, stretch |
| [RESOURCES.md](RESOURCES.md) | Verified docs, courses, YouTube (English + Hindi), books, tools with versions |
| [Project_TicketVerse/PROJECT_SPEC.md](Project_TicketVerse/PROJECT_SPEC.md) | Capstone spec: domain, services, APIs, events, state machine, saga, NFRs, milestones, resume bullets |
| [INTERVIEW_QUESTION_BANK.md](INTERVIEW_QUESTION_BANK.md) | 239 high-frequency questions (⭐ = most asked) mapped to weeks |
| [../00_Progress_Tracker/](../00_Progress_Tracker/) | XP, streaks, weekly test scores, weakness tracker, AI memory |

---

## 6. Rules, pitfalls & tips

**Rules**
1. **Write more than you read.** If a session had no code, it did not happen.
2. **Interview-proof every topic:** for each week answer the self-check questions aloud before Sunday.
3. **Version sanity:** JDK 25, Spring Boot 4.1.x (or newest stable), JUnit 6, Testcontainers 2.0.x, Maven 3.9.x / 3.10.x via the Maven Wrapper (Maven 4 is still a release candidate — don't make it your default).
4. **Never commit secrets** (`.env` in `.gitignore`; use Key Vault/identities in Azure).

**Pitfalls to avoid**
- ⚠️ Watching 3 hours of video instead of coding 25 minutes. Video is 1.5× speed, max 20 minutes per session.
- ⚠️ IDE generating `equals/hashCode`, constructors, getters in S1 — write them by hand first; generate later.
- ⚠️ "It works on my machine" concurrency — run concurrency tests 5× in a row; flaky = broken.
- ⚠️ Spring Boot 4 surprises: starters are modular (`spring-boot-starter-webmvc`), **Jackson 3** uses `tools.jackson` packages, `@MockBean` is gone (use `@MockitoBean`), Flyway needs `spring-boot-starter-flyway`. Keep the [Boot 4.0 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide) handy when old tutorials disagree.
- ⚠️ Old tutorials: Eureka/Hystrix/Zuul, `WebSecurityConfigurerAdapter`, ingress-nginx and ZooKeeper-based Kafka are **history**. Use HTTP service clients/Resilience4j, `SecurityFilterChain` beans, **Gateway API**, and **KRaft**.
- ⚠️ Docker Desktop on a corporate laptop needs a paid licence for large companies — use a licensed seat or [Rancher Desktop](https://rancherdesktop.io/)/[Podman Desktop](https://podman-desktop.io/). See the [Docker Desktop licence terms](https://docs.docker.com/subscription-billing/desktop-license/).
- ⚠️ Azure costs: every cloud lab ends with `teardown.sh`. Set budgets before creating anything.

**Tips that compound**
- Keep `notes/surprises.md`: every wrong prediction → one line. Re-read it on Sundays.
- Re-solve old katas from memory every Saturday morning warm-up (5 min).
- For every TicketVerse feature, write the interview answer *while* building it ("I prevented double booking by…").
- When stuck: (1) read the error, (2) shrink the problem, (3) docs, (4) ask AI for a **hint**, not code.

---

## 7. How you're tested on Sundays

Sunday weekly test (150 min across all tracks) — **Java part = 30 minutes**:

| Part | Format | Time |
|---|---|---|
| 8 questions | Mix of MCQ, short answer, **output prediction**, **bug spotting** on this week's topics (+1 spaced-repetition question from earlier weeks) | ~18 min |
| 1 coding task | Small, timed, from a blank file (e.g., immutable class, comparator chain, stream grouping, thread-safe counter, REST endpoint + test) | ~12 min |

**Scoring:** /100 → **≥ 80 green** · **60–79 amber** · **< 60 red**. Amber/red topics become remediation tasks in next week's "Fix-it" list (logged in `00_Progress_Tracker/WEAKNESS_TRACKER.md`). Weekly test XP = your score (78% → +78 XP).

**Self-test before Sunday:** each week's `self_check` questions (in `Weeks/Week-XX.md`) + the matching ⭐ questions in [INTERVIEW_QUESTION_BANK.md](INTERVIEW_QUESTION_BANK.md).
