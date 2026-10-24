# 🏗️ System Design · Week 02 — SOLID design and API protocols

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** SOLID is the vocabulary LLD interviewers use to judge your code, and protocol choices (REST vs gRPC, WebSockets vs SSE) show up in the API step of every HLD answer.

## 🗓️ Sessions

### Monday 02 Nov · 45 min — TCP vs UDP; HTTP/1.1 vs HTTP/2 vs HTTP/3
- 📚 **Learn:** TCP (handshake, ordering, retransmits, congestion control) vs UDP (no guarantees, low latency). HTTP/1.1 keep-alive and head-of-line blocking, HTTP/2 multiplexing + header compression, HTTP/3 over QUIC (UDP, faster handshakes, no TCP head-of-line blocking). Watch [HTTP/1 to HTTP/2 to HTTP/3 (ByteByteGo)](https://www.youtube.com/watch?v=a-sBfyiXysI); read the TCP/UDP and HTTP parts of [Networking essentials (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/networking-essentials).
- 🛠️ **Do:** Open DevTools -> Network, enable the Protocol column, load 3 sites (e.g., google.com, github.com, a news site) and note h2/h3 per request. Write `notes/03-protocols.md`: TCP vs UDP table (6 rows), HTTP versions table, and 2 UDP use cases (video call, DNS). Done when: you can explain in 3 sentences why HTTP/2 still suffers head-of-line blocking at the TCP layer.

### Wednesday 04 Nov · 45 min — SOLID in Java: violation -> fix for all five
- 📚 **Learn:** SRP (one reason to change), OCP (extend by adding classes), LSP (subtypes honour contracts: Rectangle/Square), ISP (small role interfaces), DIP (depend on abstractions; constructor injection). Watch [SOLID principles (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=XI7zep97c-Y); read [Design principles (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/design-principles).
- 🛠️ **Do:** In `com.sdlab.patterns.solid`, write five tiny violation/fix pairs (<= 30 lines each): SRP `Invoice` that prints + saves; OCP discount if/else -> `DiscountPolicy`; LSP `Bird.fly()`; ISP fat `Worker` interface; DIP `OrderService` doing `new MySqlRepo()`. Add JUnit tests for the OCP and DIP fixes (use a fake repo). Done when: tests are green and each pair has a one-line comment naming the smell it removes.

### Thursday 05 Nov · 45 min — API styles and real-time: REST, gRPC, GraphQL, WebSockets, SSE
- 📚 **Learn:** REST (resources, verbs, status codes, idempotent PUT/DELETE), gRPC (protobuf over HTTP/2, streaming; service-to-service), GraphQL (client-shaped queries, N+1 risk). Real-time: short polling vs long polling vs SSE (server -> client) vs WebSockets (bi-directional). Watch [Top 6 API architecture styles (ByteByteGo)](https://www.youtube.com/watch?v=4vLxWqE94l4) and [Long polling vs SSE vs WebSockets (Tech Primers)](https://www.youtube.com/watch?v=1cFyfT0m3bA); skim [API design (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/api-design).
- 🛠️ **Do:** Add a decision table to `notes/03-protocols.md` and pick a style for 5 cases with a one-line reason: mobile catalog API, internal booking -> payment call, live cricket score, chat app, admin dashboard with flexible filters. Then write 3 REST endpoints for TicketVerse seat holds (method, path, body, status codes). Done when: every pick names the trade-off you accepted.

### Saturday 07 Nov · 45 min — PRACTICE: Refactor a God class with SOLID
- 📚 **Learn:** Refactoring lens: DRY (one source of truth), KISS, YAGNI (do not build for imaginary needs), high cohesion + low coupling. Read [Large Class smell (refactoring.guru)](https://refactoring.guru/smells/large-class); watch [KISS, SOLID, CAP, BASE (ByteByteGo)](https://www.youtube.com/watch?v=cTyZ_hbmbDw).
- 🛠️ **Do:** Write (or ask your AI mentor to generate) a ~150-line `OrderManager` that validates, prices, saves to an in-memory DB, emails and logs. First add 3 characterization tests. Then split it into `OrderValidator`, `PricingService`, `OrderRepository`, `Notifier` behind interfaces with constructor injection. Done when: the same tests stay green, no class exceeds ~60 lines, and a short README lists the principle behind each change.

## 📦 Deliverable (by Saturday night)
`notes/03-protocols.md` (protocol + API-style tables), five SOLID pairs with tests in `patterns/solid`, and the refactored `OrderManager` with green characterization tests.

## ✅ Self-check (Sunday test preview)
- Why does DNS mostly use UDP while HTTP/1.1 and HTTP/2 use TCP? What changed with HTTP/3?
- Explain head-of-line blocking at the HTTP layer vs at the TCP layer.
- When would you choose gRPC over REST between two internal services?
- SSE or WebSockets for a live score feed? Why?
- Give a Liskov Substitution violation and how you would fix it.
- How does Dependency Inversion make a class easier to unit test?

## 🚀 Stretch (optional)
Build a tiny SSE endpoint with Spring Boot `SseEmitter` that pushes a counter every second and watch it in the browser.
