# 🏗️ System Design · Week 08 — Elevator, logger, CAP and consistency

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Elevator and Logger test state machines, scheduling and clean handler chains; CAP, PACELC and consistency models are how you justify every database and replication choice.

## 🗓️ Sessions

### Monday 14 Dec · 45 min — CAP, PACELC, consistency models, quorums
- 📚 **Learn:** CAP precisely (during a partition choose C or A), PACELC (else: latency vs consistency), models: linearizable, sequential, causal, read-your-writes, monotonic reads, eventual. Quorums: R + W > N makes read and write sets overlap, so a read sees the latest acknowledged write only with strict quorums (no sloppy quorum) and no concurrent writes - and it is still not linearizable. Watch [CAP theorem simplified (ByteByteGo, 6 min)](https://www.youtube.com/watch?v=BHqjEjzAicA). Optional: [Consistency levels (Azure Cosmos DB)](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels).
- 🛠️ **Do:** In `notes/10-consistency.md` classify 6 features (bank transfer, like counter, seat booking, shopping cart, DNS, chat read receipts) by required consistency and CP/AP choice, each with a one-line failure scenario. Then list all (R, W) pairs for N = 3 and N = 5 that give overlapping quorums and name the conditions they still need. Done when: every choice says what the user would see during a partition.

### Wednesday 16 Dec · 45 min — Elevator system LLD: states and scheduling
- 📚 **Learn:** Entities: `ElevatorSystem`, `ElevatorCar`, `Request` (internal/external), `Direction`, `Door`; states Idle/MovingUp/MovingDown/DoorsOpen; dispatch strategies (nearest car, SCAN/LOOK). Read 'Requirements' and 'Class Design' in [Elevator breakdown (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/elevator). Optional: [Elevator LLD (Concept && Coding, Hindi, 40 min)](https://www.youtube.com/watch?v=9ORcPv_Tbz8).
- 🛠️ **Do:** Write requirements, a class diagram, a `DispatchStrategy` interface and the state enum in `lld/elevator/DESIGN.md`. Trace 3 scenarios on paper: one car with mixed up/down requests; two cars where the nearest wins; a request in the opposite direction while moving. Done when: the diagram is committed and each trace lists the stop order with a one-line reason.

### Thursday 17 Dec · 45 min — Logging framework: Chain of Responsibility + Singleton
- 📚 **Learn:** Levels (DEBUG -> ERROR) with filtering, a handler chain (console -> file -> remote), a pluggable formatter (Strategy), one shared logger (enum singleton or an injected instance), and why real loggers write asynchronously (thread safety waits for the stretch, after Java W8 Fri). Read [Logging service (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/logging-service). Optional: [Logging system with Chain of Responsibility (Concept && Coding, Hindi, 15 min)](https://www.youtube.com/watch?v=gvIn5QBdGDk).
- 🛠️ **Do:** Implement `Logger` (enum singleton) with a minimum level, a chain of `LogHandler`s (`ConsoleHandler`, `InMemoryFileHandler` that stores lines in a list) and a `Formatter` strategy (plain vs JSON-like). Done when: tests pass for level filtering, handler order and swapping the formatter at runtime.

### Saturday 19 Dec · 45 min — PRACTICE: Elevator machine coding (core simulation)
- 📚 **Learn:** Core trick: each car keeps `TreeSet<Integer>` up-stops and down-stops (LOOK); a `step()` tick moves one floor and opens doors at stops; a dispatcher picks the car via a strategy. The simulation is single-threaded and deterministic: the test calls `step()`. Reference: [Elevator problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/elevator-system.md).
- 🛠️ **Do:** 25-min timer from Wednesday's design: code `ElevatorCar` (stop sets, `step()`), `NearestCarStrategy`, `ElevatorSystem.request(floor, direction)` and a tick loop. Done when: >= 4 tests pass: serves up-requests in ascending order, reverses only when no stops remain ahead, an idle car takes the nearest request, doors open at each stop; two cars splitting requests is a stretch.

## 📦 Deliverable (by Saturday night)
`notes/10-consistency.md`, `lld/elevator` (design + core simulation + tests) and `lld/logger` with level, handler-order and formatter tests.

## ✅ Self-check (Sunday test preview)
- State CAP precisely. Why is 'CA' not a real option for a distributed system?
- What does PACELC add to CAP?
- Linearizable vs eventual consistency: name one feature that needs each.
- With N = 3, which R and W values make quorums overlap, what else must hold for a read to see the latest write, and what do you pay?
- Elevator scheduling: how does LOOK differ from SCAN and FCFS?
- How do you make a logger thread-safe without slowing every caller?
- Why must the instance field be `volatile` in double-checked locking (Java W8 Wed)?

## 🚀 Stretch (optional)
After Java W8 Fri: make the logger thread-safe and prove 10 threads x 1,000 messages = exactly 10,000 lines; add a double-checked-locking `getInstance()` with `volatile` ([DCL bug, Concept && Coding, Hindi](https://www.youtube.com/watch?v=upfrQvOgC24)); make your W5 `EventBus` asynchronous with an `ExecutorService`; let two elevator cars split requests. Extra: [Elevator LLD walkthrough (Hello Interview)](https://www.youtube.com/watch?v=fODT0ldeBiU); [Logger LLD (Gaurav Sen)](https://www.youtube.com/watch?v=FKA2KgkkcqY); [CAP theorem (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/cap-theorem).
