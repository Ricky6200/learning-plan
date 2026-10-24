# 🧩 DSA · Week 13 — Binary Trees II + Binary Search Trees

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** LCA, construction, serialization and BST operations are classic follow-ups in tree rounds.

## 🧠 Concepts to master
- Lowest common ancestor (binary tree and BST)
- Build tree from preorder + inorder (index map)
- Distance K: convert to graph with parent pointers
- BST: inorder is sorted; validate with (min, max) bounds; insert/delete
- Serialize/deserialize; BST iterator with controlled stack

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Tree series](https://www.youtube.com/playlist?list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu)
- [NeetCode - Trees](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 18 Jan | [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | 25m | ☐ |
|  |  | [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | 25m | ☐ |
| Tue | 19 Jan | [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | 25m | ☐ |
|  |  | [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Medium | 25m | ☐ |
| Wed | 20 Jan | [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy | 15m | ☐ |
|  |  | [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Medium | 25m | ☐ |
| Thu | 21 Jan | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | 25m | ☐ |
|  |  | [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | 25m | ☐ |
| Fri | 22 Jan | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | 25m | ☐ |
|  |  | [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | 25m | ☐ |
| Sat | 23 Jan | [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | Medium | 25m | ☐ |
|  |  | [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Medium | 25m | ☐ |
|  |  | [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) (M)
- [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) (E)
- [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (E)
- [99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) (M)
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) (M)
- [2385. Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (H)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (M)
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Why does validating a BST by comparing only parent and child fail?
- Delete a node with two children in a BST - steps?
- LCA in a BST in O(h) - how?
- How do you serialize a tree so it can be rebuilt uniquely?
- Kth smallest in a BST - approach and complexity?

## 💡 Tip
For BST problems, think 'inorder = sorted order' first.
