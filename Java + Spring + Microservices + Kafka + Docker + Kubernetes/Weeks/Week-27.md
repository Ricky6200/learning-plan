# ☕ Java Backend · Week 27 — Platform hooks for ticketverse-ai: gateway, events, resilience

> 📅 **Mon 26 Apr 2027 → Sun 02 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 26](Week-26.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-27.md) · [Week 28 →](Week-28.md)

**Why this week:** Java + AI roles want engineers who can plug an AI service into a real platform safely: routing and auth, events, deployment values, timeouts and fallbacks. The AI track owns `ticketverse-ai` (built in AI W23-W24, extended in AI W27); this week you own everything around it. LLM calls run only in your 4-core Codespace.

## 🗓️ Sessions

### Monday 26 Apr · 60 min — Gateway route, JWT pass-through, timeouts and rate limits for /ai/**
- 📚 **Learn:** `ticketverse-ai` joins the platform behind the gateway with a route for `/ai/**`; the caller's bearer token passes through unchanged (the `TokenRelay` filter is only for gateways that log users in with OAuth2 login), so ticketverse-ai and booking validate the same JWT; LLM calls are slow, so the route needs a longer read timeout (streaming) and a per-user Bucket4j rate limit that returns 429. Read: [Spring Cloud Gateway MVC: RateLimiter filter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc/filters/ratelimiter.html). Optional: [Spring Cloud Gateway MVC: TokenRelay filter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc/filters/tokenrelay.html).
- 🛠️ **Do:** In a 4-core Codespace (LLM calls only run there), add the AI track's `ticketverse-ai` image to compose; add a gateway route `/ai/**` -> ticketverse-ai with a 30 s read timeout and a per-user limit of 10 requests per minute on `/ai/assistant/**` (429 ProblemDetail); confirm booking-service accepts the user JWT that ticketverse-ai forwards (same issuer and audience). Done when: an authenticated `/ai/hello` call works through the gateway, an anonymous one gets 401, and the 11th assistant call in a minute gets 429.

### Tuesday 27 Apr · 60 min — Resilience4j around AI calls: time limit, breaker, degraded fallback
- 📚 **Learn:** LLM calls are slow, flaky and metered: wrap the platform's calls to `ticketverse-ai` in a time limit, a circuit breaker and a bulkhead (W19) and degrade instead of failing: when AI search is down, fall back to catalog's Specifications search (W25); never blindly retry an expensive or non-idempotent AI call. The gateway's CircuitBreaker filter (Spring Cloud CircuitBreaker + Resilience4j) can forward to a fallback route. Read: [Spring Cloud Gateway MVC: CircuitBreaker filter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc/filters/circuitbreaker-filter.html). Optional: [Resilience4j: CircuitBreaker](https://resilience4j.readme.io/docs/circuitbreaker).
- 🛠️ **Do:** Add a CircuitBreaker filter to the `/ai/search` route (AI W27 Mon) with a fallback that forwards to catalog's `GET /api/events/search`, plus a 3 s time limit and a bulkhead of 10 concurrent AI calls; stop the ticketverse-ai container and show search still answering (degraded) and the breaker opening, then recovering after a restart. Done when: with AI down, search returns results within 1 s and the circuit-breaker states are recorded in `docs/ai-integration.md`.

