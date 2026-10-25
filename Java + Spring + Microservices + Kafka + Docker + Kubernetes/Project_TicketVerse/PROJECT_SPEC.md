# 🎟️ TicketVerse — Project Specification (Java track capstone)

> **One-liner:** an AI-powered movie & event ticket-booking platform that **never double-books a seat**, survives partial failures, and runs on Kubernetes/Azure — built by you, week by week, from W13 to W30.

Repo: **`ticketverse`** · Stack: Java 25 · Spring Boot 4.1.x · Spring Cloud 2025.1.x · PostgreSQL 18 · Redis 8 · Kafka 4.x (KRaft) · Keycloak · Docker · Kubernetes + Gateway API · GitHub Actions · Azure · AI service `ticketverse-ai` (Spring AI 2.0.x — built and owned by the AI track)
Why this project: it maps directly to the classic **LLD "BookMyShow"** and **HLD "Ticketmaster"** interview questions, and it forces real concurrency, consistency and failure-handling decisions.

---

## 1. Vision

Users browse events by city, pick a show, see a live seat map, **hold** seats for 10 minutes, pay, and get a confirmation — even when thousands try to book the same blockbuster show. Admins schedule shows; support staff look up bookings; an AI assistant ("Ask TicketVerse") answers policy questions and helps users find and hold seats — it is served by `ticketverse-ai`, which the AI track builds, and the Java track wires into the platform (W27). Every design choice is documented as an ADR so you can defend it in interviews.

## 2. Personas

| Persona | Goal | Key journeys |
|---|---|---|
| **Riya — moviegoer** (26, Pune, mobile-first) | Book 2 good seats fast, no surprises | Browse → seat map → hold → pay → e-ticket; view/cancel own bookings |
| **Arjun — venue admin** | Keep the schedule correct | Create events/shows, set prices, block broken seats |
| **Meera — support agent** | Resolve "I paid but no ticket" calls | Look up booking + payment status by id (read-only) |
| **You — on-call engineer** | Keep it fast, safe and observable | Dashboards, traces, runbooks, chaos tests, rollbacks |
| **Assistant user** | Ask in natural language (English/Hinglish) | "Kal shaam Pune mein 2 seats for Dune?" → options → confirm → hold |

## 3. Features by version (mapped to weeks)

