# 🧩 DSA · Week 06 — Binary Search (arrays & answer space)

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Binary search on the ANSWER is a top medium-level interview pattern (capacity, speed, split problems).

## 🧠 Concepts to master
- Template with invariant: lo/hi, mid = lo + (hi - lo) / 2, which side keeps the answer
- Lower bound / upper bound / first & last occurrence
- Rotated arrays: identify the sorted half
- Peak element & single element in sorted array (index parity)
- Answer-space search: monotonic predicate canFinish(x)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Binary Search playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF)
- [Aditya Verma - Binary Search (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2)
- [NeetCode - Binary Search](https://www.youtube.com/playlist?list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 30 Nov | [704. Binary Search](https://leetcode.com/problems/binary-search/) | Easy | 15m | ☐ |
|  |  | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | 15m | ☐ |
| Tue | 01 Dec | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | 25m | ☐ |
|  |  | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | 25m | ☐ |
| Wed | 02 Dec | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | 25m | ☐ |
|  |  | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | 25m | ☐ |
| Thu | 03 Dec | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | 25m | ☐ |
|  |  | [540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) | Medium | 25m | ☐ |
| Fri | 04 Dec | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | 25m | ☐ |
|  |  | [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | 25m | ☐ |
| Sat | 05 Dec | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | 15m | ☐ |
|  |  | [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | Medium | 25m | ☐ |
|  |  | [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [81. Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) (M)
- [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) (M)
- [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) (M)
- [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (H)
- [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/) (E)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (M)
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (M)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- How do you know a problem is 'binary search on answer'?
- Why mid = lo + (hi - lo) / 2 instead of (lo + hi) / 2?
- In a rotated sorted array, how do you decide which half to discard?
- Write the predicate for Koko Eating Bananas.
- Lower bound vs upper bound - define both.

## 💡 Tip
Always write the loop invariant as a comment before coding the loop.
