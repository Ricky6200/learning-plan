# 🏗️ System Design · Week 16 — KV store, security, DNS and edge

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** A thread-safe KV store with TTL is a favourite concurrency machine-coding problem, and authN/authZ plus edge design (DNS, CDN, WAF) come up in every senior-leaning HLD discussion.

## 🗓️ Sessions

### Monday 08 Feb · 45 min — Security in system design: OAuth2/OIDC, JWT vs sessions, API security
- 📚 **Learn:** AuthN vs authZ (RBAC/ABAC); sessions vs JWT (revocation, size, statelessness); OAuth 2.0 authorization code + PKCE and client credentials; OIDC ID tokens; API security (TLS everywhere, validation, rate limits, OWASP API Top 10); encryption in transit/at rest; secrets in a vault; DDoS/WAF. Watch [OAuth 2 explained](https://www.youtube.com/watch?v=ZV5yTm4pT8g) and [Session vs JWT](https://www.youtube.com/watch?v=fyTxwIa-1U0) (ByteByteGo); read [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/).
- 🛠️ **Do:** In `notes/19-security.md`: sequence diagram for TicketVerse login via Keycloak (authorization code + PKCE -> JWT access token -> gateway validates -> booking service checks role); a JWT vs session table (revocation, scaling, size); 5 OWASP API risks with your TicketVerse mitigation. Done when: you can explain how to limit damage from a stolen JWT (short TTL, refresh-token rotation, denylist).

### Wednesday 10 Feb · 45 min — LLD: thread-safe in-memory KV store with TTL (design)
- 📚 **Learn:** API: `put(k, v, ttl)`, `get`, `delete`, `incrBy`; storage in `ConcurrentHashMap`; expiry = lazy check on read + periodic sampling sweep (as Redis does); locking options (per-key atomic ops vs `ReentrantReadWriteLock` vs lock striping); optional LRU eviction at a size limit. Read [How Redis expires keys (EXPIRE docs)](https://redis.io/docs/latest/commands/expire/) and [ReentrantReadWriteLock docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReentrantReadWriteLock.html); watch [LLD of a cache, mock interview (Gaurav Sen)](https://www.youtube.com/watch?v=tzbX4ix2RjI).
- 🛠️ **Do:** Write `lld/kvstore/DESIGN.md`: requirements, class diagram (`KvStore`, `Entry`, `ExpiryPolicy`, `EvictionPolicy`, `Clock`), a concurrency plan (which lock or atomic op guards what) and a list of >= 8 tests for Saturday. Then code `Entry` + `put`/`get` with lazy expiry. Done when: the design is committed and the first 3 tests pass.

### Thursday 11 Feb · 45 min — DNS, GeoDNS, anycast, CDN edge, DDoS and WAF
- 📚 **Learn:** Resolution chain (recursive resolver -> root -> TLD -> authoritative), record types (A, AAAA, CNAME, NS, TXT), TTL trade-offs; GeoDNS/latency routing; anycast (one IP served from many PoPs); L3/L4 vs L7 DDoS; WAF rules; edge rate limiting. Watch [Everything you need to know about DNS (ByteByteGo)](https://www.youtube.com/watch?v=27r4Bzuj5NQ); read [What is anycast? (Cloudflare)](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) and [Traffic Manager routing methods (Azure)](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-routing-methods).
- 🛠️ **Do:** Run `Resolve-DnsName` (or `nslookup`) for 3 domains and record A/CNAME/NS answers and TTLs. Then design the global entry for TicketVerse users in India + Singapore: DNS or anycast, CDN, WAF, regional gateways; describe what happens when the Mumbai region fails. Done when: diagram + failover narrative are in `notes/20-edge.md`.

### Saturday 13 Feb · 45 min — PRACTICE: KV store machine coding
- 📚 **Learn:** Finish the store you designed on Wednesday. Useful APIs: `ConcurrentHashMap.compute/merge` for atomic updates, `ScheduledExecutorService` for the sweeper, `Clock` for deterministic expiry tests. Docs: [ConcurrentHashMap](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html).
- 🛠️ **Do:** Implement `delete`, atomic `incrBy`, TTL refresh on `put`, an active-expiry sweeper (sample 20 keys every 100 ms) and optional max-size LRU eviction. Done when: >= 8 tests pass, including 32 threads x 1,000 `incrBy(1)` = 32,000, expired keys invisible to `get`, the sweeper removing expired keys, and `delete` racing `put` without exceptions.

## 📦 Deliverable (by Saturday night)
`notes/19-security.md`, `notes/20-edge.md`, and `lld/kvstore` (design + >= 8 green tests including the concurrency test).

## ✅ Self-check (Sunday test preview)
- Sessions vs JWT: how do you revoke access in each?
- Walk through the OAuth 2.0 authorization code flow with PKCE. Why PKCE?
- AuthN vs authZ: where does each happen in a microservices system?
- How does anycast help against DDoS and reduce latency?
- What is the trade-off of a low DNS TTL?
- How does Redis expire keys, and why both lazy and active expiry?
- In your KV store, how is `incrBy` made atomic?

## 🚀 Stretch (optional)
Add an append-only log to the KV store so it survives restarts (replay on startup), and measure throughput with and without fsync.
