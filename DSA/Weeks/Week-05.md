# 🧩 DSA · Week 05 — Prefix Sums, Kadane, Matrix, Intervals

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** Range queries, max subarray and interval merging appear constantly in screening rounds.

## 🧠 Concepts to master
- 1D/2D prefix sums and difference arrays
- Prefix sum modulo K + HashMap
- Kadane (max subarray); product variant tracks both min and max
- Matrix: spiral order, rotate = transpose + reverse rows, in-place markers
- Intervals: sort by start to merge; sort by end for max non-overlapping

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Arrays playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)
- [NeetCode - Blind 75 solutions](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 23 Nov | [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | 15m | ☐ |
|  |  | [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | 15m | ☐ |
| Tue | 24 Nov | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | 25m | ☐ |
|  |  | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | 25m | ☐ |
| Wed | 25 Nov | [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | 25m | ☐ |
|  |  | [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | 25m | ☐ |
| Thu | 26 Nov | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | 25m | ☐ |
|  |  | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | 25m | ☐ |
| Fri | 27 Nov | [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | 25m | ☐ |
|  |  | [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | 25m | ☐ |
| Sat | 28 Nov | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | 25m | ☐ |
|  |  | [57. Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | 25m | ☐ |
|  |  | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) 🔥 *weekend challenge — finish Sunday if needed* | Medium | 25m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) (M)
- [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) (M)
- [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) (M)
- [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) (M)
- [289. Game of Life](https://leetcode.com/problems/game-of-life/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (H)
- [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (M)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Why does Maximum Product Subarray need both a running max and min?
- How do you rotate a matrix 90 degrees in place?
- Merge intervals: why sort by start time?
- What does a difference array let you do in O(1) per update?
- Contiguous Array (equal 0s and 1s): what transformation makes it a prefix-sum problem?

## 💡 Tip
Draw intervals on a number line before coding.
