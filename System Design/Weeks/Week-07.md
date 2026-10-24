# 🏗️ System Design · Week 07 — Parking Lot, Vending Machine, sharding

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** Parking Lot and Vending Machine are among the most-asked LLD problems in India; sharding and consistent hashing are how real systems scale writes and storage.

## 🗓️ Sessions

### Monday 07 Dec · 45 min — Sharding strategies + consistent hashing
- 📚 **Learn:** Partitioning vs replication; range, hash and directory sharding; choosing a shard key; hotspots and key salting; cross-shard queries; rebalancing. Consistent hashing: ring, virtual nodes, minimal key movement. Read [Sharding (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/sharding); watch [Consistent hashing (ByteByteGo)](https://www.youtube.com/watch?v=UF9Iqmg94tk); Hindi: [Consistent hashing (Concept && Coding)](https://www.youtube.com/watch?v=jqUNbqfsnuw).
- 🛠️ **Do:** In `notes/09-sharding.md` choose a shard key + strategy for 3 tables: TicketVerse bookings, chat messages, short-URL mappings. For each: one query it makes cheap, one it makes expensive, hotspot risk and mitigation. Then compute the fraction of keys that move when going from 4 to 5 nodes with modulo hashing vs consistent hashing. Done when: the math is shown and every table has a justified key.

### Wednesday 09 Dec · 45 min — Parking Lot LLD: design + core code
- 📚 **Learn:** Requirements: floors, spot types (bike/car/truck/EV), entry/exit gates, tickets, fee strategy (hourly/flat), spot-allocation strategy (nearest/first-free), payment. Patterns: Strategy, Factory, State for spots; avoid a global Singleton. Hindi: [Parking Lot LLD (Concept && Coding)](https://www.youtube.com/watch?v=MtjZf7291zc); reference: [Parking lot problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/parking-lot.md).
- 🛠️ **Do:** 15 min: requirements + class diagram (`ParkingLot`, `Floor`, `Spot`, `Vehicle`, `Ticket`, `SpotAllocationStrategy`, `FeeStrategy`). 30 min: implement `park(vehicle)` and `unpark(ticketId)` with `NearestSpotStrategy` and `HourlyFeeStrategy` (inject `Clock`). Done when: tests pass for park, lot-full rejection, wrong spot type and the fee for 2h30m; payments and EV spots stay for the stretch.

### Thursday 10 Dec · 45 min — Vending Machine with the State pattern
- 📚 **Learn:** States: Idle -> HasMoney -> Dispensing, plus SoldOut; events: insert coin, select item, cancel/refund; inventory; change-making. Hindi: [Vending machine with State pattern (Concept && Coding)](https://www.youtube.com/watch?v=wOXs5Z_z0Ew); references: [Vending machine problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/vending-machine.md) and [Mermaid state diagrams](https://mermaid.js.org/syntax/stateDiagram.html).
- 🛠️ **Do:** 10 min: state diagram (Mermaid `stateDiagram-v2`). 30 min: `VendingMachine` with a `State` interface and 3-4 state classes, an `Inventory`, refund on cancel. 5 min: tests. Done when: tests cover the happy path, insufficient money, sold-out item, cancel -> full refund, and every illegal action in each state throws.

### Saturday 12 Dec · 45 min — PRACTICE: Consistent-hash ring with virtual nodes
- 📚 **Learn:** Implementation: `TreeMap<Long, Node>` ring, MD5/Murmur hash (not `String.hashCode`), `ceilingEntry` with wrap-around, V virtual nodes per server. Compare later with [consistent hashing code (awesome-system-design-resources)](https://github.com/ashishps1/awesome-system-design-resources/tree/main/implementations/java/consistent_hashing); watch [Consistent hashing from first principles (Arpit Bhayani)](https://www.youtube.com/watch?v=Jvimt56KPnk).
- 🛠️ **Do:** Implement `ConsistentHashRing` (`addNode`, `removeNode`, `getNode(key)`, configurable virtual nodes). Tests: same key -> same node; removing a node remaps only its keys; with 100 vnodes, 100k keys over 5 nodes stay within +-10% of the average; adding a 6th node moves about 1/6 of keys. Done when: tests pass and you print the distribution for vnodes = 1, 10 and 100.

## 📦 Deliverable (by Saturday night)
`notes/09-sharding.md`, `lld/parkinglot` core + tests, `lld/vendingmachine` with state diagram + tests, and `labs/consistenthashing` with the distribution output.

## ✅ Self-check (Sunday test preview)
- Range vs hash sharding: which queries does each make easy or hard?
- How do virtual nodes improve consistent hashing?
- What happens to keys when a node joins a consistent-hash ring?
- Parking Lot: where do you use Strategy, and why not if/else?
- Vending Machine: why is the State pattern better than a big switch on an enum?
- How would you stop two entry gates from assigning the same spot?

## 🚀 Stretch (optional)
Finish Parking Lot payments + EV charging spots and make `park()` thread-safe for multiple gates.
