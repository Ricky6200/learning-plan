# 🏗️ System Design · Week 23 — Uber and Ticketmaster at scale

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Ride-hailing teaches geo indexes and high write rates; the Ticketmaster/BookMyShow HLD is the distributed version of the seat-locking code you wrote for TicketVerse.

## 🗓️ Sessions

### Monday 29 Mar · 45 min — Uber/Ola: location updates, geo index, matching
- 📚 **Learn:** Driver location pings every ~4 s (write-heavy), geo indexes (geohash, quadtree, H3 cells; Redis GEO), nearest-driver search, matching with offers + timeouts, locking a driver to avoid double assignment, ETA, surge (awareness). Read 'Quadtrees', 'Geohash' and 'Which Should You Use?' in [Proximity search (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/proximity-search). Optional: [QuadTrees and Hilbert curves (Gaurav Sen, 22 min)](https://www.youtube.com/watch?v=OcUKFIjhKu0).
- 🛠️ **Do:** In `hld/10-ride-hailing/README.md` do steps 1-5 in a 25-minute sprint; estimate writes/s for 1M active drivers pinging every 4 s and the memory for their latest positions. Done when: the estimate is shown and you chose a geo index with one reason.

### Wednesday 31 Mar · 45 min — Uber deep dives: matching consistency, hot cells, trips
- 📚 **Learn:** Driver lock with TTL during an offer (no double booking), dense-city hot cells (finer cells, sharding by region), the location stream through Kafka, trip state machine, failure handling when a driver goes silent. Read [Redis geospatial docs](https://redis.io/docs/latest/develop/data-types/geospatial/). Optional: [H3 docs](https://h3geo.org/docs/).
- 🛠️ **Do:** Add 3 deep dives (consistent matching, hot cells, location ingestion) + an Excalidraw diagram, then spend 5 minutes comparing with [Design Uber (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/uber). Done when: the one-page write-up + PNG are committed and you can explain why a driver never receives two simultaneous ride offers.

### Thursday 01 Apr · 45 min — Ticketmaster/BookMyShow HLD: holds, contention, waiting room
- 📚 **Learn:** Seat-map reads (cache/CDN), seat holds via Redis TTL locks vs DB row locks, booking state machine, payment timeout releases holds, virtual waiting room for spikes, search via Elasticsearch, idempotent booking API. Read [Shopify inventory reservations (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/shopify-inventory-reservations). Optional: [Thundering herd on ticket booking (Concept && Coding, Hindi, 12 min)](https://www.youtube.com/watch?v=1aamH7sA8FY).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/11-ticketverse-booking/README.md`, mapped onto TicketVerse (reuse your W11 LLD and your Java W15 locking choices). Done when: you can explain how 1M users hitting a concert drop at 10:00 are protected and how no seat is ever sold twice.

### Saturday 03 Apr · 45 min — PRACTICE: Virtual waiting room + Ticketmaster review
- 📚 **Learn:** Waiting room = FIFO queue of visitors + admission at a controlled rate (token bucket) + a signed, expiring admission token checked by the booking API; users can poll their position. Reuse your W11 `TokenBucketLimiter`. Compare Thursday's design with the deep dives of [Design Ticketmaster (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster).
- 🛠️ **Do:** 25-min timer: `labs/waitingroom/VirtualWaitingRoom` - `join(userId)` returns a ticket, `position(ticket)`, `admitBatch()` admits N per second via the token bucket, and admitted users get an expiring token. Done when: tests prove FIFO admission, rate limiting, token expiry, and no double admission under 50 concurrent joins; finish the Ticketmaster diagram on Sunday.

## 📦 Deliverable (by Saturday night)
`hld/10-ride-hailing/` and `hld/11-ticketverse-booking/` (write-up + PNG + ADR each) and `labs/waitingroom` with passing tests.

## ✅ Self-check (Sunday test preview)
- How do you find the nearest available drivers quickly?
- Geohash vs quadtree vs H3: trade-offs?
- How do you stop one driver from being matched to two riders?
- Ticketmaster: Redis TTL hold vs DB row lock: which and why?
- How does a virtual waiting room protect the booking system?
- What happens to a held seat when payment times out?

## 🚀 Stretch (optional)
Add surge pricing to the Uber design: which data feeds it, where it is computed and how often it refreshes. Extra: [Design Uber walkthrough (Hello Interview)](https://www.youtube.com/watch?v=lsKU38RKQSo); [Ticketmaster walkthrough (Hello Interview)](https://www.youtube.com/watch?v=fhdPyoO6aXI).
