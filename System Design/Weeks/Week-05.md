# 🏗️ System Design · Week 05 — Behavioral patterns and choosing databases

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** Strategy, Observer and State are the most-used patterns in machine-coding solutions, and 'which database and why?' is asked in every HLD round.

## 🗓️ Sessions

### Monday 23 Nov · 45 min — SQL vs NoSQL, ACID vs BASE, choosing a database
- 📚 **Learn:** Families: relational, key-value, document, wide-column, graph, time-series, search, vector. ACID vs BASE; isolation levels in one line each; choose by access pattern, consistency, scale, joins, schema flexibility. Watch [How to choose the right database (ByteByteGo)](https://www.youtube.com/watch?v=kkeFE6iRfMM); read [Choose a data store (Azure Architecture Center)](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-overview); Hindi: [SQL vs NoSQL (Concept && Coding)](https://www.youtube.com/watch?v=fG8c-huFt70).
- 🛠️ **Do:** Create `notes/05-databases.md`: a matrix (family, example, data model, strengths, weaknesses, typical use) and pick a store for 6 TicketVerse needs: bookings/payments, seat holds, event search, user sessions, activity feed, metrics. Done when: each pick names the access pattern and consistency need that drove it, plus one rejected alternative and why.

### Wednesday 25 Nov · 45 min — Behavioral I: Strategy, Observer, Command, State
- 📚 **Learn:** Strategy (swap algorithms; `Comparator`), Observer (in-process publish/subscribe; push vs pull), Command (requests as objects: undo/redo, queues), State (state objects replace a giant switch). Read [Strategy](https://refactoring.guru/design-patterns/strategy) and [State](https://refactoring.guru/design-patterns/state) (refactoring.guru); Hindi: [Command pattern undo/redo (Concept && Coding)](https://www.youtube.com/watch?v=E1lce5CWhE0).
- 🛠️ **Do:** Implement (1) a `TextEditor` with Command objects and undo/redo via two `Deque`s; (2) a `Document` state machine Draft -> InReview -> Published with `publish()`/`reject()` per state; (3) a `SortStrategy` swap demo. Done when: tests cover 3-level undo/redo and every illegal transition throws `IllegalStateException`.

### Thursday 26 Nov · 45 min — Behavioral II: Template, Chain, Iterator, Mediator, Memento, Visitor
- 📚 **Learn:** Template Method (fixed skeleton, overridable steps), Chain of Responsibility (servlet filters, Spring Security filter chain), Iterator, Mediator (central coordinator: chat room), Memento (snapshots), Visitor (double dispatch; awareness only). Read [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility) and [Template Method](https://refactoring.guru/design-patterns/template-method); Hindi: [All behavioral patterns (Concept && Coding)](https://www.youtube.com/watch?v=DBDnUkTobaE).
- 🛠️ **Do:** Implement a support-ticket escalation chain (L1 -> L2 -> Manager by severity) and a `ReportExporter` template method (CSV/JSON). Then fill `notes/06-behavioral.md` with 9 rows (pattern, intent, real Java/Spring example, smell it fixes). Done when: chain + template tests pass and the table has no empty cells.

### Saturday 28 Nov · 45 min — PRACTICE: Strategy + Observer kata (pricing + notifications)
- 📚 **Learn:** Kata: runtime-selectable pricing strategies plus event observers with failure isolation (one bad listener must not break checkout). Reference: [Observer (refactoring.guru)](https://refactoring.guru/design-patterns/observer); Hindi: [Strategy pattern (Concept && Coding)](https://www.youtube.com/watch?v=u8DttUrXtEw).
- 🛠️ **Do:** Tests first. `Checkout` uses a `PricingStrategy` (Regular, Festive 20% off, Bulk >= 5 tickets 10% off, Surge x1.5) chosen at runtime and publishes `OrderPlaced` to an `EventBus` with Email, SMS and Analytics listeners; support unsubscribe; a throwing listener is logged and skipped. Done when: >= 6 tests pass (each strategy, runtime swap, all listeners notified, failing listener isolated).

## 📦 Deliverable (by Saturday night)
`notes/05-databases.md`, `notes/06-behavioral.md`, behavioral pattern code with tests, and the pricing + notifications kata with >= 6 green tests.

## ✅ Self-check (Sunday test preview)
- SQL or NoSQL for a booking system? Defend your answer.
- Explain ACID vs BASE with one real example of each.
- When would you choose a wide-column store like Cassandra?
- Strategy vs State look alike in code. How do they differ?
- How does the Command pattern make undo/redo possible?
- Where does Chain of Responsibility appear in Spring?
- How do you stop one slow or failing observer from hurting the others?

## 🚀 Stretch (optional)
Make the `EventBus` asynchronous with an `ExecutorService` and write a test that checks per-listener ordering.
