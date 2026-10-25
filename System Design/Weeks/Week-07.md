# 🏗️ System Design · Week 07 — Parking Lot, Vending Machine, sharding

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** Parking Lot and Vending Machine are among the most-asked LLD problems in India; sharding and consistent hashing are how real systems scale writes and storage.

## 🗓️ Sessions

### Monday 07 Dec · 45 min — Sharding strategies + consistent hashing
- 📚 **Learn:** Partitioning vs replication; range, hash and directory sharding; choosing a shard key; hotspots and key salting; cross-shard queries; rebalancing. Consistent hashing: ring, virtual nodes, minimal key movement. Watch [Consistent hashing (ByteByteGo, 8 min)](https://www.youtube.com/watch?v=UF9Iqmg94tk). Optional: [Sharding (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/sharding).
- 🛠️ **Do:** In `notes/09-sharding.md` choose a shard key + strategy for 3 tables: TicketVerse bookings, chat messages, short-URL mappings. For each: one query it makes cheap, one it makes expensive, hotspot risk and mitigation. Then compute the fraction of keys that move when going from 4 to 5 nodes with modulo hashing vs consistent hashing. Done when: the math is shown and every table has a justified key.

### Wednesday 09 Dec · 45 min — Parking Lot LLD: design + core path
- 📚 **Learn:** Requirements: floors, spot types (bike/car/truck), entry/exit gates, tickets, fee strategy (hourly/flat), spot-allocation strategy (nearest/first-free). Patterns: Strategy for fees and allocation, Factory for spots; avoid a global Singleton. Inject your W4 `TimeSource` so fee tests can fake 2h30m. Read 'Requirements' and 'Class Design' in [Parking lot (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/parking-lot). Optional: [Parking Lot LLD (Concept && Coding, Hindi, 56 min)](https://www.youtube.com/watch?v=MtjZf7291zc).
- 🛠️ **Do:** 8 min: requirements + class diagram (`ParkingLot`, `Floor`, `Spot`, `Vehicle`, `Ticket`, `SpotAllocationStrategy`, `FeeStrategy`). 17 min: implement `park(vehicle)` and `unpark(ticketId)` with `NearestSpotStrategy` and `HourlyFeeStrategy` (time from `TimeSource`). Done when: tests pass for park, lot-full rejection, wrong spot type and the fee for 2h30m; payments, EV spots and multiple gates stay as extension questions (stretch and W10).

### Thursday 10 Dec · 45 min — Vending Machine with the State pattern
- 📚 **Learn:** States: Idle -> HasMoney -> Dispensing, plus SoldOut; events: insert coin, select item, cancel/refund; inventory; change-making. Each state class handles every event, and illegal ones throw. Read the requirements in [Vending machine problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/vending-machine.md). Optional: [Vending machine with State pattern (Concept && Coding, Hindi, 45 min)](https://www.youtube.com/watch?v=wOXs5Z_z0Ew).
- 🛠️ **Do:** 5 min: Mermaid `stateDiagram-v2` of the states. 20 min: `VendingMachine` with a `State` interface and 3-4 state classes, an `Inventory`, and a refund on cancel. Done when: tests cover the happy path, insufficient money, a sold-out item, cancel -> full refund, and one illegal action per state throwing `IllegalStateException`; fewest-coins change-making is a stretch.

### Saturday 12 Dec · 45 min — PRACTICE: Consistent-hash ring with virtual nodes
- 📚 **Learn:** Implementation: `TreeMap<Long, String>` ring (Java W5), MD5 via `MessageDigest` (not `String.hashCode`), `ceilingEntry` with wrap-around to `firstEntry`, V virtual nodes per server. Expect imbalance: with MD5, 100 vnodes and 5 nodes the busiest node is typically 5-25% off the average; 1,000 vnodes keeps it under ~10%. Watch [Consistent hashing from first principles (Arpit Bhayani, 14 min)](https://www.youtube.com/watch?v=Jvimt56KPnk). Optional: [consistent hashing code (awesome-system-design-resources)](https://github.com/ashishps1/awesome-system-design-resources/tree/main/implementations/java/consistent_hashing).
- 🛠️ **Do:** Implement `ConsistentHashRing` (`addNode`, `removeNode`, `getNode(key)`, configurable vnodes). Tests: same key -> same node; removing a node remaps only its keys; with 100 vnodes, 100k keys over 5 nodes stay within +-25% of the average (+-10% with 1,000 vnodes); adding a 6th node moves about 1/6 of the keys. Done when: tests pass and you print the distribution for vnodes = 1, 10, 100 and 1,000.

## 📦 Deliverable (by Saturday night)
`notes/09-sharding.md`, `lld/parkinglot` core + tests, `lld/vendingmachine` with state diagram + tests, and `labs/consistenthashing` with the distribution output.

## ✅ Self-check (Sunday test preview)
- Range vs hash sharding: which queries does each make easy or hard?
- How do virtual nodes improve consistent hashing, and why is 100 vnodes still not perfectly balanced?
- What happens to keys when a node joins a consistent-hash ring?
- Parking Lot: where do you use Strategy, and why not if/else?
- Vending Machine: why is the State pattern better than a big switch on an enum?
- Where would a race appear if two entry gates call `park()` at the same moment? (You fix it in W10.)

## 🚀 Stretch (optional)
Finish Parking Lot payments + EV charging spots and add fewest-coins change-making to the vending machine. References: [Parking lot problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/parking-lot.md), [Mermaid state diagrams](https://mermaid.js.org/syntax/stateDiagram.html), Hindi [Consistent hashing (Concept && Coding)](https://www.youtube.com/watch?v=jqUNbqfsnuw).
