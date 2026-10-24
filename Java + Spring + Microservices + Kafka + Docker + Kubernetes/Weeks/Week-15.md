# ☕ Java Backend · Week 15 — Microservices: DDD boundaries, gateway, service calls

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** Interviewers test judgement: when to split, how to draw boundaries, and how services talk. Splitting TicketVerse yourself gives you real trade-off stories.

## 🗓️ Sessions

### Monday 01 Feb · 60 min — Monolith vs microservices trade-offs; DDD bounded contexts and aggregates
- 📚 **Learn:** Benefits (independent deploy/scale, team autonomy) vs costs (network failures, distributed data, ops); monolith-first and modular monolith; DDD: ubiquitous language, bounded contexts, aggregates as consistency boundaries, context maps. [Martin Fowler: Microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html), [Martin Fowler: Bounded context](https://martinfowler.com/bliki/BoundedContext.html), [Martin Fowler: DDD aggregate](https://martinfowler.com/bliki/DDD_Aggregate.html).
- 🛠️ **Do:** Write `docs/adr/ADR-001-split-into-services.md` (context, options, decision, consequences) and a Mermaid context map: Catalog, Booking, Payment, Notification, Identity (Keycloak). Name each aggregate and its invariant (e.g., a Booking's seats belong to one show). Reorganize monolith packages by context and add a test that fails if booking code imports catalog repositories. Done when: ADR, map and boundary test are committed.

### Tuesday 02 Feb · 60 min — Decomposition, database-per-service, sync vs async communication
- 📚 **Learn:** Decompose by subdomain/business capability; database-per-service and why shared databases couple teams; duplicating read data (booking keeps show/seat snapshots); sync REST for queries vs async events for state changes; API composition. [microservices.io: Decompose by subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html), [microservices.io: Database per service](https://microservices.io/patterns/data/database-per-service.html), [Concept && Coding: Microservices playlist (Hindi)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c60yO3LbjYkpKikwgAZHAT5o).
- 🛠️ **Do:** Restructure `ticketverse` as a Maven multi-module repo: `catalog-service`, `booking-service`, `payment-service` (mock), `notification-service`, `gateway`, `common` (only DTO contracts). Give catalog and booking separate databases (two Postgres DBs in compose) with their own Flyway history. Done when: each service starts alone with `spring-boot:run` and owns its schema.

### Wednesday 03 Feb · 60 min — Spring Cloud Gateway: routes, predicates, filters, token relay
- 📚 **Learn:** API gateway responsibilities (routing, auth at the edge, rate limiting, CORS, request IDs) vs BFF; Spring Cloud Gateway Server Web MVC vs WebFlux variants; route predicates and filters; validating JWT at the edge and relaying it downstream. [microservices.io: API gateway](https://microservices.io/patterns/apigateway.html), [Spring Cloud Gateway: Server Web MVC](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc.html), [Spring Guide: Building a gateway](https://spring.io/guides/gs/gateway/).
- 🛠️ **Do:** Configure `gateway` routes that keep public paths unchanged: `/api/events/**`, `/api/venues/**` -> catalog-service; `/api/shows/*/seats`, `/api/shows/*/holds`, `/api/holds/**`, `/api/bookings/**` -> booking-service; add a filter that sets `X-Request-Id` when missing; validate JWT at the gateway and keep resource-server checks in services (defense in depth). Done when: all calls work through the gateway port only and the request id appears in both services' logs.

### Thursday 04 Feb · 60 min — Service discovery and configuration: Kubernetes DNS vs Eureka
- 📚 **Learn:** Client-side discovery (Eureka + load-balanced clients) vs server-side discovery (Kubernetes Services/DNS, which TicketVerse will use); externalized configuration via env vars, profiles and config trees; 12-factor config; health endpoints as readiness signals. [microservices.io: Server-side discovery](https://microservices.io/patterns/server-side-discovery.html), [microservices.io: Externalized configuration](https://microservices.io/patterns/externalized-configuration.html), [Spring Boot: Externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html).
- 🛠️ **Do:** Move every URL, credential and tunable into env vars with safe local defaults; in compose, services find each other by service name (DNS); add liveness/readiness health groups; write a 10-line comparison of Eureka vs Kubernetes DNS for TicketVerse in `docs/adr/ADR-002-discovery.md`. Done when: no hard-coded host or password remains (grep proves it).

### Friday 05 Feb · 60 min — Inter-service calls: HTTP interface clients, timeouts, OpenFeign awareness
- 📚 **Learn:** `@HttpExchange` service clients on `RestClient`; connect/read timeouts on every call; mapping remote errors to your own exceptions; service-to-service auth with client-credentials tokens; OpenFeign is feature-complete, so new code prefers HTTP service clients. [Spring: REST clients](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html), [Spring Cloud OpenFeign features](https://docs.spring.io/spring-cloud-openfeign/reference/spring-cloud-openfeign.html), [Baeldung: HTTP interface in Spring](https://www.baeldung.com/spring-6-http-interface).
- 🛠️ **Do:** booking-service calls catalog-service through a `CatalogClient` (`getShow`, `getSeats`) with a 2 s timeout and a client-credentials token; payment-service mock returns success, failure or a 3 s delay based on a header. Write tests with `MockRestServiceServer` for 200, 404 -> `ShowNotFoundException`, and timeout. Done when: the 3 client tests pass and a real call works through compose.

### Saturday 06 Feb · 60 min — BUILD: Split TicketVerse into five services with compose
- 📚 **Learn:** Compose layout for many services: one Postgres with two databases, Redis, Keycloak, five Spring services, healthchecks and `depends_on`; smoke-test script; Boot-built images via `spring-boot:build-image` for now (Dockerfiles come in W19). [Docker Docs: Compose quickstart](https://docs.docker.com/compose/gettingstarted/), [Spring Boot: Buildpacks](https://docs.spring.io/spring-boot/reference/packaging/container-images/cloud-native-buildpacks.html).
- 🛠️ **Do:** Build images, write `compose.yaml` for gateway, catalog, booking, payment-mock, notification + Postgres, Redis, Keycloak; a `scripts/smoke.sh` (or `.ps1`) gets a token, lists shows via the gateway, holds and books seats. Done when: `docker compose up` followed by the smoke script passes from a clean state and the README has an updated container diagram.

## 📦 Deliverable (by Saturday night)
TicketVerse multi-module repo with 5 services + gateway, separate databases, env-based config, HTTP interface clients with timeouts, ADR-001/002, compose stack and smoke script.

## ✅ Self-check (Sunday test preview)
- When would you NOT split a monolith into microservices?
- What is a bounded context, and how did you draw TicketVerse's boundaries?
- Why database-per-service, and how do you query data owned by another service?
- What does an API gateway do, and what should it NOT do?
- Client-side vs server-side discovery: which does Kubernetes give you?
- Why must every remote call have a timeout? What happens without one?
- HTTP service clients vs OpenFeign: what would you choose for new code and why?

## 🚀 Stretch (optional)
Watch one video from [Java Brains: Microservices Level 1](https://www.youtube.com/playlist?list=PLqq-6Pq4lTTZSKAFG6aCDVDP86Qx4lNas) and note what has changed since the Eureka/Hystrix era.
