# 🧩 DSA · Week 08 — Recursion + Backtracking I

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Recursion is the foundation of trees, graphs and DP. Backtracking generates subsets, permutations and combinations.

## 🧠 Concepts to master
- Recursion tree, base case, call stack depth; Java trap: very deep recursion (about 10^4+ frames) can throw StackOverflowError
- Fast power (divide and conquer); Java trap: n = Integer.MIN_VALUE cannot be negated as an int - widen to long first (50)
- Backtracking template: choose -> explore -> un-choose
- Subsets (include/exclude), combinations (start index), permutations (used[])
- Duplicates: sort + skip the same value at the same depth (90, 40)
- Constraint sets for N-Queens: columns, diagonals r - c + n - 1 and r + c (51)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Recursion & Backtracking playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9)
- [Aditya Verma - Recursion (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY)
- [NeetCode - Backtracking](https://www.youtube.com/playlist?list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 14 Dec | [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Easy | 15m | ☐ |
|  |  | [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | 25m | ☐ |
| Tue | 15 Dec | [78. Subsets](https://leetcode.com/problems/subsets/) | Medium | 25m | ☐ |
|  |  | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | 25m | ☐ |
| Wed | 16 Dec | [46. Permutations](https://leetcode.com/problems/permutations/) | Medium | 25m | ☐ |
|  |  | [77. Combinations](https://leetcode.com/problems/combinations/) | Medium | 25m | ☐ |
| Thu | 17 Dec | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | 25m | ☐ |
|  |  | [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | 25m | ☐ |
| Fri | 18 Dec | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | 25m | ☐ |
| Sat | 19 Dec | [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | 25m | ☐ |
|  |  | [51. N-Queens](https://leetcode.com/problems/n-queens/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) (M) | 20m |
| Tue | [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) (M) | 20m |
| Wed | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (M) | 20m |
| Thu | [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/) (M) | 20m |
| Fri | [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) (E) | 10m |
| Sat | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) (M)
- [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/) (M)
- [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) (M)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/) (M)
- [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) (M)
- [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) (H)
- [1286. Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/) (M)
- [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Draw the recursion tree for subsets of [1,2,3].
- Combinations vs permutations - what changes in the code?
- How do you avoid duplicate subsets when the input has duplicates?
- Pow(x, n): what goes wrong for n = Integer.MIN_VALUE and how do you fix it?
- Generate Parentheses: which two counters prune the tree?
- How do you check diagonal conflicts in N-Queens in O(1)?

## 💡 Tip
Say the template out loud: 'choose, explore, un-choose'. N-Queens is Saturday's weekend challenge.
