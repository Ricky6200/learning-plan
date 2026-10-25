# 🧩 DSA · Week 11 — Stack, Queue, Monotonic Stack & Deque

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** Monotonic stacks and deques solve 'next greater/smaller' and window-max problems that look impossible at first.

## 🧠 Concepts to master
- Stack for matching/undo; use ArrayDeque (push/pop/peek), not java.util.Stack
- Min stack (pair or two stacks); queue via two stacks (amortized O(1))
- Nested decoding with two stacks: counts and partial strings (394)
- Monotonic stack: next greater/smaller (circular with 2n indices), collisions, car fleet
- Monotonic deque: sliding window maximum (239) - store indices, drop out-of-window and smaller values
- Expression evaluation (RPN)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Stack & Queue playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0pOd5zvVVSzgpo6BaCpHT9c)
- [Aditya Verma - Stack (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd)
- [NeetCode - Stack problems](https://www.youtube.com/playlist?list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 04 Jan | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | 15m | ☐ |
|  |  | [155. Min Stack](https://leetcode.com/problems/min-stack/) | Medium | 25m | ☐ |
| Tue | 05 Jan | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | 15m | ☐ |
|  |  | [394. Decode String](https://leetcode.com/problems/decode-string/) | Medium | 25m | ☐ |
| Wed | 06 Jan | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | 25m | ☐ |
|  |  | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | 25m | ☐ |
| Thu | 07 Jan | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | 15m | ☐ |
|  |  | [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium | 25m | ☐ |
| Fri | 08 Jan | [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | 25m | ☐ |
| Sat | 09 Jan | [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | 25m | ☐ |
|  |  | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (E) | 10m |
| Tue | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (M) | 20m |
| Wed | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (M) | 20m |
| Thu | [143. Reorder List](https://leetcode.com/problems/reorder-list/) (M) | 20m |
| Fri | [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (M) | 20m |
| Sat | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) (E)
- [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/) (M)
- [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) (M)
- [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/) (M)
- [71. Simplify Path](https://leetcode.com/problems/simplify-path/) (M)
- [456. 132 Pattern](https://leetcode.com/problems/132-pattern/) (M)
- [2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- When do you use an increasing vs a decreasing monotonic stack?
- Why is the queue-with-two-stacks O(1) amortized?
- Decode String: what do the two stacks hold?
- Next Greater Element II: how do you handle the circular array?
- Sliding Window Maximum in O(n): what does the deque store, and why indices?
- Why prefer ArrayDeque over java.util.Stack?

## 💡 Tip
For 'next greater' problems, iterate and pop while the current element beats the stack top. Largest Rectangle in Histogram (84) comes back in the Week 27 Hard bank.
