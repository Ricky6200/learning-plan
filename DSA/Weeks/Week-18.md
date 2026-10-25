# 🧩 DSA · Week 18 — Graphs III: Union-Find, MST & bridges

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** DSU and MST questions separate strong candidates; bridges show depth. Saturday adds autocomplete with a trie - System Design builds typeahead the same day.

## 🧠 Concepts to master
- DSU with path compression + union by rank/size
- Counting components, redundant edges, equality equations
- Kruskal (sort edges + DSU) and Prim (PriorityQueue)
- Bridges/articulation points (Tarjan low-link, 1192)
- Awareness: strongly connected components (Kosaraju: DFS finish order, reverse graph, DFS again) and shortest path in a DAG (topological order + relax) - practised in Week 29
- Graph Valid Tree (261) and Number of Connected Components (323) are Premium - free on neetcode.io (valid-tree, count-connected-components)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Graph series](https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn)
- [William Fiset - Graph Theory](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)
- [cp-algorithms - Strongly connected components (Kosaraju)](https://cp-algorithms.com/graph/strongly-connected-components.html)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 22 Feb | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | 25m | ☐ |
|  |  | [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Medium | 25m | ☐ |
| Tue | 23 Feb | [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | 25m | ☐ |
|  |  | [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium | 25m | ☐ |
| Wed | 24 Feb | [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | 25m | ☐ |
|  |  | [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | 25m | ☐ |
| Thu | 25 Feb | [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | Medium | 25m | ☐ |
| Fri | 26 Feb | [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) | Medium | 25m | ☐ |
| Sat | 27 Feb | [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | 25m | ☐ |
|  |  | [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) (M) | 20m |
| Tue | [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) (M) | 20m |
| Wed | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) (M) | 20m |
| Thu | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (M) | 20m |
| Fri | [1976. Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) (M) | 20m |
| Sat | [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/) (H)
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) (M)
- [2101. Detonate the Maximum Bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/) (M)
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) (H)
- [1061. Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) (M)
- [2685. Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- What is the amortized complexity of DSU with both optimizations?
- Kruskal vs Prim: when to prefer which?
- Accounts Merge: what do you union?
- Most Stones Removed: why is the answer n - components?
- Define a bridge and how low-link detects it.
- Search Suggestions System: trie or sorting + binary search - trade-offs?

## 💡 Tip
Keep one tested DSU class in your notebook and reuse it. Contest Sunday this week; the next talk-aloud mock is Week 19's test. Full-program practice this fortnight.