| Version (git tag) | Weeks | Scope |
|---|---|---|
| **v0** (`v0.1.0`) | W13 | Spring Boot monolith: catalog APIs (events, venues, shows), Postgres via Docker Compose, record DTOs + Bean Validation, RFC 9457 errors, header-based API versioning, OpenAPI, Boot test slices + a `@ServiceConnection` Postgres test (AOP timing was learned in W12) |
| v0.x (internal) | W14–W15 | JPA/Hibernate data model + Flyway; N+1 fixed; Testcontainers; first GitHub Actions `ci.yml`. Seat **holds in Redis** (SET NX PX), optimistic/pessimistic locking, Redis cache-aside; **Boss S3 (W15):** 100-thread hold-and-book, tag `boss-s3` |
| **v1** (`v1.0.0`) | W16 | Spring Security: Keycloak OIDC, JWT resource server, roles (USER/ADMIN/SUPPORT), ownership checks, CORS; Mockito + Testcontainers; JaCoCo ≥ 70 % in CI |
| `v1.1.0` | W17–W18 | Gateway in front of the monolith (W17), then the step-by-step split into **gateway + catalog + booking + payment-mock + notification** + `common` contracts; DB per service; HTTP service clients with timeouts; OAuth2 client credentials; consumer-driven contract tests; ArchUnit rules |
| `v1.2.0` | W19 | Idempotency keys; Resilience4j (retry, circuit breaker, rate limiter, bulkhead); Micrometer → Prometheus/Grafana; OpenTelemetry → Jaeger; JSON logs; chaos report |
| `boss-s4` | W20 | Kafka fundamentals lab + timed Kafka/microservices gauntlet (**Boss S4**) |
| `v1.3.0` | W21 | Kafka events, **transactional outbox**, idempotent consumers, retry topics + DLT, **choreographed booking saga** with compensation |
| `v1.4.0` | W22 | Hardened non-root images (layered, Jib), Trivy, secret scan → public repo, images on GHCR; whole system via one `docker compose up` (milestone) |
| (internal) | W23–W24 | Kubernetes manifests → **Helm chart**; **Gateway API** (Envoy Gateway) entry; probes, HPA, StatefulSet, Jobs/CronJobs |
| **v2** (`v2.0.0`) — Boss S5 | W25 | Catalog events (`catalog.shows.v1`, `catalog.reviews.v1`), reviews API with JPA auditing, payment-timeout expirer (EXPIRED), cleanup endpoint, cancellation + refunds, JPA extras (embeddable, many-to-many, Specifications search); timed end-to-end boss, tag `boss-s5` |
| `v2.1.0` | W26 | Full CI/CD: matrix CI, Testcontainers, coverage gate, GHCR images with Trivy + SBOM, CodeQL, Dependabot, SonarQube Cloud, ephemeral kind deploy, OIDC login to Azure |
| (AI integration) | W27 | Platform hooks for the AI track's **`ticketverse-ai`**: gateway route + JWT pass-through + per-user rate limits, circuit breaker with a degraded search fallback, explicit topics + republish endpoint, Helm values + traces; joint end-to-end test (the AI track tags `ticketverse-v2.0-ai`) |
| `v2.2.0` | W28 | Live on **Azure Container Apps** on infrastructure the Azure track provisions with Bicep (deployment stack): PostgreSQL Flexible Server, Azure Managed Redis, Event Hubs Kafka endpoint, Key Vault + managed identities, Application Insights; `infra/teardown` |
| `v2.3.0` | W29 | k6 load tests, JFR/async-profiler fixes, virtual threads + pool tuning, OWASP API Top 10 audit, graceful shutdown, C4 + ADR-001..005, demo video, polished README |

## 4. Domain model

```mermaid
erDiagram
  VENUE ||--o{ SCREEN : has
  SCREEN ||--o{ SEAT : has
  EVENT ||--o{ SHOW : "scheduled as"
  SCREEN ||--o{ SHOW : hosts
  SHOW ||--o{ SHOW_SEAT : "inventory"
  SEAT ||--o{ SHOW_SEAT : "priced per show"
  BOOKING ||--|{ BOOKING_SEAT : contains
  SHOW_SEAT ||--o| BOOKING_SEAT : "sold as"
  BOOKING ||--o| PAYMENT : "paid by"
  BOOKING ||--o{ NOTIFICATION : triggers
  EVENT ||--o{ REVIEW : "reviewed in"
  EVENT }o--o{ GENRE : "tagged with"
```

