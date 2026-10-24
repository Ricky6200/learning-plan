# 🏗️ System Design · Week 06 — Machine-coding method, indexing, replication

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** A repeatable 90-minute machine-coding method turns 'I understand code' into 'I can write it under time pressure'; indexes and replication explain most database performance and consistency answers.

## 🗓️ Sessions

### Monday 30 Nov · 45 min — Indexing: B-tree vs LSM-tree vs hash indexes
- 📚 **Learn:** B+tree (pages, in-place updates, read-optimised: Postgres/MySQL), LSM-tree (memtable + WAL -> SSTables, compaction, Bloom filters; write-optimised: Cassandra/RocksDB), hash index; composite column order, covering index, read vs write amplification. Watch [DB indexing (Hello Interview)](https://www.youtube.com/watch?v=BHCSL_ZifI0) and [LSM tree (ByteByteGo)](https://www.youtube.com/watch?v=I6jB0nM9SKU); reference: [Use The Index, Luke](https://use-the-index-luke.com/).
- 🛠️ **Do:** In `notes/07-indexing.md` answer 4 scenarios: (1) index for `WHERE city = ? AND show_date BETWEEN ? AND ?`; (2) covering index for a 'my bookings' list; (3) engine for 50k writes/sec of click logs; (4) why too many indexes slow inserts. Sketch a B+tree lookup and an LSM write path. Done when: each answer states the column order or engine and the read/write trade-off.

### Wednesday 02 Dec · 45 min — Machine-coding framework + Tic-Tac-Toe
- 📚 **Learn:** The 90-min playbook in your `LLD_MACHINE_CODING_FRAMEWORK.md`: clarify -> entities -> class diagram + patterns -> code core -> tests/demo -> refactor. Tic-Tac-Toe: N x N board, players, O(1) win check with row/column/diagonal counters. Watch [Tic-Tac-Toe LLD (Gaurav Sen)](https://www.youtube.com/watch?v=gktZsX9Z8Kw); Hindi: [Tic-Tac-Toe LLD (Concept && Coding)](https://www.youtube.com/watch?v=x8N3fINNdTE).
- 🛠️ **Do:** Run a compressed playbook: 5 min requirements, 5 min entities (`Game`, `Board`, `Player`, `Move`, `GameStatus`), 5 min class diagram, 30 min code `Board.place()` + O(1) win detection + `Game` turn loop. Done when: tests pass for row, column, diagonal and anti-diagonal wins, draw and occupied-cell rejection, and diagram + code are committed in `lld/tictactoe`.

### Thursday 03 Dec · 45 min — Replication: leader-follower, multi-leader, leaderless, lag
- 📚 **Learn:** Single-leader (sync vs async vs semi-sync followers, failover, split brain), multi-leader (write conflicts, last-write-wins), leaderless (quorums, read repair). Lag anomalies: read-your-writes, monotonic reads, and their fixes. Watch [All types of database replication (Hussein Nasser)](https://www.youtube.com/watch?v=aE2UPg3Ckck); read [Leader and Followers (Patterns of Distributed Systems)](https://martinfowler.com/articles/patterns-of-distributed-systems/leader-follower.html).
- 🛠️ **Do:** Draw the 3 topologies (write and read arrows) and add a table: anomaly -> user-visible symptom -> fix (read from leader for 60 s after a write, sticky reads, version tokens). Save as `notes/08-replication.md`. Done when: you can answer 'user updates profile, refreshes, sees old data - why, and how do you fix it?' in under a minute.

### Saturday 05 Dec · 45 min — PRACTICE: Snake & Ladder machine coding
- 📚 **Learn:** Apply the full playbook on a small problem: board with a snakes/ladders map, dice strategy, player queue, game loop, winner. References: [Snake and Ladder problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/snake-and-ladder.md); Hindi: [Snake & Ladder LLD (Concept && Coding)](https://www.youtube.com/watch?v=88bcV-XV0wo).
- 🛠️ **Do:** 5 min requirements, 5 min diagram, 30 min code (`Board` with a `Map<Integer, Integer>` of jumps, `Dice` interface with `RandomDice`/`FixedDice`, `Game` with a `Deque<Player>`), 5 min tests. Done when: tests prove snake bite, ladder climb, overshooting 100 means no move, and a deterministic winner with `FixedDice`; finish leftovers as stretch.

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
Add multiple dice and a 'crooked dice' strategy to Snake & Ladder, or run `EXPLAIN` on a Postgres table with and without your composite index.
