# ☕ Java Backend · Week 17 — Microservices: DDD boundaries, gateway, service calls

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Interviewers test judgement: when to split, how to draw boundaries and how services talk. This week you design the split and put a gateway in front of the monolith; next week you extract the services one by one.

## 🗓️ Sessions

### Monday 15 Feb · 60 min — Monolith vs microservices trade-offs; DDD bounded contexts and aggregates
- 📚 **Learn:** Benefits (independent deploy/scale, team autonomy) vs costs (network failures, distributed data, ops); monolith-first and the modular monolith; DDD: ubiquitous language, bounded contexts, aggregates as consistency boundaries, context maps. Read: [Martin Fowler: Microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html). Optional: [Martin Fowler: Bounded context](https://martinfowler.com/bliki/BoundedContext.html).
- 🛠️ **Do:** Write `docs/adr/ADR-001-split-into-services.md` (context, options, decision, consequences) and a Mermaid context map: Catalog, Booking, Payment, Notification, Identity (Keycloak). Name each aggregate and its invariant (e.g., a Booking's seats belong to one show). Reorganize the monolith's packages by context (`catalog`, `booking`, ...). Done when: the ADR and map are committed and every class lives in exactly one context package.

### Tuesday 16 Feb · 60 min — Decomposition, database-per-service, sync vs async, strangler fig
- 📚 **Learn:** Decompose by subdomain/business capability; database-per-service and why shared databases couple teams; duplicating read data (booking keeps show/seat snapshots); sync REST for queries vs async events for state changes; API composition; the strangler fig: put a facade in front and move features out one at a time. Read: [microservices.io: Database per service](https://microservices.io/patterns/data/database-per-service.html). Optional: [Martin Fowler: Strangler fig application](https://martinfowler.com/bliki/StranglerFigApplication.html).
- 🛠️ **Do:** Write `docs/split-plan.md`: a table giving every table one owning service (catalog, booking, payment, notification), the snapshot fields booking copies from catalog, each cross-context interaction marked sync or async with a reason, and the 3 extraction steps for W18 (catalog; booking + common; payment and notification). Done when: no table has two owners and every cross-context call in the code is listed.

### Wednesday 17 Feb · 60 min — Spring Cloud Gateway in front of the monolith: routes, filters
- 📚 **Learn:** API gateway responsibilities (routing, auth at the edge, rate limiting, CORS, request IDs) vs BFF; Spring Cloud Gateway Server Web MVC (blocking, fits your MVC stack) vs the WebFlux variant; routes, predicates and filters; validate the JWT at the edge and pass it downstream. Use the Spring Cloud 2025.1.x BOM, which matches Boot 4.1.x. Read: [Spring Cloud Gateway: Server Web MVC](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc.html). Optional: [microservices.io: API gateway](https://microservices.io/patterns/apigateway.html).
- 🛠️ **Do:** Create a separate Boot app `gateway/` (its own POM for now; W18 makes the repo multi-module) routing `/api/**` to the monolith, so public URLs never change during the split; add a filter that sets `X-Request-Id` when missing and log it via MDC in the monolith (W12); validate the JWT at the gateway and keep resource-server checks in the app (defense in depth). Done when: all smoke calls work through the gateway port only and the same request id appears in both logs.

### Thursday 18 Feb · 60 min — Service discovery and configuration: Kubernetes DNS vs Eureka
- 📚 **Learn:** Client-side discovery (Eureka + load-balanced clients) vs server-side discovery (Kubernetes Services/DNS, which TicketVerse will use); externalized configuration via env vars, profiles and config trees; 12-factor config; health endpoints as readiness signals. Read: [Spring Boot: Externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html). Optional: [microservices.io: Server-side discovery](https://microservices.io/patterns/server-side-discovery.html).
- 🛠️ **Do:** Move every URL, credential and tunable into env vars with safe local defaults; in compose, services find each other by service name (DNS); add liveness/readiness health groups; write a 10-line comparison of Eureka vs Kubernetes DNS for TicketVerse in `docs/adr/ADR-002-discovery.md`. Done when: no hard-coded host or password remains (grep proves it).

### Friday 19 Feb · 60 min — Inter-service calls: HTTP interface clients, timeouts, OpenFeign awareness
- 📚 **Learn:** `@HttpExchange` service clients on `RestClient`; connect/read timeouts on every call; mapping remote errors to your own exceptions; testing with `MockRestServiceServer`; OpenFeign is feature-complete, so new code prefers HTTP service clients; service-to-service tokens arrive in W18. Read: [Spring: REST clients](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html) (HTTP service client section). Optional: [Baeldung: HTTP interface in Spring](https://www.baeldung.com/spring-6-http-interface).
- 🛠️ **Do:** Inside the monolith, make booking read show data only through a `CatalogClient` `@HttpExchange` interface (`getShow`, `getSeats`) on `RestClient` with 2 s timeouts, calling the catalog API over HTTP even though it is the same app; map 404 to `ShowNotFoundException`. Test with `MockRestServiceServer`: 200, 404, and a timeout (`withException(new SocketTimeoutException())`). Done when: the 3 client tests pass and booking code no longer imports catalog repositories.

### Saturday 20 Feb · 60 min — BUILD: Strangler-ready monolith behind the gateway
- 📚 **Learn:** A modular monolith is one deployable with a package per bounded context, cross-context calls only through clients or events, and each context owning its tables; that makes next week's extraction a move, not a rewrite. Images: jar built on the host + `COPY` into `eclipse-temurin:25-jre` (W11). Read: [Martin Fowler: Monolith first](https://martinfowler.com/bliki/MonolithFirst.html). Optional: [Spring Modulith reference](https://docs.spring.io/spring-modulith/reference/).
- 🛠️ **Do:** Update `compose.yaml`: Postgres, Redis, Keycloak, the monolith and the gateway (images built W11-style); write `scripts/smoke.ps1` (or `.sh`) that gets a token, lists shows via the gateway, holds and books seats; update the README container diagram. Done when: `docker compose up` followed by the smoke script passes from a clean state and nothing reaches the monolith except through the gateway.

## 📦 Deliverable (by Saturday night)
ADR-001/002, context map and `docs/split-plan.md`; Spring Cloud Gateway (MVC) in front of the modular monolith with request ids and edge JWT checks; env-based config + health groups; `CatalogClient` HTTP interface with timeouts and tests; compose stack + smoke script.

## ✅ Self-check (Sunday test preview)
- When would you NOT split a monolith into microservices?
- What is a bounded context, and how did you draw TicketVerse's boundaries?
- Why database-per-service, and how do you query data owned by another service?
- What does an API gateway do, and what should it NOT do?
- What is the strangler fig pattern, and why put the gateway in front of the monolith first?
- Client-side vs server-side discovery: which does Kubernetes give you?
- Why must every remote call have a timeout? What happens without one?

## 🚀 Stretch (optional)
Watch one video from [Java Brains: Microservices Level 1](https://www.youtube.com/playlist?list=PLqq-6Pq4lTTZSKAFG6aCDVDP86Qx4lNas) and note what has changed since the Eureka/Hystrix era. Extra: run Spring Modulith's `ApplicationModules.of(App.class).verify()` on the monolith and compare its findings with your split plan.
