# ☕ Java Backend · Week 18 — Microservices split: extract, secure, contract-test

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** Splitting a running system safely, step by step, with service-to-service auth and contract tests is what real migrations look like, and it gives you the strongest 'tell me about a hard refactor' interview story.

## 🗓️ Sessions

### Monday 22 Feb · 60 min — Split 1: multi-module build, extract catalog-service
- 📚 **Learn:** Strangler-fig extraction: (1) make the repo a Maven parent with modules, (2) move the catalog package and its Flyway migrations into `catalog-service` with its own database, (3) flip the gateway route, (4) delete the old code; public URLs stay the same. Run one module with `./mvnw -pl catalog-service -am spring-boot:run`. Read: [Baeldung: Multi-module project](https://www.baeldung.com/maven-multi-module) (you met it in W7 Fri). Optional: [Martin Fowler: Strangler fig application](https://martinfowler.com/bliki/StranglerFigApplication.html).
- 🛠️ **Do:** Create the parent POM (Boot 4.1 BOM, modules `monolith`, `gateway`, `catalog-service`); move catalog entities, repositories, controllers and migrations into `catalog-service` (port 8081, database `catalog`); point the gateway's `/api/events/**` and `/api/venues/**` routes at it; delete catalog code from the monolith. Done when: `./mvnw -B verify` builds every module and the smoke script passes through the gateway with catalog served by the new service.

### Tuesday 23 Feb · 60 min — Split 2: booking-service, a common contracts module, ArchUnit
- 📚 **Learn:** A shared module holds only contracts (request/response and event records), never entities or repositories, because shared code couples deployments; booking keeps a snapshot of the show data it needs instead of joining catalog tables. ArchUnit turns architecture rules into JUnit tests, e.g. `noClasses().that().resideInAPackage("..booking..").should().dependOnClassesThat().resideInAPackage("..catalog..")`. Read: [ArchUnit: Getting started](https://www.archunit.org/getting-started). Optional: [ArchUnit user guide](https://www.archunit.org/userguide/html/000_Index.html).
- 🛠️ **Do:** Rename `monolith` to `booking-service` (database `booking`: show_seat, booking, booking_seat; holds stay in Redis); move shared records into `common`; booking reads show data only via `CatalogClient` (W17). Add 3 ArchUnit tests: no `@Entity` in `common`, `common` depends on no service package, booking-service has no class from a `..catalog..` package. Done when: all modules build, the ArchUnit tests pass, and deliberately breaking a rule makes a test fail.

### Wednesday 24 Feb · 60 min — Split 3: payment-mock and notification skeletons
- 📚 **Learn:** Skeleton services first: a health endpoint, one API, a Dockerfile, a compose entry and a gateway route only if public. Payment is a mock whose behaviour you control (success, decline or a 3 s delay, used in W19's chaos tests); notification will consume Kafka events in W21, so today it only exposes an internal endpoint and logs. Read: [microservices.io: Decompose by business capability](https://microservices.io/patterns/decomposition/decompose-by-business-capability.html). Optional: [Spring Boot: Actuator endpoints](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html).
- 🛠️ **Do:** Add modules `payment-service` (`POST /api/payments` returns 200, 402 or a 3 s delay based on an `X-Mock-Mode` header) and `notification-service` (`POST /internal/notify` logs a fake email). booking-service calls payment through a `PaymentClient` with a 2 s timeout when a booking is confirmed: success -> CONFIRMED, decline -> CANCELLED with seats released. Done when: a booking through the gateway ends CONFIRMED or CANCELLED depending on the header and all 5 services start with `spring-boot:run`.

### Thursday 25 Feb · 60 min — Service-to-service auth: OAuth2 client credentials
- 📚 **Learn:** Users get tokens via authorization code + PKCE (W16); services get their own via client credentials: booking-service is a confidential Keycloak client, Spring Security's OAuth2 client fetches and caches its token, and `OAuth2ClientHttpRequestInterceptor` adds it to `RestClient` calls; payment-service requires a service role such as `payments:write`, not a user role. Read: [Spring Security: Authorized clients (RestClient integration)](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html). Optional: [OAuth.net: Client credentials](https://oauth.net/2/grant-types/client-credentials/).
- 🛠️ **Do:** In Keycloak create confidential client `booking-service` with a service account and client role `payments:write`; configure `spring.security.oauth2.client.registration.booking` with `authorization-grant-type: client_credentials`; add the interceptor to `PaymentClient`'s RestClient; payment-service requires that role. Done when: booking -> payment works, a call without a token gets 401 and a call with a normal user token gets 403.

### Friday 26 Feb · 60 min — Consumer-driven contract tests between booking and catalog
- 📚 **Learn:** Consumer-driven contracts: the consumer (booking) states what it needs from the provider (catalog) and the provider's build verifies it, so a breaking change fails CI before deployment. Spring Cloud Contract turns YAML/Groovy contracts into generated provider tests plus a stub jar that the consumer runs with the Stub Runner; Pact is the polyglot alternative. Read: [Spring Cloud Contract: Introduction](https://docs.spring.io/spring-cloud-contract/reference/getting-started/introducing-spring-cloud-contract.html). Optional: [Martin Fowler: Consumer-driven contracts](https://martinfowler.com/articles/consumerDrivenContracts.html).
- 🛠️ **Do:** In catalog-service add the Spring Cloud Contract verifier plugin and 2 YAML contracts for `GET /api/shows/{id}` (200 and 404) with a base test class; `./mvnw install` generates provider tests and a stub jar; in booking-service run the `CatalogClient` tests against the stub with `@AutoConfigureStubRunner` (local stubs mode). Then rename a response field in catalog and watch the provider build fail. Done when: contract tests pass on both sides and the rename breaks the build.

### Saturday 27 Feb · 60 min — BUILD: Five services with Compose and a smoke test
- 📚 **Learn:** Compose for many services: one Postgres with two databases (an init script), Redis, Keycloak and five Spring services, healthchecks and `depends_on`, env vars per service; images = jar built on the host + `COPY` into `eclipse-temurin:25-jre` (optimized images come in W22); a smoke script that proves the whole flow through the gateway. Read: [Docker: Compose services reference](https://docs.docker.com/reference/compose-file/services/). Optional: [Docker: Compose quickstart](https://docs.docker.com/compose/gettingstarted/).
- 🛠️ **Do:** Write `compose.yaml` for gateway, catalog, booking, payment-mock and notification plus Postgres (`catalog` and `booking` databases), Redis and Keycloak; extend the smoke script: get a user token, list shows via the gateway, hold and book seats once with payment success and once with a decline. Update the README container diagram. Done when: `docker compose up` followed by the smoke script passes from a clean state and `v1.1.0` is tagged.

## 📦 Deliverable (by Saturday night)
Multi-module `ticketverse`: gateway + catalog, booking, payment-mock and notification services + `common` contracts; separate catalog and booking databases; client-credentials calls booking -> payment; Spring Cloud Contract tests catalog <-> booking; ArchUnit rules; 5-service compose + smoke script, tag `v1.1.0`.

## ✅ Self-check (Sunday test preview)
- Walk through the strangler-fig steps you used to extract catalog-service. What stayed the same for clients?
- What belongs in a shared `common` module, and what must never go there?
- How does booking-service get show data without sharing catalog's database?
- Client credentials vs authorization code + PKCE: who uses which, and how is the service token cached?
- What does a consumer-driven contract test catch that an integration test might not?
- Which ArchUnit rules did you write, and what bug would each one prevent?
- Why does payment-service require a service role instead of accepting any valid user token?

## 🚀 Stretch (optional)
Write a contract for the payment API with booking as the consumer; compare Pact with Spring Cloud Contract in 10 lines; build only what changed with `./mvnw -pl booking-service -am verify`; add an ArchUnit rule that controllers never call repositories directly.
