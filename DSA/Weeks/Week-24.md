# 🧩 DSA · Week 24 — Design Data Structures + Math

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** 'Design X' coding questions (LFU, iterators, snapshots) bridge DSA and LLD and are very common for backend roles.

## 🧠 Concepts to master
- O(1) insert/delete/getRandom = array + index map (380)
- Versioned values: per-key list of (time, value) + binary search (981, 1146)
- Lazy iterators with a stack (341)
- LFU = key map + frequency buckets (LinkedHashSet) + minFreq (460); LRU was Week 10
- Counting-based geometry (2013); big-number multiplication (43)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [NeetCode practice list](https://neetcode.io/practice)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [LeetCode Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 05 Apr | [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | 25m | ☐ |
|  |  | [1146. Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | 25m | ☐ |
| Tue | 06 Apr | [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | 25m | ☐ |
|  |  | [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | 25m | ☐ |
| Wed | 07 Apr | [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) | Medium | 25m | ☐ |
|  |  | [1396. Design Underground System](https://leetcode.com/problems/design-underground-system/) | Medium | 25m | ☐ |
| Thu | 08 Apr | [2034. Stock Price Fluctuation ](https://leetcode.com/problems/stock-price-fluctuation/) | Medium | 25m | ☐ |
| Fri | 09 Apr | [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Medium | 25m | ☐ |
|  |  | [2013. Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | 25m | ☐ |
| Sat | 10 Apr | [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) (M) | 20m |
| Tue | [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) (M) | 20m |
| Wed | [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) (M) | 20m |
| Thu | [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) (M) | 20m |
| Fri | [729. My Calendar I](https://leetcode.com/problems/my-calendar-i/) (M) | 20m |
| Sat | [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) (M) · [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [284. Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) (M)
- [895. Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) (H)
- [149. Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) (H)
- [706. Design HashMap](https://leetcode.com/problems/design-hashmap/) (E)
- [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) (H)
- [705. Design HashSet](https://leetcode.com/problems/design-hashset/) (E)
- [641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) (M)
- [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) (M)
- [1352. Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/) (M)
- [202. Happy Number](https://leetcode.com/problems/happy-number/) (E)
- [66. Plus One](https://leetcode.com/problems/plus-one/) (E)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Insert Delete GetRandom O(1): how is delete O(1)?
- Time Based Key-Value Store: why binary search, and on what?
- Snapshot Array: what do you store per index?
- LFU Cache: how do you find the least-frequent key in O(1)?
- Design Underground System: which two maps?
- Multiply Strings: where does digit i * digit j land?

## 💡 Tip
These double as LLD warm-ups - write clean classes with tests. Contest Sunday: explain your up-solve aloud; LFU is Saturday's weekend challenge.
