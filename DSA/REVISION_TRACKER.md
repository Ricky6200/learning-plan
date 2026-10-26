# 🔁 DSA Revision Tracker (spaced repetition)

> Log every problem right after solving. Your AI mentor reads this file to pick Sunday test problems, remediation work and fix-it items.
> LeetCode profile: [Ricky_0618](https://leetcode.com/u/Ricky_0618/)

**Legend:** 🟢 solved alone within time · 🟡 needed a hint or over time · 🔴 needed the full solution

## 🔄 How re-solving works (30-week plan)
- **Scheduled re-solves are already in every week file** (the "Daily re-solve" table) — you don't plan them yourself:
  - **Mon–Fri:** 1 problem from the same weekday of the previous problem week (D+7; in Week 1 it is yesterday's problem).
  - **Saturday:** 1–2 quick Easy/Medium problems from 3 weeks earlier (D+21) — only 1 when Saturday's new problems need more than 50 min.
  - **Least-re-solved first:** no problem comes back more than twice while others wait (176 different problems over the plan).
- **Targets:** Easy 10 · Medium 20 · Hard 35 min, from memory, no notes. Missed the target → mark that re-solve 🔴.
- **Your own 🔴 rule:** re-solve every 🔴 of the week in the Sunday preview slot; if it is still 🔴, the mentor puts it on next week's fix-it list.
- **Re-solve weeks (no new problems):** W26 — light, 2 a day (AI-200 exam week) · W30 — final speed-run, 4 a day.
- **Contests:** on contest Sundays (W10, W12, W14, W16, W18, W22, W24, W26, W28 — never in boss weeks) log the result below and the one problem you up-solved during the week; from W20 explain that up-solve aloud.
- **Mocks:** from W15, every non-contest Sunday test opens with a talk-aloud mock — log it in the table below too.

## 📊 Running totals (update every Sunday)
| Week | Core done | Re-solves done | Bonus done | 🟢 | 🟡 | 🔴 | Contest / mock |
|---|---|---|---|---|---|---|---|
| W01 | /12 | /6 | | | | | — |
| W02 | /12 | /7 | | | | | — |
| W03 | /11 | /6 | | | | | — |
| W04 ⚔️ | /11 | /6 | | | | | — |
| W05 | /11 | /7 | | | | | — |
| W06 | /11 | /6 | | | | | — |
| W07 | /12 | /7 | | | | | — |
| W08 | /11 | /6 | | | | | — |
| W09 ⚔️ | /10 | /6 | | | | | — |
| W10 | /11 | /7 | | | | | 🏆 |
| W11 | /11 | /6 | | | | | |
| W12 | /12 | /6 | | | | | 🏆 |
| W13 | /11 | /7 | | | | | |
| W14 | /11 | /6 | | | | | 🏆 |
| W15 ⚔️ | /11 | /6 | | | | | mock |
| W16 | /10 | /7 | | | | | 🏆 |
| W17 | /10 | /6 | | | | | mock |
| W18 | /10 | /6 | | | | | 🏆 |
| W19 | /11 | /6 | | | | | mock · OA sim |
| W20 ⚔️ | /11 | /6 | | | | | mock · OA sim |
| W21 | /10 | /7 | | | | | mock |
| W22 | /9 | /6 | | | | | 🏆 · up-solve aloud |
| W23 | /10 | /7 | | | | | mock |
| W24 | /10 | /7 | | | | | 🏆 · up-solve aloud |
| W25 ⚔️ | /9 | /6 | | | | | virtual contest · mock |
| W26 | — | /12 | | | | | 🏆 · up-solve aloud |
| W27 | /7 | /6 | | | | | mock · optional virtual contests |
| W28 | /11 | /6 | | | | | 🏆 · up-solve aloud |
| W29 | /8 | /7 | | | | | 2 OA sims · mock |
| W30 👑 | — | /24 | | | | | final mock loop |
| **Total** | **/294** | **/214** | **/202** | | | | |

## 🏆 Contests, OA simulations & mocks
| Date | Type (contest / virtual / OA sim / mock) | Solved | Score or rank | Up-solved (LC #) | What to fix |
|---|---|---|---|---|---|
| | | | | | |

## 📝 Log
| Date | LC # | Problem | Pattern | Key insight (1 line) | Time | Result | Re-solves (date · time · 🟢/🟡/🔴) |
|---|---|---|---|---|---|---|---|
| 26 Oct | 1480 | Running Sum of 1d Array | Prefix sum | `out[i] = out[i-1] + nums[i]` — works in place: `nums[i] += nums[i-1]` from i = 1 | 8m | 🟢 | |
| 26 Oct | 485 | Max Consecutive Ones | Array scan (running count + max) | update `max` on every 1, not only at a 0 — a run that ends at the last index never meets a 0 | 15m | 🟡 hint | |
