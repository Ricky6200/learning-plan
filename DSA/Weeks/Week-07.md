# 🧩 DSA · Week 07 — Strings + Bit Manipulation

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** String parsing and bit tricks are favourites for 'quick' rounds and online assessments.

## 🧠 Concepts to master
- StringBuilder, char arithmetic ('c' - 'a'), String immutability cost
- Expand-around-center for palindromes
- Parsing with edge cases (whitespace, sign, overflow) - atoi
- Bit ops: & | ^ ~ << >> >>>; n & (n - 1); XOR cancels pairs
- Counting bits with DP; add without '+' using carry

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Bit Manipulation playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rnqh8QsJaHyIX7KUiaPUv7)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [NeetCode - Blind 75 solutions](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 07 Dec | [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | 15m | ☐ |
|  |  | [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/) | Easy | 15m | ☐ |
| Tue | 08 Dec | [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | Medium | 25m | ☐ |
|  |  | [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | Medium | 25m | ☐ |
| Wed | 09 Dec | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | 25m | ☐ |
|  |  | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | 25m | ☐ |
| Thu | 10 Dec | [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | 15m | ☐ |
|  |  | [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | Medium | 25m | ☐ |
| Fri | 11 Dec | [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | 15m | ☐ |
|  |  | [338. Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | 15m | ☐ |
| Sat | 12 Dec | [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | 15m | ☐ |
|  |  | [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | 25m | ☐ |
|  |  | [137. Single Number II](https://leetcode.com/problems/single-number-ii/) 🔥 *weekend challenge — finish Sunday if needed* | Medium | 25m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) (E)
- [796. Rotate String](https://leetcode.com/problems/rotate-string/) (E)
- [231. Power of Two](https://leetcode.com/problems/power-of-two/) (E)
- [260. Single Number III](https://leetcode.com/problems/single-number-iii/) (M)
- [201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [410. Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) (H)
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (M)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Why is string concatenation in a loop O(n^2) in Java?
- Explain expand-around-center and its complexity.
- What does n & (n - 1) do?
- How do you find the single number when every other appears 3 times?
- What is the difference between >> and >>> in Java?

## 💡 Tip
For parsing problems, list edge cases BEFORE coding.
