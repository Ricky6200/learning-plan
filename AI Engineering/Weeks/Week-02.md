# 🤖 AI Engineering · Week 02 — Python II: OOP, Pydantic, Async, Tests

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** Every AI SDK you will use is built on typed classes, pydantic models, async I/O and pytest. Mastering them now makes LLM code readable, testable and fast.

## 🗓️ Sessions

### Monday 02 Nov · 45 min — Classes, dataclasses and type hints
- 📚 **Learn:** Classes, `__init__`, `self`, `@property`, `__repr__`, inheritance vs composition, `@dataclass` (like Java records/Lombok), type hints (`list[str]`, `X | None`, `Protocol`). Read: [Classes tutorial](https://docs.python.org/3/tutorial/classes.html) 9.3-9.5, [dataclasses](https://docs.python.org/3/library/dataclasses.html), [type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
- 🛠️ **Do:** In `01-python-async-cli/models.py` create `@dataclass Job(title, company, location, salary: int | None)` and a `JobBoard` class with `add`, `search(keyword)` and `top_paying(n)`. Type-hint everything and run `uvx ruff check .`. Done when: a script creates 5 jobs, prints the 2 top-paying ones, and ruff reports no errors.

### Tuesday 03 Nov · 45 min — Pydantic v2 validation, files and JSON
- 📚 **Learn:** Validate at boundaries: `BaseModel`, `Field` constraints, `model_validate`, `model_dump_json`, `field_validator`, `ValidationError`; plus `json`, `pathlib`, `with open`. Read: [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/), [Validators](https://docs.pydantic.dev/latest/concepts/validators/), [pathlib](https://docs.python.org/3/library/pathlib.html).
- 🛠️ **Do:** Convert `Job` into a pydantic model (non-empty title, salary >= 0). Create `jobs.json` with 8 entries, 2 of them invalid. Load with `pathlib`, validate each item, print a clean error report with field names, and save valid ones to `valid_jobs.json`. Done when: invalid rows are reported clearly and the valid file round-trips through `model_validate_json`.

### Thursday 05 Nov · 45 min — HTTP with httpx and asyncio basics
- 📚 **Learn:** Blocking vs non-blocking I/O, the event loop, `async def`/`await`, `asyncio.gather`, timeouts; `httpx.AsyncClient` (like Java's async HttpClient). Read: [Coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html) (gather, timeouts), [httpx async](https://www.python-httpx.org/async/); optional [Async IO in Python (Real Python)](https://realpython.com/async-io-python/).
- 🛠️ **Do:** Call the free [Open-Meteo forecast API](https://open-meteo.com/en/docs) for 5 Indian cities: first sequentially with `httpx.get`, then concurrently with `AsyncClient` + `asyncio.gather`. Time both with `time.perf_counter()`, add a 5 s timeout and handle `httpx.HTTPError`. Done when: the concurrent version is clearly faster and you explain why in 2 lines in your notes.

### Friday 06 Nov · 45 min — uv projects and pytest basics
- 📚 **Learn:** `pyproject.toml`, `uv add`, `uv add --dev pytest`, `uv run pytest`, lockfile; pytest asserts, fixtures, parametrize, `tmp_path`, faking HTTP responses with saved JSON. Read: [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html), [fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html).
- 🛠️ **Do:** Write 6 tests: pydantic validation (valid and invalid cases via parametrize), a JSON round-trip using `tmp_path`, and `parse_weather()` against a saved sample response (no network). Done when: `uv run pytest -q` shows 6 passed with Wi-Fi off.

### Saturday 07 Nov · 45 min — BUILD: async weather CLI with pydantic and pytest
- 📚 **Learn:** CLI ergonomics with [Typer](https://typer.tiangolo.com/) commands/options and [Rich](https://rich.readthedocs.io/en/latest/) tables; keep I/O at the edges and pure functions in the middle so they are easy to test. City lookup: [Open-Meteo geocoding API](https://open-meteo.com/en/docs/geocoding-api) (no key).
- 🛠️ **Do:** Build `weather-cli`: `uv run weather compare Delhi Mumbai Bengaluru` geocodes and fetches concurrently, validates responses with pydantic, prints a Rich table (temp, wind, daily max) and handles timeouts and unknown cities. Add 4 more tests (10+ total). Done when: the CLI works end-to-end, `uv run pytest` is green and the README shows usage plus a screenshot.

## 📦 Deliverable (by Saturday night)
`01-python-async-cli/` with typed models, pydantic validation, async httpx client, Typer + Rich CLI, 10+ offline pytest tests and a README with usage.

## ✅ Self-check (Sunday test preview)
- When would you use `@dataclass` instead of a pydantic `BaseModel`, and vice versa?
- What happens if you call an `async def` function without `await`?
- Why does `asyncio.gather` speed up I/O-bound work but not CPU-bound work?
- What is a pytest fixture? Show one that uses `tmp_path`.
- How does `uv run` differ from installing packages into a global Python?
- How do you parse a JSON string into a validated model in Pydantic v2?

## 🚀 Stretch (optional)
Add a `--json` output flag and a GitHub Actions workflow that runs `uv run pytest` on every push ([Building and testing Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)).
