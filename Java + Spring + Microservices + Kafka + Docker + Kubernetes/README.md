# ☕ Java Backend Track — Core Java → Spring → Microservices → Kafka → Docker → Kubernetes → Azure

> **Mission:** in 30 weeks, go from "I can read Java" to "I can **write**, test, ship and defend a production-grade Java backend" — proven by the **TicketVerse** capstone running on Azure (with the AI track's `ticketverse-ai` service plugged in) and a 60-minute mock interview you pass.

Week 1 starts **Mon 26 Oct 2026** · Week 30 ends **Sun 23 May 2027** · Stack: **JDK 25 LTS (Corretto 25 on your laptop) · Spring Boot 4.1.x · Spring Cloud 2025.1.x · Kafka 4.x (KRaft) · Docker · Kubernetes + Gateway API · GitHub Actions · Azure**

---

## 1. By Week 30 you will…

| # | Outcome (measurable) | Proof |
|---|---|---|
| 1 | Write Core Java from a blank file: OOP, constructors, equals/hashCode, immutability, generics, collections, streams | `java-mastery` repo (W1–W12), weekly packages, 150+ JUnit tests |
| 2 | Explain and build collection internals | Your own `MyArrayList`, `MyHashMap`, `MinHeap` and a `LinkedHashMap` LRU cache (the hand-rolled O(1) LRU is DSA W10) |
| 3 | Write correct concurrent code and debug it | Producer–consumer, deadlock found with `jstack`, Lock/Condition queue, CompletableFuture + virtual threads gauntlet |
| 4 | Close the classic Core Java gaps | NIO.2 file tools, serialization and deep copies, a 50-line reflective DI container, Mockito + AssertJ tests, regex validators (W10) |
| 5 | Package Java for containers and diagnose the JVM | Layered Boot images, container-aware heap flags, GC comparison table, leak hunt with `jcmd` histograms + JFR views, flame graphs |
| 6 | Explain Spring internals (IoC, bean lifecycle, proxies, `@Async`/events, auto-config, `@Transactional`) | Spring-without-Boot lab (W12) + TicketVerse code |
| 7 | Guarantee **zero double booking** under concurrency | 100-thread boss test: optimistic/pessimistic locking + Redis holds + DB constraints |
| 8 | Secure APIs with OAuth2/OIDC + JWT | Keycloak + resource server + method security (USER/ADMIN/SUPPORT), client credentials between services, OWASP API Top 10 audit |
| 9 | Split a monolith and build event-driven microservices | Step-by-step split with contract tests + ArchUnit, 5 services + gateway, Kafka saga, transactional outbox, idempotent consumers, DLT, expiry and cancellation |
| 10 | Run it anywhere | One-command Docker Compose, Helm chart on Kubernetes with Gateway API, GitHub Actions CI/CD |
| 11 | Deploy and operate on Azure | Live demo URL on Container Apps (infrastructure provisioned by the Azure track), Key Vault + managed identities, App Insights traces, verified teardown |
| 12 | Plug an AI service into a real platform | Gateway route, JWT pass-through, rate limits, fallbacks, Kafka topics and Helm values for the AI track's `ticketverse-ai` |
| 13 | Interview-ready | 255-question bank answered aloud, 5 STAR stories, mock interview score ≥ 75/100 |

---

## 2. Your weekly slots

| Day | Java slot | What happens |
|---|---|---|
| Mon–Fri | 60 min each | One concept + one coding exercise (≤ 35 min hands-on) |
| Sat | 60 min | **BUILD** (mini-project / TicketVerse milestone) — or a timed **BOSS BATTLE** in W4, W9, W15, W20, W25, W30 |
| Sun | 30 min (inside the 150-min weekly test) | Java test: 8 questions + 1 coding task |

Total ≈ **6.5 h/week** for this track. Repos: **`java-mastery`** (W1–W12, one package or module per week, JUnit tests from W2) → **`ticketverse`** (W13–W30).

**Lighter days are built in:** Christmas (Fri 25 Dec, W9), New Year (Fri 1 Jan, W10) and Holi (Mon 22 Mar, W22) are lite days; the AZ-104 week (W16) and the AI-200 week (W26) keep Friday and Saturday light.

---

## 3. How to run one session (built for "I understand code but freeze when writing it")

```text
10 min  RECAP + PREDICT   Re-type yesterday's key snippet from memory. Read today's topic and
                          PREDICT outputs/behaviour on paper before running anything.
15 min  LEARN             ONE main resource (the "Read:" link; "Optional:" links are extra).
                          Write 3 bullet notes in your own words (notes/<week>.md).
35 min  CODE              1) TYPE the example (never paste)   2) MODIFY it (break it, extend it)
                          3) WRITE IT FROM SCRATCH in a new file without looking.
                          Finish with the "Done when:" check, then commit.
                          Anything that does not fit goes to the week's stretch.
```

**Session rules**
- ✍️ **No copy-paste, no AI-generated code** for katas and boss battles. AI may *review* your code or give a **hint** after you have been stuck 10 minutes.
- 🔮 **Predict → run → explain.** Every surprise gets one sentence in your notes — that sentence is tomorrow's recap.
- ✅ **"Done when:" is binary.** If it is not met, the session is not done; carry it to the next slot (catch-up rules are in `../00_Progress_Tracker/AI_MEMORY.md`).
- 🧪 **Tests prove it.** Your first two JUnit tests come in W2; from W3 every exercise gets at least one test (JUnit 6 — Jupiter, same API as JUnit 5). Mockito + AssertJ join in W10.
- 📦 **Commit every session**: `git commit -m "W05-Tue: LinkedHashMap LRU cache, 4 tests green"`.
- 🗣️ **Say it aloud.** End each session by explaining the concept in 60 seconds as if in an interview.

**Saturday BUILD protocol:** 10 min plan (classes/endpoints/tests list) → 35–40 min build → 10 min README + commit + tag if it is a milestone.
**Boss Battle rules:** 60-minute timer, fresh package/branch, docs allowed, no AI code, pass = acceptance tests green. Cleared = **+300 XP**; shipped TicketVerse milestone = **+200 XP**.

---

## 4. Phase map

| Season | Weeks | Dates | Focus | Milestone / Boss |
|---|---|---|---|---|
| S1 "Foundation Forge" | W1–W4 | 26 Oct – 22 Nov 2026 | JVM basics, operators (incl. bitwise), methods + recursion, first HashMap/ArrayList/JUnit, OOP (constructors, init order, equals/hashCode, immutability), inheritance/interfaces/enums, Strings, exceptions, generics, collections, lambda-syntax primer | **Boss W4 (Sat 21 Nov):** timed Library Management System |
| S2 "Concurrency Crucible" | W5–W9 | 23 Nov – 27 Dec 2026 | Collections internals, streams, Java 9→25 (records, sealed types, JPMS), Maven/Git, multithreading, JMM, executors, locks, atomics, CompletableFuture, virtual threads | **Boss W9 (Sat 26 Dec):** concurrency gauntlet |
| S3 "Spring Citadel" | W10–W15 | 28 Dec 2026 – 7 Feb 2027 | Core Java gaps (I/O, serialization, reflection, Mockito, regex), Docker for Java + JVM/GC, Spring Core, Boot internals + testing, REST, JPA/Hibernate, first CI, transactions & locking, Redis | 🎟️ TicketVerse **v0.1.0** (W13) · **Boss W15 (Sat 6 Feb):** hold-and-book under 100 threads |
| S4 "Distributed Kingdom" | W16–W20 | 8 Feb – 14 Mar 2027 | Spring Security + OAuth2, microservices + DDD, gateway, the step-by-step split (client credentials, contract tests, ArchUnit), resilience, observability, Kafka | 🚀 **v1.0.0** (W16) · **Boss W20 (Sat 13 Mar):** Kafka + microservices gauntlet · 💼 start applying |
| S5 "Cloud Ascension" | W21–W25 | 15 Mar – 18 Apr 2027 | Spring Kafka, outbox, saga, Docker deep dive, Kubernetes I–II (Gateway API, HPA, Helm), loose ends (catalog/review events, payment expiry, cancellation, JPA extras) | 🐳 Full system in Docker (W22) · **Boss W25 (Sat 17 Apr):** TicketVerse **v2.0.0** end to end |
| S6 "Final Boss: The Offer" | W26–W30 | 19 Apr – 23 May 2027 | CI/CD + DevSecOps, platform hooks for `ticketverse-ai`, Azure deployment, performance & hardening, interview mode | ☁️ Live on Azure (W28) · **Final Boss W30 (Sat 22 May):** 60-min mock technical interview |

TicketVerse versions: `v0.1.0` (W13) → `v1.0.0` (W16) → `v1.1.0` five services (W18) → `v1.2.0` resilience + observability (W19) → `v1.3.0` saga + outbox (W21) → `v1.4.0` full system in Docker (W22) → `v2.0.0` Boss S5 (W25) → `v2.1.0` CI/CD (W26) → AI integration with `ticketverse-ai` (W27; the AI track tags `ticketverse-v2.0-ai`) → `v2.2.0` live on Azure (W28) → `v2.3.0` performance + portfolio (W29). Boss tags: `boss-s1`/`boss-s2` in `java-mastery`, `boss-s3`/`boss-s4`/`boss-s5` in `ticketverse`. Details: [PROJECT_SPEC](Project_TicketVerse/PROJECT_SPEC.md).

### Week by week

| Week | Dates | Theme | Saturday | Milestone |
|---|---|---|---|---|
| [W01](Weeks/Week-01.md) | 26 Oct – 1 Nov | Java foundations rebuilt: JVM to methods | BUILD: CLI Expense Tracker v0 with HashMap totals | |
| [W02](Weeks/Week-02.md) | 2 – 8 Nov | OOP I: constructors, encapsulation, object contracts | BUILD: Bank Account System with clean OOP | |
| [W03](Weeks/Week-03.md) | 9 – 15 Nov | OOP II: inheritance, interfaces, Strings, JUnit | BUILD: Library domain model with JUnit tests | |
| [W04](Weeks/Week-04.md) | 16 – 22 Nov | Exceptions, generics, collections: Season 1 boss | BOSS BATTLE: Library Management System, 60 min timed | ⚔️ Boss S1 |
| [W05](Weeks/Week-05.md) | 23 – 29 Nov | Collections internals: HashMap, TreeMap, heaps, LRU | BUILD: MyHashMap with chaining and resize | |
| [W06](Weeks/Week-06.md) | 30 Nov – 6 Dec | Functional Java: lambdas, streams, Optional drills | BUILD: Sales analytics over a CSV using streams | |
| [W07](Weeks/Week-07.md) | 7 – 13 Dec | Modern Java 9 to 25, Maven, Git | BUILD: Git workflow: branch, conflict, rebase, PR, recovery | |
| [W08](Weeks/Week-08.md) | 14 – 20 Dec | Multithreading I: threads, locks, JMM, executors | BUILD: odd-even printer, BlockingQueue pipeline, deadlock fix | |
| [W09](Weeks/Week-09.md) | 21 – 27 Dec | Concurrency II: locks, async, virtual threads, Season 2 boss | BOSS BATTLE: Concurrency gauntlet, 60 min timed | ⚔️ Boss S2 |
| [W10](Weeks/Week-10.md) | 28 Dec – 3 Jan | Core Java gaps: I/O, copies, reflection, Mockito, regex | BUILD: Timed rewrite of the W4 library: records, streams, mocks | |
| [W11](Weeks/Week-11.md) | 4 – 10 Jan | Docker for Java, then JVM internals and GC | BUILD: Containerised Java app + Postgres via Compose, tuned JVM | |
| [W12](Weeks/Week-12.md) | 11 – 17 Jan | Spring Core: DI, lifecycle, AOP, async, logging | BUILD: Spring Core app without Boot + Postgres + Testcontainers | |
| [W13](Weeks/Week-13.md) | 18 – 24 Jan | Spring Boot internals, testing, REST APIs, TicketVerse v0 | BUILD: TicketVerse v0 catalog APIs on Postgres in Docker | 🎟️ `v0.1.0` |
| [W14](Weeks/Week-14.md) | 25 – 31 Jan | Data layer: JDBC, JPA/Hibernate, Flyway, SQL, first CI | BUILD: Data model, migrations, Testcontainers tests, first CI workflow | |
| [W15](Weeks/Week-15.md) | 1 – 7 Feb | Transactions, locking, Redis seat holds: Season 3 boss | BOSS BATTLE: Hold-and-book under 100 threads, 60 min timed | ⚔️ Boss S3 |
| [W16](Weeks/Week-16.md) | 8 – 14 Feb | Spring Security, OAuth2 and the v1.0 release | BUILD: TicketVerse v1.0 release (light day, AZ-104 week) | 🚀 `v1.0.0` |
| [W17](Weeks/Week-17.md) | 15 – 21 Feb | Microservices: DDD boundaries, gateway, service calls | BUILD: Strangler-ready monolith behind the gateway | |
| [W18](Weeks/Week-18.md) | 22 – 28 Feb | Microservices split: extract, secure, contract-test | BUILD: Five services with Compose and a smoke test | `v1.1.0` |
| [W19](Weeks/Week-19.md) | 1 – 7 Mar | Resilience and observability: survive and see failures | BUILD: Chaos test: kill payment, prove resilience with evidence | `v1.2.0` |
| [W20](Weeks/Week-20.md) | 8 – 14 Mar | Kafka fundamentals and delivery semantics: Season 4 boss | BOSS BATTLE: Kafka + microservices gauntlet, 60 min timed | ⚔️ Boss S4 |
| [W21](Weeks/Week-21.md) | 15 – 21 Mar | Spring Kafka, outbox and the booking saga | BUILD: TicketVerse booking saga with outbox, end to end | `v1.3.0` |
| [W22](Weeks/Week-22.md) | 22 – 28 Mar | Docker deep dive: full TicketVerse in containers | BUILD: Full TicketVerse system in Docker with one command | 🐳 `v1.4.0` |
| [W23](Weeks/Week-23.md) | 29 Mar – 4 Apr | Kubernetes I: pods, deployments, services, config | BUILD: Catalog and booking services on local Kubernetes | |
| [W24](Weeks/Week-24.md) | 5 – 11 Apr | Kubernetes II: Gateway API, autoscaling, state, Helm | BUILD: TicketVerse Helm chart on local Kubernetes | |
| [W25](Weeks/Week-25.md) | 12 – 18 Apr | TicketVerse loose ends and the Season 5 boss | BOSS BATTLE: TicketVerse v2 end to end, 60 min timed | ⚔️ Boss S5 · `v2.0.0` |
| [W26](Weeks/Week-26.md) | 19 – 25 Apr | CI/CD and DevSecOps with GitHub Actions | BUILD: One change from PR to tagged release (light day, AI-200 week) | `v2.1.0` |
| [W27](Weeks/Week-27.md) | 26 Apr – 2 May | Platform hooks for ticketverse-ai: gateway, events, resilience | BUILD: Joint end-to-end test with the AI track | 🤖 joint AI end-to-end |
| [W28](Weeks/Week-28.md) | 3 – 9 May | Azure deployment: TicketVerse live with AI | BUILD: TicketVerse live on Azure (joint deploy with Azure W28) | ☁️ `v2.2.0` live on Azure |
| [W29](Weeks/Week-29.md) | 10 – 16 May | Performance, hardening and production-ready docs | BUILD: Performance report and polished portfolio repository | `v2.3.0` |
| [W30](Weeks/Week-30.md) | 17 – 23 May | Interview mode: revise, tell stories, Final Boss | BOSS BATTLE: Full mock technical interview, 60 minutes | 👑 Final Boss |

### Cross-track anchors

- **Exams:** AZ-900 W5 (Fri 27 Nov) · AZ-104 W16 · AI-200 W26 — Java keeps Friday and Saturday light in W16 and W26.
- **Bridges to the AI track:** W6 Fri rewrites two stream katas as Python comprehensions (AI W1) · W7 Mon compares records with `@dataclass(frozen=True)` (AI W2) · W9 Thu compares CompletableFuture with `asyncio.gather` (AI W2).
- **Docker:** AI W8 (14–19 Dec) teaches Docker and Compose basics in Codespaces; Java W11 recaps them in 10 minutes and goes Java-specific (Boot jar on a JRE base, layered jars, container-aware JVM flags, Compose with Postgres); W22 hardens every image.
- **Events for AI:** Java W25 publishes `catalog.shows.v1` and `catalog.reviews.v1`; AI W27 consumes them.
- **`ticketverse-ai`** is owned by the AI track (AI W23–W24, extended in AI W27). Java W27 adds the platform hooks — gateway route, JWT pass-through, rate limits, circuit breaker with a degraded fallback, Kafka topics, Helm values — and runs the joint end-to-end test.
- **W28 joint deploy (Sat 8 May):** DSA → **Azure lab** (provisions the TicketVerse deployment stack with Bicep) → **Java** (deploy with `deploy-azure`, both sagas + the AI end-to-end script on the live URL, demo video) → **AI** (live check, then `infra/teardown`) → SD.
- **LRU progression:** Java W5 (`LinkedHashMap` LRU) → SD W4/W9 (drawings, thread-safe wrapper) → DSA W10 (hand-rolled HashMap + doubly linked list).

### Environment notes (company laptop)

- **W1+:** Corretto 25 for learning (work stays on JDK 11); Maven through the company JFrog. A `PKIX path building failed` error when your code calls an internet API means Java does not trust the corporate proxy's certificate: add the VM option `-Djavax.net.ssl.trustStoreType=Windows-ROOT` (Section 5 of `03_SETUP_YOUR_LAPTOP.md`).
- **W11+:** on the company laptop the container engine is **Podman** inside the company's WSL Ubuntu image (Docker isn't allowed there): `alias docker=podman`, Compose via `podman-compose`, and Testcontainers runs inside WSL with `DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock` and `TESTCONTAINERS_RYUK_DISABLED=true`. Images come through the company's mirror in JFrog. Keep the mirror prefix out of every repo: images as `${MIRROR:-}postgres:18` with `MIRROR` in a git-ignored `.env`, and `hub.image.name.prefix` in `~/.testcontainers.properties`. Not set up yet? Use a GitHub Codespace on your personal laptop.
- **W22:** `ticketverse` goes public only after a secret scan (gitleaks) and a check that no company name or hostname was ever committed.
- **W23–W24:** kubectl, kind and Helm ship with the company's WSL Ubuntu image (kind on Podman: `KIND_EXPERIMENTAL_PROVIDER=podman`); fallback: a 4-core Codespace pulling your images from GHCR, or Killercoda for plain manifests.
- **W27:** LLM calls run only in a 4-core Codespace (free LLM APIs are blocked on the company network).
- **W28:** personal Azure account work happens on the personal laptop or in a Codespace.

