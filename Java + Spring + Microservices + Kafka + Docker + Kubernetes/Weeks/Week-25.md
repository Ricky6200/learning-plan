# ☕ Java Backend · Week 25 — TicketVerse loose ends and the Season 5 boss

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** Real systems are judged at their edges: unpaid bookings that must expire, cancellations, cleanup jobs and the events other services (like the AI track's `ticketverse-ai` in W27) depend on; JPA mapping extras (embeddables, many-to-many, inheritance, auditing, Specifications) are interview staples too.

## 🗓️ Sessions

### Monday 12 Apr · 60 min — Catalog change events: catalog.shows.v1 via an outbox
- 📚 **Learn:** Catalog becomes an event producer with W21's outbox: `ShowScheduled`, `ShowUpdated` and `ShowCancelled` go to `catalog.shows.v1` (key = showId, 3 partitions, `cleanup.policy=compact`, so the topic keeps the latest state of every show); the payload carries what consumers need without calling back (title, genres, city, venue, start time, minimum price, status). Consumers: booking (seat inventory) and `ticketverse-ai` (search, AI W27). Read: [Kafka 4.3: Topic configs](https://kafka.apache.org/43/configuration/topic-configs/) (`cleanup.policy`). Optional: [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html).
- 🛠️ **Do:** In catalog-service add `outbox_event` (Flyway) and a `@Scheduled` relay (copy W21's); creating, updating or cancelling a show writes the matching event in the same transaction; create `catalog.shows.v1` as a compacted topic; booking-service consumes `ShowScheduled` and creates the show's `show_seat` inventory idempotently. Done when: a new show produces exactly one event, a replayed event creates no extra seats, and `kafka-console-consumer --from-beginning` shows every change keyed by showId.

### Tuesday 13 Apr · 60 min — Reviews API with JPA auditing and a ReviewCreated event
- 📚 **Learn:** Real reviews replace W13's stand-in client: a `Review` entity in catalog-service with Spring Data JPA auditing (`@EnableJpaAuditing`, `@CreatedDate`, `@CreatedBy` filled from the JWT subject by an `AuditorAware` bean); validation (1-5 stars, text up to 1,000 chars); `ReviewCreated` goes through the outbox to `catalog.reviews.v1` (key = eventId), which `ticketverse-ai` uses to refresh review summaries (AI W27). Read: [Spring Data JPA: Auditing](https://docs.spring.io/spring-data/jpa/reference/auditing.html).
- 🛠️ **Do:** Add `POST /api/events/{id}/reviews` (USER) and a paged `GET /api/events/{id}/reviews` (public) in catalog-service, replacing the jsonplaceholder stand-in from W13; audit fields fill automatically; each new review writes `ReviewCreated` to the outbox. Tests: auditing sets `createdBy` to the token's subject, invalid stars give a 400 ProblemDetail, one review produces one event. Done when: 3 tests pass and the event appears on `catalog.reviews.v1` with the right key.

### Wednesday 14 Apr · 60 min — Payment-timeout expirer and a cleanup endpoint
- 📚 **Learn:** Sagas need a timeout path: a booking with no payment result after 10 minutes moves PAYMENT_PENDING -> EXPIRED, its seats return to AVAILABLE and `BookingExpired` is published (compensation); with several booking-service replicas, claim due rows with `FOR UPDATE SKIP LOCKED` (W15) so each booking expires once. Housekeeping sits behind an internal endpoint that a CronJob calls: delete idempotency keys older than 24 h and processed-event rows older than 7 days. Read: [Spring: Task execution and scheduling](https://docs.spring.io/spring-framework/reference/integration/scheduling.html) (`@Scheduled`). Optional: [PostgreSQL: SELECT (the locking clause)](https://www.postgresql.org/docs/current/sql-select.html).
- 🛠️ **Do:** Add `PaymentTimeoutExpirer` (`@Scheduled` every minute) that expires due bookings in batches with SKIP LOCKED, releases their seats and writes `BookingExpired` to the outbox; add `POST /internal/maintenance/cleanup` (service role only) and point your W24 CronJob at it. Tests with an injected `Clock`: an 11-minute-old pending booking expires and frees its seats; a confirmed one is untouched; two expirer threads never expire the same booking twice. Done when: 3 tests pass and a CronJob run deletes old rows.

### Thursday 15 Apr · 60 min — Booking cancellation with compensation and refunds
- 📚 **Learn:** Cancellation is another saga: CONFIRMED -> CANCELLED is allowed only for the owner and before a cut-off (e.g. 2 hours before the show); booking writes `BookingCancelled`, payment-service reacts with `PaymentRefunded`, seats go back to AVAILABLE; the endpoint is idempotent (a second cancel returns the same result) and your W21 state machine rejects illegal transitions. Read: [microservices.io: Saga](https://microservices.io/patterns/data/saga.html) (compensating transactions). Optional: [Martin Fowler: Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html).
- 🛠️ **Do:** Add `POST /api/bookings/{id}/cancel` (owner only; 409 ProblemDetail after the cut-off) that moves the booking to CANCELLED, releases seats and writes `BookingCancelled`; payment-service consumes it and publishes `PaymentRefunded`; notification informs the user. Tests: the owner cancels before the cut-off, another user gets 404, after the cut-off gives 409, a second cancel is a no-op. Done when: 4 tests pass and the smoke script shows a refund event.

### Friday 16 Apr · 60 min — JPA extras: embeddables, many-to-many, inheritance, Specifications
- 📚 **Learn:** `@Embeddable` value objects (an `Address` inside `Venue`) map to columns of the owner's table; `@ManyToMany` (Event <-> Genre) needs a join table, a `Set` and helper methods, and becomes an explicit join entity once the link carries data; inheritance strategies: SINGLE_TABLE (fast, nullable columns), JOINED (normalized, needs joins), TABLE_PER_CLASS (rare); `Specification`s combine optional filters into one query (`JpaSpecificationExecutor`). Read: [Spring Data JPA: Specifications](https://docs.spring.io/spring-data/jpa/reference/jpa/specifications.html). Optional: [Vlad Mihalcea: The best way to use @ManyToMany](https://vladmihalcea.com/the-best-way-to-use-the-manytomany-annotation-with-jpa-and-hibernate/).
- 🛠️ **Do:** In catalog-service (Flyway migration first): make `Venue.address` an `@Embeddable Address`, map `Event` <-> `Genre` as `@ManyToMany` with a `Set` and an `event_genre` join table, and add `EventSpecs` (city, genre, date range) combined with `and()` behind `GET /api/events/search`. Write one `@DataJpaTest` per feature (3 tests). For inheritance, sketch SINGLE_TABLE vs JOINED tables for Movie/Concert/Standup in `docs/jpa-inheritance.md`. Done when: 3 tests pass and the sketch names the strategy you would pick and why.

### Saturday 17 Apr · 60 min — BOSS BATTLE: TicketVerse v2 end to end, 60 min timed
- 📚 **Learn:** Rules: 60 minutes, start from `docker compose down -v` (or a fresh kind cluster with your Helm chart), README instructions only, fix only what blocks the run. Scenario: user token -> search events by genre and city (Specifications) -> hold -> book -> pay -> post a review -> cancel a second booking (refund) -> let a third booking expire unpaid -> check the events on Kafka -> find one booking's Jaeger trace. Reference: [microservices.io: Pattern language](https://microservices.io/patterns/index.html).
- 🛠️ **Do:** Run the scenario through the gateway and collect evidence in `docs/BOSS_S5.md`: smoke output, `kafka-console-consumer` output for `catalog.shows.v1`, `catalog.reviews.v1` and `booking.events.v1`, the EXPIRED booking row, the refund event and the trace. Tag `v2.0.0` and `boss-s5`. Done when: every step passes within 60 minutes on a clean start, plus a 5-line retro.

## 📦 Deliverable (by Saturday night)
TicketVerse v2.0.0: `catalog.shows.v1` (compacted) and `catalog.reviews.v1` events via outbox, booking inventory built from show events, reviews API with JPA auditing, payment-timeout expirer (EXPIRED) + cleanup endpoint called by the CronJob, cancellation with refunds, JPA extras (embeddable, many-to-many, Specifications search, inheritance notes); Boss S5 evidence tagged `boss-s5`.

## ✅ Self-check (Sunday test preview)
- Why is `catalog.shows.v1` a compacted topic, and what does a brand-new consumer see when it starts?
- How does booking-service build its seat inventory from catalog events idempotently?
- What happens to a booking that never gets a payment result, and how do you stop two replicas expiring it twice?
- Walk through cancellation as a saga: events, compensation and idempotency.
- How does Spring Data JPA auditing know who created a review?
- @Embeddable vs a separate entity; when should @ManyToMany become an explicit join entity?
- SINGLE_TABLE vs JOINED inheritance: trade-offs. How do Specifications help dynamic search?

## 🚀 Stretch (optional)
Implement the inheritance sketch (SINGLE_TABLE `Event` subtypes with a discriminator column) and compare the SQL with JOINED. Write in 5 lines how SKIP LOCKED compares with leader election for scheduled jobs on many replicas. Publish a JSON Schema for both catalog events in `docs/events.md`.
