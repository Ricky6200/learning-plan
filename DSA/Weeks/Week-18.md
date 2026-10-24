# 🧩 DSA · Week 18 — Graphs III: Union-Find & MST

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** DSU and MST questions separate strong candidates; bridges show depth.

## 🧠 Concepts to master
- DSU with path compression + union by rank/size
- Counting components, redundant edges, equality equations
- Kruskal (sort edges + DSU) and Prim (PriorityQueue)
- Bridges/articulation points (Tarjan low-link)
- Critical vs pseudo-critical MST edges

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Graph series](https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn)
- [William Fiset - Graph Theory](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)
- [cp-algorithms](https://cp-algorithms.com/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 22 Feb | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | 25m | ☐ |
|  |  | [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Medium | 25m | ☐ |
| Tue | 23 Feb | [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | 25m | ☐ |
|  |  | [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium | 25m | ☐ |
| Wed | 24 Feb | [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | 25m | ☐ |
|  |  | [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | 25m | ☐ |
| Thu | 25 Feb | [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/) | Hard | 40m | ☐ |
|  |  | [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | Medium | 25m | ☐ |
| Fri | 26 Feb | [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | 40m | ☐ |
|  |  | [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) | Medium | 25m | ☐ |
| Sat | 27 Feb | [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | Medium | 25m | ☐ |
|  |  | [2101. Detonate the Maximum Bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/) | Medium | 25m | ☐ |
|  |  | [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) (H)
- [1061. Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) (M)
- [2685. Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/) (H)
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/) (M)
- [135. Candy](https://leetcode.com/problems/candy/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- What is the amortized complexity of DSU with both optimizations?
- Kruskal vs Prim: when to prefer which?
- Accounts Merge: what do you union?
- Define a bridge and how low-link detects it.
- Most Stones Removed: why is the answer n - components?

## 💡 Tip
Keep one tested DSU class in your notebook and reuse it.
