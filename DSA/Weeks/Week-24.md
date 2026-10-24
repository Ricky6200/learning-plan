# 🧩 DSA · Week 24 — Design Data Structures + Math

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** 'Design X' coding questions (LRU/LFU/iterators) bridge DSA and LLD and are very common for backend roles.

## 🧠 Concepts to master
- LRU = HashMap + doubly linked list; LFU = frequency buckets
- O(1) insert/delete/getRandom = array + index map
- Lazy iterators with stacks
- Max frequency stack; All O'one buckets
- Geometry via slope normalization (GCD); big-number multiplication

## 🎥 Learn from (pick ONE per topic — don't binge)
- [NeetCode practice list](https://neetcode.io/practice)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [LeetCode Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 05 Apr | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | 25m | ☐ |
|  |  | [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | 40m | ☐ |
| Tue | 06 Apr | [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | 25m | ☐ |
|  |  | [706. Design HashMap](https://leetcode.com/problems/design-hashmap/) | Easy | 15m | ☐ |
| Wed | 07 Apr | [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | 25m | ☐ |
|  |  | [284. Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Medium | 25m | ☐ |
| Thu | 08 Apr | [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) | Medium | 25m | ☐ |
|  |  | [1396. Design Underground System](https://leetcode.com/problems/design-underground-system/) | Medium | 25m | ☐ |
| Fri | 09 Apr | [895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) | Hard | 40m | ☐ |
|  |  | [2034. Stock Price Fluctuation ](https://leetcode.com/problems/stock-price-fluctuation/) | Medium | 25m | ☐ |
| Sat | 10 Apr | [2013. Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | 25m | ☐ |
|  |  | [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium | 25m | ☐ |
|  |  | [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) (H)
- [705. Design HashSet](https://leetcode.com/problems/design-hashset/) (E)
- [641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) (M)
- [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) (M)
- [1352. Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/) (M)
- [202. Happy Number](https://leetcode.com/problems/happy-number/) (E)
- [66. Plus One](https://leetcode.com/problems/plus-one/) (E)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [212. Word Search II](https://leetcode.com/problems/word-search-ii/) (H)
- [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) (H)
- [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- LRU get/put in O(1): which two structures and why?
- LFU: how do you find the least-frequent key in O(1)?
- Insert Delete GetRandom: how is delete O(1)?
- Design HashMap: how do you handle collisions?
- Max Points on a Line: why normalize slopes with GCD?

## 💡 Tip
These double as LLD warm-ups - write clean classes with tests.
