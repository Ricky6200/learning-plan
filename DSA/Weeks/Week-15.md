# 🧩 DSA · Week 15 — Greedy

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** Greedy problems test reasoning: you must justify why a local choice is globally optimal.

## 🧠 Concepts to master
- Greedy choice + exchange argument
- Sort-then-greedy; intervals by end time
- Reachability (jump game), net balance (gas station)
- Two-pass greedy (candy)
- When greedy fails -> switch to DP

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Greedy playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rF1w2Koyh78zafB0cz7tea)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [NeetCode practice list](https://neetcode.io/practice)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 01 Feb | [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | 15m | ☐ |
|  |  | [860. Lemonade Change](https://leetcode.com/problems/lemonade-change/) | Easy | 15m | ☐ |
| Tue | 02 Feb | [55. Jump Game](https://leetcode.com/problems/jump-game/) | Medium | 25m | ☐ |
|  |  | [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | 25m | ☐ |
| Wed | 03 Feb | [134. Gas Station](https://leetcode.com/problems/gas-station/) | Medium | 25m | ☐ |
|  |  | [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | 25m | ☐ |
| Thu | 04 Feb | [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | 25m | ☐ |
|  |  | [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | 25m | ☐ |
| Fri | 05 Feb | [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | 25m | ☐ |
|  |  | [1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | 25m | ☐ |
| Sat | 06 Feb | [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | 25m | ☐ |
|  |  | [179. Largest Number](https://leetcode.com/problems/largest-number/) | Medium | 25m | ☐ |
|  |  | [135. Candy](https://leetcode.com/problems/candy/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) (M)
- [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) (H)
- [330. Patching Array](https://leetcode.com/problems/patching-array/) (H)
- [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) (M)
- [2405. Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (H)
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (H)
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Why does Gas Station only need one pass?
- Jump Game II: BFS-like levels or greedy - explain.
- Partition labels: what do you precompute?
- Largest Number: how do you compare two numbers as strings?
- Give an example where greedy fails (hint: coin change with arbitrary coins).

## 💡 Tip
Before coding greedy, try to break it with a counter-example for 2 minutes.
