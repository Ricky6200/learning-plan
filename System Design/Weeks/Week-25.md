# 🏗️ System Design · Week 25 — Kafka internals, ad clicks, top-K (Boss week)

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** Designing a message queue and stream aggregations shows deep understanding of logs, partitions, consensus and exactly-once trade-offs; top-K and leaderboards are common product questions. The Season 5 boss is a random unseen HLD mock.

## 🗓️ Sessions

### Monday 12 Apr · 45 min — Kafka internals + consensus: Raft, leader election, gossip
- 📚 **Learn:** Kafka: log segments, partition leaders/followers, ISR, `acks=all` + `min.insync.replicas`, high watermark, idempotent producer. KRaft (ZooKeeper removed in Kafka 4.0) stores cluster metadata with Raft: terms, leader election by majority vote, log replication, an entry is committed once a majority has it. Heartbeats vs gossip for failure detection. Read 'Fault Tolerance and Durability' in [Kafka deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/kafka). Optional: [Raft visualization](https://thesecretlivesofdata.com/raft/).
- 🛠️ **Do:** In `hld/14-message-queue/README.md` design 'Kafka-lite' in a 25-minute sprint (partitions, replication, consumer groups, retention), plus a Raft cheat-sheet in `notes/23-consensus.md`: election steps, what 'committed' means, why a majority. Done when: you can explain what happens to acknowledged writes when a partition leader dies, for `acks=1` vs `acks=all`.

### Wednesday 14 Apr · 45 min — Ad-click aggregation: stream processing and exactly-once
- 📚 **Learn:** Click ingestion -> Kafka -> stream processor (e.g., Flink) with tumbling 1-minute windows -> OLAP store; dedupe by click ID; late events and watermarks (W21 Mon); reconciliation with a batch job; fraud filtering; query API for advertisers. Watch the first 15 minutes of [Design an ad click aggregator (Hello Interview)](https://www.youtube.com/watch?v=Zcv_899yqhI). Optional: [Ad click aggregator breakdown (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ad-click-aggregator).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/15-ad-clicks/README.md` for 10k clicks/s average and 50k/s peak. Done when: you can explain how a click is counted exactly once even when a processor crashes; deep dives return in W29.

### Thursday 15 Apr · 45 min — Top-K and heavy hitters: count-min sketch
- 📚 **Learn:** Exact top-K (sharded counters + min-heap merge) vs approximate (count-min sketch + heap), sliding time windows, precomputed windows vs on-demand; Redis sorted sets as a leaderboard preview (full design in W29). Read 'Count-Min Sketch' in [Data structures for big data (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/data-structures-for-big-data). Optional: [Top-K (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/top-k).
- 🛠️ **Do:** 25-min timer: implement `labs/topk/CountMinSketch` (width, depth, `add`, `estimate`) and `TopK` with a min-heap over the sketch estimates. Done when: tests on a skewed stream prove the true top 5 are found and estimates never undercount.

### Saturday 17 Apr · 45 min — BOSS BATTLE: Timed 45-min HLD mock (random unseen case)
- 📚 **Learn:** Boss rules: your AI mentor (or a peer) picks a random case you have NOT designed yet, e.g., Design LeetCode, Design Tinder or an online auction; same time splits and 8-line rubric as W20, with 3 interviewer follow-ups. Optional: read the matching breakdown, e.g., [Design LeetCode (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/leetcode), only after the mock.
- 🛠️ **Do:** Run a full 45-minute mock, recorded, the interviewer asking 3 follow-ups. Score with the 8-line rubric (0-3 each). Done when: recording, scorecard and 3 improvement actions are in `boss/W25.md`; >= 17/24 clears the boss.

## 📦 Deliverable (by Saturday night)
`hld/14-message-queue/` and `hld/15-ad-clicks/` (write-up + PNG each), `notes/23-consensus.md`, `labs/topk` with tests, and the Boss scorecard in `boss/W25.md`.

## ✅ Self-check (Sunday test preview)
- What is the ISR, and how do `acks=all` + `min.insync.replicas` protect data?
- How does Kafka achieve high throughput (sequential I/O, batching, zero-copy)?
- What changed in Kafka 4.0 regarding ZooKeeper, and what does KRaft use instead?
- In Raft, when is a log entry committed, and why does a leader need a majority?
- Ad clicks: how do you handle late-arriving events in windowed aggregation?
- Count-min sketch: why does it overestimate but never underestimate?
- Heartbeats vs gossip: when would you use each for failure detection?

## 🚀 Stretch (optional)
Watch the [Raft lecture (Martin Kleppmann)](https://www.youtube.com/watch?v=uXEYuDwm7e4) and the [Kafka deep dive video (Hello Interview)](https://www.youtube.com/watch?v=DU8o-OTeoCc); go deeper with the [Kafka internals course (Confluent)](https://developer.confluent.io/courses/architecture/get-started/) and [Bloom filters, count-min sketch, HyperLogLog (Hello Interview)](https://www.youtube.com/watch?v=IgyU0iFIoqM). Re-run the boss case a week later with a peer as interviewer and compare scores.