---

## 5. Navigation

| File / folder | Use it for |
|---|---|
| [ROADMAP.md](ROADMAP.md) | One-page view of all 30 weeks (generated) |
| [Weeks/](Weeks/) | Daily sessions (`Week-01.md` … `Week-30.md`): topic, learn, do, "Done when", self-check, stretch |
| [RESOURCES.md](RESOURCES.md) | Verified docs, courses, YouTube (English + Hindi), books, tools with versions |
| [Project_TicketVerse/PROJECT_SPEC.md](Project_TicketVerse/PROJECT_SPEC.md) | Capstone spec: domain, services, APIs, events, state machines, saga, NFRs, milestones, resume bullets |
| [INTERVIEW_QUESTION_BANK.md](INTERVIEW_QUESTION_BANK.md) | 255 high-frequency questions (⭐ = most asked) mapped to weeks |
| `Java_Track_Complete_Plan.pdf` | This folder (README, roadmap, spec, all weeks, question bank, resources) as one read-only PDF |
| `../01_Daily_Planner/` | Daily checklists across all five tracks; all weeks in one PDF: `Daily_Planner_All_30_Weeks.pdf` |
| [../00_Progress_Tracker/](../00_Progress_Tracker/) | XP, streaks, weekly test scores, weakness tracker, AI memory |

