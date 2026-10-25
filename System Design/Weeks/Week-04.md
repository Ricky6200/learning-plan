# 🏗️ System Design · Week 04 — Structural patterns and caching (Boss week)

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Caching is the first scaling lever in HLD answers, and Adapter, Decorator, Proxy and Composite appear in almost every codebase; the boss proves you can stack them cleanly under a timer.

## 🗓️ Sessions

### Monday 16 Nov · 45 min — Caching deep dive: strategies, eviction, invalidation, stampede
- 📚 **Learn:** Cache layers (browser, CDN, gateway, in-process, Redis, DB buffer pool); cache-aside, read-through, write-through, write-back, write-around; LRU/LFU eviction; TTL; invalidation; stampede (locks, request coalescing, jittered TTL); hot keys. Watch [Cache systems every developer should know (ByteByteGo, 6 min)](https://www.youtube.com/watch?v=dGAgxozNWFE). Optional: [Caching pitfalls (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=wh98s0XhMmQ).
- 🛠️ **Do:** Write `notes/04-caching.md`: a table (strategy -> read path -> write path -> consistency -> failure mode) and decisions for 3 scenarios: movie catalog, seat availability during a big sale, user profile. For each give strategy, TTL, invalidation trigger and stampede protection. Done when: each decision fits in 2 lines and names what can go stale and for how long.

### Wednesday 18 Nov · 45 min — Structural patterns I: Adapter, Decorator, Proxy, Facade
- 📚 **Learn:** Adapter (wrap an incompatible API), Decorator (add behaviour by wrapping an object that has the same interface), Proxy (same interface, controls access: lazy loading, caching, permission checks), Facade (simple front door to a subsystem). Decorator vs Proxy: same shape, different intent. Read [Decorator (refactoring.guru)](https://refactoring.guru/design-patterns/decorator). Optional: [Proxy (refactoring.guru)](https://refactoring.guru/design-patterns/proxy).
- 🛠️ **Do:** In `patterns.structural`: (1) `LegacyPayAdapter` fitting `LegacyPaySdk.makePayment(String, double)` into your W3 `PaymentProcessor`; (2) `DataSource` decorators `CompressionDecorator` + `EncryptionDecorator` (fake transforms, e.g., reverse and upper-case the text); (3) `LazyReportProxy` that builds an expensive `Report` only on the first `render()` and counts builds. Facade stays a one-paragraph note. Done when: tests prove the adapter converts the call, the decorators work in either order, and the proxy builds the report exactly once.

### Thursday 19 Nov · 45 min — Composite, Bridge, Flyweight + LRU/LFU pointer drawings
- 📚 **Learn:** Composite (uniform tree: files/folders), Bridge (split two dimensions: shape x renderer), Flyweight (share immutable intrinsic state: the `Integer.valueOf` cache). LRU in O(1) = hash map + doubly linked list; LFU adds frequency buckets. Today you only DRAW them (Java W5 Tue builds LRU on `LinkedHashMap`; W9 makes it thread-safe). Read [Composite (refactoring.guru)](https://refactoring.guru/design-patterns/composite). Optional: [File system with Composite (Concept && Coding, Hindi, 22 min)](https://www.youtube.com/watch?v=FLkCkUY7Wu0).
- 🛠️ **Do:** One kata, three patterns: `FileNode`/`DirectoryNode` with `size()` (Composite), printed through a `TreeRenderer` interface with `PlainRenderer` and `IndentedRenderer` (Bridge), using one shared `Icon` object per file extension from an `IconFactory` map (Flyweight). Then 5 min on paper: draw the pointer changes for LRU `get`, `put` and eviction at capacity 3. Done when: tests prove nested sizes add up and two `.txt` files share one `Icon` instance, and a photo of the drawing is in `notes/04-caching.md`.

### Saturday 21 Nov · 45 min — BOSS BATTLE: Pattern-stacked PriceService + caching pitch
- 📚 **Learn:** Boss rules: blank package, 35-min coding timer, then a recorded pitch. Single-threaded and pattern-based: Adapter + caching Proxy + logging Decorator behind one interface. Time primer: `interface TimeSource { long nowMillis(); }` - production reads the system clock, tests use a `FakeTimeSource` you can advance, so TTL expiry is deterministic. Quick refresh: [Proxy (refactoring.guru)](https://refactoring.guru/design-patterns/proxy).
- 🛠️ **Do:** 0-5 min: interface `PriceService` (`priceOf(String sku)`). 5-30: `FxQuoteAdapter` over a legacy `FxQuoteSdk` (Adapter), `CachingPriceProxy` with per-entry TTL via `TimeSource` (Proxy), `LoggingPriceService` recording calls (Decorator), stacked logging -> caching -> adapter. 30-35: >= 5 tests (hit, expiry with `FakeTimeSource`, one SDK call per key, decorator logs, stack order). 35-45: record a pitch on cache-aside vs write-through, stampede and hot keys. Done when: tests pass inside 35 minutes, the recording exists and `boss/W04.md` has your score.

## 📦 Deliverable (by Saturday night)
`notes/04-caching.md` (with the LRU drawing), structural pattern code + tests, and the Boss `PriceService` stack with green tests + recorded pitch, self-scored in `boss/W04.md` (correctness, pattern fit, tests, explanation).

## ✅ Self-check (Sunday test preview)
- Cache-aside vs write-through vs write-back: what are the consistency and failure trade-offs?
- What is a cache stampede? Give three ways to prevent it.
- How do you handle a hot key in a distributed cache?
- Draw how LRU `get` and `put` move nodes in a hash map + doubly linked list. Why is each O(1)?
- Decorator vs Proxy: same structure, different intent. Explain.
- LRU vs LFU: when does LFU win?
- How do you invalidate cached data when the underlying DB row changes?

## 🚀 Stretch (optional)
Draw an O(1) LFU with frequency buckets, then add `invalidate(sku)` and hit/miss counters to your caching proxy. Deeper read: [Caching (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/caching) - 'Cache Architectures' and 'Common Caching Problems'. Hindi: [All structural patterns (Concept && Coding)](https://www.youtube.com/watch?v=WxGtmIBZszk).
