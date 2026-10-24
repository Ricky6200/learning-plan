# 🏗️ System Design · Week 14 — Chess, inventory, storage and search (Boss week)

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Uploads, CDNs and search indexes appear in most product designs, and chess/inventory problems test polymorphism and concurrency; the boss proves you can code and design under a timer.

## 🗓️ Sessions

### Monday 25 Jan · 45 min — Object storage, CDN, large uploads, search and geo indexes
- 📚 **Learn:** Object vs block vs file storage; CDN pull vs push, cache keys, invalidation; multipart/chunked + resumable uploads straight to storage with presigned URLs (Azure: SAS, the Valet Key pattern); inverted index, analyzers, Elasticsearch shards/replicas; geohash/quadtree preview (deep dive in W21). Watch [Object storage (Hello Interview)](https://www.youtube.com/watch?v=RvaMHMxHjp4); read [Valet Key pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key) and [Elasticsearch deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/elasticsearch).
- 🛠️ **Do:** In `notes/17-storage-search.md`: (1) sequence diagram for a 2 GB video upload with chunking, resume and a presigned/SAS URL; (2) an inverted index built by hand for 4 short movie blurbs, answering one AND query; (3) one paragraph on geohash vs quadtree. Done when: file bytes never pass through your app servers and you can explain how Elasticsearch routes a query to shards.

### Wednesday 27 Jan · 45 min — Chess LLD (or Cricbuzz): design + move rules
- 📚 **Learn:** Entities: `Game`, `Board`, `Cell`, abstract `Piece` with subclasses implementing `canMove`, `Player`, `Move`, `GameStatus`; polymorphic move rules, Command for move history/undo; check detection as awareness. Watch [Chess LLD (Gaurav Sen)](https://www.youtube.com/watch?v=I-iZbOVXwxg); Hindi: [Chess LLD mock (Concept && Coding)](https://www.youtube.com/watch?v=kk6QkWxz5jM); alternative problem: [Cricbuzz LLD (Concept && Coding)](https://www.youtube.com/watch?v=P0TJIONZi8E).
- 🛠️ **Do:** 10 min class diagram, 35 min code: `Piece.canMove(board, from, to)` for King, Rook, Bishop, Knight and Queen (Rook + Bishop), path-blocking checks, turn alternation and captures. Done when: tests pass for legal/illegal moves per piece, a blocked path, and capturing your own piece being rejected; pawns and castling are stretch.

### Thursday 28 Jan · 45 min — Inventory & order management core + Bloom filter lab
- 📚 **Learn:** Inventory: stock per SKU per warehouse, all-or-nothing `reserve(orderId, items)` with TTL, `confirm`/`release`, order state machine (CREATED -> RESERVED -> PAID -> SHIPPED, or CANCELLED). Bloom filter: bit array + k hashes, no false negatives, tunable false-positive rate. Hindi: [Inventory management LLD (Concept && Coding)](https://www.youtube.com/watch?v=DDKdMTFNvxc); watch [Bloom filters (ByteByteGo)](https://www.youtube.com/watch?v=V3pzxngeLqw).
- 🛠️ **Do:** 30 min: `InventoryService.reserve/confirm/release` reusing your W10 seat-hold locking ideas, plus an `Order` state machine; test that 50 threads ordering the last 10 units never oversell. 15 min: `labs/bloom/BloomFilter` (`BitSet`, double hashing); add 10k keys and measure the false-positive rate on 10k other keys. Done when: no oversell and the measured FP rate is within 2x of theory.

### Saturday 30 Jan · 45 min — BOSS BATTLE: 35-min machine coding + verbal Pastebin HLD
- 📚 **Learn:** Boss rules: your AI mentor (or a dice roll) picks one problem from Tic-Tac-Toe, Snake & Ladder, Parking Lot, Vending Machine, Elevator, Splitwise, BookMyShow, ATM, meeting rooms, Chess, inventory; code its core from a blank package in 35 min, then pitch a Pastebin HLD for 10 min. Reference: [Pastebin solution (system-design-primer)](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md).
- 🛠️ **Do:** 0-35 min: requirements (3 min), class sketch (5 min), core code + >= 4 tests. 35-45 min: talk through Pastebin (requirements, estimate, API, storage of pastes in object storage, key generation, cache, expiry cleanup) while recording. Score 0-3 each: working code, design quality, tests, HLD structure, trade-offs. Done when: `boss/W14.md` has the score; >= 10/15 clears the boss.

## 📦 Deliverable (by Saturday night)
`notes/17-storage-search.md`, `lld/chess`, `lld/inventory`, `labs/bloom` with tests, and the Boss score + recording in `boss/W14.md`.

## ✅ Self-check (Sunday test preview)
- Why upload large files with presigned/SAS URLs instead of through your API servers?
- How does a CDN decide what to cache, and how do you invalidate content?
- Explain an inverted index and how Elasticsearch scales it with shards and replicas.
- Bloom filter: why can't it give false negatives, and how do you size it?
- Chess: how does polymorphism keep move validation clean?
- How do you prevent overselling the last unit of stock under concurrency?
- Geohash vs quadtree: what is the difference at a high level?

## 🚀 Stretch (optional)
Add pawn moves, castling and check detection to Chess, or build the Cricbuzz scoreboard (Observer for live score updates).
