# 🧩 DSA · Week 16 — Graphs I: BFS/DFS, grids, components

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Graph traversal on grids and adjacency lists is a must for product companies. AZ-104 exam week: Friday and Saturday have one problem each.

## 🧠 Concepts to master
- Adjacency list in Java: List<List<Integer>>
- DFS (recursive/iterative), BFS for unweighted shortest path
- Multi-source BFS (rotting oranges)
- Boundary DFS (surrounded regions, Pacific Atlantic)
- Bipartite check (2-colouring); clone graph with a HashMap
- Trie preview on Saturday (208): node = children[26] + isEnd; the System Design track builds typeahead on it

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Graph series](https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn)
- [NeetCode - Graph problems](https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI)
- [Striver - Trie series](https://www.youtube.com/playlist?list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 08 Feb | [733. Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | 15m | ☐ |
|  |  | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | 25m | ☐ |
| Tue | 09 Feb | [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | 25m | ☐ |
|  |  | [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | 25m | ☐ |
| Wed | 10 Feb | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | 25m | ☐ |
|  |  | [133. Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | 25m | ☐ |
| Thu | 11 Feb | [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | 25m | ☐ |
|  |  | [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | 25m | ☐ |
| Fri | 12 Feb | [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium | 25m | ☐ |
| Sat | 13 Feb | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | 25m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (M) | 20m |
| Tue | [55. Jump Game](https://leetcode.com/problems/jump-game/) (M) | 20m |
| Wed | [134. Gas Station](https://leetcode.com/problems/gas-station/) (M) | 20m |
| Thu | [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) (M) | 20m |
| Fri | [1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) (M) | 20m |
| Sat | [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) (M) · [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) (M)
- [1020. Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) (M)
- [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) (M)
- [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) (E)
- [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) (M)
- [886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) (M)
- [1162. As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- When is BFS guaranteed to give the shortest path?
- Rotting Oranges: what goes into the queue first?
- Surrounded Regions: why start from the border?
- How do you check if a graph is bipartite?
- Number of Islands: time and space complexity?
- Implement Trie: what does startsWith check that search does not?

## 💡 Tip
Use dr/dc direction arrays for grids; mark visited when you ENQUEUE, not when you dequeue. Full-program practice this fortnight (after the exam).
