# 🤖 AI Engineering · Week 08 — Backend Foundations: Docker, SQL and FastAPI

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Every AI backend you build next runs in containers, keeps its data in PostgreSQL and serves it over an API. Learning these three in your codespace now means W9 can focus on vectors instead of fighting tooling.

## 🗓️ Sessions

### Monday 14 Dec · 45 min — Docker essentials: images, containers, ports, volumes
- 📚 **Learn:** An image is a read-only template; a container is a running instance with its own filesystem and network. Key flags: `-d`, `--name`, `-p host:container`, `-e`, `-v name:/path` (a named volume keeps data when the container is removed); commands `docker ps`, `logs`, `exec`, `stop`, `rm`. Docker is preinstalled in your codespace via the docker-in-docker feature. Read: [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) (about 10 min). Optional: [What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/).
- 🛠️ **Do:** Run `docker run -d --name pg -e POSTGRES_PASSWORD=pass -p 5432:5432 -v pgdata:/var/lib/postgresql postgres:18`, open `docker exec -it pg psql -U postgres`, create a table and insert 2 rows. Remove the container, start a new one with the same volume and query again. Done when: the rows survive the container swap and `07-backend-foundations/docker-notes.md` explains image vs container vs volume in 3 lines.

### Tuesday 15 Dec · 45 min — SQL for AI developers I: tables, CRUD, upserts, JSONB
- 📚 **Learn:** `CREATE TABLE` with types and a primary key, `INSERT`, `SELECT ... WHERE ... ORDER BY ... LIMIT`, `UPDATE`, `DELETE`. `INSERT ... ON CONFLICT (id) DO UPDATE` (an upsert) makes ingestion safe to re-run; `jsonb` columns hold flexible metadata, read with `->>`. From Python, psycopg 3 sends parameterised queries (`%s`), never string concatenation. Read: [PostgreSQL tutorial: the SQL language](https://www.postgresql.org/docs/current/tutorial-sql.html) (2.1-2.6). Optional: [psycopg 3 basic usage](https://www.psycopg.org/psycopg3/docs/basic/usage.html).
- 🛠️ **Do:** In `07-backend-foundations/db.py` (`uv add 'psycopg[binary]'`) create `jobs(id text primary key, title text, company text, data jsonb)` and load your W7 `postings.jsonl` with an upsert. Run the loader twice, then select remote jobs with `data->>'remote'`. Done when: the row count is identical after both runs and the JSONB query returns the expected postings.

### Thursday 17 Dec · 45 min — SQL for AI developers II: indexes and EXPLAIN ANALYZE
- 📚 **Learn:** An index (B-tree by default, the structure from SD W6) is a sorted lookup that speeds filtered or sorted reads and costs writes and storage. `EXPLAIN ANALYZE` runs the query and shows the real plan: Seq Scan vs Index Scan, row counts and time; small tables are often scanned anyway. You will read vector-index plans the same way in W9. Read: [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) (14.1.1 and 14.1.2). Optional: [Use The Index, Luke](https://use-the-index-luke.com/).
- 🛠️ **Do:** Generate 200,000 fake job rows with `generate_series`, then `EXPLAIN ANALYZE` a filter on `company` before and after `CREATE INDEX`. Repeat on a 50-row table. Done when: `sql-notes.md` records both plans and timings and explains in 2 lines why the tiny table ignores the index.

### Friday 18 Dec · 45 min — FastAPI basics: routes, models, dependencies, tests
- 📚 **Learn:** Path and query parameters, pydantic request/response models, async endpoints, dependency injection with `Depends` (FastAPI creates the repository or service and passes it in, so tests can swap it), automatic OpenAPI docs at `/docs`, and `TestClient`. Read: [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/) (about 10 min). Optional: [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/).
- 🛠️ **Do:** Create `07-backend-foundations/api` with `fastapi[standard]`: `GET /health`, `POST /jobs` (inserts through a `get_repo` dependency) and `GET /jobs/{id}` (404 when missing). In tests, replace `get_repo` with an in-memory fake via `app.dependency_overrides`. Done when: `uv run fastapi dev` serves `/docs` and 3 `TestClient` tests pass without a database.

### Saturday 19 Dec · 45 min — BUILD: FastAPI + Postgres with a Dockerfile and Compose
- 📚 **Learn:** A Dockerfile builds your image step by step (`FROM`, `COPY`, `RUN uv sync`, `CMD`); order the steps so dependency layers stay cached. Compose describes several containers, their environment, ports, volumes and `depends_on` with a healthcheck in one `compose.yaml`; `docker compose up --build` starts them all. Read: [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/) (getting started). Optional: [Compose quickstart](https://docs.docker.com/compose/gettingstarted/).
- 🛠️ **Do:** Write a single-stage Dockerfile for your API and a `compose.yaml` with `api` and `db` (postgres:18, named volume, healthcheck, `depends_on: condition: service_healthy`), reading the password from a git-ignored `.env`. Add `smoke.sh` that creates and fetches a job with curl. Done when: `docker compose up --build` from a clean clone passes `smoke.sh` and the README has a 'Run in 3 commands' section.

## 📦 Deliverable (by Saturday night)
`07-backend-foundations/`: Docker notes, SQL loader with idempotent upserts and JSONB queries, EXPLAIN ANALYZE notes, a tested FastAPI service, and a Dockerfile + Compose stack with a smoke test.

## ✅ Self-check (Sunday test preview)
- Image vs container vs volume: what survives `docker rm`?
- What does `INSERT ... ON CONFLICT DO UPDATE` give you during ingestion?
- Why must SQL parameters never be concatenated into the query string?
- Reading an EXPLAIN ANALYZE plan: what tells you that an index was used?
- How does FastAPI's `Depends` make code testable?
- Why does Compose need a healthcheck when the API depends on the database?

## 🚀 Stretch (optional)
Add plain SQL migration files for the jobs table, or add keyset pagination (SD W2) to `GET /jobs` and compare it with `OFFSET` on 200,000 rows.
