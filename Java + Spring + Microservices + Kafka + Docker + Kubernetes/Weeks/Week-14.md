# ☕ Java Backend · Week 14 — Spring Security, OAuth2, testing: Season 3 boss

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Every product company asks how you secured an API (filter chain, JWT, OAuth2/OIDC, method security), and a tested, tagged v1.0 is what makes TicketVerse resume-worthy.

## 🗓️ Sessions

### Monday 25 Jan · 60 min — Security filter chain, authN vs authZ, UserDetailsService, BCrypt
- 📚 **Learn:** DelegatingFilterProxy -> FilterChainProxy -> SecurityFilterChain; SecurityContextHolder; AuthenticationManager/Provider; UserDetailsService; PasswordEncoder (BCrypt, DelegatingPasswordEncoder); `authorizeHttpRequests` rules; 401 vs 403. [Spring Security: Architecture](https://docs.spring.io/spring-security/reference/servlet/architecture.html), [Spring Security: Authorize HTTP requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html), [Engineering Digest: Spring Security (Hindi video)](https://www.youtube.com/watch?v=02WP1FbiNSQ).
- 🛠️ **Do:** Add `spring-boot-starter-security`; define a `SecurityFilterChain`: public catalog GETs, authenticated holds/bookings, ADMIN for event writes; JPA-backed `UserDetailsService` with BCrypt-hashed users from a Flyway seed; set `org.springframework.security` logging to TRACE and read the filter list once. Done when: anonymous POST /api/bookings gets 401, a USER on admin endpoints gets 403.

### Tuesday 26 Jan · 60 min — JWT and OAuth2/OIDC flows: auth code + PKCE, client credentials
- 📚 **Learn:** JWT structure (header, claims, signature), RS256 vs HS256, validating `exp/iss/aud`; OAuth2 roles; authorization code + PKCE for users/SPAs, client credentials for service-to-service; OIDC ID token vs access token; why stateless APIs use bearer tokens. [JWT introduction](https://jwt.io/introduction), [OAuth.net: PKCE](https://oauth.net/2/pkce/), [Java Brains: What is JWT (video)](https://www.youtube.com/watch?v=soGRyl9ztjI).
- 🛠️ **Do:** Write a JUnit test that signs an RS256 JWT with `NimbusJwtEncoder` and verifies it with `NimbusJwtDecoder` (spring-security-oauth2-jose); tamper one claim and expired `exp` and assert both fail. Draw the auth-code + PKCE sequence as Mermaid in `docs/auth.md`. Done when: 3 token tests pass and the diagram shows every redirect and token exchange.

### Wednesday 27 Jan · 60 min — Keycloak in Docker and Spring Resource Server (JWT)
- 📚 **Learn:** Keycloak realm, clients (public SPA client with PKCE, confidential service client), realm roles and token mappers; Spring `oauth2ResourceServer().jwt()` with `issuer-uri`; mapping realm roles to authorities with a `JwtAuthenticationConverter`; Boot 4 starter name `spring-boot-starter-security-oauth2-resource-server`. [Keycloak: Getting started with Docker](https://www.keycloak.org/getting-started/getting-started-docker), [Spring Security: Resource server JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html), [Baeldung: Keycloak with Spring Boot](https://www.baeldung.com/spring-boot-keycloak).
- 🛠️ **Do:** Run Keycloak (`start-dev`) in compose; create realm `ticketverse`, roles USER/ADMIN, users, a public client and a confidential client; switch TicketVerse to resource-server JWT; get a token with curl (password flow for local testing only, plus client credentials) and call APIs. Done when: realm roles become `ROLE_USER/ROLE_ADMIN` and the 401/403 rules from Monday still hold.

### Thursday 28 Jan · 60 min — Method security, ownership checks, CORS and CSRF
- 📚 **Learn:** `@EnableMethodSecurity`, `@PreAuthorize` with roles and ownership (`#userId == authentication.name`), avoiding BOLA; CORS for a browser SPA origin; CSRF protects cookie sessions, so stateless bearer-token APIs disable it consciously. [Spring Security: Method security](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html), [Spring Security: CORS](https://docs.spring.io/spring-security/reference/servlet/integrations/cors.html), [Spring Security: CSRF](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html).
- 🛠️ **Do:** Make `GET /api/bookings/{id}` return 404 for bookings the caller does not own (no ID probing); admin-only event writes via `@PreAuthorize`; allow CORS only from your local SPA origin (localhost, port 5173). Tests with `jwt()` request post-processor: owner 200, other user 404, admin 200, anonymous 401. Done when: 4 security tests pass and a comment explains your CSRF decision.

### Friday 29 Jan · 60 min — Testing push: Mockito, slice tests, Testcontainers, JaCoCo 70% gate
- 📚 **Learn:** Test pyramid; Mockito stubbing, `verify`, `ArgumentCaptor`; slices (`@WebMvcTest` with security, `@DataJpaTest`) vs `@SpringBootTest` + Testcontainers; Spring Security test support; JaCoCo `check` goal enforcing coverage. [Martin Fowler: Practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html), [Spring Security: Testing](https://docs.spring.io/spring-security/reference/servlet/test/index.html), [JaCoCo Maven plugin](https://www.jacoco.org/jacoco/trunk/doc/maven.html).
- 🛠️ **Do:** Add JaCoCo with a `check` rule of 0.70 line coverage on `verify`; write Mockito unit tests for BookingService (happy path, hold expired, seat taken, idempotent confirm) using `ArgumentCaptor`; add one `@SpringBootTest` booking flow on Testcontainers Postgres + Redis + Keycloak (or mocked JWT). Done when: `./mvnw verify` passes the 70% gate.

### Saturday 30 Jan · 60 min — BOSS BATTLE: TicketVerse v1.0 release under security, 60 min
- 📚 **Learn:** Release checklist: clean clone builds; `mvnw verify` green (tests + 70% coverage); README with architecture diagram, run steps, API examples; demo script; tag `v1.0.0` and GitHub Release notes. Rules: 60 minutes, fix only what blocks the release. [GitHub Docs: Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests), [Spring Boot: Docker Compose support](https://docs.spring.io/spring-boot/how-to/docker-compose.html).
- 🛠️ **Do:** From a fresh clone: `docker compose up` (Postgres, Redis, Keycloak) + app; scripted demo: get a user token -> browse events -> hold 2 seats -> book -> view own booking -> other user gets 404 -> admin creates an event. Record a 3-minute screen capture. Done when: the demo passes end-to-end inside 60 minutes and `v1.0.0` is tagged with release notes (+200 XP milestone).

## 📦 Deliverable (by Saturday night)
TicketVerse v1.0.0: JWT resource server with Keycloak, method security with ownership checks, CORS, 70%+ coverage gate, release notes and demo recording.

## ✅ Self-check (Sunday test preview)
- Walk through the Spring Security filter chain for a request with a bearer token.
- Authentication vs authorization; 401 vs 403?
- Why BCrypt? What does DelegatingPasswordEncoder add?
- Authorization code + PKCE vs client credentials: who uses which and why?
- How does a resource server validate a JWT without calling Keycloak on every request?
- What is BOLA and how did you prevent it in TicketVerse?
- When must CSRF protection stay enabled, and why can a stateless JWT API disable it?

## 🚀 Stretch (optional)
Add refresh-token handling to a tiny SPA or Postman collection and document token lifetimes in `docs/auth.md`.
