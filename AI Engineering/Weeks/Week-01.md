# 🤖 AI Engineering · Week 01 — Python for Java Developers I

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Python is the working language of AI tooling (SDKs, evals, agents, notebooks); fluency removes friction from every later week. You already know programming from Java, so focus on the differences and Pythonic idioms.

## 🗓️ Sessions

### Monday 26 Oct · 45 min — Setup: Python 3.12, uv projects, VS Code and Jupyter
- 📚 **Learn:** Toolchain on your company laptop: Python 3.12 from the Company Portal (start it with `py`), uv (already installed and pointed at the company JFrog) for projects: `uv init` creates `pyproject.toml`, `uv add` installs into the project's own `.venv` (like a project-local classpath), `uv run` runs code inside it. VS Code Python + Jupyter extensions, the REPL. Read: [uv: working on projects](https://docs.astral.sh/uv/guides/projects/) (about 10 min). Optional: [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial).
- 🛠️ **Do:** Clone repo `ai-engineering-lab` into `C:\dev\personal`, run `uv init 00-python-katas` and `cd` into it, then `uv add --dev ipykernel` and select `.venv` as the notebook kernel in VS Code. Print `sys.version` in a notebook. Add `.gitignore` (.venv, .env) and a README, then commit. uv not working today? Use `py -3.12 -m venv .venv` + pip (Section 4 of `03_SETUP_YOUR_LAPTOP.md`). Done when: `uv run python -V` prints 3.12 and the notebook runs in VS Code.

### Tuesday 27 Oct · 45 min — Syntax, types, strings: Java vs Python side by side
- 📚 **Learn:** Dynamic typing vs Java static types, indentation blocks, `None` and truthiness, int/float/str/bool, f-strings, slicing, `for` with `range`/`enumerate`/`zip`, `==` vs `is`. Read: [Learn X in Y minutes: Python](https://learnxinyminutes.com/python/) (first half, about 15 min). Optional: [Python vs Java (Real Python)](https://realpython.com/java-vs-python/).
- 🛠️ **Do:** Create `java_vs_python.md` with 10 Java snippets you know and their Python equivalents (loops, StringBuilder, ternary, null checks, if/else chains). Then solve 5 [CodingBat Python](https://codingbat.com/python) Warmup-1/String-1 problems without AI help, predicting each output before running. Done when: the 10-pair cheat sheet is committed and 5 katas pass.

### Thursday 29 Oct · 45 min — Collections and comprehensions
- 📚 **Learn:** list/dict/set/tuple compared with the ArrayList/HashMap/HashSet toolkit from your DSA W1 concepts: mutability, unpacking, `sorted(key=...)`, `collections.Counter` and `defaultdict`, and list/dict/set comprehensions as the compact replacement for build-a-new-list loops. Read: [Data Structures (official tutorial)](https://docs.python.org/3/tutorial/datastructures.html) sections 5.1-5.6. Optional: [List comprehensions (Real Python)](https://realpython.com/list-comprehension-python/).
- 🛠️ **Do:** Solve 5 CodingBat List-1/List-2/Logic-1 katas, then rewrite 3 Java for-loops you know in Python: filtering into a new ArrayList (a comprehension), a HashMap word count (`Counter`) and a sum-by-key map (`defaultdict`). Put one `assert` per kata in `katas.py`. Done when: 8 katas are done and `uv run python katas.py` runs all asserts silently.

### Friday 30 Oct · 45 min — Functions, modules, exceptions, context managers
- 📚 **Learn:** `def`, default and keyword args, `*args/**kwargs` (compare with the Java varargs you met in Java W1 Thu), functions as values and lambdas, modules and packages, `if __name__ == '__main__'`, try/except/else/finally, custom exceptions, `with`. Read: [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html) (8.1-8.6). Optional: [Modules](https://docs.python.org/3/tutorial/modules.html).
- 🛠️ **Do:** Create package `katas/` with `strings.py`, `lists.py` and `utils.py` (a `retry(fn, times, *args, **kwargs)` helper). Add `InvalidInputError` and handle it in `main.py`. Move your katas into the modules and add 2 more. Done when: all katas pass via `uv run python -m katas.main` and a deliberate bad input prints a friendly message instead of a traceback.

### Saturday 31 Oct · 45 min — BUILD: katas + port 3 small Java programs
- 📚 **Learn:** Porting mindset: translate intent, not syntax; prefer Pythonic idioms (comprehensions, unpacking, `with open`, `pathlib`). More reps: [Exercism Python track](https://exercism.org/tracks/python). Optional (Hindi): [CodeWithHarry Python course](https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg).
- 🛠️ **Do:** Port 3 small Java programs into `00-python-katas/ports/`: today's Java W1 Sat Expense Tracker (or a word-frequency counter), a student grade report and a temperature converter with input validation. For each, write a 5-line note: what got shorter and why. Done when: 15 katas + 3 ports run with `uv run`, are pushed to GitHub, and the notes are in the README.

## 📦 Deliverable (by Saturday night)
`ai-engineering-lab/00-python-katas/` on GitHub: 15 passing katas, `katas/` package with custom exception + retry helper, 3 Java-to-Python ports with notes, `java_vs_python.md` cheat sheet.

## ✅ Self-check (Sunday test preview)
- How is a Python list different from a Java ArrayList, and a tuple from a list?
- What do `*args` and `**kwargs` do? Give a use case.
- Which values are falsy in Python, and why does that matter in `if` checks?
- What is the difference between `==` and `is`?
- Why is `def f(items=[])` a bug, and how do you fix it?
- Rewrite a for-loop that keeps numbers greater than 2 and squares them as a list comprehension.

## 🚀 Stretch (optional)
Do 10 more Exercism Python exercises and request mentor feedback on one; or watch [CS50P](https://cs50.harvard.edu/python/) lectures 0-1 at 1.5x.
