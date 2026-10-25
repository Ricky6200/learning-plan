# 🧩 DSA · Week 03 — Two Pointers + Sorting algorithms

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Two pointers solve sorted-array, pair/triplet and partition problems in O(n); merge sort is a classic viva topic and your first real recursion.

## 🧠 Concepts to master
- Opposite-end pointers (sorted pair sum, palindrome, container)
- Same-direction pointers (read/write); Dutch national flag partition (75)
- 3Sum: sort + fix one + two pointers + skip duplicates
- Recursion basics (the Java track showed the call stack on Thu 29 Oct): base case, trust the smaller call, combine - merge sort = sort left half, sort right half, merge
- LC 912 with merge sort only (O(n log n), stable, O(n) extra); bonus: redo it with quicksort + random pivot + 3-way partition (plain quicksort gets TLE)
- Java: Arrays.sort uses dual-pivot quicksort for primitives, TimSort (stable) for objects

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Two Pointer & Sliding Window playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL)
- [Abdul Bari - Algorithms](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 09 Nov | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | 15m | ☐ |
|  |  | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | 25m | ☐ |
| Tue | 10 Nov | [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | 15m | ☐ |
|  |  | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | 25m | ☐ |
| Wed | 11 Nov | [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | 15m | ☐ |
|  |  | [15. 3Sum](https://leetcode.com/problems/3sum/) | Medium | 25m | ☐ |
| Thu | 12 Nov | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | 25m | ☐ |
|  |  | [31. Next Permutation](https://leetcode.com/problems/next-permutation/) | Medium | 25m | ☐ |
| Fri | 13 Nov | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium | 25m | ☐ |
| Sat | 14 Nov | [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | 25m | ☐ |
|  |  | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (E) | 10m |
| Tue | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (M) | 20m |
| Wed | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (M) | 20m |
| Thu | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (M) | 20m |
| Fri | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (M) | 20m |
| Sat | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [344. Reverse String](https://leetcode.com/problems/reverse-string/) (E)
- [18. 4Sum](https://leetcode.com/problems/4sum/) (M)
- [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) (E)
- [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) (E)
- [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) (E)
- [2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) (M)
- [1089. Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/) (E)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Why does the two-pointer approach work for Container With Most Water?
- How do you avoid duplicate triplets in 3Sum?
- Explain Dutch national flag (Sort Colors) in one sentence.
- Merge sort vs quick sort: complexity, stability, extra space. Why does naive quicksort fail on LC 912?
- Next Permutation: describe the 3 steps.
- Trapping Rain Water: what does each pointer remember?

## 💡 Tip
LC 912: write merge sort yourself (no Arrays.sort) and draw the recursion tree for 4 elements first. 4Sum (LC 18) is in bonus - 3Sum with one more loop.
