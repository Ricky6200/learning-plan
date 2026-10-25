# 🧩 DSA · Week 05 — Prefix Sums, Kadane, Matrix, Intervals

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** Range queries, max subarray, matrix walks and interval merging appear constantly in screening rounds. AZ-900 is on Friday, so Friday has one problem.

## 🧠 Concepts to master
- 1D/2D prefix sums; difference array: +v at l, -v at r + 1, prefix-sum once (1094)
- Sweep line: turn intervals into +1/-1 events, sort, track the running count (2406 is a free twin of Meeting Rooms II, which is Premium; Meeting Rooms I/II are free on neetcode.io as meeting-schedule / meeting-schedule-ii)
- Prefix sum modulo K + HashMap; Java trap: % can be negative - use ((x % k) + k) % k (974)
- Kadane (max subarray); the product variant tracks both min and max (152)
- Matrix: spiral order, rotate = transpose + reverse rows, in-place markers (73)
- Intervals: sort by start to merge (56, 57); Java: collect a List<int[]> and return list.toArray(new int[0][]); comparator (a, b) -> Integer.compare(a[0], b[0]) (lambda primer: Java W4 Fri)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Arrays playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)
- [NeetCode - Blind 75 solutions](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 23 Nov | [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | 15m | ☐ |
|  |  | [1094. Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | 25m | ☐ |
| Tue | 24 Nov | [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | 25m | ☐ |
|  |  | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | 25m | ☐ |
| Wed | 25 Nov | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | 25m | ☐ |
|  |  | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | 25m | ☐ |
| Thu | 26 Nov | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | 25m | ☐ |
|  |  | [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | 25m | ☐ |
| Fri | 27 Nov | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | 25m | ☐ |
| Sat | 28 Nov | [57. Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | 25m | ☐ |
|  |  | [2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | Medium | 25m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (M) | 20m |
| Tue | [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (M) | 20m |
| Wed | [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (M) | 20m |
| Thu | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (M) | 20m |
| Fri | [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) (M) | 20m |
| Sat | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (M) · [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (E) | 20m / 10m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (E)
- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) (M)
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/) (M)
- [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/) (E)
- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) (M)
- [986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) (M)
- [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) (M)
- [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) (M)
- [289. Game of Life](https://leetcode.com/problems/game-of-life/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Car Pooling: how does a difference array check capacity in O(n + range)?
- Subarray Sums Divisible by K: why must you fix negative remainders in Java?
- Why does Maximum Product Subarray need both a running max and min?
- How do you rotate a matrix 90 degrees in place?
- Merge Intervals: why sort by start time? How do you turn a List<int[]> into int[][]?
- Divide Intervals Into Minimum Number of Groups: why is the answer the maximum overlap?

## 💡 Tip
Draw intervals on a number line before coding. Exam day Friday: one problem only (Merge Intervals).
