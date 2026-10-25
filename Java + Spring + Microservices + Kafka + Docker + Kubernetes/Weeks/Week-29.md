# ☕ Java Backend · Week 29 — Performance, hardening and production-ready docs

> 📅 **Mon 10 May 2027 → Sun 16 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 28](Week-28.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-29.md) · [Week 30 →](Week-30.md)

**Why this week:** Senior interviews ask 'how did you know it was fast and safe?'; load tests, profiles, OWASP fixes and clear architecture docs turn TicketVerse into evidence instead of claims.

## 🗓️ Sessions

### Monday 10 May · 60 min — Load testing with k6: scenarios, thresholds, realistic flows
- 📚 **Learn:** Load vs stress vs soak vs spike tests; open (arrival-rate) vs closed (VU) models; k6 scenarios, checks and thresholds (p95, error rate) as pass/fail; realistic test data and think time; never load-test shared or production systems without permission. k6 runs as a container (`grafana/k6` through your mirror), so there is nothing new to install. Read: [k6: Write your first test](https://grafana.com/docs/k6/latest/get-started/write-your-first-test/). Optional: [k6: Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/).
- 🛠️ **Do:** Write `perf/booking-flow.js`: get token, browse events, view a show, hold 2 random seats, book; ramp to 50 VUs over 2 minutes then a constant 20 requests/s for 3 minutes, with thresholds p95 < 400 ms and errors < 1%. Run it against the compose stack. Done when: a baseline report (RPS, p95, p99, errors, CPU/memory per service) is saved in `docs/PERFORMANCE.md`.

### Tuesday 11 May · 60 min — Profiling under load: JFR views and async-profiler flame graphs
- 📚 **Learn:** Sampling vs instrumentation; JFR recordings (CPU, allocation, locks, GC, I/O) summarized with `jfr view hot-methods` and `allocation-by-class` (W11; JMC only if IT approved it); async-profiler flame graphs for CPU, allocation and wall-clock, run inside the Linux container because it has no Windows build; typical hotspots: N+1 queries, JSON mapping, logging, lock contention. Read: [dev.java: Getting started with JFR](https://dev.java/learn/jvm/monitoring-troubleshooting/jfr/getting-started/). Optional: [async-profiler on GitHub](https://github.com/async-profiler/async-profiler).
- 🛠️ **Do:** Record a 2-minute JFR on booking-service during the k6 run (`-XX:StartFlightRecording` via `JAVA_TOOL_OPTIONS`) and summarize it with `jfr view hot-methods`; add async-profiler to the booking-service container and capture a CPU flame graph; list the top 3 hotspots with evidence; fix the biggest one (e.g. an N+1, a missing index or an over-chatty log) and re-run k6. Done when: before/after numbers for that fix are in `docs/PERFORMANCE.md` with the flame graph image.

### Wednesday 12 May · 60 min — Throughput levers: pool sizing, virtual threads, caching, query tuning
- 📚 **Learn:** Little's law; HikariCP sizing vs database cores; `spring.threads.virtual.enabled=true` helps blocking I/O but moves the bottleneck to pools and downstream services; cache hit ratio; batch inserts and projections; connection and read timeouts everywhere. Read: [Spring Boot: Task execution and scheduling (virtual threads)](https://docs.spring.io/spring-boot/reference/features/task-execution-and-scheduling.html). Optional: [HikariCP: About pool sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing).
- 🛠️ **Do:** Run 4 k6 experiments on booking-service: platform threads vs virtual threads, each with Hikari pool 10 vs 30; record RPS, p95, errors and Hikari pending-connection metrics; keep only the changes your data supports. Done when: a 4-row results table and a written recommendation (with reasons) are in `docs/PERFORMANCE.md`.

### Thursday 13 May · 60 min — Security hardening: OWASP API Top 10, rate limits, headers
- 📚 **Learn:** OWASP API Security Top 10 (2023): broken object-level authorization, broken authentication, object property-level authorization, unrestricted resource consumption, function-level authorization, sensitive business flows, SSRF, misconfiguration, inventory, unsafe API consumption; per-user rate limits at your MVC gateway with the Bucket4j RateLimiter filter (W27); security headers; dependency hygiene. Read: [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10). Optional: [Spring Cloud Gateway MVC: RateLimiter filter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc/filters/ratelimiter.html).
- 🛠️ **Do:** Audit TicketVerse against all 10 risks in a table (status, evidence, fix); write tests for BOLA on bookings and for mass assignment on event updates; add a per-user rate limit on the hold endpoint at the gateway (the assistant already has one from W27); cap page sizes and request body sizes. Done when: the audit table is in `docs/SECURITY.md` and at least 3 issues are fixed with tests.

### Friday 14 May · 60 min — Graceful shutdown, readiness, runbooks; C4 diagrams and ADRs
- 📚 **Learn:** Graceful shutdown is on by default in Spring Boot (tune `spring.lifecycle.timeout-per-shutdown-phase`); in Kubernetes it pairs with a preStop hook, the termination grace period, readiness flipping first and Kafka consumers closing cleanly; SLOs and error budgets; documentation that hiring managers read: README, C4 context and container diagrams, ADRs, runbook. Read: [Spring Boot: Graceful shutdown](https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html). Optional: [C4 model](https://c4model.com/).
- 🛠️ **Do:** Prove graceful shutdown: during a k6 run, `kubectl rollout restart` booking-service with zero failed requests. Draw C4 context and container diagrams in Mermaid, finish ADR-001..004 plus ADR-005 (your Wednesday virtual-threads decision), and define 2 SLOs (booking p95, availability). Done when: the restart shows 0 errors and the docs are linked from the README.

### Saturday 15 May · 60 min — BUILD: Performance report and polished portfolio repository
- 📚 **Learn:** What reviewers scan in 60 seconds: a one-line pitch, an architecture diagram, tech stack badges, how to run in one command, a demo video, key engineering decisions with numbers, tests and pipeline status. Read: [Grafana k6 documentation](https://grafana.com/docs/k6/latest/) (results output, for your report).
- 🛠️ **Do:** Finalize `docs/PERFORMANCE.md` (baseline vs tuned: RPS, p95, p99, errors, resource use); record a 5-minute demo video; rewrite the README top section (pitch, diagram, 'run in one command', highlights with numbers); pin the repo on your GitHub profile; tag `v2.3.0`. Done when: a friend unfamiliar with the project explains TicketVerse back to you after reading only the README for 60 seconds.

## 📦 Deliverable (by Saturday night)
k6 suite + PERFORMANCE.md (baseline vs tuned), JFR/flame-graph evidence, virtual-thread/pool experiment table, SECURITY.md (OWASP API Top 10 audit + fixes), graceful-shutdown proof, C4 diagrams, ADR-001..005, polished README + demo video, `v2.3.0`.

## ✅ Self-check (Sunday test preview)
- Load vs stress vs soak testing: what does each tell you?
- How do you find a CPU hotspot in a running Spring Boot service with only JDK tools?
- When do virtual threads improve throughput, and when do they just move the bottleneck?
- How do you size a database connection pool?
- What is BOLA and how did you test for it?
- How does graceful shutdown work in Kubernetes for a Spring Boot app?
- What would you put on a one-page architecture overview for an interviewer?

## 🚀 Stretch (optional)
If you redeploy to Azure for a final demo, repeat the k6 run there for 5 minutes (watch the budget) and compare cloud vs local numbers.
