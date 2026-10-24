# 🧩 DSA · Week 17 — Graphs II: Topological sort & shortest paths

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Dependency ordering and weighted shortest paths (Dijkstra) are high-frequency medium/hard questions.

## 🧠 Concepts to master
- Directed cycle detection (3 colours) and Kahn's algorithm (indegree)
- Eventual safe states via reverse graph
- Dijkstra with PriorityQueue and lazy deletion
- Bellman-Ford / BFS with K stops; Floyd-Warshall for all pairs
- BFS on implicit graphs (word ladder, snakes & ladders)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Graph series](https://www.youtube.com/playlist?list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn)
- [William Fiset - Graph Theory](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)
- [NeetCode - Graph problems](https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 15 Feb | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | 25m | ☐ |
|  |  | [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | 25m | ☐ |
| Tue | 16 Feb | [802. Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Medium | 25m | ☐ |
|  |  | [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | Medium | 25m | ☐ |
| Wed | 17 Feb | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | 25m | ☐ |
|  |  | [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | 25m | ☐ |
| Thu | 18 Feb | [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | 25m | ☐ |
|  |  | [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | 25m | ☐ |
| Fri | 19 Feb | [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | 25m | ☐ |
|  |  | [1976. Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | Medium | 25m | ☐ |
| Sat | 20 Feb | [909. Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/) | Medium | 25m | ☐ |
|  |  | [752. Open the Lock](https://leetcode.com/problems/open-the-lock/) | Medium | 25m | ☐ |
|  |  | [127. Word Ladder](https://leetcode.com/problems/word-ladder/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (H)
- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) (M)
- [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/) (M)
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) (H)
- [1129. Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (M)
- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (M)
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Why does Dijkstra fail with negative edges?
- Kahn's algorithm: how do you detect a cycle?
- Cheapest Flights Within K Stops: why is plain Dijkstra tricky?
- What is the complexity of Dijkstra with a binary heap?
- Word Ladder: how do you build neighbours efficiently?

## 💡 Tip
Write graph templates in PATTERNS_CHEATSHEET.md from memory once a week.
