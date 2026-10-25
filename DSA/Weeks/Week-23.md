# 🧩 DSA · Week 23 — Tries, String Algorithms, Segment Tree/BIT

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Autocomplete, word search and range-query problems need these structures; they are also great talking points for system design.

## 🧠 Concepts to master
- Trie refresher (built in Week 16): wildcard search with DFS; Word Search II = trie + backtracking pruning
- Bitwise trie for maximum XOR
- KMP: build the LPS array, then match without moving backwards (28); rolling hash / Rabin-Karp (187); Z-function awareness
- Fenwick tree & segment tree for point update + range sum (307)
- TreeMap for calendars: floorKey/ceilingKey, or a +1/-1 sweep for double bookings (729, 731)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Trie series](https://www.youtube.com/playlist?list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp)
- [cp-algorithms - Prefix function (KMP)](https://cp-algorithms.com/string/prefix-function.html)
- [cp-algorithms - String hashing (rolling hash)](https://cp-algorithms.com/string/string-hashing.html)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 29 Mar | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | 25m | ☐ |
|  |  | [648. Replace Words](https://leetcode.com/problems/replace-words/) | Medium | 25m | ☐ |
| Tue | 30 Mar | [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | 25m | ☐ |
| Wed | 31 Mar | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Easy | 15m | ☐ |
|  |  | [187. Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | Medium | 25m | ☐ |
| Thu | 01 Apr | [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | Easy | 15m | ☐ |
|  |  | [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | 25m | ☐ |
| Fri | 02 Apr | [729. My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | 25m | ☐ |
|  |  | [731. My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | Medium | 25m | ☐ |
| Sat | 03 Apr | [212. Word Search II](https://leetcode.com/problems/word-search-ii/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (M) | 20m |
| Tue | [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (M) | 20m |
| Wed | [1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) (M) | 20m |
| Thu | [1626. Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/) (M) | 20m |
| Fri | [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) (M) | 20m |
| Sat | [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) (M) · [120. Triangle](https://leetcode.com/problems/triangle/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) (H)
- [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) (M)
- [1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) (H)
- [686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/) (M)
- [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) (H)
- [732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/) (H)
- [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Design Add and Search Words: how does '.' change the search?
- Maximum XOR of Two Numbers: why go bit by bit from the top?
- What does the KMP LPS array store?
- Repeated DNA Sequences: HashSet of substrings vs rolling hash - trade-offs?
- Fenwick tree: complexity of update and prefix query?
- My Calendar I with TreeMap: which methods do you use?

## 💡 Tip
Implement Trie and Fenwick tree from memory in under 15 minutes each. Weekly mock; Word Search II is Saturday's weekend challenge.
