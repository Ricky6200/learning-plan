# 🤖 AI Engineering · Week 01 — Python for Java Developers I

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Python is the working language of AI tooling (SDKs, evals, agents, notebooks); fluency removes friction from every later week. You already know programming from Java, so focus on the differences and Pythonic idioms.

## 🗓️ Sessions

### Monday 26 Oct · 45 min — Setup: Python 3.12+, venv + pip via Artifactory, VS Code, Jupyter
- 📚 **Learn:** Toolchain on your company laptop: Python 3.12 from the Company Portal (start it with `py`; plain `python` is the old 3.9), one virtual environment per project (`py -3.12 -m venv .venv`, like a project-local classpath), pip installing through JFrog Artifactory (public PyPI is blocked), VS Code Python + Jupyter extensions, the REPL. Read: [venv tutorial](https://docs.python.org/3/tutorial/venv.html), [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial), [uv projects guide](https://docs.astral.sh/uv/guides/projects/) (if uv is approved).
- 🛠️ **Do:** Follow Section 4 of `03_SETUP_YOUR_LAPTOP.md` to connect pip to JFrog. Clone repo `ai-engineering-lab` under `C:\dev\personal`, add folder `00-python-katas`, run `py -3.12 -m venv .venv`, select it in VS Code, `pip install ipykernel`, then open a notebook and print `sys.version`. Add `.gitignore` (.venv, .env) and a README. Pip not working yet? Use the REPL today (Week 1 needs no packages); add the notebook later. Done when: Python 3.12 runs in your venv inside VS Code.

### Tuesday 27 Oct · 45 min — Syntax, types, strings: Java vs Python side by side
- 📚 **Learn:** Dynamic typing vs Java static types, indentation blocks, `None` and truthiness, int/float/str/bool, f-strings, slicing, `for` with `range`/`enumerate`/`zip`, `==` vs `is`. Skim: [Learn X in Y minutes: Python](https://learnxinyminutes.com/python/) (first half) and [Python vs Java (Real Python)](https://realpython.com/java-vs-python/).
- 🛠️ **Do:** Create `java_vs_python.md` with 10 Java snippets you know and their Python equivalents (loops, StringBuilder, ternary, null checks, switch). Then solve 5 [CodingBat Python](https://codingbat.com/python) Warmup-1/String-1 problems without AI help, predicting each output before running. Done when: the 10-pair cheat sheet is committed and 5 katas pass.

### Thursday 29 Oct · 45 min — Collections and comprehensions vs Java Streams
- 📚 **Learn:** list/dict/set/tuple vs ArrayList/HashMap/HashSet/records, mutability, unpacking, `sorted(key=...)`, `collections.Counter` and `defaultdict`, list/dict/set comprehensions vs Stream pipelines. Read: [Data Structures (official tutorial)](https://docs.python.org/3/tutorial/datastructures.html) and [List comprehensions (Real Python)](https://realpython.com/list-comprehension-python/).
- 🛠️ **Do:** Solve 5 CodingBat List-1/List-2/Logic-1 katas, then rewrite 3 Java Stream pipelines you know as comprehensions (filter-map-collect, groupingBy as `defaultdict`/`Counter`, sum by key). Put one `assert` per kata in `katas.py`. Done when: 10 katas are done and `python katas.py` (venv selected) runs all asserts silently.

### Friday 30 Oct · 45 min — Functions, modules, exceptions, context managers
- 📚 **Learn:** `def`, default and keyword args, `*args/**kwargs` (vs varargs), functions as values and lambdas, modules and packages, `if __name__ == '__main__'`, try/except/else/finally, custom exceptions, `with`. Read: [Defining functions](https://docs.python.org/3/tutorial/controlflow.html), [Modules](https://docs.python.org/3/tutorial/modules.html), [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html).
- 🛠️ **Do:** Create package `katas/` with `strings.py`, `lists.py` and `utils.py` (a `retry(fn, times, *args, **kwargs)` helper). Add `InvalidInputError` and handle it in `main.py`. Move your katas into the modules and add 5 more. Done when: 15 katas pass via `python -m katas.main` and a deliberate bad input prints a friendly message instead of a traceback.

### Saturday 31 Oct · 45 min — BUILD: 15 katas + port 3 Java programs
- 📚 **Learn:** Porting mindset: translate intent, not syntax; prefer Pythonic idioms (comprehensions, unpacking, `with open`, `pathlib`). More reps: [Exercism Python track](https://exercism.org/tracks/python). Hindi option: [CodeWithHarry Python course](https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg); English: [Telusko Python](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3).
- 🛠️ **Do:** Port 3 small Java programs (from `java-mastery`, or: word-frequency counter for a text file, student grade report, bank account with an insufficient-funds exception) into `00-python-katas/ports/`. For each, write a 5-line note: what got shorter and why. Done when: 15 katas + 3 ports run from your venv, are pushed to GitHub, and the notes are in the README.

## 📦 Deliverable (by Saturday night)
`ai-engineering-lab/00-python-katas/` on GitHub: 15 passing katas, `katas/` package with custom exception + retry helper, 3 Java-to-Python ports with notes, `java_vs_python.md` cheat sheet.

## ✅ Self-check (Sunday test preview)
- How is a Python list different from a Java ArrayList, and a tuple from a record?
- What do `*args` and `**kwargs` do? Give a use case.
- Which values are falsy in Python, and why does that matter in `if` checks?
- What is the difference between `==` and `is`?
- Why is `def f(items=[])` a bug, and how do you fix it?
- Rewrite `list.stream().filter(x -> x > 2).map(x -> x * x).collect(toList())` in Python.

## 🚀 Stretch (optional)
Do 10 more Exercism Python exercises and request mentor feedback on one; or watch [CS50P](https://cs50.harvard.edu/python/) lectures 0-1 at 1.5x.
