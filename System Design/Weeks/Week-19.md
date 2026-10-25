# 🏗️ System Design · Week 19 — Case studies: news feed, typeahead, search

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** News feed (fan-out trade-offs), typeahead (tries, precomputation, caching) and full-text search (inverted indexes) are among the most frequently asked HLD topics and teach read-heavy design.

## 🗓️ Sessions

### Monday 01 Mar · 45 min — News feed: fan-out on write vs read, celebrity problem
- 📚 **Learn:** Fan-out on write (push post IDs into follower feed caches), fan-out on read (pull and merge at read time), hybrid (pull for celebrities), feed cache in Redis (lists/sorted sets of post IDs), cursor pagination, ranking hook, media via CDN. Watch the first 15 minutes of [Design FB news feed (Hello Interview)](https://www.youtube.com/watch?v=Qj4-GruzyDU). Optional: [Designing Instagram news feed (Gaurav Sen, 24 min)](https://www.youtube.com/watch?v=QmX2NPkJTKg).
- 🛠️ **Do:** In `hld/04-news-feed/README.md` do framework steps 1-5 solo in a 25-minute sprint, including an estimate of feed-cache memory for 100M users x 200 post IDs. Done when: the estimate is shown and you can state your fan-out choice in one sentence.

### Wednesday 03 Mar · 45 min — News feed deep dives: celebrities, ranking, pagination
- 📚 **Learn:** Hybrid fan-out thresholds, async fan-out workers via a queue, cursor vs offset pagination, cache warm-up for inactive users, ranking pipeline (candidates -> features -> score), new-post visibility (eventual is fine). Read 'Step 3: Design core components' of the [Twitter timeline solution (system-design-primer)](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md). Optional: [API pagination (ByteByteGo, 3 min)](https://www.youtube.com/watch?v=14K_a2kKTxU).
- 🛠️ **Do:** Finish steps 6-7 with 3 deep dives and an Excalidraw diagram, plus a walkthrough of 'a celebrity with 50M followers posts': what is written, what is read, and the latency. Done when: the one-page write-up + PNG are committed.

### Thursday 04 Mar · 45 min — Typeahead autocomplete + inverted-index search
- 📚 **Learn:** Typeahead: top-5 suggestions in < 100 ms, prefix match, popularity + freshness; trie with top-K cached per node, offline aggregation (query logs -> counts -> rebuilt trie snapshots), sharding by prefix, browser/CDN caching, client debouncing. Its sibling, full-text search: inverted index (term -> posting list), analyzers, Elasticsearch shards and replicas. Watch the first 15 minutes of [Typeahead system design (Tushar Roy)](https://www.youtube.com/watch?v=us0qySiUsGU). Optional: [Elasticsearch deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/elasticsearch).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/05-typeahead/README.md` for 5B searches/day, including the trie memory estimate and the update pipeline (how often snapshots rebuild). Add one paragraph on when an inverted index (Elasticsearch) replaces the trie. Done when: the read path for typing 'avat' is traced step by step.

### Saturday 06 Mar · 45 min — PRACTICE: Typeahead trie with cached top-K
- 📚 **Learn:** Warm-up (10 min): re-type your DSA W16 Sat trie for [Implement Trie (LeetCode 208)](https://leetcode.com/problems/implement-trie-prefix-tree/) from memory. Then compare Thursday's design with the video's final diagram (5 min). Today's idea: each trie node keeps its top-K completions, refreshed on insert by walking the path - memory traded for O(prefix length) reads.
- 🛠️ **Do:** 25-min timer: implement `AutocompleteTrie` (`insert(term, count)` updating per-node top-5, `suggest(prefix)` returning the top 5 by count, then alphabetical on ties). Done when: tests pass for ranking, ties, an unknown prefix, updated counts re-ranking, and 100k inserted terms answering `suggest` without a DFS.

## 📦 Deliverable (by Saturday night)
`hld/04-news-feed/` and `hld/05-typeahead/` (write-up + PNG + ADR each) and `labs/typeahead` with passing tests.

## ✅ Self-check (Sunday test preview)
- Fan-out on write vs fan-out on read: trade-offs, and when to use the hybrid?
- How do you handle a celebrity with 50M followers?
- Why is cursor pagination better than offset pagination for feeds?
- Typeahead: why precompute top-K per trie node?
- How often should the typeahead index be rebuilt, and how is it swapped safely?
- Explain an inverted index and how Elasticsearch scales it with shards and replicas.

## 🚀 Stretch (optional)
Add personalised suggestions (recent searches per user) and explain how they merge with global suggestions; polish both W19 diagrams. Compare your feed with the full [FB news feed breakdown (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed).