| Entity (owner) | Key fields | Notes / invariants |
|---|---|---|
| `Venue` (catalog) | id, name, city, address (`@Embeddable Address`, W25), timezone | — |
| `Screen` (catalog) | id, venue_id, name, screen_type (2D/3D/IMAX), seat_count | — |
| `Seat` (catalog) | id, screen_id, row_label, number, category (CLASSIC/PRIME/RECLINER), accessible | unique (screen_id, row_label, number) |
| `Event` (catalog) | id, title, type (MOVIE/CONCERT/STANDUP), language, duration_min, certificate, genres (`@ManyToMany` via `event_genre`, W25), status | inheritance options for MOVIE/CONCERT/STANDUP are compared in `docs/jpa-inheritance.md` |
| `Review` (catalog, W25) | id, event_id, stars (1–5), text (≤ 1,000 chars), created_by (JWT `sub`), created_at (JPA auditing) | every new review publishes `ReviewCreated` via the outbox |
| `Show` (catalog) | id, event_id, screen_id, starts_at (UTC), ends_at, base_price, status (SCHEDULED/OPEN/CLOSED/CANCELLED) | no overlapping shows on one screen |
| `ShowSeat` (booking — inventory) | id, show_id, seat_id, price, status (AVAILABLE/RESERVED/BOOKED/BLOCKED), booking_id, **version** | unique (show_id, seat_id); `@Version` for optimistic locking |
| Seat hold (booking — Redis) | key `hold:{showId}:{seatId}` → `{userId, holdId}`, TTL 10 min; `holdset:{holdId}` → seat ids | release only by owner (Lua compare-and-delete) |
| `Booking` (booking) | id, user_id (JWT `sub`), show_id, status, total_amount, currency (INR), idempotency_key, created_at, confirmed_at, version | aggregate root; owns its seats |
| `BookingSeat` (booking) | booking_id, show_id, seat_id, price | **UNIQUE (show_id, seat_id)** among live bookings = last line of defence against double booking |
| `Payment` (payment) | id, booking_id, amount, status (INITIATED/SUCCEEDED/FAILED/REFUNDED), provider_ref, idempotency_key | one successful payment per booking |
| `Notification` (notification) | id, user_id, booking_id, channel (EMAIL/SMS), template, status, sent_at | simulated sending |
| `OutboxEvent` (every producer) | id (eventId), aggregate_type, aggregate_id, event_type, payload (jsonb), created_at, published_at | written in the same transaction as the state change |
| `ProcessedEvent` (every consumer) | event_id, consumer, processed_at | dedupe = idempotent consumer |
| `IdempotencyKey` (booking) | key, user_id, request_hash, response_status, response_body, expires_at (24 h) | replay returns the original response |
| `PolicyChunk` (`ticketverse-ai`, AI track — pgvector) | id, content, metadata (source, section), embedding | RAG source with citations; designed and owned by the AI track |

Users live in **Keycloak** (realm `ticketverse`, roles USER/ADMIN/SUPPORT); services store only the JWT `sub`.

## 5. Service boundaries (from `v1.1.0`, W18)

| Service | Bounded context | Owns data | Sync API (via gateway) | Publishes | Consumes |
|---|---|---|---|---|---|
| `gateway` | Edge | — | routes, JWT validation, rate limits, `X-Request-Id`, CORS | — | — |
| `catalog-service` | Catalog | venues, screens, seats, events, shows, reviews (`catalog_db`) | events, venues, shows, seat layouts, reviews, event search | `catalog.shows.v1`, `catalog.reviews.v1` (W25) | — |
| `booking-service` | Booking (inventory + holds + bookings) | show_seat, bookings, outbox, idempotency (`booking_db`, Redis) | seat availability, holds, bookings, cancellation | `booking.events.v1` | `payment.events.v1` (W21), `catalog.shows.v1` (W25) |
| `payment-service` (mock) | Payment | payments (`payment_db`) | payment status (SUPPORT), chaos switch (local only) | `payment.events.v1` | `booking.events.v1` |
| `notification-service` | Notification | notifications | — | — | `booking.events.v1` |
| `ticketverse-ai` (**AI track**, AI W23–W28) | Assistant | chat memory, policy vectors (pgvector) | `/ai/**` (search, assistant, review summaries), MCP endpoint | — | `catalog.shows.v1`, `catalog.reviews.v1`; calls catalog/booking over HTTP with the user's JWT |
| Keycloak | Identity | users, roles, clients | OIDC endpoints | — | — |

Rules: no shared database; booking keeps the inventory it needs (a catalog call from W18, built from `ShowScheduled` events from W25); public URLs do not change when the monolith is split (the gateway routes by path); services call each other with OAuth2 client-credentials tokens (W18). The Java track owns everything around `ticketverse-ai` (gateway route, rate limits, fallbacks, topics, Helm values — W27). On Kubernetes, the Gateway API (Envoy Gateway) is the north–south entry and forwards `/api/**` and `/ai/**` to the Spring Cloud Gateway service.

## 6. REST API sketch

