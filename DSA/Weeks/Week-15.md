# 🧩 DSA · Week 15 — Greedy + Season 3 Review - BOSS week

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** Greedy problems test reasoning: you must justify why a local choice is globally optimal. Saturday's boss mixes greedy with Season 3 (lists, stacks, trees, heaps).

## 🧠 Concepts to master
- Greedy choice + exchange argument
- Sort-then-greedy; intervals by end time for max non-overlapping (435)
- Reachability (jump game), net balance (gas station)
- Grouping with counts or a TreeMap (846 Hand of Straights)
- Custom string order: compare a + b with b + a (179)
- When greedy fails -> switch to DP

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Greedy playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rF1w2Koyh78zafB0cz7tea)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [NeetCode practice list](https://neetcode.io/practice)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 01 Feb | [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | 15m | ☐ |
|  |  | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | 25m | ☐ |
| Tue | 02 Feb | [55. Jump Game](https://leetcode.com/problems/jump-game/) | Medium | 25m | ☐ |
|  |  | [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | 25m | ☐ |
| Wed | 03 Feb | [134. Gas Station](https://leetcode.com/problems/gas-station/) | Medium | 25m | ☐ |
|  |  | [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | 25m | ☐ |
| Thu | 04 Feb | [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | 25m | ☐ |
|  |  | [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | 25m | ☐ |
| Fri | 05 Feb | [1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | 25m | ☐ |
| Sat | 06 Feb | [179. Largest Number](https://leetcode.com/problems/largest-number/) | Medium | 25m | ☐ |
|  |  | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (E) | 10m |
| Tue | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (M) | 20m |
| Wed | [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) (M) | 20m |
| Thu | [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) (M) | 20m |
| Fri | [355. Design Twitter](https://leetcode.com/problems/design-twitter/) (M) | 20m |
| Sat | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [860. Lemonade Change](https://leetcode.com/problems/lemonade-change/) (E)
- [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (M)
- [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) (M)
- [135. Candy](https://leetcode.com/problems/candy/) (H)
- [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) (M)
- [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) (H)
- [330. Patching Array](https://leetcode.com/problems/patching-array/) (H)
- [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) (M)
- [2405. Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Why does Gas Station only need one pass?
- Jump Game II: BFS-like levels or greedy - explain.
- Non-overlapping Intervals: why sort by end time?
- Partition Labels: what do you precompute?
- Largest Number: how do you compare two numbers as strings?
- Merge k Sorted Lists: heap vs divide-and-conquer - complexity of each?

## 💡 Tip
BOSS Saturday: LC 179 + LC 23 timed (60 min, no hints). Before coding any greedy, try to break it with a counter-example for 2 minutes. Candy (135) is a bonus favourite.
