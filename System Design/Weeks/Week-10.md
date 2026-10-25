# 🏗️ System Design · Week 10 — LLD under time pressure: mock + file system

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Machine-coding rounds are 90-minute marathons: this week turns Java W8-W9 concurrency into LLD habits and runs your first full-length unseen mock while Season 2 is fresh. New Year's Day is Friday 1 Jan - SD has no Friday session, so the week runs as normal.

## 🗓️ Sessions

### Monday 28 Dec · 45 min — Concurrency for LLD: lock per aggregate, lock ordering, queues
- 📚 **Learn:** LLD concurrency checklist: find the shared mutable state; guard each aggregate (one floor, one show) with its own lock instead of one global lock; take several locks in a fixed order (sorted ids) to avoid deadlock; use `ConcurrentHashMap.compute/merge/putIfAbsent` for atomic check-then-act; hand work between threads with a `BlockingQueue` (producer-consumer, Java W8). Read [Concurrency in LLD (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/concurrency/intro). Optional: [Concurrency in LLD interviews (Hello Interview, 23 min)](https://www.youtube.com/watch?v=d8rmosXttTE).
- 🛠️ **Do:** Multi-gate Parking Lot: make your W7 `park()`/`unpark()` safe when 4 entry gates call them at once - one lock per `Floor`, and `ConcurrentHashMap.remove(ticketId)` for unpark. Race test: 4 gate threads park 200 cars into 100 spots, started together by a `CountDownLatch`. Done when: exactly 100 cars park, no spot holds two cars, the test passes 10 runs in a row, and `lld/parkinglot/CONCURRENCY.md` names the lock that guards each piece of state.

### Wednesday 30 Dec · 45 min — Unseen mock part 1: car rental CLI (minutes 0-45)
- 📚 **Learn:** Mock rules: one 90-minute mock split over today and Thursday, no references, the playbook clock from `LLD_MACHINE_CODING_FRAMEWORK.md` (0-10 clarify, 10-30 entities + class diagram, 30-45 start the core). Input arrives as commands on standard input: read line by line with `BufferedReader` or `Scanner` (Java W1 Sat) and split on spaces. Read only after Thursday: [Car rental problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/car-rental-system.md).
- 🛠️ **Do:** Problem: a car-rental CLI. Commands: `ADD_BRANCH <id> <city>`, `ADD_CAR <branch> <carId> <type> <pricePerDay>`, `SEARCH <city> <type> <fromDay> <toDay>` (cheapest first), `BOOK <user> <carId> <fromDay> <toDay>`, `CANCEL <bookingId>`, `RETURN <bookingId> <day>` (late days cost 1.5x). Today: assumptions in `lld/mock-w10/DESIGN.md`, class diagram, model classes and a command parser dispatching to a `RentalService`. Done when: the design is committed and `ADD_BRANCH`/`ADD_CAR` work end to end from a sample input file.

### Thursday 31 Dec · 45 min — Unseen mock part 2: car rental (minutes 45-90) + scoring
- 📚 **Learn:** Second half of the clock: 45-70 core rules (overlap check `from <= otherTo && otherFrom <= to`, cheapest-first search with a `Comparator`, late fee), 70-80 tests or a scripted input file, 80-90 refactor + README of assumptions. Score yourself 0-3 on requirements, model, patterns, working code, tests, extensibility, communication. Afterwards compare your flow with [Delivery (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/delivery).
- 🛠️ **Do:** Finish `SEARCH`, `BOOK`, `CANCEL` and `RETURN`, then run a 12-line input file that books, rejects an overlapping booking, cancels and returns late; afterwards read the awesome-low-level-design write-up and note 3 gaps. Done when: the output matches your expected output, the 7-line scorecard is in `mocks/W10-lld.md`, and 2 extension answers (new car type, weekend pricing) are written.

### Saturday 02 Jan · 45 min — PRACTICE: In-memory file system (Composite + path parsing)
- 📚 **Learn:** Composite again (W4 Thu): an `Entry` with `Directory` and `File`; a directory keeps children in a `TreeMap<String, Entry>` so listings are sorted. Path parsing: split on `/`, skip empty parts, walk from the root; `mkdir` creates missing parents. Read 'Requirements' and 'Class Design' in [File system (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/file-system). Optional: [File system with Composite (Concept && Coding, Hindi, 22 min)](https://www.youtube.com/watch?v=FLkCkUY7Wu0).
- 🛠️ **Do:** 25-min timer: `FileSystem` with `mkdir(path)` (creates parents), `ls(path)` (sorted names; a file path lists just that file), `addContent(path, text)` (creates or appends) and `read(path)`. Done when: tests pass for nested `mkdir`, `ls` on root/directory/file, append twice then read, and a missing path throwing a clear exception; move/rename and size totals go to the stretch.

## 📦 Deliverable (by Saturday night)
`lld/parkinglot/CONCURRENCY.md` + the multi-gate race test, the car-rental mock (`lld/mock-w10/`, input file, scorecard in `mocks/W10-lld.md`) and `lld/filesystem` with passing tests.

## ✅ Self-check (Sunday test preview)
- How do you choose lock granularity in an LLD problem (one global lock vs one per aggregate)?
- Two threads need locks on seats 5 and 9. How do you avoid deadlock?
- Which `ConcurrentHashMap` methods give atomic check-then-act, and why is `containsKey` + `put` unsafe?
- Where would a `BlockingQueue` (producer-consumer) appear in a machine-coding solution?
- In your car-rental mock, how do you detect overlapping bookings?
- What did you spend too long on in the 90-minute mock, and what will you cut next time?
- How does Composite keep `ls` uniform for files and directories?

## 🚀 Stretch (optional)
Add `move`/`rename` and `size(path)` to the file system and a weekend-pricing strategy to car rental. Read [Concurrency: correctness (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/concurrency/correctness) and classify each bug you fixed in the parking lot as check-then-act or read-modify-write. From W11 on, inject `java.time.Clock` (Java W7 Thu) instead of your own `TimeSource`: `Clock.fixed` and `Clock.offset` make expiry tests deterministic ([Clock docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/Clock.html)).