### Wednesday 28 Apr · 60 min — Kafka topics and event contracts for AI consumers
- 📚 **Learn:** Topic ownership: catalog owns `catalog.shows.v1` and `catalog.reviews.v1` (W25), and `ticketverse-ai` is just another consumer group with its own offsets; create shared topics explicitly (partitions, compaction for shows, 7-day retention for reviews) instead of relying on auto-create; the contract is the documented schema plus compatibility rules (W20 Fri); new consumers backfill from the compacted topic or a republish endpoint; watch consumer lag. Read: [Spring Kafka: Configuring topics](https://docs.spring.io/spring-kafka/reference/kafka/configuring-topics.html). Optional: [Kafka 4.3: Topic configs](https://kafka.apache.org/43/configuration/topic-configs/).
- 🛠️ **Do:** Declare both topics as `NewTopic` beans in catalog-service (3 partitions; compact for shows; 7-day retention for reviews); add a contract test asserting the event JSON matches `docs/events.md` (fields and `eventVersion`); add an admin-only `POST /internal/catalog/republish` that re-emits every show; check ticketverse-ai's group with `kafka-consumer-groups.sh --describe`. Done when: a fresh ticketverse-ai consumer group indexes all shows after one republish and its lag returns to 0.

### Thursday 29 Apr · 60 min — Helm values and traces for ticketverse-ai
- 📚 **Learn:** Ship the AI service like the others: Helm values for image, resources (AI pods need more memory), env per profile and a Kubernetes Secret for the model API key, never the key itself in values files; readiness should not depend on the model provider being up; Spring AI emits `gen_ai` observations, so with OpenTelemetry one trace can show gateway -> ticketverse-ai -> model -> booking. Read: [Helm: Values files](https://helm.sh/docs/chart_template_guide/values_files/). Optional: [Spring AI: Observability](https://docs.spring.io/spring-ai/reference/observability/index.html).
- 🛠️ **Do:** Add `ticketverse-ai` to `charts/ticketverse` (image from GHCR, 1 Gi memory limit, `SPRING_PROFILES_ACTIVE=cloud`, the API key from a Secret created with `kubectl create secret`); deploy to kind in the Codespace; make one assistant call and find its trace in Jaeger with model and tool spans. Done when: `helm upgrade --install` brings ticketverse-ai to Ready, `helm get values` shows no key, and the trace shows every hop.

### Friday 30 Apr · 60 min — Awareness: WebFlux and Reactor, gRPC and GraphQL
- 📚 **Learn:** Reactive = non-blocking with backpressure: `Mono` (0..1) and `Flux` (0..n), operators (`map`, `flatMap`, `zip`, `timeout`), nothing runs until you subscribe; WebFlux suits streaming (LLM tokens over SSE) and very high concurrency, but virtual threads (W9) give MVC most of that scalability with simpler code. gRPC: Protobuf contracts over HTTP/2 for fast internal calls; GraphQL: client-shaped queries for UIs. Read: [Reactor reference: Introduction to reactive programming](https://projectreactor.io/docs/core/release/reference/reactiveProgramming.html). Optional: [Spring for GraphQL reference](https://docs.spring.io/spring-graphql/reference/).
- 🛠️ **Do:** In a scratch module: `Flux.interval` + `take(5)` + `map`, and `Mono.zip` of two delayed calls with `timeout`, each verified by a `StepVerifier` test; a WebFlux `GET /stream` returning server-sent ticks (like token streaming) watched with `curl -N`. Write `docs/adr/ADR-004-api-styles.md` choosing REST, gRPC, GraphQL or reactive for 4 TicketVerse cases. Done when: 3 StepVerifier tests pass and the ADR gives one style per case with a reason.

### Saturday 01 May · 60 min — BUILD: Joint end-to-end test with the AI track
- 📚 **Learn:** Joint definition of done with AI W27 Sat: search -> ask -> propose -> confirm -> booked, plus a new review that refreshes the AI summary. You own the platform checks (auth, rate limits, events, traces, fallbacks); the AI track owns answer quality. Poll for eventual results instead of fixed sleeps, run everything in the 4-core Codespace, then stop it. Read: [Martin Fowler: Testing strategies in a microservice architecture](https://martinfowler.com/articles/microservice-testing/) (end-to-end tests section).
- 🛠️ **Do:** Extend your smoke script into `scripts/e2e-ai`: get a user token, call `/ai/search`, let the assistant propose seats, confirm through the normal booking API with an idempotency key, post a review and poll until the review summary changes, then stop ticketverse-ai and show search degrading gracefully. Done when: the script passes twice on a fresh Codespace stack, both tracks reference the same commit, and the Codespace is stopped.

## 📦 Deliverable (by Saturday night)
Gateway route + rate limit for `/ai/**` with JWT pass-through, circuit breaker + bulkhead + degraded search fallback, explicit catalog topics with contract tests and a republish endpoint, ticketverse-ai in the Helm chart with secrets and traces, ADR-004 on API styles with StepVerifier tests, a joint `scripts/e2e-ai` run with the AI track.

## ✅ Self-check (Sunday test preview)
- How does the user's identity travel from the gateway through ticketverse-ai to booking-service?
- TokenRelay vs simply forwarding the bearer header: when do you need each?
- Which resilience patterns did you put around AI calls, and what does the degraded experience look like?
- Why create shared topics explicitly, and how does a brand-new consumer backfill?
- How do you keep model API keys out of Helm values and Git?
- Mono vs Flux; when does WebFlux beat MVC with virtual threads?
- REST vs gRPC vs GraphQL: one TicketVerse use case each.

## 🚀 Stretch (optional)
Prototype a gRPC `SeatAvailability` service with [Spring gRPC](https://docs.spring.io/spring-grpc/reference/) and compare latency with REST; add a GraphQL `events` query with Spring for GraphQL; rebuild `/stream` with Spring MVC + `SseEmitter` on virtual threads and compare the code.
