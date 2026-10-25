# 🧩 DSA · Week 02 — Hashing: frequency maps & fast lookups

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** HashMap/HashSet turn O(n^2) brute force into O(n). It is the most common optimization interviewers want to see.

## 🧠 Concepts to master
- Java collections for DSA (recipes): HashSet add/contains; HashMap put/get/containsKey, map.getOrDefault(k, 0) + 1, map.merge(k, 1, Integer::sum), map.computeIfAbsent(k, x -> new ArrayList<>()).add(v); ArrayDeque as a stack/queue - copy them now, the Java track explains generics (18-19 Nov) and lambdas (20 Nov, 30 Nov)
- Custom order before 20 Nov: write the Comparator as an anonymous class - new Comparator<int[]>() { public int compare(int[] a, int[] b) { return Integer.compare(a[0], b[0]); } }
- Frequency counting with HashMap or int[26]; complement lookup (Two Sum); 'seen' sets
- Group by a canonical key (sorted string or char-count signature); bucket sort for top-K by frequency
- Prefix sum + HashMap for 'subarray sum equals K' (560)
- Java trap: map.get(a) != map.get(b) compares Integer objects - only safe for -128..127; use .equals() or int locals (205, 290)
- Encode and Decode Strings (LC 271) is Premium - practise it free on neetcode.io (string-encode-and-decode)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Arrays playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)
- [NeetCode - Blind 75 solutions](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (12 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 02 Nov | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | 15m | ☐ |
|  |  | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | 15m | ☐ |
| Tue | 03 Nov | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | 15m | ☐ |
|  |  | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | 25m | ☐ |
| Wed | 04 Nov | [169. Majority Element](https://leetcode.com/problems/majority-element/) | Easy | 15m | ☐ |
|  |  | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | 25m | ☐ |
| Thu | 05 Nov | [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | 15m | ☐ |
|  |  | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | 25m | ☐ |
| Fri | 06 Nov | [290. Word Pattern](https://leetcode.com/problems/word-pattern/) | Easy | 15m | ☐ |
|  |  | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | 25m | ☐ |
| Sat | 07 Nov | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | 25m | ☐ |
|  |  | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | 25m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (E) | 10m |
| Tue | [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) (E) | 10m |
| Wed | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (E) | 10m |
| Thu | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (E) | 10m |
| Fri | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) (E) | 10m |
| Sat | [268. Missing Number](https://leetcode.com/problems/missing-number/) (E) · [136. Single Number](https://leetcode.com/problems/single-number/) (E) | 10m / 10m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [383. Ransom Note](https://leetcode.com/problems/ransom-note/) (E)
- [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) (M)
- [454. 4Sum II](https://leetcode.com/problems/4sum-ii/) (M)
- [1636. Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) (E)
- [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) (E)
- [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) (E)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Two Sum on an unsorted array in O(n) - describe the idea.
- Group Anagrams: what key do you use, and how can you avoid sorting each word?
- Why does prefix sum + HashMap work for Subarray Sum Equals K with negative numbers?
- Longest Consecutive Sequence in O(n) - what is the trick?
- Isomorphic Strings / Word Pattern: why can `!=` on two Integer values from a map give a wrong answer?
- Top K Frequent Elements without a heap: how does bucket sort work?

## 💡 Tip
Say the brute force first in interviews, then optimize with a map - interviewers score the journey. Keep the recipes above in a 'Java for DSA' note; the Java track explains why they work.
