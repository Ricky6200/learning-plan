# 🏗️ System Design · Week 06 — Machine-coding method, indexing, replication

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** A repeatable machine-coding method turns 'I understand code' into 'I can write it under time pressure'; indexes and replication explain most database performance and consistency answers.

## 🗓️ Sessions

### Monday 30 Nov · 45 min — Indexing: B-tree vs LSM-tree vs hash indexes
- 📚 **Learn:** B+tree (pages, in-place updates, read-optimised: Postgres/MySQL), LSM-tree (memtable + WAL -> SSTables, compaction, Bloom filters; write-optimised: Cassandra/RocksDB), hash index; composite column order, covering index, read vs write amplification. Watch [DB indexing (Hello Interview, 14 min)](https://www.youtube.com/watch?v=BHCSL_ZifI0). Optional: [LSM tree (ByteByteGo, 8 min)](https://www.youtube.com/watch?v=I6jB0nM9SKU).
- 🛠️ **Do:** In `notes/07-indexing.md` answer 4 scenarios: (1) index for `WHERE city = ? AND show_date BETWEEN ? AND ?`; (2) covering index for a 'my bookings' list; (3) engine for 50k writes/sec of click logs; (4) why too many indexes slow inserts. Sketch a B+tree lookup and an LSM write path. Done when: each answer states the column order or engine and the read/write trade-off.

### Wednesday 02 Dec · 45 min — Machine-coding framework + Tic-Tac-Toe
- 📚 **Learn:** The 90-min playbook in your `LLD_MACHINE_CODING_FRAMEWORK.md`: clarify -> entities -> class diagram + patterns -> code core -> tests/demo -> refactor (today you use its compressed version). Tic-Tac-Toe: N x N board, players, O(1) win check with row/column/diagonal counters. Watch [Tic-Tac-Toe LLD (Gaurav Sen, 16 min)](https://www.youtube.com/watch?v=gktZsX9Z8Kw). Optional: [Tic-Tac-Toe LLD (Concept && Coding, Hindi, 20 min)](https://www.youtube.com/watch?v=x8N3fINNdTE).
- 🛠️ **Do:** 5 min: requirements + entities (`Game`, `Board`, `Player`, `Move`, `GameStatus`) sketched in `lld/tictactoe/DESIGN.md`. 20 min: code `Board.place()` with O(1) win detection (row/column/diagonal counters, +1 for X and -1 for O) and a `Game` that alternates turns. Done when: tests pass for row, column, diagonal and anti-diagonal wins, a draw and occupied-cell rejection; extras such as undo go to the stretch.

### Thursday 03 Dec · 45 min — Replication: leader-follower, multi-leader, leaderless, lag
- 📚 **Learn:** Single-leader (sync vs async vs semi-sync followers, failover, split brain), multi-leader (write conflicts, last-write-wins), leaderless (quorums, read repair). Lag anomalies: read-your-writes, monotonic reads, and their fixes. Read [Leader and Followers (Patterns of Distributed Systems)](https://martinfowler.com/articles/patterns-of-distributed-systems/leader-follower.html). Optional: [All types of database replication (Hussein Nasser, 19 min)](https://www.youtube.com/watch?v=aE2UPg3Ckck).
- 🛠️ **Do:** Draw the 3 topologies (write and read arrows) and add a table: anomaly -> user-visible symptom -> fix (read from leader for 60 s after a write, sticky reads, version tokens). Save as `notes/08-replication.md`. Done when: you can answer 'user updates profile, refreshes, sees old data - why, and how do you fix it?' in under a minute.

### Saturday 05 Dec · 45 min — PRACTICE: Snake & Ladder machine coding
- 📚 **Learn:** Apply the compressed playbook to a small problem: board with a snakes/ladders map, a dice strategy, a player queue, game loop, winner. Read the requirements in [Snake and Ladder problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/snake-and-ladder.md) and sketch your classes before starting the timer. Optional: [Snake & Ladder LLD (Concept && Coding, Hindi, 32 min)](https://www.youtube.com/watch?v=88bcV-XV0wo).
- 🛠️ **Do:** 25-min timer: `Board` with a `Map<Integer, Integer>` of jumps, a `Dice` interface with `RandomDice`/`FixedDice`, and a `Game` with an `ArrayDeque<Player>` turn queue. Done when: tests prove snake bite, ladder climb, overshooting 100 means no move, and a deterministic winner with `FixedDice`; leftovers go to the stretch.

## 📦 Deliverable (by Saturday night)
`notes/07-indexing.md`, `notes/08-replication.md` (with diagram), and `lld/tictactoe` + `lld/snakeladder` with passing tests.

## ✅ Self-check (Sunday test preview)
- B-tree vs LSM-tree: which suits write-heavy workloads, and why?
- What is a covering index, and when does column order in a composite index matter?
- Synchronous vs asynchronous replication: what do you trade?
- What is replication lag, and how do you guarantee read-your-writes?
- Leaderless replication: how do quorum reads and read repair work?
- In Tic-Tac-Toe, how do you detect a win in O(1) per move?

## 🚀 Stretch (optional)
Now that lambdas exist (Java W6 Mon), rewrite your W3 payment registry as `Map<PaymentType, Supplier<PaymentProcessor>>` filled with constructor references (`UpiProcessor::new`) so each call gets a fresh processor. Add multiple dice or a crooked-dice strategy to Snake & Ladder. Skim [Use The Index, Luke](https://use-the-index-luke.com/); Postgres `EXPLAIN` with and without your composite index is Codespaces only until Docker arrives (Java W11).
