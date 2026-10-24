# 🏗️ System Design · Week 18 — Case studies: news feed, typeahead

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** News feed (fan-out trade-offs) and typeahead (tries, precomputation, caching) are among the most frequently asked HLD questions and teach read-heavy design.

## 🗓️ Sessions

### Monday 22 Feb · 45 min — News feed: fan-out on write vs read, celebrity problem
- 📚 **Learn:** Fan-out on write (push to follower feed caches), fan-out on read (pull and merge at read time), hybrid (pull for celebrities), feed cache in Redis (lists/sorted sets of post IDs), cursor pagination, ranking hook, media via CDN. Read [Design FB news feed (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed); watch its [walkthrough](https://www.youtube.com/watch?v=Qj4-GruzyDU); alternative: [Designing Instagram news feed (Gaurav Sen)](https://www.youtube.com/watch?v=QmX2NPkJTKg).
- 🛠️ **Do:** In `hld/04-news-feed/README.md` do framework steps 1-5 solo in 30 minutes, including an estimate of feed-cache memory for 100M users x 200 post IDs; then 15 minutes comparing with Hello Interview and fixing gaps. Done when: the estimate is shown and you can state your fan-out choice in one sentence.

### Wednesday 24 Feb · 45 min — News feed deep dives: celebrities, ranking, pagination
- 📚 **Learn:** Hybrid fan-out thresholds, async fan-out workers via a queue, cursor vs offset pagination, cache warm-up for inactive users, ranking pipeline (candidates -> features -> score), new-post visibility (eventual is fine). Read the [Twitter timeline solution (system-design-primer)](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md); watch [API pagination (ByteByteGo)](https://www.youtube.com/watch?v=14K_a2kKTxU).
- 🛠️ **Do:** Finish steps 6-7 with 3 deep dives and an Excalidraw diagram, plus a walkthrough of 'a celebrity with 50M followers posts': what is written, what is read, and the latency. Done when: one-page write-up + PNG are committed.

### Thursday 25 Feb · 45 min — Typeahead / search autocomplete
- 📚 **Learn:** Requirements: top-5 suggestions in < 100 ms, prefix match, popularity + freshness. Design: trie with top-K cached per node, offline aggregation (query logs -> counts -> rebuilt trie snapshots), sharding by prefix, browser/CDN caching, client debouncing, filtering bad terms. Watch [Typeahead suggestions system design (Tushar Roy)](https://www.youtube.com/watch?v=us0qySiUsGU); practise the core structure: [Implement Trie (LeetCode 208)](https://leetcode.com/problems/implement-trie-prefix-tree/).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/05-typeahead/README.md` for 5B searches/day, including trie memory estimate, the update pipeline (how often snapshots rebuild) and where caching happens. Done when: all 7 sections are filled and the read path for typing 'avat' is traced step by step.

### Saturday 27 Feb · 45 min — PRACTICE: Typeahead trie with cached top-K
- 📚 **Learn:** Each trie node keeps its top-K completions, refreshed on insert by walking the path; trade memory for O(prefix length) reads. Compare: pure DFS on every keystroke vs cached top-K. Refresher: [Implement Trie (LeetCode 208)](https://leetcode.com/problems/implement-trie-prefix-tree/).
- 🛠️ **Do:** 25 min: implement `AutocompleteTrie` (`insert(term, count)` that updates per-node top-5, `suggest(prefix)` returning the top 5 by count, then alphabetical on ties). 20 min: polish both W18 diagrams. Done when: tests pass for ranking, ties, unknown prefix, updated counts re-ranking, and 100k inserted terms answering `suggest` without DFS.

## 📦 Deliverable (by Saturday night)
`hld/04-news-feed/` and `hld/05-typeahead/` (write-up + PNG each) and `labs/typeahead` with passing tests.

## ✅ Self-check (Sunday test preview)
- Fan-out on write vs fan-out on read: trade-offs, and when to use the hybrid?
- How do you handle a celebrity with 50M followers?
- Why is cursor pagination better than offset pagination for feeds?
- Typeahead: why precompute top-K per trie node?
- How often should the typeahead index be rebuilt, and how is it swapped safely?
- Where would you cache typeahead results, and for how long?

## 🚀 Stretch (optional)
Add personalised suggestions (recent searches per user) and explain how they merge with global suggestions.
