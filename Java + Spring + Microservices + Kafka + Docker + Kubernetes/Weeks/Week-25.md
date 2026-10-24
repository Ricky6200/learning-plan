# ☕ Java Backend · Week 25 — Performance, hardening and production-ready docs

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** Senior interviews ask 'how did you know it was fast and safe?'; load tests, profiles, OWASP fixes and clear architecture docs turn TicketVerse into evidence instead of claims.

## 🗓️ Sessions

### Monday 12 Apr · 60 min — Load testing with k6: scenarios, thresholds, realistic flows
- 📚 **Learn:** Load vs stress vs soak vs spike tests; open (arrival-rate) vs closed (VU) models; k6 scenarios, checks and thresholds (p95, error rate) as pass/fail; realistic test data and think time; never load-test shared or production systems without permission. [k6: Write your first test](https://grafana.com/docs/k6/latest/get-started/write-your-first-test/), [k6: Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/), [k6: Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/).
- 🛠️ **Do:** Write `perf/booking-flow.js`: get token, browse events, view a show, hold 2 random seats, book; ramp to 50 VUs over 2 minutes then a constant 20 requests/s for 3 minutes, with thresholds p95 < 400 ms and errors < 1%. Run it against the compose stack. Done when: a baseline report (RPS, p95, p99, errors, CPU/memory per service) is saved in `docs/PERFORMANCE.md`.

### Tuesday 13 Apr · 60 min — Profiling under load: JFR, JMC, async-profiler flame graphs
- 📚 **Learn:** Sampling vs instrumentation; JFR recordings (CPU, allocation, locks, GC, I/O) and JDK Mission Control; async-profiler flame graphs for CPU, allocation and wall-clock; finding hotspots such as N+1 queries, JSON mapping, logging, lock contention. [dev.java: Getting started with JFR](https://dev.java/learn/jvm/monitoring-troubleshooting/jfr/getting-started/), [async-profiler on GitHub](https://github.com/async-profiler/async-profiler), [Baeldung: Monitoring with Flight Recorder](https://www.baeldung.com/java-flight-recorder-monitoring).
- 🛠️ **Do:** Record a 2-minute JFR on booking-service during the k6 run and an async-profiler CPU flame graph; list the top 3 hotspots with evidence; fix the biggest one (e.g., an N+1, a missing index or an over-chatty log) and re-run k6. Done when: before/after numbers for that fix are in `docs/PERFORMANCE.md` with the flame graph images.

### Wednesday 14 Apr · 60 min — Throughput levers: pool sizing, virtual threads, caching, query tuning
- 📚 **Learn:** Little's law; HikariCP sizing vs database cores; `spring.threads.virtual.enabled=true` helps blocking I/O but moves the bottleneck to pools and downstream services; cache hit ratio; batch inserts and projections; connection and read timeouts everywhere. [Spring Boot: Task execution (virtual threads)](https://docs.spring.io/spring-boot/reference/features/task-execution-and-scheduling.html), [Vlad Mihalcea: Maximum database connections](https://vladmihalcea.com/maximum-database-connections/), [HikariCP: About pool sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing).
- 🛠️ **Do:** Run 4 k6 experiments on booking-service: platform threads vs virtual threads, each with Hikari pool 10 vs 30; record RPS, p95, errors and Hikari pending-connection metrics; keep only the changes your data supports. Done when: a 4-row results table and a written recommendation (with reasons) are in `docs/PERFORMANCE.md`.

### Thursday 15 Apr · 60 min — Security hardening: OWASP API Top 10, rate limits, headers
- 📚 **Learn:** OWASP API Security Top 10 (2023): broken object-level authorization, broken authentication, object property-level authorization, unrestricted resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory, unsafe API consumption; gateway rate limiting; security headers; dependency hygiene. [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10), [OWASP: REST security cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [Spring Cloud Gateway: RequestRateLimiter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webflux/gatewayfilter-factories/requestratelimiter-factory.html).
- 🛠️ **Do:** Audit TicketVerse against all 10 risks in a table (status, evidence, fix); write tests for BOLA on bookings and for mass assignment on event updates; add per-user rate limits on hold and assistant endpoints at the gateway; cap page sizes and request body sizes. Done when: the audit table is in `docs/SECURITY.md` and at least 3 issues are fixed with tests.

### Friday 16 Apr · 60 min — Graceful shutdown, readiness, runbooks; C4 diagrams and ADRs
- 📚 **Learn:** Graceful shutdown (`server.shutdown=graceful`, Kubernetes preStop and termination grace period, readiness flips first, Kafka consumers close cleanly); SLOs and error budgets; documentation that hiring managers read: README, C4 context and container diagrams, ADRs, runbook. [Spring Boot: Graceful shutdown](https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html), [C4 model](https://c4model.com/), [ADR GitHub organization](https://adr.github.io/).
- 🛠️ **Do:** Enable graceful shutdown on all services and prove it: during a k6 run, `kubectl rollout restart` booking-service with zero failed requests. Draw C4 context and container diagrams in Mermaid, finish ADR-001..004 (+ ADR-005 virtual threads decision), and define 2 SLOs (booking p95, availability). Done when: the restart shows 0 errors and docs are linked from the README.

### Saturday 17 Apr · 60 min — BUILD: Performance report and polished portfolio repository
- 📚 **Learn:** What reviewers scan in 60 seconds: one-line pitch, architecture diagram, tech stack badges, how to run in one command, demo video, key engineering decisions with numbers, tests and pipeline status. [Grafana k6 documentation](https://grafana.com/docs/k6/latest/), [Spring Boot: Graceful shutdown](https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html).
- 🛠️ **Do:** Finalize `docs/PERFORMANCE.md` (baseline vs tuned: RPS, p95, p99, errors, resource use); record a 5-minute demo video; rewrite the README top section (pitch, diagram, 'run in one command', highlights with numbers); pin the repo on your GitHub profile; tag `v7.0.0`. Done when: a friend unfamiliar with the project explains TicketVerse back to you after reading only the README for 60 seconds.

## 📦 Deliverable (by Saturday night)
k6 suite + PERFORMANCE.md (baseline vs tuned), JFR/flame-graph evidence, virtual-thread/pool experiment table, SECURITY.md (OWASP API Top 10 audit + fixes), graceful-shutdown proof, C4 diagrams, ADRs, polished README + demo video, `v7.0.0`.

## ✅ Self-check (Sunday test preview)
- Load vs stress vs soak testing: what does each tell you?
- How do you find a CPU hotspot in a running Spring Boot service?
- When do virtual threads improve throughput, and when do they just move the bottleneck?
- How do you size a database connection pool?
- What is BOLA and how did you test for it?
- How does graceful shutdown work in Kubernetes for a Spring Boot app?
- What would you put on a one-page architecture overview for an interviewer?

## 🚀 Stretch (optional)
Repeat the k6 run against your Azure deployment for 5 minutes (watch the budget) and compare cloud vs local numbers.
