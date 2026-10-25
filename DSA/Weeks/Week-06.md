# 🧩 DSA · Week 06 — Binary Search (arrays & answer space)

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Binary search on the ANSWER (capacity, speed, minimise the max / maximise the min) is a top medium-level interview pattern.

## 🧠 Concepts to master
- Template with invariant: lo/hi, mid = lo + (hi - lo) / 2, which side keeps the answer
- Lower bound / upper bound / first & last occurrence (34)
- Rotated arrays: identify the sorted half (33, 153)
- Peak element (162): move towards the bigger neighbour
- Answer-space search with a monotonic predicate canFinish(x): minimise the max (875, 1011, 410) or maximise the min (1552, the classic 'Aggressive Cows')

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Binary Search playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF)
- [Aditya Verma - Binary Search (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2)
- [NeetCode - Binary Search](https://www.youtube.com/playlist?list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 30 Nov | [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | 15m | ☐ |
|  |  | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | 25m | ☐ |
| Tue | 01 Dec | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | 25m | ☐ |
|  |  | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | 25m | ☐ |
| Wed | 02 Dec | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | 25m | ☐ |
|  |  | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | 25m | ☐ |
| Thu | 03 Dec | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | 15m | ☐ |
|  |  | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | 25m | ☐ |
| Fri | 04 Dec | [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | 25m | ☐ |
| Sat | 05 Dec | [1552. Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/) | Medium | 25m | ☐ |
|  |  | [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [1094. Car Pooling](https://leetcode.com/problems/car-pooling/) (M) | 20m |
| Tue | [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) (M) | 20m |
| Wed | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (M) | 20m |
| Thu | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (M) | 20m |
| Fri | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) (M) | 20m |
| Sat | [31. Next Permutation](https://leetcode.com/problems/next-permutation/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) (E)
- [540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) (M)
- [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) (M)
- [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) (M)
- [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) (M)
- [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/) (E)
- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- How do you know a problem is 'binary search on answer'?
- Why mid = lo + (hi - lo) / 2 instead of (lo + hi) / 2?
- In a rotated sorted array, how do you decide which half to discard?
- Write the predicate for Koko Eating Bananas.
- Magnetic Force Between Two Balls: why is 'maximise the minimum distance' monotonic?
- Lower bound vs upper bound - define both.

## 💡 Tip
Always write the loop invariant as a comment before coding the loop. From this week the Sunday test's second problem is an unseen one from an earlier pattern.
