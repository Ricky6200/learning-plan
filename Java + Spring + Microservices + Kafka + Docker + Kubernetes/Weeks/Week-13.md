# ☕ Java Backend · Week 13 — Spring Boot internals, testing, REST APIs, TicketVerse v0

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** SDE-2 rounds go past `@RestController`: auto-configuration, test slices, error contracts and API versioning. TicketVerse v0 starts your portfolio project.

## 🗓️ Sessions

### Monday 18 Jan · 60 min — Boot auto-configuration, conditions, starters, @ConfigurationProperties, Actuator
- 📚 **Learn:** `@SpringBootApplication` = configuration + auto-configuration + component scan; `@ConditionalOnClass/OnMissingBean/OnProperty`; the `--debug` condition report; Boot 4 modular starters (`spring-boot-starter-webmvc`); typed `@ConfigurationProperties` records; profiles, logging, Actuator, DevTools. Read: [Spring Boot: Auto-configuration](https://docs.spring.io/spring-boot/reference/using/auto-configuration.html). Optional: [Marco Behler: How auto-configuration works](https://www.marcobehler.com/guides/spring-boot-autoconfiguration).
- 🛠️ **Do:** Generate `ticketverse` on start.spring.io (Spring Boot 4.1.x, Java 25, Maven: webmvc, validation, actuator, devtools; Boot 4 uses Jackson 3, packages `tools.jackson`). Stay on 4.1.x for the rest of the plan; if you upgrade, move Boot, Spring Cloud and Spring AI together. Run with `--debug` and explain 3 positive and 3 negative conditions. Add a validated `@ConfigurationProperties("tv")` record (city list, max seats per booking) and `application-dev.yaml`; expose `health` and `info`. Done when: changing a property per profile changes `/actuator/info` output.

### Tuesday 19 Jan · 60 min — Boot testing: slices vs @SpringBootTest, @MockitoBean, @ServiceConnection
- 📚 **Learn:** Test the smallest slice that proves the behaviour: `@SpringBootTest` loads the whole context (slow, realistic); slices load one layer (`@WebMvcTest`, `@JsonTest`, `@JdbcTest`, `@DataJpaTest`); `@MockitoBean` swaps a bean for a Mockito mock (W10); `@ServiceConnection` on a Testcontainers field wires URL and credentials automatically; identical test contexts are cached; `ApplicationContextRunner` tests configuration without starting the app. Read: [Spring Boot: Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html) (detecting configuration and the slice sections). Optional: [Spring Boot: Test modules](https://docs.spring.io/spring-boot/reference/testing/test-modules.html).
- 🛠️ **Do:** Add `spring-boot-starter-test`. Write: (1) an `ApplicationContextRunner` test proving your `tv.*` properties bind and an invalid value fails startup; (2) a `@JsonTest` checking a record DTO's JSON with `JacksonTester`; (3) a `@SpringBootTest` + `@AutoConfigureMockMvc` test of `/actuator/info` under `@ActiveProfiles("dev")`. Note each test's startup time (a `@ServiceConnection` Postgres test follows on Saturday). Done when: 3 tests pass and a comment ranks them by speed and says when to use each.

### Wednesday 20 Jan · 60 min — REST controllers: DispatcherServlet flow, record DTOs, validation, pagination
- 📚 **Learn:** Request flow: filters -> DispatcherServlet -> HandlerMapping -> controller -> message converters; resource naming; correct status codes (200/201/204/400/404/409/422); `ResponseEntity` with `Location`; record DTOs (never expose entities); Bean Validation (`@Valid`, `@NotBlank`, `@Positive`); page/size/sort parameters. Read: [Spring: DispatcherServlet](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html). Optional: [Spring Boot: Validation](https://docs.spring.io/spring-boot/reference/io/validation.html).
- 🛠️ **Do:** Build in-memory catalog APIs: `GET /api/events?city=&page=&size=&sort=`, `GET /api/events/{id}`, `POST /api/events` (validated `CreateEventRequest` record -> 201 + Location), `PUT`, `DELETE` -> 204. Exercise them with IntelliJ HTTP client or curl. Done when: invalid input returns 400, unknown id 404, and every endpoint returns the correct status.

### Thursday 21 Jan · 60 min — @RestControllerAdvice, ProblemDetail (RFC 9457), API versioning, OpenAPI
- 📚 **Learn:** Centralized errors with `@RestControllerAdvice` returning `ProblemDetail` (type, title, status, detail, custom fields); validation error mapping; Spring Framework 7 native API versioning (header or path, `version` attribute on mappings); OpenAPI docs with springdoc-openapi 3.x. Read: [Spring: Error responses (ProblemDetail)](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html). Optional: [Spring: API versioning](https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html).
- 🛠️ **Do:** Map `EventNotFoundException` -> 404 and validation errors -> 400 ProblemDetail with an `errors` field list and an `errorCode`; enable API versioning via an `X-API-Version` header and add a v2 of `GET /api/events/{id}` returning an extra field; add springdoc and open Swagger UI. Done when: v1 and v2 both work and every error body follows RFC 9457.

### Friday 22 Jan · 60 min — RestClient and HTTP interfaces; @WebMvcTest slice tests
- 📚 **Learn:** `RestClient` fluent API, timeouts and error handlers; declarative HTTP service clients with `@HttpExchange`; `@WebMvcTest` slices (Boot 4: `spring-boot-starter-webmvc-test`) with `MockMvcTester` (AssertJ style) and `@MockitoBean` (replaces the removed `@MockBean`). Calling the internet from the app on the company laptop? A PKIX error needs the VM option `-Djavax.net.ssl.trustStoreType=Windows-ROOT` (setup guide Section 5). Read: [Spring: REST clients](https://docs.spring.io/spring-framework/reference/integration/rest-clients.html). Optional: [Spring: MockMvc](https://docs.spring.io/spring-framework/reference/testing/mockmvc.html).
- 🛠️ **Do:** Create `ReviewsClient` as an `@HttpExchange` interface calling `https://jsonplaceholder.typicode.com/comments?postId=1` (stand-in reviews; real reviews arrive in W25) with a 3 s timeout, exposed as `GET /api/events/{id}/reviews`. Write 6 `@WebMvcTest` tests for EventController: 200, 201 + Location, 400 ProblemDetail, 404, v2 header, and a mocked service failure -> 500. Done when: all 6 slice tests pass in under 10 seconds.

### Saturday 23 Jan · 60 min — BUILD: TicketVerse v0 catalog APIs on Postgres in Docker
- 📚 **Learn:** Catalog bounded context: Event, Venue, Show; Boot's Docker Compose support starts Postgres automatically in dev (mirror prefix in a git-ignored `.env`, as in W11); `JdbcClient` + `schema.sql` for now (JPA arrives in W14); `@JdbcTest` with a `@ServiceConnection` Postgres container for repository tests; a README with run instructions and curl examples. Read: [Spring Boot: Docker Compose support](https://docs.spring.io/spring-boot/how-to/docker-compose.html). Optional: [Spring Boot: Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html).
- 🛠️ **Do:** Add `compose.yaml` with Postgres 18; persist events with `JdbcClient` and seed venues and shows in `data.sql`; add `GET /api/venues` and `GET /api/events/{id}/shows?date=`; keep ProblemDetail errors, API v1 and the OpenAPI page; add one `@JdbcTest` with a `@ServiceConnection` Postgres container for the event repository; push the `ticketverse` repo with a README and tag `v0.1.0`. Done when: `./mvnw spring-boot:run` starts Postgres automatically, the container test is green, and a fresh clone works by following only the README.

## 📦 Deliverable (by Saturday night)
`ticketverse` v0 (`v0.1.0`): Boot 4.1 + Java 25, catalog APIs (events/venues/shows) on Postgres via Docker Compose, ProblemDetail errors, API versioning, OpenAPI; tests: context-runner config test, `@JsonTest`, 6 `@WebMvcTest` slices and a `@JdbcTest` with `@ServiceConnection`.

## ✅ Self-check (Sunday test preview)
- How does Spring Boot auto-configuration decide what to create? Name three conditional annotations.
- @WebMvcTest vs @SpringBootTest vs @DataJpaTest: what does each load, and when do you use each?
- What does `@ServiceConnection` do, and why test against a real Postgres instead of H2?
- Walk through what DispatcherServlet does for `POST /api/events`.
- PUT vs PATCH vs POST; 400 vs 404 vs 409 vs 422: when do you return each?
- What is ProblemDetail (RFC 9457) and why standardize error bodies?
- RestClient vs an `@HttpExchange` interface client: what does the declarative style buy you?

## 🚀 Stretch (optional)
Write your own `@AutoConfiguration` with `@ConditionalOnMissingBean`, register it in `AutoConfiguration.imports`, and override it from the app. Extra: add a second `@SpringBootTest` class with the same configuration and measure how the test context cache speeds it up.
