# 🧩 DSA · Week 09 — Backtracking II + Season 2 Review - BOSS week

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Harder backtracking plus a mixed review trains pattern recognition under time pressure. Christmas (Friday) is a one-problem day.

## 🧠 Concepts to master
- Grid backtracking with in-place visited marking (79)
- Partitioning strings: palindrome partitioning, IP segments (131, 93)
- Pruning: sort descending, fail fast when a side overflows (473)
- Cyclic sort / index-as-hash: put value v at index v - 1, or mark nums[v - 1] negative (442 on Friday -> 41 on Saturday)
- Mixed review: identify the pattern within 2 minutes (16, 1838, 1239, 1760)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Recursion & Backtracking playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9)
- [NeetCode - Backtracking](https://www.youtube.com/playlist?list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo)
- [Sean Prashad - LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 21 Dec | [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | 25m | ☐ |
|  |  | [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | 25m | ☐ |
| Tue | 22 Dec | [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) | Medium | 25m | ☐ |
|  |  | [1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) | Medium | 25m | ☐ |
| Wed | 23 Dec | [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | 25m | ☐ |
|  |  | [1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | Medium | 25m | ☐ |
| Thu | 24 Dec | [473. Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) | Medium | 25m | ☐ |
| Fri | 25 Dec | [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Medium | 25m | ☐ |
| Sat | 26 Dec | [1760. Minimum Limit of Balls in a Bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/) | Medium | 25m | ☐ |
|  |  | [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) (M) | 20m |
| Tue | [78. Subsets](https://leetcode.com/problems/subsets/) (M) | 20m |
| Wed | [46. Permutations](https://leetcode.com/problems/permutations/) (M) | 20m |
| Thu | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) (M) | 20m |
| Fri | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (M) | 20m |
| Sat | [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) (H)
- [1208. Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) (M)
- [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/) (E)
- [980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) (H)
- [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) (H)
- [282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Why does Word Search need un-marking after recursion?
- Restore IP Addresses: which checks prune invalid segments?
- Find All Duplicates in an Array: how does marking nums[abs(x) - 1] negative find duplicates in O(1) space?
- First Missing Positive in O(n) time, O(1) space - idea?
- Name the pattern: 'minimum largest value after operations' (LC 1760).
- Frequency of the Most Frequent Element: why sort first?

## 💡 Tip
BOSS Saturday: LC 1760 + LC 41 timed (60 min, no hints). Record which patterns you failed to spot. Sudoku Solver (37) is a bonus weekend project.