All errors are [RFC 9457 ProblemDetail](https://www.rfc-editor.org/rfc/rfc9457.html) with `type, title, status, detail, instance, errorCode, traceId`. Version via header `X-API-Version` (Spring Framework 7 API versioning). Pagination: `page, size (max 50), sort`.

| Method & path | Auth | Purpose / notes |
|---|---|---|
| `GET /api/events?city=&type=&date=&page=&size=&sort=` | public | Browse events (cached) |
| `GET /api/events/{eventId}` | public | Event details (API version 2 via `X-API-Version` adds extra fields) |
| `POST /api/events` · `PUT /api/events/{id}` · `DELETE /api/events/{id}` | ADMIN | Manage events → 201 + `Location` / 200 / 204 |
| `GET /api/venues?city=` | public | Venues |
| `GET /api/events/{eventId}/shows?city=&date=` | public | Shows for an event |
| `GET /api/events/search?city=&genre=&from=&to=` | public | Dynamic search with JPA Specifications (W25); also the fallback when AI search is down (W27) |
| `POST /api/events/{eventId}/reviews` · `GET /api/events/{eventId}/reviews?page=` | USER · public | Reviews with JPA auditing; each new review publishes `ReviewCreated` (W25) |
| `GET /api/shows/{showId}/seats` | public | Seat map with AVAILABLE/HELD/RESERVED/BOOKED |
| `POST /api/shows/{showId}/holds` `{seatIds[]}` | USER | All-or-nothing hold, 10-min TTL → 201 `{holdId, expiresAt}`; 409 if any seat taken; 429 if rate-limited |
| `DELETE /api/holds/{holdId}` | USER (owner) | Release hold → 204 |
| `POST /api/bookings` `{holdId}` + `Idempotency-Key` | USER (owner of hold) | `v1.0.0`: 201 CONFIRMED (sync); `v1.1.0`–`v1.2.0`: synchronous payment call (PAYMENT_PENDING while payment is down); `v1.3.0`+: 202 `{bookingId, status: PAYMENT_PENDING}` (saga) |
| `GET /api/bookings/{bookingId}` | owner / SUPPORT / ADMIN | 404 for non-owners (no ID probing) |
| `GET /api/bookings?page=` | USER (own) / SUPPORT, ADMIN (filter by `userId`) | List bookings |
| `POST /api/bookings/{bookingId}/cancel` | owner | Before the cut-off (2 h before the show) → CANCELLED, refund via events; 409 after (W25) |
| `GET /api/payments/{bookingId}` | SUPPORT | Payment status |
| `POST /internal/maintenance/cleanup` | service role | Called by a Kubernetes CronJob: purge old idempotency keys and processed events (W25) |
| `POST /internal/catalog/republish` | ADMIN | Re-emit every show to `catalog.shows.v1` so new consumers can backfill (W27) |
| `/ai/**` (e.g. `/ai/search`, `/ai/assistant/{conversationId}`, `/ai/events/{id}/review-summary`) | USER | Served by the AI track's `ticketverse-ai`; the gateway route passes the JWT through, limits `/ai/assistant/**` to 10 requests/min per user and falls back to `/api/events/search` when AI search is down (W27) |
| `/mcp` | token | MCP tools served by `ticketverse-ai` (AI track): `searchShows`, `checkSeats` (read-only) |
| `/actuator/health/{liveness,readiness}`, `/actuator/prometheus` | internal | Probes and metrics (not exposed publicly) |

## 7. Kafka topics & event schemas (from `v1.3.0`, W21; catalog topics from `v2.0.0`, W25)

| Topic | Key | Producer | Consumers | Event types | Partitions | Cleanup |
|---|---|---|---|---|---|---|
| `booking.events.v1` | bookingId | booking (outbox) | payment, notification | BookingRequested, BookingConfirmed, BookingCancelled, BookingExpired | 6 | delete, 7 days |
| `payment.events.v1` | bookingId | payment (outbox) | booking | PaymentSucceeded, PaymentFailed, PaymentRefunded | 6 | delete, 7 days |
| `catalog.shows.v1` | showId | catalog (outbox) | booking, `ticketverse-ai` | ShowScheduled, ShowUpdated, ShowCancelled | 3 | **compact** (latest state per show) |
| `catalog.reviews.v1` | eventId | catalog (outbox) | `ticketverse-ai` (refreshes review summaries) | ReviewCreated | 3 | delete, 7 days |
| `*-retry-*`, `*-dlt` | same | Spring Kafka | DLT listener | failed records + exception headers | same as source | delete, 14 days |

Shared topics are created explicitly (`NewTopic` beans), never by auto-create (W27). Key = bookingId keeps every event of one booking **in order** on one partition. Trace context travels in Kafka headers. Event envelope:

```json
{
  "eventId": "0b8f6c1e-5a0e-4c51-9a4e-2f0d7e1c9a10",
  "eventType": "BookingRequested",
  "eventVersion": 1,
  "occurredAt": "2027-02-24T14:05:11Z",
  "aggregateType": "Booking",
  "aggregateId": "bk_7f3a",
  "payload": {
    "bookingId": "bk_7f3a",
    "userId": "kc-sub-123",
    "showId": 42,
    "seats": [{ "seatId": 1001, "price": 320.00 }, { "seatId": 1002, "price": 320.00 }],
    "amount": 640.00,
    "currency": "INR"
  }
}
```
Evolution rule: only add optional fields within a version; breaking change → new event version (`eventVersion: 2`) and a new topic if needed.

## 8. State machines

**Seat (per show)** — HELD lives in Redis; the other states live in `show_seat`:

```mermaid
stateDiagram-v2
  [*] --> AVAILABLE
  AVAILABLE --> HELD: hold (Redis SET NX PX, 10 min)
  HELD --> AVAILABLE: release or TTL expiry
  HELD --> RESERVED: booking requested (DB tx + version check)
  RESERVED --> BOOKED: PaymentSucceeded
  RESERVED --> AVAILABLE: PaymentFailed or payment timeout (compensation)
  BOOKED --> AVAILABLE: user cancels before cut-off (refund)
  AVAILABLE --> BLOCKED: admin blocks seat
  BLOCKED --> AVAILABLE: admin unblocks
```

**Booking**:

```mermaid
stateDiagram-v2
  [*] --> PAYMENT_PENDING: seats RESERVED, outbox BookingRequested
  PAYMENT_PENDING --> CONFIRMED: PaymentSucceeded
  PAYMENT_PENDING --> CANCELLED: PaymentFailed
  PAYMENT_PENDING --> EXPIRED: no payment result within 10 min
  CONFIRMED --> CANCELLED: user cancels (refund requested)
  CANCELLED --> [*]
  EXPIRED --> [*]
```
Illegal transitions throw and are unit-tested (enum-based state machine).

## 9. Booking saga (choreography + transactional outbox)

```mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant G as Gateway
  participant B as booking-service
  participant R as Redis
  participant DB as booking DB
  participant K as Kafka
  participant P as payment-service
  participant N as notification-service
  U->>G: POST /api/shows/42/holds (JWT)
  G->>B: forward with X-Request-Id
  B->>R: SET hold keys NX PX 600000
  B-->>U: 201 holdId, expiresAt
  U->>G: POST /api/bookings (holdId, Idempotency-Key)
  G->>B: forward
  B->>DB: TX verify hold, seats RESERVED (version check), booking PAYMENT_PENDING, outbox BookingRequested
  B-->>U: 202 bookingId, PAYMENT_PENDING
  B->>K: outbox relay publishes BookingRequested
  K->>P: BookingRequested
  alt payment succeeds
    P->>K: PaymentSucceeded
    K->>B: PaymentSucceeded (dedupe by eventId)
    B->>DB: TX seats BOOKED, booking CONFIRMED, outbox BookingConfirmed
    B->>R: delete hold keys
    K->>N: BookingConfirmed
    N-->>U: e-ticket (simulated email)
  else payment fails or times out
    P->>K: PaymentFailed
    K->>B: PaymentFailed
    B->>DB: TX seats AVAILABLE, booking CANCELLED, outbox BookingCancelled
    K->>N: BookingCancelled
    N-->>U: failure notice
  end
```
Background jobs: outbox relay (every 500 ms, `FOR UPDATE SKIP LOCKED`), payment-timeout expirer (every minute, `SKIP LOCKED` so each booking expires once — W25), cleanup endpoint called by a Kubernetes CronJob (stand-in in W24, real in W25). References: [Saga pattern](https://microservices.io/patterns/data/saga.html) · [Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html).

## 10. Non-functional requirements

| Area | Requirement | Verified by |
|---|---|---|
| **No double booking** | A seat is sold at most once per show, under any concurrency | DB `UNIQUE(show_id, seat_id)` + `@Version` on `show_seat` + Redis hold ownership; 100-thread boss test (W15), saga tests (W21) |
| **Latency** (local, 20 req/s) | p95: browse < 200 ms · hold < 300 ms · booking request (202) < 400 ms · confirmation end-to-end < 3 s | k6 thresholds (W29) |
| **Idempotency** | Retried `POST /api/bookings` never creates a second booking; duplicate events have no effect | `Idempotency-Key` table (24 h, W19), `processed_event` dedupe (W21), payment idempotency key |
| **Resilience** | Payment or AI outage must not take down browsing or holds | Timeouts on every call (≤ 2 s; longer for AI streaming), retries only for idempotent ops (backoff + jitter), circuit breaker, bulkhead, rate limits; chaos report (W19); degraded search when `ticketverse-ai` is down (W27) |
| **Security** | OAuth2/OIDC everywhere, least privilege, no BOLA | Keycloak JWT at gateway + services, role and ownership checks (W16), client credentials between services (W18), OWASP API Top 10 audit (W29), secrets in Key Vault (W28) |
| **Observability** | Any booking traceable end to end in < 2 minutes | RED + business metrics, OpenTelemetry traces across HTTP and Kafka (W19, W21), JSON logs with `traceId`, Grafana dashboard, App Insights (cloud, W28) |
| **Availability** | Rolling deploys with zero failed requests; target 99.5 % for the demo | Readiness/liveness probes (W23), HPA (W24), graceful shutdown proof (W29) |
| **Data** | Versioned schemas; minimal PII (email only); retention: holds 10 min, idempotency keys 24 h, Kafka 7 days | Flyway per service; cleanup endpoint + CronJob (W25); PITR backups on Azure PostgreSQL |
| **Cost** | Cloud spend within the monthly budget; nothing left running after demos | Budget alerts + `infra/teardown` (W28: deletes the deployment stack first, because its deny settings block a plain resource-group delete) |
| **Quality** | ≥ 70 % line coverage; no CRITICAL vulnerabilities; green pipeline on `main` | JaCoCo gate (W16), first CI (W14), Trivy (W22), CodeQL, SonarQube Cloud (W26) |

## 11. Repository structure

```text
ticketverse/
├─ pom.xml                      # parent (W18): Spring Boot 4.1.x BOM, Spring Cloud 2025.1.x, Java 25, JaCoCo, plugin management
├─ mvnw, .mvn/                  # Maven Wrapper (Maven 3.9.x / 3.10.x)
├─ common/                      # event contracts (records), ProblemDetail types — no business logic (W18, guarded by ArchUnit)
├─ gateway/                     # Spring Cloud Gateway Server Web MVC (W17)
├─ catalog-service/             # src/main/java/.../catalog/{api,application,domain,infrastructure}; reviews + catalog events (W25)
├─ booking-service/             # inventory, holds (Redis), bookings, outbox, saga handlers, expirer (W25)
├─ payment-service/             # mock payments with chaos switch (local only)
├─ notification-service/
├─ ticketverse-ai/              # Spring AI service — built and owned by the AI track (AI W23–W28); Java adds the hooks around it (W27)
├─ compose.yaml, .env.example   # profiles: infra, apps, obs; images as ${MIRROR:-}name with MIRROR only in the git-ignored .env
├─ k8s/                         # raw manifests (W23)
├─ charts/ticketverse/          # Helm umbrella chart (W24; ticketverse-ai added in W27)
├─ infra/                       # azure/ Bicep + outputs.json (Azure track, W28) · teardown (W28)
├─ perf/booking-flow.js         # k6 (W29)
├─ docs/                        # adr/, events.md, auth.md, split-plan.md, azure-contract.md, ai-integration.md, RUNBOOK.md, SECURITY.md, PERFORMANCE.md, CHAOS_REPORT.md, kql.md, diagrams/
└─ .github/                     # workflows/ci.yml (W14), images.yml + cd.yml (W26, deploy-azure job W28) · dependabot.yml
```

## 12. Milestones

| Week | Version | Acceptance criteria | XP |
|---|---|---|---|
| W13 | v0 · `v0.1.0` | Fresh clone runs with one command (Postgres auto-started); catalog CRUD; ProblemDetail errors; v1/v2 via header; Swagger UI; slice tests + a `@ServiceConnection` Postgres test green | +200 on ship |
| W15 | `boss-s3` **(Boss S3)** | Hold-and-book in one transaction: 100 threads on the same 2 seats → exactly 1 success and 99 clean 409s; no seat booked twice; a repeated confirm returns the same booking — inside 60 min | +300 boss |
| W16 | v1 · `v1.0.0` | Keycloak login → browse → hold → book → own booking visible, other user gets 404, SUPPORT can view it; JaCoCo ≥ 70 % enforced in CI; release notes (light day, AZ-104 week) | +200 |
| W18 | `v1.1.0` | 5 services + gateway from a clean `docker compose up`; client-credentials call booking → payment; contract tests green on both sides; ArchUnit rules pass | +200 |
| W19 | `v1.2.0` | Idempotent bookings; circuit breaker visible in actuator; Grafana dashboard + Jaeger trace; chaos report with p95 ≤ 2× baseline | +200 |
| W20 | `boss-s4` **(Boss S4)** | Kafka evidence (keyed ordering, unkeyed spread, duplicates on a late commit, loss on commit-before-process) + circuit breaker opening and recovering — inside 60 min | +300 boss |
| W21 | `v1.3.0` | Happy + failure sagas pass in automated e2e tests; no lost events when Kafka restarts; poison message in DLT | +200 |
| W22 | `v1.4.0` | `docker compose up` from a clean clone → all healthy → both sagas pass; non-root images on GHCR (semver + sha tags), no unexplained CRITICAL CVEs; clean secret scan, public repo | +200 |
| W25 | v2 · `v2.0.0` **(Boss S5)** | Timed end-to-end run: search → hold → book → pay → review → cancel (refund) → unpaid booking EXPIRED; events visible on `catalog.shows.v1`, `catalog.reviews.v1`, `booking.events.v1`; one Jaeger trace — inside 60 min | +200 (+300 boss) |
| W26 | `v2.1.0` | PR → CI (matrix, Testcontainers, coverage, CodeQL, Sonar) → images scanned and pushed → ephemeral kind smoke test; OIDC login to Azure; release with generated notes | +200 |
| W27 | joint run with the AI track | `scripts/e2e-ai`: search → ask → propose → confirm → booked; a new review refreshes the AI summary; search degrades gracefully with `ticketverse-ai` stopped | +200 |
| W28 | `v2.2.0` | Public HTTPS URL on Container Apps; both sagas + the AI end-to-end script pass live; zero secrets in Git/images; App Insights trace; demo video; teardown verified (run by the AI block after its live check) | +200 |
| W29 | `v2.3.0` | PERFORMANCE.md (baseline vs tuned), SECURITY.md audit with fixes, zero-error rolling restart, C4 + ADR-001..005, 5-min demo video | +200 |
| W30 | **Final Boss** | 60-minute mock technical interview scored ≥ 75/100 | +300 boss |

## 13. Tech stack (versions as of Oct 2026 — let the Boot BOM manage library versions)

| Layer | Choice |
|---|---|
| Language/runtime | Java 25 (Corretto 25 on your laptop, Temurin 25 images in Docker/CI), virtual threads where they help |
| Framework | Spring Boot 4.1.x → Spring Framework 7.0.x, Spring Security 7.1.x, Hibernate ORM 7.4, Jackson 3.x, Micrometer 1.17 · Spring Cloud 2025.1.x (Gateway Server Web MVC, Contract, CircuitBreaker) |
| Data | PostgreSQL 18 + Flyway 12 · Redis 8 (Azure Managed Redis in cloud) |
| Messaging | Kafka 4.x KRaft (4.4 is the newest release; clients 4.2.x via Boot), Spring for Apache Kafka 4.1.x · Event Hubs Kafka endpoint (cloud) |
| Edge & resilience | Spring Cloud Gateway (MVC; Bucket4j rate limits, circuit-breaker fallbacks) · Resilience4j 2.4.x · HTTP service clients (`@HttpExchange`) |
| Security | Keycloak (OIDC), OAuth2 resource server (JWT), OAuth2 client credentials between services |
| Testing | JUnit 6 (Jupiter — same API as JUnit 5) · Mockito 5.2x · AssertJ · Testcontainers 2.0.x · JaCoCo · Spring Cloud Contract · ArchUnit |
| Observability | Micrometer + Prometheus + Grafana · OpenTelemetry → Jaeger v2 · Application Insights (cloud) |
| Delivery | Docker (layered, non-root; jar built on the host, Jib) · Kubernetes + Gateway API (Envoy Gateway) · Helm 4 · GitHub Actions · GHCR/ACR · Azure Container Apps on a Bicep deployment stack from the Azure track (AKS as a stretch) |
| AI | `ticketverse-ai` — Spring AI 2.0.x service built and owned by the AI track; the Java track provides the platform around it (gateway route, JWT pass-through, rate limits, fallbacks, topics, Helm values) |

## 14. Definition of Done (every feature)

- [ ] Tests: unit + slice/integration (Testcontainers) green; concurrency tests run 5× without flakes
- [ ] Errors return ProblemDetail; inputs validated; authz rule written and tested
- [ ] Timeouts on outbound calls; idempotency considered
- [ ] Metrics/traces/logs let you debug it; dashboards updated if needed
- [ ] README/ADR/events doc updated; commit message explains *why*

## 15. Resume bullets you'll earn (fill in your real numbers)

- Built **TicketVerse**, an event-driven ticket-booking platform (Java 25, Spring Boot 4, Kafka, PostgreSQL, Redis) with 5 microservices behind an API gateway, deployed to **Azure** through a GitHub Actions pipeline using OIDC (no stored cloud secrets).
- Guaranteed **zero double bookings under 100 concurrent requests** by combining Redis seat holds (SET NX PX), optimistic locking (`@Version`) and database unique constraints; proven by automated concurrency tests.
- Implemented a **choreographed booking saga** with transactional outbox, idempotent consumers, retry topics and DLT — no lost or duplicated events across broker restarts; added payment-timeout expiry and cancellation with refunds.
- Split a monolith into **5 services step by step** (strangler fig) with OAuth2 client credentials between services, consumer-driven contract tests and ArchUnit rules — public URLs never changed.
- Reduced **p95 booking latency from __ ms to __ ms (__ %)** by fixing N+1 queries, adding composite indexes and tuning connection pools/virtual threads; validated with k6, JFR and async-profiler.
- Added resilience (circuit breaker, retries with jitter, bulkheads, rate limits) and observability (Prometheus/Grafana, OpenTelemetry/Jaeger, Application Insights); chaos test kept p95 within 2× during a payment outage.
- Secured APIs with **OAuth2/OIDC (Keycloak)**, JWT resource servers and ownership checks; audited against the OWASP API Security Top 10 and fixed __ findings.
- Integrated an AI service (**`ticketverse-ai`**, Spring AI) into the platform safely: JWT pass-through, per-user rate limits, a circuit breaker with a degraded search fallback, explicit Kafka topics with contract tests and Helm-managed secrets.
- Containerized services with multi-stage non-root images (__ % smaller), packaged a Helm chart with **Gateway API** routing, and enforced quality gates (Testcontainers, JaCoCo ≥ 70 %, CodeQL, Trivy, SonarQube Cloud).
