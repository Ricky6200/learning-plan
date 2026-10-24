# 🧩 DSA · Week 11 — Stack, Queue, Monotonic Stack & Deque

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** Monotonic stacks solve 'next greater/smaller' and histogram problems that look impossible at first.

## 🧠 Concepts to master
- Stack for matching/undo; use ArrayDeque, not Stack
- Min stack (pair or two stacks); queue via two stacks (amortized O(1))
- Monotonic stack: next greater/smaller, previous smaller, histogram
- Monotonic deque: sliding window maximum
- Expression evaluation (RPN)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Stack & Queue playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0pOd5zvVVSzgpo6BaCpHT9c)
- [Aditya Verma - Stack (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd)
- [NeetCode - Stack problems](https://www.youtube.com/playlist?list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 04 Jan | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | 15m | ☐ |
|  |  | [155. Min Stack](https://leetcode.com/problems/min-stack/) | Medium | 25m | ☐ |
| Tue | 05 Jan | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | 15m | ☐ |
|  |  | [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | 15m | ☐ |
| Wed | 06 Jan | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | 25m | ☐ |
|  |  | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | 25m | ☐ |
| Thu | 07 Jan | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | 15m | ☐ |
|  |  | [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium | 25m | ☐ |
| Fri | 08 Jan | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | 40m | ☐ |
|  |  | [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | 25m | ☐ |
| Sat | 09 Jan | [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Medium | 25m | ☐ |
|  |  | [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | 25m | ☐ |
|  |  | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) (M)
- [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/) (M)
- [394. Decode String](https://leetcode.com/problems/decode-string/) (M)
- [71. Simplify Path](https://leetcode.com/problems/simplify-path/) (M)
- [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (M)
- [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (M)
- [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- When do you use an increasing vs a decreasing monotonic stack?
- Largest rectangle in histogram: what do you compute for each bar?
- Why is the queue-with-two-stacks O(1) amortized?
- Sliding window maximum in O(n): what does the deque store?
- Why prefer ArrayDeque over java.util.Stack?

## 💡 Tip
For 'next greater' problems, iterate and pop while the current element beats the stack top.
