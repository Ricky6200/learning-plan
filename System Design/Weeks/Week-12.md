# 🏗️ System Design · Week 12 — HLD method, estimation, IDs, URL shortener

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** A fixed HLD framework plus fast estimation is what makes you sound like an SDE-2; the URL shortener is the canonical first case study and introduces ID generation.

## 🗓️ Sessions

### Monday 11 Jan · 45 min — HLD interview framework + back-of-the-envelope estimation
- 📚 **Learn:** The 7-step framework in your `HLD_INTERVIEW_FRAMEWORK.md` (requirements -> estimation -> API -> data model -> diagram -> deep dives -> trade-offs) and its time splits. Estimation: powers of 2, latency numbers, QPS = DAU x actions / 86,400 x peak factor, storage = items/day x size x retention x replicas. Watch [System design interview: step by step (ByteByteGo, 10 min)](https://www.youtube.com/watch?v=i7twT3x5yv8). Optional: [Back-of-the-envelope estimation (ByteByteGo, 9 min)](https://www.youtube.com/watch?v=UC5xf8FbdJc).
- 🛠️ **Do:** Solve 3 drills in `notes/13-estimation.md`, with units: (1) 100M DAU x 20 feed reads/day -> average and peak QPS; (2) 5M photo uploads/day x 2 MB for 5 years with 3 replicas -> storage; (3) 1M concurrent chat users sending 1 message per 10 s -> writes/s and bandwidth at 1 KB/message. Done when: each answer is within 2x of your AI mentor's check and you can do drill 1 aloud in 2 minutes.

### Wednesday 13 Jan · 45 min — Unique ID generation: UUID, ticket server, Snowflake
- 📚 **Learn:** Requirements: unique, roughly time-sortable, 64-bit, no coordination, high rate. Options: DB auto-increment with offsets, Flickr ticket server, UUIDv4 (random, fragments B-tree indexes) vs UUIDv7 (time-ordered), Snowflake (41-bit ms timestamp, 10-bit worker, 12-bit sequence); clock-skew handling. Read [Flickr ticket servers](https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/). Optional: [original Snowflake README (Twitter archive)](https://github.com/twitter-archive/snowflake/tree/snowflake-2010).
- 🛠️ **Do:** Implement `labs/idgen/SnowflakeIdGenerator` (custom epoch, workerId 0-1023, sequence 0-4095, wait for the next millisecond on overflow, throw if the clock moves backwards) with an injected clock, plus `decode(id)`. Done when: tests prove 1M IDs from one thread are unique and increasing, 8 threads produce no duplicates, and decode returns the original timestamp and worker.

### Thursday 14 Jan · 45 min — Case study #1: URL shortener (25-min solo design)
- 📚 **Learn:** FR: shorten, redirect, custom alias, expiry. NFR: low-latency redirects, ~100:1 read:write, high availability. Key generation (counter + Base62, hash + collision check, pre-generated key pool), 301 vs 302, caching hot links, async click analytics. Watch [How a URL shortener works (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=HHUi8F_qAXM). Optional: [URL shortener (Concept && Coding, Hindi, 32 min)](https://www.youtube.com/watch?v=C7_--hAhiaM).
- 🛠️ **Do:** Timer on, 25 minutes solo: fill all 7 sections of the write-up template from `HLD_INTERVIEW_FRAMEWORK.md` in `hld/01-url-shortener/README.md` (bullets are fine; include the estimation and a box diagram). Done when: every section has content and you have marked your 2 weakest sections for Saturday.

### Saturday 16 Jan · 45 min — PRACTICE: URL shortener review + Base62 implementation
- 📚 **Learn:** Base62 (0-9, a-z, A-Z): 7 characters give 62^7 ~ 3.5 trillion codes, and encoding a unique number is collision-free. A 64-bit Snowflake ID needs 10-11 Base62 characters, so for 7-char codes use a counter whose ranges (e.g., 1,000 ids) a coordinator hands to each server - trade-offs: codes are guessable and the range allocator must stay available. Compare your design with [Design Bitly (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly).
- 🛠️ **Do:** 5 min: fix your 2 weakest sections and export an Excalidraw PNG (cache, DB, range allocator, analytics queue). 20 min: implement `Base62.encode/decode` and an in-memory `UrlShortenerService` (`shorten`, `resolve`, custom-alias conflicts, expiry via `Clock`) fed by a `RangeAllocator` handing out blocks of 1,000 ids. Done when: tests pass for round-trip, alias conflict, expired link and no duplicate codes across two allocators, and the PNG is in the repo.

## 📦 Deliverable (by Saturday night)
`notes/13-estimation.md`, `labs/idgen` (Snowflake + tests), and `hld/01-url-shortener/` with write-up, diagram PNG, Base62 + service code with tests, plus `adr/0002-short-code-generation.md` for the key-generation decision.

## ✅ Self-check (Sunday test preview)
- Estimate peak QPS for 100M DAU making 20 reads a day. Show each step.
- Why not use UUIDv4 as a primary key? When is UUIDv7 better?
- Explain the Snowflake bit layout and what happens if the clock goes backwards.
- URL shortener: 301 or 302 for redirects, and why?
- Why does a 64-bit Snowflake ID not fit in 7 Base62 characters, and how do you generate 7-char codes without collisions across many servers?
- Where would you cache in the URL shortener, and with what eviction policy?

## 🚀 Stretch (optional)
Design a pre-generated key-pool service for short codes and estimate its storage for 5 years. Optional deep watch: [Design Bitly walkthrough (Hello Interview)](https://www.youtube.com/watch?v=iUU4O1sWtJA).
