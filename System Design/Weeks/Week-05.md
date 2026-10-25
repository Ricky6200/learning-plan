# 🏗️ System Design · Week 05 — Behavioral patterns and choosing databases

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** Strategy, Observer and State are the most-used patterns in machine-coding solutions, and 'which database and why?' is asked in every HLD round.

## 🗓️ Sessions

### Monday 23 Nov · 45 min — SQL vs NoSQL, ACID vs BASE, choosing a database
- 📚 **Learn:** Families: relational, key-value, document, wide-column, graph, time-series, search, vector. ACID vs BASE; isolation levels in one line each; choose by access pattern, consistency, scale, joins, schema flexibility. Watch [How to choose the right database (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=kkeFE6iRfMM). Optional: [Choose a data store (Azure Architecture Center)](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-overview).
- 🛠️ **Do:** Create `notes/05-databases.md`: a matrix (family, example, data model, strengths, weaknesses, typical use) and pick a store for 6 TicketVerse needs: bookings/payments, seat holds, event search, user sessions, activity feed, metrics. Done when: each pick names the access pattern and consistency need that drove it, plus one rejected alternative and why.

### Wednesday 25 Nov · 45 min — Behavioral I: Strategy, Observer, Command, State
- 📚 **Learn:** Strategy (swap algorithms; the `Comparator` from Java W4 Fri is one), Observer (in-process publish/subscribe; push vs pull), Command (requests as objects: undo/redo, queues), State (state objects replace a giant switch). Read [State (refactoring.guru)](https://refactoring.guru/design-patterns/state). Optional: [Command pattern undo/redo (Concept && Coding, Hindi, 25 min)](https://www.youtube.com/watch?v=E1lce5CWhE0).
- 🛠️ **Do:** Implement (1) a `TextEditor` with `Command` objects (`TypeCommand`, `DeleteCommand`) and undo/redo via two `ArrayDeque`s (Java W5); (2) a `Document` state machine Draft -> InReview -> Published with `publish()`/`reject()` implemented per state class. Done when: tests cover 3-level undo/redo (a new command clears redo) and every illegal transition throws `IllegalStateException`.

### Thursday 26 Nov · 45 min — Behavioral II: Template, Chain, Iterator, Mediator, Memento, Visitor
- 📚 **Learn:** Template Method (fixed skeleton, overridable steps), Chain of Responsibility (a request passes handlers in order: auth check -> rate limit -> logging filters, or L1 -> L2 -> manager support escalation), Iterator, Mediator (central coordinator: chat room), Memento (snapshots), Visitor (double dispatch; awareness only). Read [Chain of Responsibility (refactoring.guru)](https://refactoring.guru/design-patterns/chain-of-responsibility). Optional: [All behavioral patterns (Concept && Coding, Hindi, 47 min)](https://www.youtube.com/watch?v=DBDnUkTobaE).
- 🛠️ **Do:** Implement a support-ticket escalation chain (L1 -> L2 -> Manager by severity; each handler passes on what it cannot handle) and a `ReportExporter` template method with CSV and JSON subclasses. Then start `notes/06-behavioral.md` with one row per pattern coded so far (pattern, intent, real Java example, smell it fixes). Done when: chain + template tests pass and the rows have no empty cells.

### Saturday 28 Nov · 45 min — PRACTICE: Strategy + Observer kata (pricing + notifications)
- 📚 **Learn:** Kata: runtime-selectable pricing strategies plus event observers with failure isolation (one bad listener must not break checkout: catch, log, continue). Listeners may be written as lambdas now (Java W4 Fri primer). Read [Observer (refactoring.guru)](https://refactoring.guru/design-patterns/observer). Optional: [Strategy pattern (Concept && Coding, Hindi, 17 min)](https://www.youtube.com/watch?v=u8DttUrXtEw).
- 🛠️ **Do:** Tests first. `Checkout` uses a `PricingStrategy` (Regular, Festive 20% off, Bulk >= 5 tickets 10% off) chosen at runtime and publishes `OrderPlaced` to an `EventBus` with Email and Analytics listeners; support unsubscribe; a throwing listener is logged and skipped. Done when: >= 5 tests pass (each strategy, runtime swap, all listeners notified, failing listener isolated).

## 📦 Deliverable (by Saturday night)
`notes/05-databases.md`, `notes/06-behavioral.md`, behavioral pattern code with tests, and the pricing + notifications kata with >= 5 green tests.

## ✅ Self-check (Sunday test preview)
- SQL or NoSQL for a booking system? Defend your answer.
- Explain ACID vs BASE with one real example of each.
- When would you choose a wide-column store like Cassandra?
- Strategy vs State look alike in code. How do they differ?
- How does the Command pattern make undo/redo possible?
- Give two real examples of Chain of Responsibility (request filters, support escalation).
- How do you stop one slow or failing observer from hurting the others?

## 🚀 Stretch (optional)
Complete the behavioral table (Strategy, Observer, Iterator, Mediator, Memento, Visitor), add a Surge x1.5 strategy, and read [Strategy](https://refactoring.guru/design-patterns/strategy) + [Template Method](https://refactoring.guru/design-patterns/template-method). Hindi: [SQL vs NoSQL (Concept && Coding)](https://www.youtube.com/watch?v=fG8c-huFt70).
