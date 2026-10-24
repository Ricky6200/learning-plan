# 🧩 DSA · Week 03 — Two Pointers + Sorting algorithms

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Two pointers solve sorted-array, pair/triplet and partition problems in O(n); sorting knowledge is a classic viva topic.

## 🧠 Concepts to master
- Opposite-end pointers (sorted pair sum, palindrome, container)
- Same-direction pointers (read/write), Dutch national flag partition
- 3Sum: sort + fix one + two pointers + skip duplicates
- Merge sort & quick sort from scratch; stable vs unstable; worst cases
- Java: Arrays.sort uses dual-pivot quicksort for primitives, TimSort for objects

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Two Pointer & Sliding Window playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL)
- [Abdul Bari - Algorithms](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 09 Nov | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | 15m | ☐ |
|  |  | [344. Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | 15m | ☐ |
| Tue | 10 Nov | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | 25m | ☐ |
|  |  | [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | 15m | ☐ |
| Wed | 11 Nov | [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | 25m | ☐ |
|  |  | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | 25m | ☐ |
| Thu | 12 Nov | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | 25m | ☐ |
|  |  | [31. Next Permutation](https://leetcode.com/problems/next-permutation/) | Medium | 25m | ☐ |
| Fri | 13 Nov | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium | 25m | ☐ |
|  |  | [18. 4Sum](https://leetcode.com/problems/4sum/) | Medium | 25m | ☐ |
| Sat | 14 Nov | [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | 15m | ☐ |
|  |  | [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | 25m | ☐ |
|  |  | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) (E)
- [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) (E)
- [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) (E)
- [2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) (M)
- [1089. Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/) (E)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (M)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Why does the two-pointer approach work for Container With Most Water?
- How do you avoid duplicate triplets in 3Sum?
- Explain Dutch national flag in one sentence.
- Merge sort vs quick sort: complexity, stability, extra space.
- Next Permutation: describe the 3 steps.

## 💡 Tip
In LC 912 implement BOTH merge sort and quick sort yourself - no Arrays.sort.
