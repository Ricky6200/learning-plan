# 🧩 DSA · Week 01 — Restart: Complexity, Java DSA toolkit, Arrays

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Every interview starts with arrays + complexity talk. Rebuild speed and Java fluency on easy wins first: 2 new problems a day, and from Tuesday a short re-solve of yesterday's problem.

## 🧠 Concepts to master
- Big-O time/space; read constraints -> target complexity (n <= 1e5 means O(n log n) or better)
- Java toolkit: int[] vs Integer[], Arrays.sort/fill/toString, StringBuilder, overflow -> use long
- Java collections for DSA (copy these recipes; the Java track explains them in Weeks 2-5): List<Integer> res = new ArrayList<>(); res.add(x); res.get(i); res.size(); List<List<Integer>> rows = new ArrayList<>(); rows.add(new ArrayList<>()) (LC 118, 448)
- In-place array tricks: read/write pointers (27, 26, 80), swap, reverse-based rotation (189)
- Index marking: use the array itself as a 'seen' table by negating nums[abs(x) - 1] (448)
- Write dry-run tables for loops (index, value, state)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Arrays playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rENwdL0nEH0uGom9no0nyB)
- [Big-O cheat sheet](https://www.bigocheatsheet.com/)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (12 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 26 Oct | [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | 15m | ☐ |
|  |  | [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Easy | 15m | ☐ |
| Tue | 27 Oct | [27. Remove Element](https://leetcode.com/problems/remove-element/) | Easy | 15m | ☐ |
|  |  | [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Easy | 15m | ☐ |
| Wed | 28 Oct | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | 15m | ☐ |
|  |  | [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Medium | 25m | ☐ |
| Thu | 29 Oct | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | 15m | ☐ |
|  |  | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | 15m | ☐ |
| Fri | 30 Oct | [189. Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | 25m | ☐ |
|  |  | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | 15m | ☐ |
| Sat | 31 Oct | [268. Missing Number](https://leetcode.com/problems/missing-number/) | Easy | 15m | ☐ |
|  |  | [136. Single Number](https://leetcode.com/problems/single-number/) | Easy | 15m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | — (first day) |  |
| Tue | [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (E) | 10m |
| Wed | [27. Remove Element](https://leetcode.com/problems/remove-element/) (E) | 10m |
| Thu | [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) (M) | 20m |
| Fri | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) (E) | 10m |
| Sat | [189. Rotate Array](https://leetcode.com/problems/rotate-array/) (M) · [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) (E) | 20m / 10m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) (E)
- [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) (E)
- [1752. Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) (E)
- [1295. Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) (E)
- [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) (E)
- [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) (E)
- [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) (E)
- [204. Count Primes](https://leetcode.com/problems/count-primes/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- What is the time complexity of nested loops where the inner loop runs i times?
- n = 10^5: is O(n^2) acceptable? Why not?
- How do you rotate an array by k in O(1) extra space (LC 189)?
- Why can `int sum` overflow and how do you prevent it in Java?
- Remove Duplicates from Sorted Array II: what condition keeps at most two copies?
- Find All Numbers Disappeared in an Array: how does negating values mark 'seen' without extra space?

## 💡 Tip
Start REVISION_TRACKER.md: for every problem write the pattern + key insight in 2 lines. Daily habit from today: record a 2-minute talk-aloud explanation of one problem on your phone (approach, complexity, one edge case) - interviews grade explanation, not just code.
