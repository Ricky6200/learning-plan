# 🏗️ System Design · Week 29 — HLD finish: hotels, leaderboards, unseen mocks

> 📅 **Mon 10 May 2027 → Sun 16 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 28](Week-28.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-29.md) · [Week 30 →](Week-30.md)

**Why this week:** Hotel booking, leaderboards, exchanges and flash sales round out the commonly asked HLD set; two final unseen mocks and a refreshed summary sheet leave you interview-ready for the final boss.

## 🗓️ Sessions

### Monday 10 May · 45 min — Hotel booking / Airbnb HLD: date-range inventory, overbooking
- 📚 **Learn:** Inventory per hotel, room type and night (`total`, `reserved`) instead of per physical room; a 3-night booking = one transaction with a conditional update on 3 rows (`reserved + n <= total * 1.1` allows 10% overbooking); idempotent reservation ids; search from a cache/search index, booking from the strongly consistent DB; unique listings (Airbnb) can use a date-range exclusion constraint. Read 'Database design and data modeling' and 'Real-time availability and booking process' in [Design a hotel booking system](https://www.systemdesignhandbook.com/guides/design-hotel-booking-system/). Optional: [Range types (PostgreSQL docs)](https://www.postgresql.org/docs/current/rangetypes.html).
- 🛠️ **Do:** Timer on, 25 minutes: steps 1-5 in `hld/21-hotel-booking/README.md`, starting from your W16 Sunday mini-design and your W28 mock: requirements, estimate, API, the room-night inventory table, diagram. Done when: you can write the conditional update for a 3-night booking and explain how overbooking is capped.

### Wednesday 12 May · 45 min — Ad-click follow-up + full leaderboard design
- 📚 **Learn:** Leaderboard: one Redis sorted set per board (`ZINCRBY` updates, `ZREVRANGE 0 9` top 10, `ZREVRANK` my rank, neighbours via a rank range), sharding by game/region or by score range with a merge, ties, daily/weekly boards, rebuild from the DB. Ad-click follow-up: apply your W21 batch-vs-stream notes to the W25 design (replay from Kafka vs batch reconciliation). Read 'Leaderboard API' through 'Capacity Planning' in [Leaderboard system design (systemdesign.one)](https://systemdesign.one/leaderboard-system-design/). Optional: [Ad click aggregator (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ad-click-aggregator).
- 🛠️ **Do:** 10 min: add 2 deep dives to `hld/15-ad-clicks/` (no lost clicks via replay; how batch corrections reach advertisers). 15 min: `hld/22-leaderboard/README.md` for 10M players (API, ZSET commands, sharding plan, the 'my rank' path). Done when: both are committed and you can explain how a rank is computed when the board is sharded.

### Thursday 13 May · 45 min — Unseen HLD mock: stock exchange (45 min)
- 📚 **Learn:** Unseen mock rules as in W20. Case: a stock exchange - brokers send limit and market orders; a matching engine keeps an order book per symbol and matches by price-time priority; trades are published as market data; low latency, strict ordering, no lost orders. Optional: watch [How a stock exchange matches orders](https://www.youtube.com/watch?v=FXXjo2yjjAk) only after the mock.
- 🛠️ **Do:** Run the 45-minute mock end to end, recorded, and score it with the 8-line rubric. Done when: `mocks/W29-stock-exchange.md` has the score, the deep dive you were weakest on, and how a real exchange handles it (sequencer, single-threaded matching per symbol, replicated journal).

### Saturday 15 May · 45 min — PRACTICE: Unseen flash-sale mock (35 min) + SUMMARY refresh
- 📚 **Learn:** Unseen mock rules again, shortened to 35 minutes. Case: a flash sale - 10,000 discounted phones go on sale at 12:00 for millions of users; no overselling, fair access, a payment window that releases unpaid units. Optional: read [Design a flash sale (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/flash-sale) only after the mock.
- 🛠️ **Do:** 0-35 min: the mock, recorded and scored with the 8-line rubric in `mocks/W29-flash-sale.md`. 35-45 min: refresh `hld/SUMMARY.md` with the W28-W29 designs and mocks (one row each: key requirement, numbers, core components, the big trade-off, a failure mode). Done when: the scorecard is committed and the summary has no empty cells.

## 📦 Deliverable (by Saturday night)
`hld/21-hotel-booking/` and `hld/22-leaderboard/` (write-up + diagram each), 2 new ad-click deep dives, two unseen-mock scorecards in `mocks/`, and a refreshed `hld/SUMMARY.md`.

## ✅ Self-check (Sunday test preview)
- Why model hotel inventory per room type and night instead of per physical room?
- How do you cap overbooking, and why do hotels overbook at all?
- How do you get a player's rank when the leaderboard is sharded?
- Ad clicks: how do batch reconciliation results correct the real-time numbers?
- Stock exchange: why is matching usually single-threaded per symbol?
- Flash sale: how do you stop overselling while keeping the purchase path fast?

## 🚀 Stretch (optional)
Add a 'friends leaderboard' and weekly resets to the leaderboard design (command reference: [Redis sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/)); compare your stock-exchange mock with [Design Robinhood (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/robinhood), which designs the broker side.
