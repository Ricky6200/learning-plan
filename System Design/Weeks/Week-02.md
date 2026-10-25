# 🏗️ System Design · Week 02 — SOLID design and API protocols

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** SOLID is the vocabulary LLD interviewers use to judge your code, and protocol choices (REST vs gRPC, WebSockets vs SSE, pagination, idempotency) show up in the API step of every HLD answer.

## 🗓️ Sessions

### Monday 02 Nov · 45 min — TCP vs UDP; HTTP/1.1 vs HTTP/2 vs HTTP/3
- 📚 **Learn:** TCP (handshake, ordering, retransmits, congestion control) vs UDP (no guarantees, low latency). HTTP/1.1 keep-alive and head-of-line blocking, HTTP/2 multiplexing + header compression, HTTP/3 over QUIC (UDP, faster handshakes, no TCP head-of-line blocking). Read the 'Transport Layer Protocols' and 'HTTP/HTTPS' sections of [Networking essentials (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/networking-essentials). Optional: [HTTP/1 to HTTP/2 to HTTP/3 (ByteByteGo, 4 min)](https://www.youtube.com/watch?v=a-sBfyiXysI).
- 🛠️ **Do:** Open DevTools -> Network, enable the Protocol column, load 3 sites (e.g., google.com, github.com, a news site) and note h2/h3 per request. Write `notes/03-protocols.md`: TCP vs UDP table (6 rows), HTTP versions table, and 2 UDP use cases (video call, DNS). Done when: you can explain in 3 sentences why HTTP/2 still suffers head-of-line blocking at the TCP layer.

### Wednesday 04 Nov · 45 min — SOLID in Java: violation -> fix pairs
- 📚 **Learn:** SRP (one reason to change), OCP (extend by adding classes), LSP (implementations honour the contract), ISP (small role interfaces), DIP (depend on abstractions; constructor injection). JUnit primer (5 min, builds on Java W2 Mon): a `@Test` method arranges objects, acts, then asserts with `assertThat(actual).isEqualTo(expected)`; run `mvn test`. Read the SOLID sections of [Design principles (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/design-principles). Optional: [SOLID principles (Concept && Coding, Hindi, 19 min)](https://www.youtube.com/watch?v=XI7zep97c-Y).
- 🛠️ **Do:** In `notes/03-solid.md` write a one-line violation + fix for each principle (e.g., SRP `Invoice` that prints and saves; LSP `Penguin` implementing a `FlyingBird` interface; ISP fat `Worker` interface). Then code two pairs in `com.sdlab.patterns.solid`: OCP discount if/else -> `DiscountPolicy` implementations, and DIP `OrderService` doing `new MySqlRepo()` -> a constructor-injected `OrderRepository` with an in-memory fake. Done when: 2+ JUnit tests per coded pair are green and each pair has a one-line comment naming the smell it removes.

### Thursday 05 Nov · 45 min — API styles, real-time options and REST conventions
- 📚 **Learn:** REST (resources, verbs, status codes, idempotent PUT/DELETE), gRPC (protobuf over HTTP/2; service-to-service), GraphQL (client-shaped queries, N+1 risk); real-time: polling vs long polling vs SSE vs WebSockets. REST conventions: keyset (cursor) pagination over offset, versioning (`/v1/` or a header), an `Idempotency-Key` header for retried POSTs, `429 Too Many Requests` + `Retry-After`. Read [API design (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/api-design) (API Types + Common API Patterns). Optional: [Top 6 API architecture styles (ByteByteGo, 4 min)](https://www.youtube.com/watch?v=4vLxWqE94l4).
- 🛠️ **Do:** Add a decision table to `notes/03-protocols.md`: pick a style for 5 cases with a one-line reason (mobile catalog API, internal booking -> payment call, live cricket score, chat app, admin dashboard with flexible filters). Then write 3 REST endpoints for TicketVerse seat holds (method, path, body, status codes) using `/v1/`, an `Idempotency-Key` on the POST, cursor pagination on the list, and a 429 + `Retry-After` response. Done when: every pick names the trade-off you accepted and each endpoint lists its error codes.

### Saturday 07 Nov · 45 min — PRACTICE: Refactor a God class with SOLID
- 📚 **Learn:** Refactoring lens: DRY (one source of truth), KISS, YAGNI (do not build for imaginary needs), high cohesion + low coupling. Characterization tests pin today's behaviour before you move code. Read [Large Class smell (refactoring.guru)](https://refactoring.guru/smells/large-class). Optional: [KISS, SOLID, CAP, BASE (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=cTyZ_hbmbDw).
- 🛠️ **Do:** Ask your AI mentor for a ~100-line `OrderManager` (validates, prices, saves to an in-memory list, 'emails' via `System.out`) and paste it in. Add 3 characterization tests first. Then extract `OrderValidator`, `PricingService` and `OrderRepository` (interface + in-memory class) with constructor injection. Done when: the same 3 tests stay green, no class exceeds ~60 lines, and a short README lists the principle behind each extraction.

## 📦 Deliverable (by Saturday night)
`notes/03-protocols.md` (protocol, API-style and REST-convention tables), `notes/03-solid.md` + OCP/DIP pairs with green tests in `patterns/solid`, and the refactored `OrderManager` with green characterization tests.

## ✅ Self-check (Sunday test preview)
- Why does DNS mostly use UDP while HTTP/1.1 and HTTP/2 use TCP? What changed with HTTP/3?
- Explain head-of-line blocking at the HTTP layer vs at the TCP layer.
- When would you choose gRPC over REST between two internal services?
- SSE or WebSockets for a live score feed? Why?
- Give a Liskov Substitution violation and how you would fix it.
- How does Dependency Inversion make a class easier to unit test?
- How do keyset pagination, an `Idempotency-Key` header and `429` + `Retry-After` make a public REST API safer to use?

## 🚀 Stretch (optional)
Watch [Long polling vs SSE vs WebSockets (Tech Primers, 14 min)](https://www.youtube.com/watch?v=1cFyfT0m3bA), then find one site that uses a WebSocket (DevTools -> Network -> WS filter) and note what its frames look like.
