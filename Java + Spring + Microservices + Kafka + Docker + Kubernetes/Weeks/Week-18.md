# ☕ Java Backend · Week 18 — Spring Kafka, outbox and the booking saga

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** Reliable event-driven flows (retries, DLTs, idempotent consumers, outbox, sagas) are what senior interviewers dig into after 'have you used Kafka?'.

## 🗓️ Sessions

### Monday 22 Feb · 60 min — Spring for Apache Kafka: KafkaTemplate, @KafkaListener, JSON serialization
- 📚 **Learn:** Boot auto-configuration (`spring.kafka.*`); `KafkaTemplate.send` returning a `CompletableFuture`; `@KafkaListener` with group ids and concurrency; JSON (de)serializers and trusted packages; message keys and headers; listener container basics. [Spring Kafka: Quick tour](https://docs.spring.io/spring-kafka/reference/quick-tour.html), [Spring Kafka: @KafkaListener](https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/listener-annotation.html), [Concept && Coding: Event-driven architecture with Kafka (Hindi playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c62YCR2kkE-0tg3-y1QwaIWk).
- 🛠️ **Do:** booking-service publishes `BookingRequested` (key = bookingId) after a booking is created; notification-service consumes it with `@KafkaListener` (concurrency 3) and logs a fake email; add a Testcontainers Kafka test asserting the event arrives with the right key and headers. Done when: the test passes and the compose stack shows the message flowing.

### Tuesday 23 Feb · 60 min — Error handling: DefaultErrorHandler, backoff, DLT, @RetryableTopic
- 📚 **Learn:** Blocking retries with `DefaultErrorHandler` + backoff; `DeadLetterPublishingRecoverer`; non-retryable exceptions; non-blocking retries with `@RetryableTopic` (retry topics + DLT) and their ordering trade-off; poison pills and `ErrorHandlingDeserializer`. [Spring Kafka: Handling exceptions](https://docs.spring.io/spring-kafka/reference/kafka/annotation-error-handling.html), [Spring Kafka: Non-blocking retries](https://docs.spring.io/spring-kafka/reference/retrytopic.html), [Baeldung: Dead letter queue with Spring Kafka](https://www.baeldung.com/kafka-spring-dead-letter-queue).
- 🛠️ **Do:** In notification-service, fail on events whose email contains `fail`; configure 3 non-blocking retries with exponential delays and a DLT; send a malformed JSON message and route it to the DLT via `ErrorHandlingDeserializer`; add a DLT listener that logs the original topic and exception header. Done when: tests show retry topics used, the DLT receiving both bad messages, and healthy messages unaffected.

### Wednesday 24 Feb · 60 min — Idempotent consumers and the transactional outbox pattern
- 📚 **Learn:** Dual-write problem (DB commit + Kafka send can diverge); outbox: write the event into an `outbox` table in the same DB transaction, a relay publishes it (polling with `FOR UPDATE SKIP LOCKED`, or CDC with Debezium); consumers dedupe by eventId. [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), [Confluent: Transactional outbox course](https://developer.confluent.io/courses/microservices/the-transactional-outbox-pattern/), [Java Techie: Outbox hands-on (video)](https://www.youtube.com/watch?v=01jVbPHr3hc).
- 🛠️ **Do:** Add `outbox_event` (id, aggregateId, type, payload jsonb, createdAt, publishedAt) via Flyway; `BookingService` writes booking + outbox row in one transaction; a `@Scheduled` relay publishes batches with SKIP LOCKED and marks them published; consumers record processed eventIds in a `processed_event` table. Done when: killing Kafka during booking loses no event (published after restart) and duplicates are ignored.

### Thursday 25 Feb · 60 min — Sagas: choreography vs orchestration, compensation, CQRS intro
- 📚 **Learn:** Sagas replace distributed transactions with local transactions + events; choreography (services react to events) vs orchestration (central coordinator); compensating actions (release seats, refund); booking state machine; CQRS and event sourcing as related ideas, and when they are overkill. [microservices.io: Saga](https://microservices.io/patterns/data/saga.html), [microservices.io: CQRS](https://microservices.io/patterns/data/cqrs.html), [Martin Fowler: Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html).
- 🛠️ **Do:** Implement the choreographed saga: BookingRequested -> payment-service emits PaymentSucceeded or PaymentFailed -> booking-service confirms or cancels (compensation: release seats and holds) -> notification-service informs the user. Model `BookingStatus` transitions as an enum state machine with unit tests for illegal transitions. Done when: both paths work in compose and the state-machine tests pass.

### Friday 26 Feb · 60 min — Testing event-driven flows; tracing through Kafka
- 📚 **Learn:** Testcontainers Kafka with `@ServiceConnection`; Awaitility for eventual consistency; testing listeners and the outbox relay; contract tests for event payloads; enabling observation on KafkaTemplate and listeners so traces continue across Kafka headers. [Testcontainers: Testing a Spring Kafka listener](https://testcontainers.com/guides/testing-spring-boot-kafka-listener-using-testcontainers/), [Spring Kafka: Testing](https://docs.spring.io/spring-kafka/reference/testing.html), [Spring Boot: Kafka support](https://docs.spring.io/spring-boot/reference/messaging/kafka.html).
- 🛠️ **Do:** Write an end-to-end test with Testcontainers (Postgres + Kafka): POST a booking -> eventually CONFIRMED; with payment forced to fail -> eventually CANCELLED and seats free again (Awaitility, max 10 s). Enable Kafka observation and check Jaeger shows one trace spanning HTTP and Kafka hops. Done when: both saga tests pass 3 runs in a row and the trace screenshot is saved.

### Saturday 27 Feb · 60 min — BUILD: TicketVerse booking saga with outbox, end to end
- 📚 **Learn:** Definition of done for an event-driven feature: outbox-backed publishing, idempotent consumers, retries + DLT, compensations, observability, documented event contracts and a sequence diagram. [microservices.io: Idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html), [Spring Kafka: Transactions](https://docs.spring.io/spring-kafka/reference/kafka/transactions.html).
- 🛠️ **Do:** Polish and demo: run the smoke script for happy and failure paths through the gateway; replay a duplicate PaymentSucceeded (no double confirmation); push a poison message (lands in DLT); add Mermaid sequence diagrams for both saga paths to the README; tag `v3.0.0`. Done when: all four demos pass from a clean compose start.

## 📦 Deliverable (by Saturday night)
TicketVerse v3.0.0: Spring Kafka events with retries/DLT, transactional outbox + relay, idempotent consumers, choreographed booking saga with compensation, Testcontainers e2e tests, traces across Kafka.

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
