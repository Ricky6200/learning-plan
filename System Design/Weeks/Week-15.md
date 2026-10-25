# 🏗️ System Design · Week 15 — Chess, inventory, blobs and CDN (Boss week)

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** Uploads and CDNs appear in most product designs, and chess/inventory problems test polymorphism and concurrency; the Season 3 boss proves you can code and design under a timer.

## 🗓️ Sessions

### Monday 01 Feb · 45 min — Object storage, CDN and large uploads
- 📚 **Learn:** Object vs block vs file storage; CDN pull vs push, cache keys, invalidation; multipart/chunked + resumable uploads straight to storage with presigned URLs (Azure: SAS tokens, the Valet Key pattern); metadata in a DB, bytes in blob storage; downloads served via CDN. Read [Handling large blobs (Hello Interview)](https://www.hellointerview.com/learn/system-design/patterns/large-blobs). Optional: [Object storage (Hello Interview, 13 min)](https://www.youtube.com/watch?v=RvaMHMxHjp4).
- 🛠️ **Do:** In `notes/17-blobs-cdn.md`: (1) a sequence diagram for a 2 GB video upload with chunking, resume after failure at 60%, and a presigned/SAS URL; (2) a download path through a CDN with cache key, TTL and invalidation on re-upload; (3) where metadata vs bytes live. Done when: file bytes never pass through your app servers and you can explain what the client does when the upload fails halfway.

### Wednesday 03 Feb · 45 min — Chess LLD: design + core move rules
- 📚 **Learn:** Entities: `Game`, `Board`, `Cell`, abstract `Piece` with subclasses implementing `canMove`, `Player`, `Move`, `GameStatus`; polymorphic move rules, Command for move history/undo; check detection as awareness. Read the requirements in [Chess game problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/chess-game.md). Optional: [Chess LLD mock (Concept && Coding, Hindi, 67 min)](https://www.youtube.com/watch?v=kk6QkWxz5jM).
- 🛠️ **Do:** 5 min class diagram, 20 min code: `Piece.canMove(board, from, to)` for King, Rook and Knight, path-blocking for the Rook, turn alternation and captures. Done when: tests pass for legal/illegal moves of the three pieces, a blocked Rook path, and capturing your own piece being rejected; Bishop, Queen, pawns and castling are extension questions.

### Thursday 04 Feb · 45 min — Inventory & order management core
- 📚 **Learn:** Inventory: stock per SKU per warehouse, all-or-nothing `reserve(orderId, items)` with a TTL, `confirm`/`release`, order state machine (CREATED -> RESERVED -> PAID -> SHIPPED, or CANCELLED); per-SKU locks taken in sorted order (W10 Mon). Read 'Requirements', 'Class Design' and the overselling question in [Inventory management (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/inventory-management). Optional: [Inventory management LLD (Concept && Coding, Hindi, 39 min)](https://www.youtube.com/watch?v=DDKdMTFNvxc).
- 🛠️ **Do:** `InventoryService.reserve/confirm/release` reusing your W11 seat-hold ideas, plus the `Order` state machine. Done when: tests prove 50 threads ordering the last 10 units never oversell, an expired reservation returns stock, and an illegal order transition throws; the Bloom-filter lab moves to the stretch.

### Saturday 06 Feb · 45 min — BOSS BATTLE: 35-min machine coding + verbal Pastebin HLD
- 📚 **Learn:** Boss rules: your AI mentor (or a dice roll) picks one Season 3 problem - car rental, file system, BookMyShow seat holds, rate limiter, pub-sub, job scheduler, ATM, meeting rooms, Chess, inventory; code its core from a blank package in 35 min, then pitch a Pastebin HLD for 10 min. Reference (after the pitch): [Pastebin solution (system-design-primer)](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md).
- 🛠️ **Do:** 0-35 min: requirements (3 min), class sketch (5 min), core code + >= 4 tests. 35-45 min: talk through Pastebin (requirements, estimate, API, pastes in object storage, key generation, cache, expiry cleanup) while recording. Score 0-3 each: working code, design quality, tests, HLD structure, trade-offs. Done when: `boss/W15.md` has the score; >= 10/15 clears the boss.

## 📦 Deliverable (by Saturday night)
`notes/17-blobs-cdn.md`, `lld/chess`, `lld/inventory` with tests, and the Boss score + recording in `boss/W15.md`. Sunday mini-design: turn your boss pitch into a full-template `hld/mini/W15-pastebin.md`.

## ✅ Self-check (Sunday test preview)
- Why upload large files with presigned/SAS URLs instead of through your API servers?
- How do resumable (chunked) uploads recover from a failure at 99%?
- How does a CDN decide what to cache, and how do you invalidate content?
- Chess: how does polymorphism keep move validation clean?
- How do you prevent overselling the last unit of stock under concurrency?
- Pastebin: where do you store paste bodies vs metadata, and how do you clean up expired pastes?

## 🚀 Stretch (optional)
Bloom-filter lab: `labs/bloom/BloomFilter` (`BitSet`, double hashing); add 10k keys and check the false-positive rate on 10k others is within 2x of theory ([Bloom filters (ByteByteGo)](https://www.youtube.com/watch?v=V3pzxngeLqw)). Read [Change data capture (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/change-data-capture) and the [Valet Key pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key). Chess: add Bishop, Queen, pawns and castling ([Chess LLD (Gaurav Sen)](https://www.youtube.com/watch?v=I-iZbOVXwxg)), or build a Cricbuzz scoreboard with Observer for live score updates ([Cricbuzz LLD (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=P0TJIONZi8E)).
