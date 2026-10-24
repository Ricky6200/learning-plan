# 🏗️ System Design · Week 03 — Creational patterns and scaling basics

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Factories, builders and singletons appear in almost every machine-coding solution, and 'how would you scale this?' is the first follow-up in any HLD round.

## 🗓️ Sessions

### Monday 09 Nov · 45 min — Scaling out: stateless services, load balancers, proxies, gateways
- 📚 **Learn:** Vertical vs horizontal scaling; stateless app tier (sessions in Redis); L4 vs L7 load balancers; algorithms (round robin, weighted, least connections, IP hash); health checks; sticky sessions; reverse proxy vs API gateway (auth, rate limits, routing). Watch [Top 6 load-balancing algorithms](https://www.youtube.com/watch?v=dBmxNsS3BGE) and [Reverse proxy vs API gateway vs load balancer](https://www.youtube.com/watch?v=RqfaTIWc3LQ) (ByteByteGo); Hindi: [Load balancer algorithms (Concept && Coding)](https://www.youtube.com/watch?v=vJYycNWAYZU).
- 🛠️ **Do:** In Excalidraw draw the evolution: 1 server -> app + DB split -> L7 LB + 3 stateless app servers + Redis session store -> API gateway in front. Below it add a table: LB algorithm -> when to use -> weakness. Save `hld/00-scaling-basics.png` + a short note. Done when: you can explain why sticky sessions hurt scaling and how a shared session store removes them.

### Wednesday 11 Nov · 45 min — Singleton (thread-safe variants) and Builder
- 📚 **Learn:** Singleton: eager, lazy `synchronized`, double-checked locking with `volatile`, holder idiom, enum (serialization/reflection safe); why singletons hurt testability. Builder: telescoping constructors, immutable objects, validation in `build()`. Read [Singleton](https://refactoring.guru/design-patterns/singleton) and [Builder](https://refactoring.guru/design-patterns/builder) (refactoring.guru); watch [Double-checked locking bug (Concept && Coding)](https://www.youtube.com/watch?v=upfrQvOgC24).
- 🛠️ **Do:** In `patterns.creational`, implement 4 singleton variants (eager, DCL with `volatile`, holder, enum) and a test that calls `getInstance()` from 100 threads via `ExecutorService` and asserts one identity. Then build an immutable `Notification` with a Builder (to, channel, subject, body, priority) that rejects a missing `to`. Done when: all tests pass and you can explain why DCL needs `volatile`.

### Thursday 12 Nov · 45 min — Factory Method, Abstract Factory, Prototype
- 📚 **Learn:** Factory Method (a creator decides which product), simple factory + registry map (no switch, keeps OCP), Abstract Factory (families: UI themes, cloud providers), Prototype (clone expensive objects; deep vs shallow copy). Read [Factory Method](https://refactoring.guru/design-patterns/factory-method) and [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory); Hindi: [Factory vs Abstract Factory (Concept && Coding)](https://www.youtube.com/watch?v=7g9S371qzwM).
- 🛠️ **Do:** Implement: (1) `PaymentProcessorFactory` backed by a `Map<PaymentType, Supplier<PaymentProcessor>>` registry; (2) Abstract Factory `CloudFactory` with `AwsFactory`/`AzureFactory` producing `Storage` + `Queue`; (3) Prototype `SeatMapTemplate.copy()` with a deep-copy test. Done when: tests prove a new payment type needs no edit to the factory class and the cloned seat map is independent of the original.

### Saturday 14 Nov · 45 min — PRACTICE: Notification factory kata
- 📚 **Learn:** Kata goal: combine Factory (choose channel), Builder (build the message) and a single registry of senders. Refresh with [All creational patterns (Concept && Coding)](https://www.youtube.com/watch?v=OuNOyFg942M); compare later with [Java pattern samples (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/tree/main/design-patterns/java).
- 🛠️ **Do:** Tests first. `NotificationService.send(Notification)` routes to EMAIL/SMS/PUSH/WHATSAPP senders via a factory registry; senders are fakes that record messages; an unknown channel throws `UnsupportedChannelException`; HIGH priority bypasses a simple per-user throttle. Done when: >= 6 tests pass and adding `SlackSender` touches only one new class plus one registration line.

## 📦 Deliverable (by Saturday night)
Scaling-evolution diagram in `hld/`, creational pattern code + tests in `patterns/creational`, and the notification kata with >= 6 green tests.

## ✅ Self-check (Sunday test preview)
- Why must the instance field be `volatile` in double-checked locking?
- Why is the enum singleton considered the safest variant in Java?
- Factory Method vs Abstract Factory: what is the difference? Give an example.
- When is a Builder better than constructors or setters?
- L4 vs L7 load balancer: what can an L7 balancer do that L4 cannot?
- Why are stateless services easier to scale horizontally, and where does the state go?
- Reverse proxy vs API gateway vs load balancer: one sentence each.

## 🚀 Stretch (optional)
Run 2 instances of a tiny Spring Boot app behind NGINX in Docker with round robin and watch requests alternate between them.
