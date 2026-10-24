# 🧩 DSA · Week 01 — Restart: Complexity, Java DSA toolkit, Arrays

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Every interview starts with arrays + complexity talk. Rebuild speed and Java fluency on easy wins first.

## 🧠 Concepts to master
- Big-O time/space; read constraints -> target complexity (n <= 1e5 means O(n log n) or better)
- Java toolkit: int[] vs Integer[], Arrays.sort/fill/toString, ArrayList, HashMap/HashSet, StringBuilder, overflow -> use long
- In-place array tricks: read/write pointers, swap, reverse-based rotation
- Write dry-run tables for loops (index, value, state)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Arrays playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)
- [Big-O cheat sheet](https://www.bigocheatsheet.com/)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 26 Oct | [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | 15m | ☐ |
|  |  | [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | 15m | ☐ |
| Tue | 27 Oct | [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | 15m | ☐ |
|  |  | [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Easy | 15m | ☐ |
| Wed | 28 Oct | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | 15m | ☐ |
|  |  | [27. Remove Element](https://leetcode.com/problems/remove-element/) | Easy | 15m | ☐ |
| Thu | 29 Oct | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | 15m | ☐ |
|  |  | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | 15m | ☐ |
| Fri | 30 Oct | [189. Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | 25m | ☐ |
|  |  | [1752. Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) | Easy | 15m | ☐ |
| Sat | 31 Oct | [268. Missing Number](https://leetcode.com/problems/missing-number/) | Easy | 15m | ☐ |
|  |  | [136. Single Number](https://leetcode.com/problems/single-number/) | Easy | 15m | ☐ |
|  |  | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) 🔥 *weekend challenge — finish Sunday if needed* | Easy | 15m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1295. Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) (E)
- [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) (E)
- [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) (E)
- [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) (E)
- [204. Count Primes](https://leetcode.com/problems/count-primes/) (M)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- What is the time complexity of nested loops where the inner loop runs i times?
- n = 10^5: is O(n^2) acceptable? Why not?
- How do you rotate an array by k in O(1) extra space?
- Why can `int sum` overflow and how do you prevent it in Java?
- Remove duplicates from a sorted array in place - which pattern?

## 💡 Tip
Start a DSA notebook (or REVISION_TRACKER.md): for every problem write the pattern + key insight in 2 lines.
