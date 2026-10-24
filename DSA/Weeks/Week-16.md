# 🧩 DSA · Week 16 — Graphs I: BFS/DFS, grids, components

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Graph traversal on grids and adjacency lists is a must for product companies.

## 🧠 Concepts to master
- Adjacency list in Java: List<List<Integer>>
- DFS (recursive/iterative), BFS for unweighted shortest path
- Multi-source BFS (rotting oranges, 01 matrix)
- Boundary DFS (surrounded regions, enclaves)
- Bipartite check (2-colouring); clone graph with a map

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Graph series](https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn)
- [NeetCode - Graph problems](https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI)
- [William Fiset - Graph Theory](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 08 Feb | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | 15m | ☐ |
|  |  | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | 25m | ☐ |
| Tue | 09 Feb | [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | 25m | ☐ |
|  |  | [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | 25m | ☐ |
| Wed | 10 Feb | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | 25m | ☐ |
|  |  | [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium | 25m | ☐ |
| Thu | 11 Feb | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | 25m | ☐ |
|  |  | [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | 25m | ☐ |
| Fri | 12 Feb | [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | 25m | ☐ |
|  |  | [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) | Medium | 25m | ☐ |
| Sat | 13 Feb | [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium | 25m | ☐ |
|  |  | [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | Medium | 25m | ☐ |
|  |  | [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) 🔥 *weekend challenge — finish Sunday if needed* | Easy | 15m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) (M)
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) (M)
- [886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) (M)
- [1162. As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [135. Candy](https://leetcode.com/problems/candy/) (H)
- [55. Jump Game](https://leetcode.com/problems/jump-game/) (M)
- [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- When is BFS guaranteed to give the shortest path?
- Multi-source BFS: what goes into the queue first?
- Surrounded regions: why start from the border?
- How do you check if a graph is bipartite?
- Number of islands: time and space complexity?

## 💡 Tip
Use dr/dc direction arrays for grids; mark visited when you ENQUEUE, not when you dequeue.
