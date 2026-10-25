# ☕ Java Backend · Week 21 — Spring Kafka, outbox and the booking saga

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** Reliable event-driven flows (retries, DLTs, idempotent consumers, outbox, sagas) are what senior interviewers dig into after 'have you used Kafka?'.

## 🗓️ Sessions

### Monday 15 Mar · 60 min — Spring for Apache Kafka: KafkaTemplate, @KafkaListener, JSON serialization
- 📚 **Learn:** Boot auto-configuration (`spring.kafka.*`); `KafkaTemplate.send` returning a `CompletableFuture`; `@KafkaListener` with group ids and concurrency; JSON (de)serializers and trusted packages; message keys and headers; listener container basics. Read: [Spring Kafka: Quick tour](https://docs.spring.io/spring-kafka/reference/quick-tour.html). Optional: [Concept && Coding: Event-driven architecture with Kafka (Hindi playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c62YCR2kkE-0tg3-y1QwaIWk).
- 🛠️ **Do:** booking-service publishes `BookingRequested` (key = bookingId) to `booking.events.v1` after a booking is created; notification-service (your W18 skeleton) consumes it with `@KafkaListener` (concurrency 3) and logs a fake email; add a Testcontainers Kafka test asserting the event arrives with the right key and headers. Done when: the test passes and the compose stack shows the message flowing.

### Tuesday 16 Mar · 60 min — Error handling: DefaultErrorHandler, backoff, DLT, @RetryableTopic
- 📚 **Learn:** Blocking retries with `DefaultErrorHandler` + backoff; `DeadLetterPublishingRecoverer`; non-retryable exceptions; non-blocking retries with `@RetryableTopic` (retry topics + DLT) and their ordering trade-off; poison pills and `ErrorHandlingDeserializer`. Read: [Spring Kafka: Non-blocking retries](https://docs.spring.io/spring-kafka/reference/retrytopic.html). Optional: [Baeldung: Dead letter queue with Spring Kafka](https://www.baeldung.com/kafka-spring-dead-letter-queue).
- 🛠️ **Do:** In notification-service, fail on events whose email contains `fail`; configure 3 non-blocking retries with exponential delays and a DLT; send a malformed JSON message and route it to the DLT via `ErrorHandlingDeserializer`; add a DLT listener that logs the original topic and exception header. Done when: tests show retry topics used, the DLT receiving both bad messages, and healthy messages unaffected.

### Wednesday 17 Mar · 60 min — Idempotent consumers and the transactional outbox pattern
- 📚 **Learn:** The dual-write problem (DB commit + Kafka send can diverge); outbox: write the event into an `outbox` table in the same DB transaction and let a relay publish it (polling with `FOR UPDATE SKIP LOCKED` from a `@Scheduled` job as in W12, or CDC with Debezium); consumers dedupe by eventId. Read: [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html). Optional: [Confluent: Transactional outbox course](https://developer.confluent.io/courses/microservices/the-transactional-outbox-pattern/).
- 🛠️ **Do:** Add `outbox_event` (id, aggregateId, type, payload jsonb, createdAt, publishedAt) via Flyway; `BookingService` writes booking + outbox row in one transaction; a `@Scheduled` relay publishes batches with SKIP LOCKED and marks them published; consumers record processed eventIds in a `processed_event` table. Done when: killing Kafka during booking loses no event (published after restart) and duplicates are ignored.

### Thursday 18 Mar · 60 min — Sagas: choreography vs orchestration, compensation, CQRS intro
- 📚 **Learn:** Sagas replace distributed transactions with local transactions + events; choreography (services react to events) vs orchestration (a central coordinator); compensating actions (release seats, refund); the booking state machine; CQRS and event sourcing as related ideas, and when they are overkill. Read: [microservices.io: Saga](https://microservices.io/patterns/data/saga.html). Optional: [microservices.io: CQRS](https://microservices.io/patterns/data/cqrs.html).
- 🛠️ **Do:** Replace W18's synchronous payment call with the choreographed saga: `BookingRequested` -> payment-service emits `PaymentSucceeded` or `PaymentFailed` on `payment.events.v1` -> booking-service confirms or cancels (compensation: release seats and holds) -> notification-service informs the user. Model `BookingStatus` transitions as an enum state machine with unit tests for illegal transitions. Done when: both paths work in compose and the state-machine tests pass.

### Friday 19 Mar · 60 min — Testing event-driven flows; tracing through Kafka
- 📚 **Learn:** Testcontainers Kafka with `@ServiceConnection`; Awaitility for eventual consistency; testing listeners and the outbox relay; contract tests for event payloads; enabling observation on KafkaTemplate and listeners so traces continue across Kafka headers. Read: [Testcontainers: Testing a Spring Kafka listener](https://testcontainers.com/guides/testing-spring-boot-kafka-listener-using-testcontainers/). Optional: [Spring Kafka: Testing](https://docs.spring.io/spring-kafka/reference/testing.html).
- 🛠️ **Do:** Write an end-to-end test with Testcontainers (Postgres + Kafka): POST a booking -> eventually CONFIRMED; with payment forced to fail -> eventually CANCELLED and seats free again (Awaitility, max 10 s). Enable Kafka observation and check Jaeger shows one trace spanning HTTP and Kafka hops. Done when: both saga tests pass 3 runs in a row and the trace screenshot is saved.

### Saturday 20 Mar · 60 min — BUILD: TicketVerse booking saga with outbox, end to end
- 📚 **Learn:** Definition of done for an event-driven feature: outbox-backed publishing, idempotent consumers, retries + DLT, compensations, observability, documented event contracts and a sequence diagram. Read: [Spring Kafka: Transactions](https://docs.spring.io/spring-kafka/reference/kafka/transactions.html). Optional: [microservices.io: Idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html).
- 🛠️ **Do:** Polish and demo: run the smoke script for happy and failure paths through the gateway; replay a duplicate `PaymentSucceeded` (no double confirmation); push a poison message (it lands in the DLT); add Mermaid sequence diagrams for both saga paths to the README; tag `v1.3.0`. Done when: all four demos pass from a clean compose start.

## 📦 Deliverable (by Saturday night)
TicketVerse v1.3.0: Spring Kafka events with retries/DLT, transactional outbox + relay, idempotent consumers, choreographed booking saga with compensation, Testcontainers e2e tests, traces across Kafka.

## ✅ Self-check (Sunday test preview)
- What is the dual-write problem and how does the transactional outbox solve it?
- Blocking retries vs @RetryableTopic: what happens to ordering in each?
- How do you make a Kafka consumer idempotent?
- Choreography vs orchestration sagas: pros, cons and when you would switch.
- What compensations run in TicketVerse when payment fails?
- How do you test eventually consistent flows without sleeps?
- What is CQRS, and why did TicketVerse not need full event sourcing?

## 🚀 Stretch (optional)
Prototype an orchestrated version with a `BookingSagaOrchestrator` and compare code size and failure handling with choreography.
