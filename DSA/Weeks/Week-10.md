# 🧩 DSA · Week 10 — Linked List

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Pointer manipulation tests careful coding - a favourite at service and product companies alike.

## 🧠 Concepts to master
- Dummy head node to simplify edge cases
- Fast/slow pointers: middle, cycle detection, Floyd's cycle start
- Reverse iteratively and recursively; reverse a sub-list
- Merge two lists; merge sort on a linked list
- Deep copy with random pointers (map or interleaving)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Linked List playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0rAuz8tVcM0AymmhTRsfaLU)
- [NeetCode - Linked List](https://www.youtube.com/playlist?list=PLot-Xpze53leU0Ec0VkBhnf4npMRFiNcB)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 28 Dec | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | 15m | ☐ |
|  |  | [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | 15m | ☐ |
| Tue | 29 Dec | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | 15m | ☐ |
|  |  | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | 15m | ☐ |
| Wed | 30 Dec | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | 25m | ☐ |
|  |  | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | 25m | ☐ |
| Thu | 31 Dec | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | 15m | ☐ |
|  |  | [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Easy | 15m | ☐ |
| Fri | 01 Jan | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | 25m | ☐ |
|  |  | [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) | Medium | 25m | ☐ |
| Sat | 02 Jan | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | 25m | ☐ |
|  |  | [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | 25m | ☐ |
|  |  | [148. Sort List](https://leetcode.com/problems/sort-list/) 🔥 *weekend challenge — finish Sunday if needed* | Medium | 25m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [61. Rotate List](https://leetcode.com/problems/rotate-list/) (M)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) (M)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) (M)
- [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) (M)
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [51. N-Queens](https://leetcode.com/problems/n-queens/) (H)
- [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) (H)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Prove why Floyd's algorithm finds the cycle start.
- Remove the Nth node from end in one pass - how?
- How do you check a palindrome linked list in O(1) extra space?
- Why is merge sort preferred over quick sort for linked lists?
- What does a dummy node save you from?

## 💡 Tip
Draw boxes and arrows for every pointer change. Most bugs are lost references.
