# 🧩 DSA · Week 02 — Hashing: frequency maps & fast lookups

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** HashMap/HashSet turn O(n^2) brute force into O(n). It is the most common optimization interviewers want to see.

## 🧠 Concepts to master
- Frequency counting with HashMap or int[26]
- Complement lookup (Two Sum) and 'seen' sets
- Group by a canonical key (sorted string / char-count signature)
- Prefix sum + HashMap for 'subarray sum equals K'
- Bucket sort idea for top-K by frequency

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Arrays playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)
- [NeetCode - Blind 75 solutions](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 02 Nov | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | 15m | ☐ |
|  |  | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | 15m | ☐ |
| Tue | 03 Nov | [1. Two Sum](https://leetcode.com/problems/two-sum/) | Easy | 15m | ☐ |
|  |  | [169. Majority Element](https://leetcode.com/problems/majority-element/) | Easy | 15m | ☐ |
| Wed | 04 Nov | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | 25m | ☐ |
|  |  | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | 25m | ☐ |
| Thu | 05 Nov | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | 25m | ☐ |
|  |  | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | 25m | ☐ |
| Fri | 06 Nov | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | 25m | ☐ |
|  |  | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | 25m | ☐ |
| Sat | 07 Nov | [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | 15m | ☐ |
|  |  | [290. Word Pattern](https://leetcode.com/problems/word-pattern/) | Easy | 15m | ☐ |
|  |  | [383. Ransom Note](https://leetcode.com/problems/ransom-note/) 🔥 *weekend challenge — finish Sunday if needed* | Easy | 15m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) (M)
- [454. 4Sum II](https://leetcode.com/problems/4sum-ii/) (M)
- [1636. Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) (E)
- [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) (E)
- [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) (E)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/) (M)
- [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (E)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Two Sum on an unsorted array in O(n) - describe the idea.
- How do you group anagrams without sorting each word?
- Why does prefix-sum + hashmap work for subarray sum = K with negative numbers?
- Longest consecutive sequence in O(n) - what is the trick?
- When is int[26] better than HashMap<Character,Integer>?

## 💡 Tip
Say the brute force first in interviews, then optimize with a map. Interviewers score the journey.
