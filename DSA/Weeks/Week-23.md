# 🧩 DSA · Week 23 — Tries, String Algorithms, Segment Tree/BIT - BOSS week

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Autocomplete, word search and range-query problems need these structures; also great talking points for system design.

## 🧠 Concepts to master
- Trie node (children[26], isEnd); insert/search/startsWith
- Wildcard search with DFS; Word Search II = trie + backtracking pruning
- Bitwise trie for maximum XOR
- KMP (LPS array), rolling hash (Rabin-Karp), Z-function awareness
- Fenwick tree & segment tree; merge-sort counting; TreeMap for calendars

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Trie series](https://www.youtube.com/playlist?list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp)
- [cp-algorithms](https://cp-algorithms.com/)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 29 Mar | [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | 25m | ☐ |
|  |  | [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | 25m | ☐ |
| Tue | 30 Mar | [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | 25m | ☐ |
|  |  | [648. Replace Words](https://leetcode.com/problems/replace-words/) | Medium | 25m | ☐ |
| Wed | 31 Mar | [212. Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | 40m | ☐ |
|  |  | [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | 25m | ☐ |
| Thu | 01 Apr | [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | Easy | 15m | ☐ |
|  |  | [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | Hard | 40m | ☐ |
| Fri | 02 Apr | [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | 25m | ☐ |
|  |  | [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | 40m | ☐ |
| Sat | 03 Apr | [729. My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | 25m | ☐ |
|  |  | [731. My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | Medium | 25m | ☐ |
|  |  | [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) (H)
- [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) (M)
- [686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/) (M)
- [218. The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) (H)
- [732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (H)
- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) (H)
- [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Trie vs HashSet for prefix queries - trade-offs?
- What does the KMP LPS array store?
- Fenwick tree: complexity of update and prefix query?
- Reverse Pairs: why does merge sort help?
- My Calendar I with TreeMap: which methods do you use?

## 💡 Tip
BOSS: implement Trie and Fenwick tree from memory in under 15 minutes each.
