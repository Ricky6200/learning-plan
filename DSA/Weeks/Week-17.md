# 🧩 DSA · Week 17 — Graphs II: Topological sort & shortest paths

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Dependency ordering and weighted shortest paths (Dijkstra) are high-frequency medium/hard questions.

## 🧠 Concepts to master
- Directed cycle detection (3 colours) and Kahn's algorithm (indegree)
- Eventual safe states via colouring or the reverse graph
- Dijkstra with PriorityQueue and lazy deletion; Bellman-Ford / BFS with K stops; Floyd-Warshall for all pairs (1334)
- 0-1 BFS: edge weights 0/1 -> ArrayDeque, offerFirst for 0, offerLast for 1 (3286; the Hard 2290 is in bonus)
- Java traps: distances and path counts overflow int - use long (1976); LeetCode's Pair is not in the JDK - use int[] or a record
- Alien Dictionary (LC 269) is Premium - free on neetcode.io (foreign-dictionary)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Graph series](https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn)
- [William Fiset - Graph Theory](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)
- [cp-algorithms - 0-1 BFS](https://cp-algorithms.com/graph/01_bfs.html)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 15 Feb | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | 25m | ☐ |
|  |  | [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | 25m | ☐ |
| Tue | 16 Feb | [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Medium | 25m | ☐ |
| Wed | 17 Feb | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | 25m | ☐ |
|  |  | [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | 25m | ☐ |
| Thu | 18 Feb | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | 25m | ☐ |
|  |  | [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | 25m | ☐ |
| Fri | 19 Feb | [1976. Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | Medium | 25m | ☐ |
| Sat | 20 Feb | [3286. Find a Safe Walk Through a Grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/) | Medium | 25m | ☐ |
|  |  | [127. Word Ladder](https://leetcode.com/problems/word-ladder/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (M) | 20m |
| Tue | [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (M) | 20m |
| Wed | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (M) | 20m |
| Thu | [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (M) | 20m |
| Fri | [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) (M) | 20m |
| Sat | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [2290. Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) (H)
- [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) (M)
- [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) (M)
- [752. Open the Lock](https://leetcode.com/problems/open-the-lock/) (M)
- [909. Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/) (M)
- [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (H)
- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) (M)
- [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/) (M)
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) (H)
- [1129. Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Why does Dijkstra fail with negative edges?
- Kahn's algorithm: how do you detect a cycle?
- Cheapest Flights Within K Stops: why is plain Dijkstra tricky?
- Number of Ways to Arrive at Destination: what overflows and how do you fix it?
- 0-1 BFS: why can a deque replace the priority queue?
- Word Ladder: how do you build neighbours efficiently?

## 💡 Tip
Write graph templates in PATTERNS_CHEATSHEET.md from memory once a week. Word Ladder is Saturday's weekend challenge.
