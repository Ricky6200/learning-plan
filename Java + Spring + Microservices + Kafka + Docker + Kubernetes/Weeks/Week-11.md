# ☕ Java Backend · Week 11 — Spring Boot internals, REST APIs, TicketVerse v0

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** SDE-2 rounds go past `@RestController`: auto-configuration, proxies, @Transactional pitfalls, error contracts and API versioning. TicketVerse v0 starts your portfolio project.

## 🗓️ Sessions

### Monday 04 Jan · 60 min — Boot auto-configuration, conditions, starters, @ConfigurationProperties, Actuator
- 📚 **Learn:** `@SpringBootApplication` = configuration + auto-configuration + component scan; `@ConditionalOnClass/OnMissingBean/OnProperty`; `--debug` condition report; Boot 4 modular starters (`spring-boot-starter-webmvc`); typed `@ConfigurationProperties` records; profiles, logging, Actuator, DevTools. [Spring Boot: Auto-configuration](https://docs.spring.io/spring-boot/reference/using/auto-configuration.html), [Marco Behler: How auto-configuration works](https://www.marcobehler.com/guides/spring-boot-autoconfiguration), [Spring Boot 4.0 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide).
- 🛠️ **Do:** Generate `ticketverse` on start.spring.io (Spring Boot 4.1.x or newest stable, Java 25, Maven: webmvc, validation, actuator, devtools; note Boot 4 uses Jackson 3, packages `tools.jackson`). Run with `--debug` and explain 3 positive and 3 negative conditions. Add a validated `@ConfigurationProperties("tv")` record (city list, max seats per booking) and `application-dev.yaml`; expose `health` and `info`. Done when: changing a property per profile changes `/actuator/info` output.

### Tuesday 05 Jan · 60 min — AOP and proxies: JDK vs CGLIB, self-invocation pitfall
- 📚 **Learn:** Aspect, advice, pointcut, join point; Spring AOP uses runtime proxies (JDK dynamic proxies for interfaces, CGLIB subclasses otherwise; Boot defaults to CGLIB); why `this.method()` bypasses `@Transactional`, `@Async`, `@Cacheable`; final/private methods are not advised; fixes. [Spring: Proxying mechanisms](https://docs.spring.io/spring-framework/reference/core/aop/proxying.html), [Baeldung: Dynamic proxies](https://www.baeldung.com/java-dynamic-proxies), [Baeldung: Spring AOP](https://www.baeldung.com/spring-aop).
- 🛠️ **Do:** Write a plain `java.lang.reflect.Proxy` that times any interface call (no Spring). In TicketVerse add a custom `@Timed` annotation and an `@Around` aspect; print a bean's `getClass()` to spot the CGLIB proxy; call a `@Timed` method via `this` from the same bean and observe no timing, then fix by moving it to another bean. Done when: both behaviours are visible in logs.

### Wednesday 06 Jan · 60 min — REST controllers: DispatcherServlet flow, record DTOs, validation, pagination
- 📚 **Learn:** Request flow: filters -> DispatcherServlet -> HandlerMapping -> controller -> message converters; resource naming; correct status codes (200/201/204/400/404/409/422); `ResponseEntity` with `Location`; record DTOs (never expose entities); Bean Validation (`@Valid`, `@NotBlank`, `@Positive`); page/size/sort parameters. [Spring: DispatcherServlet](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html), [Spring Boot: Validation](https://docs.spring.io/spring-boot/reference/io/validation.html), [Baeldung: REST pagination](https://www.baeldung.com/rest-api-pagination-in-spring).
- 🛠️ **Do:** Build in-memory catalog APIs: `GET /api/events?city=&page=&size=&sort=`, `GET /api/events/{id}`, `POST /api/events` (validated `CreateEventRequest` record -> 201 + Location), `PUT`, `DELETE` -> 204. Exercise them with IntelliJ HTTP client or curl. Done when: invalid input returns 400, unknown id 404, and every endpoint returns the correct status.

### Thursday 07 Jan · 60 min — @RestControllerAdvice, ProblemDetail (RFC 9457), API versioning, OpenAPI
- 📚 **Learn:** Centralized errors with `@RestControllerAdvice` returning `ProblemDetail` (type, title, status, detail, custom fields); validation error mapping; Spring Framework 7 native API versioning (header or path, `version` attribute on mappings); OpenAPI docs with springdoc-openapi 3.x. [Spring: Error responses (ProblemDetail)](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html), [Spring: API versioning](https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html), [springdoc-openapi](https://springdoc.org/).
- 🛠️ **Do:** Map `EventNotFoundException` -> 404 and validation errors -> 400 ProblemDetail with an `errors` field list and an `errorCode`; enable API versioning via an `X-API-Version` header and add a v2 of `GET /api/events/{id}` returning an extra field; add springdoc and open Swagger UI. Done when: v1 and v2 both work and every error body follows RFC 9457.

### Friday 08 Jan · 60 min — RestClient and HTTP interfaces; @WebMvcTest slice tests
- 📚 **Learn:** `RestClient` fluent API, timeouts and error handlers; declarative HTTP service clients with `@HttpExchange`; slice testing with `@WebMvcTest` (Boot 4: `spring-boot-starter-webmvc-test`), `MockMvcTester` (AssertJ style) and `@MockitoBean` (replaces removed `@MockBean`). [Spring: REST clients](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html), [Spring Boot: Testing applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html), [Spring: MockMvc](https://docs.spring.io/spring-framework/reference/testing/mockmvc.html).
- 🛠️ **Do:** Create `ReviewsClient` as an `@HttpExchange` interface calling `https://jsonplaceholder.typicode.com/comments?postId=1` (stand-in movie reviews) with a 3 s timeout, exposed as `GET /api/events/{id}/reviews`. Write 6 `@WebMvcTest` tests for EventController: 200, 201 + Location, 400 ProblemDetail, 404, v2 header, and a mocked service failure -> 500. Done when: all 6 slice tests pass in under 10 seconds.

### Saturday 09 Jan · 60 min — BUILD: TicketVerse v0 catalog APIs on Postgres in Docker
- 📚 **Learn:** Catalog bounded context: Event, Venue, Show; Boot's Docker Compose support starts Postgres automatically in dev; `JdbcClient` + `schema.sql` for now (JPA arrives in W12); README with run instructions and curl examples. [Spring Boot: Docker Compose support](https://docs.spring.io/spring-boot/how-to/docker-compose.html), [Spring Framework: JDBC core classes](https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html).
- 🛠️ **Do:** Add `compose.yaml` with Postgres 18; persist events, venues and shows with `JdbcClient`; endpoints: events CRUD, `GET /api/venues`, `GET /api/events/{id}/shows?date=`; ProblemDetail errors, API v1, OpenAPI page; push the `ticketverse` repo with README and tag `v0.1.0`. Done when: `./mvnw spring-boot:run` starts Postgres automatically and a fresh clone works by following only the README.

## 📦 Deliverable (by Saturday night)
`ticketverse` repo v0: Boot 4.1 + Java 25, catalog APIs (events/venues/shows) on Postgres via Docker Compose, ProblemDetail errors, API versioning, OpenAPI, AOP timing aspect, 6+ slice tests.

## ✅ Self-check (Sunday test preview)
- How does Spring Boot auto-configuration decide what to create? Name three conditional annotations.
- JDK dynamic proxy vs CGLIB proxy: when is each used?
- Why does calling a `@Transactional` method from the same class not start a transaction? Give two fixes.
- Walk through what DispatcherServlet does for `POST /api/events`.
- PUT vs PATCH vs POST; 400 vs 404 vs 409 vs 422: when do you return each?
- What is ProblemDetail (RFC 9457) and why standardize error bodies?
- @WebMvcTest vs @SpringBootTest: what does each load?

## 🚀 Stretch (optional)
Write your own `@AutoConfiguration` with `@ConditionalOnMissingBean`, register it in `AutoConfiguration.imports`, and override it from the app.
