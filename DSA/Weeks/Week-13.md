# 🧩 DSA · Week 13 — Binary Trees II + Binary Search Trees

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** LCA, construction, serialization and BST operations are classic follow-ups in tree rounds.

## 🧠 Concepts to master
- Lowest common ancestor (binary tree and BST)
- Build a tree from preorder + inorder (index map)
- Distance K: convert to a graph with parent pointers
- BST: inorder is sorted; validate with (min, max) bounds held in long or Integer null; delete with the inorder successor
- BST iterator with a controlled stack; serialize/deserialize with preorder + null markers

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Tree series](https://www.youtube.com/playlist?list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu)
- [NeetCode - Trees](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 18 Jan | [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | 25m | ☐ |
|  |  | [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | 25m | ☐ |
| Tue | 19 Jan | [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | 25m | ☐ |
|  |  | [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Medium | 25m | ☐ |
| Wed | 20 Jan | [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy | 15m | ☐ |
|  |  | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | 25m | ☐ |
| Thu | 21 Jan | [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | 25m | ☐ |
|  |  | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | 25m | ☐ |
| Fri | 22 Jan | [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | 25m | ☐ |
|  |  | [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | Medium | 25m | ☐ |
| Sat | 23 Jan | [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (E) | 10m |
| Tue | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (M) | 20m |
| Wed | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (E) | 10m |
| Thu | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) (E) | 10m |
| Fri | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) (E) | 10m |
| Sat | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (M) · [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) (M)
- [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) (M)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) (M)
- [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) (E)
- [653. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) (E)
- [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/) (M)
- [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) (E)
- [427. Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/) (M)
- [1008. Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Why does validating a BST by comparing only parent and child fail?
- Delete a node with two children in a BST - steps?
- LCA in a BST in O(h) - how?
- All Nodes Distance K: why add parent pointers?
- How do you serialize a tree so it can be rebuilt uniquely?
- BST Iterator: why is next() O(1) amortized?

## 💡 Tip
For BST problems, think 'inorder = sorted order' first. Serialize/Deserialize is Saturday's weekend challenge.
