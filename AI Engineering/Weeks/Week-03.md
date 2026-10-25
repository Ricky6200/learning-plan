# 🤖 AI Engineering · Week 03 — Python III: Generators, Decorators, Typing and Data

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** LLM SDKs stream with generators, frameworks configure you through decorators, agent state is typed with TypedDict, and every evaluation ends in a NumPy array or a pandas table. Learning these idioms now means the AI code of later weeks reads like familiar code.

## 🗓️ Sessions

### Monday 09 Nov · 45 min — Iterators and generators, sync and async
- 📚 **Learn:** The iteration protocol (`__iter__`/`__next__`), generator functions with `yield`, generator expressions, lazy pipelines (nothing runs until you iterate), `yield from`, `itertools.islice` and `itertools.batched`; async generators (`async def` + `yield`, consumed with `async for`) are how streamed LLM tokens arrive. Read: [How to use generators and yield (Real Python)](https://realpython.com/introduction-to-python-generators/) (first four sections). Optional: [itertools](https://docs.python.org/3/library/itertools.html).
- 🛠️ **Do:** In `02-python-data/gen.py` write `read_lines(path)` (yields stripped lines), `batched_words(lines, n)` and an async generator `fake_tokens(text, delay=0.05)` that yields one word at a time. Stream a sentence to the terminal with `async for` and `print(tok, end=' ', flush=True)`. Add 3 pytest tests (laziness, batch sizes, token order). Done when: tests pass and you can explain in one line why `read_lines` needs almost no memory for a huge file.

### Tuesday 10 Nov · 45 min — Decorators and context managers
- 📚 **Learn:** Functions are objects, closures capture variables, and a decorator is a function that wraps another (`functools.wraps` keeps its name); `@retry`, `@app.get` and `@mcp.tool` all follow this pattern. `contextlib.contextmanager` turns a generator into a `with` block (setup, `yield`, cleanup). `logging.basicConfig(level=logging.INFO)` gives timestamped logs instead of prints. Read: [Primer on Python decorators (Real Python)](https://realpython.com/primer-on-python-decorators/) (simple decorators and decorators with arguments). Optional: [contextlib](https://docs.python.org/3/library/contextlib.html).
- 🛠️ **Do:** In `02-python-data/wrappers.py` write `@timed` (logs the duration with `logging`), a parameterised `@retry(times=3, on=(TimeoutError,))` and a `timer(label)` context manager via `@contextmanager`. Apply them to a function that fails twice, then succeeds. Add 3 tests using pytest's `caplog`. Done when: tests pass and the log shows 2 retries, the success and the measured time.

### Thursday 12 Nov · 45 min — Typing for real code: Literal, Enum, TypedDict, Annotated
- 📚 **Learn:** `Literal['onsite', 'remote']` restricts values, `Enum` names a closed set (like the Java enums of Java W3 Wed), `TypedDict` types plain dicts (LangGraph state uses it), `Annotated[T, meta]` attaches metadata that frameworks read (pydantic `Field`, LangGraph reducers), plus `Callable`; a checker such as mypy finds bugs without running code. Read: [typing module](https://docs.python.org/3/library/typing.html) (the TypedDict, Literal and Annotated entries). Optional: [Enum HOWTO](https://docs.python.org/3/howto/enum.html).
- 🛠️ **Do:** In `02-python-data/typing_lab.py` model a job-search state: `Seniority(Enum)`, `Remote = Literal['onsite', 'hybrid', 'remote']` and `class SearchState(TypedDict)` with `query: str` and `results: Annotated[list[str], 'append-only']`. Write `merge(state, update)` that appends results, then add 3 deliberate type errors and run `uvx mypy typing_lab.py`. Done when: mypy reports your 3 errors, you fix them, and it then reports no issues.

### Friday 13 Nov · 45 min — NumPy arrays and matplotlib plots
- 📚 **Learn:** ndarrays (shape, dtype), vectorised maths instead of loops, broadcasting, `@` for dot products, `np.linalg.norm`, seeded random arrays; matplotlib `plt.plot`/`plt.imshow`, labels and saving a figure. You will compute cosine similarity, attention weights and loss curves with exactly these tools. Read: [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) (array creation, basic operations, broadcasting). Optional: [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html).
- 🛠️ **Do:** In `02-python-data/numpy_lab.ipynb` (`uv add numpy matplotlib`) build 5 random 8-dimensional vectors and compute pairwise cosine similarity with one vectorised expression; then time a pure-Python loop vs NumPy on 1,000 x 384 vectors. Plot the similarity matrix with `plt.imshow` and save it as PNG. Done when: both methods agree to 6 decimals, NumPy is at least 10x faster and the PNG is committed.

### Saturday 14 Nov · 45 min — BUILD: weather data analysis with pandas and pytest
- 📚 **Learn:** pandas DataFrame basics: reading CSV/JSON, selecting and filtering, `groupby` + `agg`, dates with `pd.to_datetime`, monthly resampling and plotting from a DataFrame; keep transformations as pure functions you can unit-test. Read: [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) (selection, grouping, time series). Optional: [Open-Meteo historical weather API](https://open-meteo.com/en/docs/historical-weather-api).
- 🛠️ **Do:** Extend your W2 client to download one year of daily maximum temperature and rainfall for 5 cities from the historical API into `weather.csv`. In `02-python-data/analysis.py` write pure functions `monthly_means(df)`, `hottest_days(df, n)` and `rainy_days_per_city(df)`, with 4 pytest tests on a tiny hand-made DataFrame, then plot the monthly means. Done when: `uv run pytest` is green and the chart plus a 5-line findings note are in the README.

## 📦 Deliverable (by Saturday night)
`02-python-data/`: generator, decorator/context-manager and typing labs with tests, a NumPy similarity notebook and a tested pandas weather analysis with a chart and findings.

## ✅ Self-check (Sunday test preview)
- What is the difference between a list comprehension and a generator expression, and when does it matter?
- How does an async generator differ from a normal generator? Where will you meet one in LLM code?
- Write a decorator that logs how long a function takes. Why use `functools.wraps`?
- What do `TypedDict`, `Literal` and `Annotated` add over a plain `dict` and `str`?
- What is broadcasting in NumPy? Give an example with a (5, 384) and a (384,) array.
- How do `groupby` and `agg` work in pandas?

## 🚀 Stretch (optional)
Finish the remaining sections of 10 minutes to pandas, or cache the downloader with `functools.lru_cache` plus an on-disk JSON cache and measure the speed-up.