---

## 6. Rules, pitfalls & tips

**Rules**
1. **Write more than you read.** If a session had no code, it did not happen.
2. **Interview-proof every topic:** for each week answer the self-check questions aloud before Sunday.
3. **Version sanity:** JDK 25, Spring Boot 4.1.x for the whole plan (if you upgrade, move Boot, Spring Cloud and Spring AI together; Spring Cloud 2025.1.x matches Boot 4.1), JUnit 6, Testcontainers 2.0.x, Maven 3.9.x / 3.10.x via the Maven Wrapper (Maven 4 is still a release candidate — don't make it your default).
4. **Never commit secrets** (`.env` in `.gitignore`; use Key Vault/identities in Azure).

**Pitfalls to avoid**
- ⚠️ Watching 3 hours of video instead of coding 35 minutes. Video is 1.5× speed, max 15 minutes per session.
- ⚠️ IDE generating `equals/hashCode`, constructors, getters in S1 — write them by hand first; generate later.
- ⚠️ "It works on my machine" concurrency — run concurrency tests 5× in a row; flaky = broken.
- ⚠️ Spring Boot 4 surprises: starters are modular (`spring-boot-starter-webmvc`), **Jackson 3** uses `tools.jackson` packages, `@MockBean` is gone (use `@MockitoBean`), Flyway needs `spring-boot-starter-flyway`. Keep the [Boot 4.0 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide) handy when old tutorials disagree.
- ⚠️ Spring 7 traps: Spring Security 7 accepts only the lambda DSL (`oauth2ResourceServer(o -> o.jwt(Customizer.withDefaults()))`), and Spring Framework's `@Retryable` does nothing until you declare `@EnableResilientMethods`.
- ⚠️ Old tutorials: Eureka/Hystrix/Zuul, `WebSecurityConfigurerAdapter`, ingress-nginx and ZooKeeper-based Kafka are **history**. Use HTTP service clients/Resilience4j, `SecurityFilterChain` beans, **Gateway API**, and **KRaft**.
- ⚠️ Building images behind the corporate proxy: build the jar on the host and `COPY` it into `eclipse-temurin:25-jre` (or use Jib); a Maven build or Buildpacks inside the image build would fail on TLS — run the Buildpacks comparison in GitHub Actions instead.
- ⚠️ Azure costs: every cloud session ends with a verified teardown (`infra/teardown` deletes the deployment stack first, because its deny settings block a plain resource-group delete). Set budgets before creating anything.

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
