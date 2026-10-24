# 🏗️ System Design · Week 11 — HLD method, estimation, IDs, URL shortener

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** A fixed HLD framework plus fast estimation is what makes you sound like an SDE-2; the URL shortener is the canonical first case study and introduces ID generation.

## 🗓️ Sessions

### Monday 04 Jan · 45 min — HLD interview framework + back-of-the-envelope estimation
- 📚 **Learn:** The 7-step framework in your `HLD_INTERVIEW_FRAMEWORK.md` (requirements -> estimation -> API -> data model -> diagram -> deep dives -> trade-offs) and its time splits. Estimation: powers of 2, latency numbers, QPS = DAU x actions / 86,400 x peak factor, storage = items/day x size x retention x replicas. Watch [System design interview: step by step](https://www.youtube.com/watch?v=i7twT3x5yv8) and [Back-of-the-envelope estimation](https://www.youtube.com/watch?v=UC5xf8FbdJc) (ByteByteGo).
- 🛠️ **Do:** Solve 3 drills in `notes/13-estimation.md`, with units: (1) 100M DAU x 20 feed reads/day -> average and peak QPS; (2) 5M photo uploads/day x 2 MB for 5 years with 3 replicas -> storage; (3) 1M concurrent chat users sending 1 message per 10 s -> writes/s and bandwidth at 1 KB/message. Done when: each answer is within 2x of your AI mentor's check and you can do drill 1 aloud in 2 minutes.

### Wednesday 06 Jan · 45 min — Unique ID generation: UUID, ticket server, Snowflake
- 📚 **Learn:** Requirements: unique, roughly time-sortable, 64-bit, no coordination, high rate. Options: DB auto-increment with offsets, Flickr ticket server, UUIDv4 (random, fragments B-tree indexes) vs UUIDv7 (time-ordered), Snowflake (41-bit ms timestamp, 10-bit worker, 12-bit sequence); clock-skew handling. Read [Flickr ticket servers](https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/) and the [original Snowflake README (Twitter archive)](https://github.com/twitter-archive/snowflake/tree/snowflake-2010).
- 🛠️ **Do:** Implement `labs/idgen/SnowflakeIdGenerator` (custom epoch, workerId 0-1023, sequence 0-4095, wait for the next millisecond on overflow, throw if the clock moves backwards) with an injectable time source, plus `decode(id)`. Done when: tests prove 1M IDs from one thread are unique and increasing, 8 threads produce no duplicates, and decode returns the original timestamp and worker.

### Thursday 07 Jan · 45 min — Case study #1: URL shortener
- 📚 **Learn:** FR: shorten, redirect, custom alias, expiry. NFR: low-latency redirects, ~100:1 read:write, high availability. Key generation (counter + base62, hash + collision check, pre-generated key pool), 301 vs 302, caching hot links, async click analytics. Read [Design Bitly (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly); watch [How a URL shortener works (ByteByteGo)](https://www.youtube.com/watch?v=HHUi8F_qAXM); Hindi: [URL shortener (Concept && Coding)](https://www.youtube.com/watch?v=C7_--hAhiaM).
- 🛠️ **Do:** Timer on: 35 min solo design in `hld/01-url-shortener/README.md` using the framework's write-up template (all 7 sections, estimation included). Then 10 min: compare with the Hello Interview breakdown and list 3 gaps + 1 thing you did better. Done when: every template section has content and the gap list is committed.

### Saturday 09 Jan · 45 min — PRACTICE: URL shortener write-up + Base62 implementation
- 📚 **Learn:** Base62 (0-9, a-z, A-Z): 7 characters give about 3.5 trillion codes; encoding unique IDs is collision-free by construction. Draw with [Excalidraw](https://excalidraw.com/); optional deep watch: [Design Bitly walkthrough (Hello Interview)](https://www.youtube.com/watch?v=iUU4O1sWtJA).
- 🛠️ **Do:** 20 min: finish the 1-page write-up and an Excalidraw diagram (export PNG) with cache, DB, ID generator and analytics queue. 25 min: implement `Base62.encode/decode` and an in-memory `UrlShortenerService` (`shorten`, `resolve`, custom-alias conflicts, expiry via `Clock`) using your Snowflake generator. Done when: tests pass for encode/decode round-trip, alias conflict and expired link, and the PNG is in the repo.

## 📦 Deliverable (by Saturday night)
`notes/13-estimation.md`, `labs/idgen` (Snowflake + tests) and `hld/01-url-shortener/` with write-up, diagram PNG, and Base62 + service code with tests.

## ✅ Self-check (Sunday test preview)
- Estimate peak QPS for 100M DAU making 20 reads a day. Show each step.
- Why not use UUIDv4 as a primary key? When is UUIDv7 better?
- Explain the Snowflake bit layout and what happens if the clock goes backwards.
- URL shortener: 301 or 302 for redirects, and why?
- How do you generate short codes without collisions across many servers?
- Where would you cache in the URL shortener, and with what eviction policy?

## 🚀 Stretch (optional)
Design a pre-generated key-pool service for short codes and estimate its storage for 5 years.
