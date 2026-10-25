# 🧩 DSA · Week 10 — Linked List

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Pointer manipulation tests careful coding - a favourite at service and product companies alike. New Year's Day (Friday) has one problem; Saturday hand-rolls an LRU cache.

## 🧠 Concepts to master
- Dummy head node to simplify edge cases
- Fast/slow pointers: middle, cycle detection, Floyd's cycle start (142) - the same idea finds the duplicate in an array (287)
- Reverse iteratively and recursively; reverse the second half (234, 143)
- Merge two lists; gap pointers for 'Nth from end' (19); digit addition with a carry (2)
- Deep copy with random pointers (HashMap or interleaving)
- LRU = HashMap<key, node> + doubly linked list with dummy head/tail (146); the Java track used LinkedHashMap's access order - now build it by hand

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Linked List playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rAuz8tVcM0AymmhTRsfaLU)
- [NeetCode - Linked List](https://www.youtube.com/playlist?list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 28 Dec | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | 15m | ☐ |
|  |  | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | 15m | ☐ |
| Tue | 29 Dec | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | 25m | ☐ |
|  |  | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | 25m | ☐ |
| Wed | 30 Dec | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | 15m | ☐ |
|  |  | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | 25m | ☐ |
| Thu | 31 Dec | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | 15m | ☐ |
|  |  | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | 25m | ☐ |
| Fri | 01 Jan | [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | 25m | ☐ |
| Sat | 02 Jan | [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | 25m | ☐ |
|  |  | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | 25m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [79. Word Search](https://leetcode.com/problems/word-search/) (M) | 20m |
| Tue | [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) (M) | 20m |
| Wed | [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) (M) | 20m |
| Thu | [473. Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) (M) | 20m |
| Fri | [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) (M) | 20m |
| Sat | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (M) · [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) (E)
- [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (E)
- [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) (M)
- [148. Sort List](https://leetcode.com/problems/sort-list/) (M)
- [61. Rotate List](https://leetcode.com/problems/rotate-list/) (M)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (M)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (M)
- [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) (M)
- [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Prove why Floyd's algorithm finds the cycle start.
- Find the Duplicate Number: why can the array be treated as a linked list with a cycle?
- Remove the Nth node from the end in one pass - how?
- How do you check a palindrome linked list in O(1) extra space?
- LRU Cache: why a doubly linked list, and what does each operation touch?
- What does a dummy node save you from?

## 💡 Tip
Draw boxes and arrows for every pointer change - most bugs are lost references. Sort List (148) is in bonus: merge sort on a list.
