# 🏗️ System Design · Week 23 — Kafka internals, ad clicks, top-K (Boss week)

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Designing a message queue and stream aggregations shows deep understanding of logs, partitions and exactly-once trade-offs; top-K and leaderboards are common product questions.

## 🗓️ Sessions

### Monday 29 Mar · 45 min — Distributed message queue: Kafka internals
- 📚 **Learn:** Log segments + index files, partition leaders/followers, ISR, `acks=all` + `min.insync.replicas`, high watermark, KRaft controller quorum (ZooKeeper removed in Kafka 4.0), consumer-group rebalancing, idempotent producer + transactions, retention vs compaction, zero-copy reads. Read [Kafka deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/kafka); watch its [video](https://www.youtube.com/watch?v=DU8o-OTeoCc); go deeper: [Kafka internals course (Confluent)](https://developer.confluent.io/courses/architecture/get-started/).
- 🛠️ **Do:** In `hld/14-message-queue/README.md` design 'Kafka-lite' with the framework in 30 minutes, then 15 minutes comparing with real Kafka. Done when: you can explain what happens to acknowledged writes when a partition leader dies, for `acks=1` vs `acks=all`.

### Wednesday 31 Mar · 45 min — Ad-click aggregation: stream processing and exactly-once
- 📚 **Learn:** Click ingestion -> Kafka -> stream processor (e.g., Flink) with tumbling 1-minute windows -> OLAP store; dedupe by click ID; late events and watermarks; reconciliation with a batch job; fraud filtering; query API for advertisers. Read [Design an ad click aggregator (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ad-click-aggregator); watch its [walkthrough](https://www.youtube.com/watch?v=Zcv_899yqhI).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/15-ad-clicks/README.md` for 10k clicks/s average and 50k/s peak. Done when: all 7 sections are filled and you can explain how a click is counted exactly once even when a processor crashes.

### Thursday 01 Apr · 45 min — Top-K / leaderboards: heavy hitters and count-min sketch
- 📚 **Learn:** Exact top-K (sharded counters + min-heap merge) vs approximate (count-min sketch + heap), sliding time windows, precomputed windows vs on-demand, Redis sorted sets for leaderboards. Read [Top-K (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/top-k); watch [Bloom filters, count-min sketch, HyperLogLog (Hello Interview)](https://www.youtube.com/watch?v=IgyU0iFIoqM); reference: [Redis sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/).
- 🛠️ **Do:** 25 min: implement `labs/topk/CountMinSketch` (width, depth, `add`, `estimate`) and `TopK` with a min-heap; test on a skewed stream that the true top 5 are found and estimates never undercount. 20 min: sketch a game leaderboard with Redis ZSETs (commands for score update, top 10, my rank). Done when: tests pass and the ZSET design is in `notes/21-topk.md`.

### Saturday 03 Apr · 45 min — BOSS BATTLE: Timed 45-min HLD mock (random case)
- 📚 **Learn:** Boss rules: your AI mentor (or a peer) picks a random case you have NOT presented aloud yet, e.g., [Design LeetCode](https://www.hellointerview.com/learn/system-design/problem-breakdowns/leetcode), [Design Tinder](https://www.hellointerview.com/learn/system-design/problem-breakdowns/tinder) or [FB live comments](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-live-comments) (all Hello Interview); read the breakdown only after the mock.
- 🛠️ **Do:** Run a full 45-minute mock with the W19 time splits, recorded, the interviewer asking 3 follow-ups. Score with the same 8-line rubric (0-3 each). Done when: recording, scorecard and 3 improvement actions are in `boss/W23.md`; >= 17/24 clears the boss.

## 📦 Deliverable (by Saturday night)
`hld/14-message-queue/` and `hld/15-ad-clicks/` (write-up + PNG each), `labs/topk` with tests, `notes/21-topk.md`, and the Boss scorecard in `boss/W23.md`.

## ✅ Self-check (Sunday test preview)
- What is the ISR, and how do `acks=all` + `min.insync.replicas` protect data?
- How does Kafka achieve high throughput (sequential I/O, batching, zero-copy)?
- What changed in Kafka 4.0 regarding ZooKeeper?
- Ad clicks: how do you handle late-arriving events in windowed aggregation?
- Count-min sketch: why does it overestimate but never underestimate?
- How would you build a real-time leaderboard for 10M players?

## 🚀 Stretch (optional)
Re-run the boss case a week later with a peer as interviewer and compare scores.
