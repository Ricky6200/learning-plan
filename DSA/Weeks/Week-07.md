# 🧩 DSA · Week 07 — Strings + Bit Manipulation

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** String parsing and bit tricks are favourites for quick rounds and online assessments.

## 🧠 Concepts to master
- StringBuilder, char arithmetic ('c' - 'a'), String immutability cost
- String arithmetic digit by digit with a carry (415)
- Expand-around-center for palindromes (5, 647)
- Parsing with edge cases (whitespace, sign, overflow) - atoi (8)
- Bit ops: & | ^ ~ << >> >>>; n & (n - 1) clears the lowest set bit; XOR cancels pairs
- Counting bits with DP (338); add without '+' using XOR + carry (371)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Bit Manipulation playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rnqh8QsJaHyIX7KUiaPUv7)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [NeetCode - Blind 75 solutions](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (12 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 07 Dec | [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | 15m | ☐ |
|  |  | [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | Medium | 25m | ☐ |
| Tue | 08 Dec | [415. Add Strings](https://leetcode.com/problems/add-strings/) | Easy | 15m | ☐ |
|  |  | [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | Medium | 25m | ☐ |
| Wed | 09 Dec | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | 25m | ☐ |
|  |  | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | 25m | ☐ |
| Thu | 10 Dec | [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | 15m | ☐ |
|  |  | [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | Medium | 25m | ☐ |
| Fri | 11 Dec | [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | 15m | ☐ |
|  |  | [338. Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | 15m | ☐ |
| Sat | 12 Dec | [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | 15m | ☐ |
|  |  | [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | 25m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (M) | 20m |
| Tue | [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (M) | 20m |
| Wed | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (M) | 20m |
| Thu | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (M) | 20m |
| Fri | [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) (M) | 20m |
| Sat | [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) (M) · [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) (E)
- [137. Single Number II](https://leetcode.com/problems/single-number-ii/) (M)
- [796. Rotate String](https://leetcode.com/problems/rotate-string/) (E)
- [231. Power of Two](https://leetcode.com/problems/power-of-two/) (E)
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/) (M)
- [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) (M)
- [67. Add Binary](https://leetcode.com/problems/add-binary/) (E)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Why is string concatenation in a loop O(n^2) in Java?
- Add Strings: how do you handle different lengths and the final carry?
- Explain expand-around-center and its complexity.
- What does n & (n - 1) do? Use it for Number of 1 Bits.
- What is the difference between >> and >>> in Java?
- Sum of Two Integers: how do XOR and AND give sum and carry?

## 💡 Tip
For parsing problems, list edge cases BEFORE coding. Single Number II (137) is in bonus if bits click.
