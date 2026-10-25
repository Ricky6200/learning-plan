# ☕ Java Backend · Week 16 — Spring Security, OAuth2 and the v1.0 release

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Every product company asks how you secured an API (filter chain, JWT, OAuth2/OIDC, method security), and a tested, tagged v1.0 is what makes TicketVerse resume-worthy. AZ-104 exam week: Friday and Saturday are deliberately lighter.

## 🗓️ Sessions

### Monday 08 Feb · 60 min — Security filter chain, authN vs authZ, UserDetailsService, BCrypt
- 📚 **Learn:** DelegatingFilterProxy -> FilterChainProxy -> SecurityFilterChain; SecurityContextHolder; AuthenticationManager/Provider; UserDetailsService; PasswordEncoder (BCrypt, DelegatingPasswordEncoder); `authorizeHttpRequests` rules written with the lambda DSL (the only style Spring Security 7 accepts); 401 vs 403. Read: [Spring Security: Architecture](https://docs.spring.io/spring-security/reference/servlet/architecture.html). Optional: [Engineering Digest: Spring Security (Hindi video)](https://www.youtube.com/watch?v=02WP1FbiNSQ).
- 🛠️ **Do:** Add `spring-boot-starter-security`; define a `SecurityFilterChain`: public catalog GETs, authenticated holds/bookings, ADMIN for event writes, SUPPORT for read-only booking lookups; a JPA-backed `UserDetailsService` with BCrypt-hashed users (USER, ADMIN, SUPPORT) from a Flyway seed; set `org.springframework.security` logging to TRACE and read the filter list once. Done when: anonymous POST /api/bookings gets 401 and a USER on admin endpoints gets 403.

### Tuesday 09 Feb · 60 min — JWT and OAuth2/OIDC flows: auth code + PKCE, client credentials
- 📚 **Learn:** JWT structure (header, claims, signature), RS256 vs HS256, validating `exp/iss/aud`; OAuth2 roles; authorization code + PKCE for users/SPAs, client credentials for service-to-service; OIDC ID token vs access token; why stateless APIs use bearer tokens. Read: [JWT introduction](https://jwt.io/introduction). Optional: [OAuth.net: PKCE](https://oauth.net/2/pkce/).
- 🛠️ **Do:** Write a JUnit test that signs an RS256 JWT with `NimbusJwtEncoder` and verifies it with `NimbusJwtDecoder` (spring-security-oauth2-jose); tamper one claim and expired `exp` and assert both fail. Draw the auth-code + PKCE sequence as Mermaid in `docs/auth.md`. Done when: 3 token tests pass and the diagram shows every redirect and token exchange.

### Wednesday 10 Feb · 60 min — Keycloak in Docker and Spring Resource Server (JWT)
- 📚 **Learn:** Keycloak realm, clients (public SPA client with PKCE, confidential service client), realm roles and token mappers; resource server: `http.oauth2ResourceServer(o -> o.jwt(Customizer.withDefaults()))` with `issuer-uri` (Security 7 removed the old `.and()`-chained style); map realm roles to authorities with a `JwtAuthenticationConverter`; Boot 4 starter `spring-boot-starter-security-oauth2-resource-server`. Read: [Spring Security: Resource server JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html). Optional: [Keycloak: Getting started with Docker](https://www.keycloak.org/getting-started/getting-started-docker).
- 🛠️ **Do:** Run Keycloak (`start-dev`, image `keycloak/keycloak` through your mirror) in compose; create realm `ticketverse`, roles USER/ADMIN/SUPPORT, users, a public client and a confidential client; switch TicketVerse to the JWT resource server; get a token with curl (password grant for local testing only, plus client credentials) and call the APIs. Done when: realm roles become `ROLE_USER/ROLE_ADMIN/ROLE_SUPPORT` and Monday's 401/403 rules still hold.

### Thursday 11 Feb · 60 min — Method security, ownership checks, CORS and CSRF
- 📚 **Learn:** `@EnableMethodSecurity`, `@PreAuthorize` with roles and ownership (`#userId == authentication.name`), avoiding BOLA (broken object-level authorization); CORS for a browser SPA origin; CSRF protects cookie sessions, so stateless bearer-token APIs disable it consciously. Read: [Spring Security: Method security](https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html). Optional: [Spring Security: CSRF](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html).
- 🛠️ **Do:** Make `GET /api/bookings/{id}` return 404 for bookings the caller does not own (no ID probing) unless the caller has SUPPORT or ADMIN; admin-only event writes via `@PreAuthorize`; allow CORS only from your local SPA origin (localhost, port 5173). Tests with the `jwt()` request post-processor: owner 200, other user 404, SUPPORT 200, anonymous 401. Done when: 4 security tests pass and a comment explains your CSRF decision.

### Friday 12 Feb · 60 min — Coverage gate and service unit tests (light day, AZ-104 week)
- 📚 **Learn:** Test pyramid: many fast unit tests (Mockito, W10), fewer slice tests (W13), a few `@SpringBootTest` + Testcontainers flows; Spring Security test support (`jwt()`, `@WithMockUser`); JaCoCo's `check` goal fails the build below a coverage threshold, and your W14 CI runs it on every push. Read: [Martin Fowler: Practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) (first half). Optional: [JaCoCo Maven plugin](https://www.jacoco.org/jacoco/trunk/doc/maven.html).
- 🛠️ **Do:** Add JaCoCo with a `check` rule of 0.70 line coverage bound to `verify`; write 3 Mockito unit tests for `BookingService` (hold expired, seat taken, idempotent confirm) using an `ArgumentCaptor`. Push and watch CI enforce the gate. Done when: `./mvnw verify` passes the 70% gate locally and in GitHub Actions.

### Saturday 13 Feb · 60 min — BUILD: TicketVerse v1.0 release (light day, AZ-104 week)
- 📚 **Learn:** Release checklist: a clean clone builds; `mvnw verify` is green (tests + 70% coverage); the README has an architecture diagram, run steps and API examples; a scripted demo; tag `v1.0.0` with GitHub Release notes. Keep it small: fix only what blocks the release. Read: [GitHub Docs: Managing releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository). Optional: [Spring Boot: Docker Compose support](https://docs.spring.io/spring-boot/how-to/docker-compose.html).
- 🛠️ **Do:** From a fresh clone: `docker compose up` (Postgres, Redis, Keycloak) + the app; scripted demo: get a user token -> browse events -> hold 2 seats -> book -> view own booking -> another user gets 404 -> SUPPORT can view it -> admin creates an event. Tag `v1.0.0` and publish release notes. Done when: the demo passes end-to-end from the clean clone and `v1.0.0` is on GitHub with notes (+200 XP milestone).

## 📦 Deliverable (by Saturday night)
TicketVerse v1.0.0: JWT resource server with Keycloak (USER/ADMIN/SUPPORT), method security with ownership checks, CORS, a 70%+ coverage gate enforced in CI, release notes.

## ✅ Self-check (Sunday test preview)
- Walk through the Spring Security filter chain for a request with a bearer token.
- Authentication vs authorization; 401 vs 403?
- Why BCrypt? What does DelegatingPasswordEncoder add?
- Authorization code + PKCE vs client credentials: who uses which and why?
- How does a resource server validate a JWT without calling Keycloak on every request?
- What is BOLA and how did you prevent it in TicketVerse (owner, SUPPORT, ADMIN)?
- When must CSRF protection stay enabled, and why can a stateless JWT API disable it?

## 🚀 Stretch (optional)
Record a 3-minute demo video of the release flow. Add refresh-token handling to a tiny SPA or Postman collection and document token lifetimes in `docs/auth.md`. Add one `@SpringBootTest` booking flow on Testcontainers Postgres + Redis with a mocked JWT.
