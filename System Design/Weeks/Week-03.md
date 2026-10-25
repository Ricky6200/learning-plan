# 🏗️ System Design · Week 03 — Creational patterns and scaling basics

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Factories, builders and singletons appear in almost every machine-coding solution, and 'how would you scale this?' is the first follow-up in any HLD round.

## 🗓️ Sessions

### Monday 09 Nov · 45 min — Scaling out: stateless services, load balancers, proxies, gateways
- 📚 **Learn:** Vertical vs horizontal scaling; stateless app tier (sessions in a shared store such as Redis); L4 vs L7 load balancers; algorithms (round robin, weighted, least connections, IP hash); health checks; sticky sessions; reverse proxy vs API gateway (auth, rate limits, routing). Watch [Top 6 load-balancing algorithms (ByteByteGo, 5 min)](https://www.youtube.com/watch?v=dBmxNsS3BGE). Optional: [Reverse proxy vs API gateway vs load balancer (ByteByteGo, 3 min)](https://www.youtube.com/watch?v=RqfaTIWc3LQ).
- 🛠️ **Do:** In [Excalidraw](https://excalidraw.com/) draw the evolution: 1 server -> app + DB split -> L7 LB + 3 stateless app servers + Redis session store -> API gateway in front. Below it add a table: LB algorithm -> when to use -> weakness. Save `hld/00-scaling-basics.png` + a short note. Done when: you can explain why sticky sessions hurt scaling and how a shared session store removes them.

### Wednesday 11 Nov · 45 min — Singleton variants and Builder
- 📚 **Learn:** Singleton: eager, holder idiom (lazy, created on first use), enum singleton (serialization/reflection safe; enums are today's Java topic); why singletons hurt testability (prefer injecting one shared instance). Lazy double-checked locking needs threads and `volatile` - it waits for Java W8 Wed. Builder: replaces telescoping constructors, builds immutable objects, validates in `build()` with `IllegalArgumentException` (Java W2 Mon). Read [Builder (refactoring.guru)](https://refactoring.guru/design-patterns/builder). Optional: [Singleton (refactoring.guru)](https://refactoring.guru/design-patterns/singleton).
- 🛠️ **Do:** In `com.sdlab.patterns.creational` implement 3 singleton variants (eager, holder, enum) with a test per variant that `getInstance()` returns the same object twice. Then build an immutable `Notification` with a Builder (to, channel, subject, body, priority; `final` fields, no setters) whose `build()` rejects a missing `to`. Done when: tests prove singleton identity and the built values, and a small `main` demo shows a missing `to` is rejected.

### Thursday 12 Nov · 45 min — Factory Method, Abstract Factory, Prototype
- 📚 **Learn:** Factory Method (a creator decides which product), simple factory + registry map (no switch, keeps OCP), Abstract Factory (families: UI themes, cloud providers), Prototype (copy a configured object; deep vs shallow copy). `EnumMap` (Java W3 Wed) is a compact map keyed by an enum - ideal for registries. Read [Factory Method (refactoring.guru)](https://refactoring.guru/design-patterns/factory-method). Optional: [Factory vs Abstract Factory (Concept && Coding, Hindi, 12 min)](https://www.youtube.com/watch?v=7g9S371qzwM).
- 🛠️ **Do:** Implement (1) `PaymentProcessorFactory` backed by an `EnumMap<PaymentType, PaymentProcessor>` registry of ready-made instances (UPI, CARD, WALLET); (2) Abstract Factory `CloudFactory` with `AwsFactory`/`AzureFactory` producing `Storage` + `Queue` (each a tiny fake). Prototype goes to the stretch. Done when: tests prove a new payment type needs only a new class plus one `put`, and each factory returns products from its own family.

### Saturday 14 Nov · 45 min — PRACTICE: Notification factory kata
- 📚 **Learn:** Kata goal: combine Factory (choose the channel sender), Builder (your Wednesday `Notification`) and one registry of senders. Senders are fakes that record messages in a list so tests can inspect them. Refresh with the Factory and Builder parts of [All creational patterns (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=OuNOyFg942M). Optional: [Java pattern samples (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/tree/main/design-patterns/java).
- 🛠️ **Do:** Tests first. `NotificationService.send(Notification)` routes EMAIL/SMS/PUSH/WHATSAPP to fake senders via an `EnumMap` registry; a channel with no registered sender returns a failed `SendResult` (custom exceptions come in Java W4); HIGH priority bypasses a simple per-user throttle (max 3 sends per user, counted in a `HashMap`). Done when: >= 4 tests pass and adding `SlackSender` touches only one new class plus one registration line.

## 📦 Deliverable (by Saturday night)
Scaling-evolution diagram in `hld/`, creational pattern code + tests in `patterns/creational`, and the notification kata with >= 4 green tests.

## ✅ Self-check (Sunday test preview)
- Eager vs holder vs enum singleton: when is each instance created, and why is the enum version the safest?
- Why do singletons make unit testing harder, and what do you do instead?
- Factory Method vs Abstract Factory: what is the difference? Give an example.
- When is a Builder better than constructors or setters?
- L4 vs L7 load balancer: what can an L7 balancer do that L4 cannot?
- Why are stateless services easier to scale horizontally, and where does the state go?
- Reverse proxy vs API gateway vs load balancer: one sentence each.

## 🚀 Stretch (optional)
Prototype: add `SeatMapTemplate.copy()` (deep copy via a copy constructor) with a test that the copy is independent, and read [Abstract Factory (refactoring.guru)](https://refactoring.guru/design-patterns/abstract-factory). Codespaces only (Docker arrives in Java W11): run two `python -m http.server` instances behind NGINX round robin. Hindi: [Load balancer algorithms (Concept && Coding)](https://www.youtube.com/watch?v=vJYycNWAYZU).
