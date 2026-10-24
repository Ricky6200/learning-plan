# 🧩 DSA · Week 08 — Recursion + Backtracking I

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Recursion is the foundation of trees, graphs and DP. Backtracking generates subsets/permutations/combinations.

## 🧠 Concepts to master
- Recursion tree, base case, call stack depth
- Fast power (divide and conquer)
- Backtracking template: choose -> explore -> un-choose
- Subsets (include/exclude), combinations (start index), permutations (used[])
- Duplicates: sort + skip same value at the same depth

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Recursion & Backtracking playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9)
- [Aditya Verma - Recursion (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY)
- [NeetCode - Backtracking](https://www.youtube.com/playlist?list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 14 Dec | [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Easy | 15m | ☐ |
|  |  | [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | 25m | ☐ |
| Tue | 15 Dec | [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/) | Medium | 25m | ☐ |
|  |  | [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) | Medium | 25m | ☐ |
| Wed | 16 Dec | [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | 25m | ☐ |
|  |  | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | 25m | ☐ |
| Thu | 17 Dec | [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | 25m | ☐ |
|  |  | [77. Combinations](https://leetcode.com/problems/combinations/) | Medium | 25m | ☐ |
| Fri | 18 Dec | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | 25m | ☐ |
|  |  | [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | 25m | ☐ |
| Sat | 19 Dec | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | 25m | ☐ |
|  |  | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | 25m | ☐ |
|  |  | [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) 🔥 *weekend challenge — finish Sunday if needed* | Medium | 25m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/) (M)
- [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) (M)
- [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) (H)
- [1286. Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) (M)
- [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) (M)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Draw the recursion tree for subsets of [1,2,3].
- Combinations vs permutations - what changes in the code?
- How do you avoid duplicate subsets when input has duplicates?
- Time complexity of generating all permutations?
- How does fast power reduce O(n) to O(log n)?

## 💡 Tip
Say the template out loud: 'choose, explore, un-choose'.
