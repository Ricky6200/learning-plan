# 🏗️ System Design · Week 21 — HLD gaps: streams, job scheduler, Yelp mock

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** Batch vs stream processing and OLAP stores show up in every analytics design (view counts, ad clicks, metrics), a distributed job scheduler tests leases and idempotent execution, and an unseen proximity mock keeps your HLD sharp while you apply for jobs.

## 🗓️ Sessions

### Monday 15 Mar · 45 min — Batch vs stream processing, windows, watermarks, OLAP
- 📚 **Learn:** Batch (Spark: bounded data, high throughput, minutes-hours latency) vs stream (Flink/Kafka Streams: unbounded, seconds); tumbling, sliding and session windows; event time vs processing time; watermarks and late events; Lambda (batch + speed layers) vs Kappa (stream only, replay from the log); OLAP stores (columnar: ClickHouse, Druid, Pinot) for slice-and-dice queries. Read 'Basic Concepts' (through 'Windows') in [Flink deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/flink). Optional: [Big data architectures (Azure)](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/big-data-architectures).
- 🛠️ **Do:** In `notes/22-batch-vs-stream.md`: a batch vs stream table (latency, cost, correctness, tools); pick one for 4 cases (daily payouts, live view counter, fraud alerts, monthly invoices); by hand, put 6 click events with event times into 1-minute tumbling windows with a 30-second allowed lateness and show which late event is dropped; one row on OLTP vs OLAP. Done when: every pick names its latency need and the window table is correct.

### Wednesday 17 Mar · 45 min — Distributed job scheduler HLD (steps 1-5)
- 📚 **Learn:** Requirements: one-off, delayed and cron jobs; 10k jobs/s; run within ~2 s of the due time; at-least-once execution; job status. Core ideas: a jobs table plus an executions table keyed by time bucket, a scheduler that scans only the current bucket and pushes due executions to a queue, workers that lease an execution, idempotent job handlers. You sketched this on W17 Sunday - now read 'Functional Requirements' through 'High-Level Design' of [Design a job scheduler (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/job-scheduler) and note what you missed. Optional: [Managing long-running tasks (Hello Interview)](https://www.hellointerview.com/learn/system-design/patterns/long-running-tasks).
- 🛠️ **Do:** Timer on, 25 minutes: steps 1-5 in `hld/20-job-scheduler/README.md` (start from your W17 Sunday mini-design): requirements, estimate (10k jobs/s, executions storage per day), API, data model with the time-bucket key, high-level diagram. Done when: the data model shows how the scheduler finds due jobs without scanning the whole table.

### Thursday 18 Mar · 45 min — Job scheduler deep dives: leases, retries, idempotency
- 📚 **Learn:** Deep dives: precise timing (a short-interval in-memory delay queue in front of the time-bucket scan), worker leases with heartbeats and visibility timeouts (W14 fencing tokens stop a zombie worker), retries with backoff + DLQ, idempotent execution via an execution id, scheduler high availability (partition buckets across scheduler instances). Read [Slack's job queue redesign (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/slack-job-queue). Optional: [Temporal deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/temporal).
- 🛠️ **Do:** Add 3 deep dives (2-second precision, a worker dying mid-job, a job that must not run twice) + an Excalidraw diagram + one ADR to `hld/20-job-scheduler/`. Done when: you can explain what happens, second by second, when a worker crashes after starting a job, and the PNG is committed.

### Saturday 20 Mar · 45 min — PRACTICE: Unseen 45-min HLD mock - Design Yelp
- 📚 **Learn:** Unseen mock rules as in W20 (blank canvas, recording, framework time splits). Case: Yelp - search businesses near me with filters and ratings, view a business, write reviews. Geo primer (deep dive in W23): a geohash turns latitude/longitude into a string cell id where a shared prefix means nearby; search the user's cell plus its 8 neighbours. Optional: read [Design Yelp (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/yelp) only after the mock.
- 🛠️ **Do:** Run the 45-minute mock end to end, recorded, then score it with the 8-line rubric (0-3 each). Done when: `mocks/W21-yelp.md` has the score, your 3 weakest moments and one fix for each.

## 📦 Deliverable (by Saturday night)
`notes/22-batch-vs-stream.md`, `hld/20-job-scheduler/` (write-up + PNG + ADR) and the Yelp mock recording + scorecard in `mocks/W21-yelp.md`.

## ✅ Self-check (Sunday test preview)
- Batch vs stream: when is a nightly batch job the better answer?
- Event time vs processing time: what is a watermark, and what happens to a late event?
- Lambda vs Kappa architecture: what does each cost you?
- Why do OLAP stores use columnar storage?
- Job scheduler: how does the scheduler find due jobs without a full table scan?
- How do you guarantee a scheduled job runs at least once but its effect happens only once?
- Yelp: how do you find businesses within 5 km quickly?

## 🚀 Stretch (optional)
Read [What is OLAP? (ClickHouse)](https://clickhouse.com/docs/concepts/olap) and add an OLAP-backed 'views per minute' dashboard to your job-scheduler or Yelp design. Compare your Yelp mock with the [Proximity search deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/proximity-search).
