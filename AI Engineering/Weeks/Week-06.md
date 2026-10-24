# 🤖 AI Engineering · Week 06 — Embeddings, Vector Search, FastAPI and pgvector

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Semantic search is the backbone of RAG, recommendations and de-duplication. FastAPI + pgvector is a production-grade stack you will reuse all plan, and AI-200 tests vector databases.

## 🗓️ Sessions

### Monday 30 Nov · 45 min — Embeddings and similarity metrics
- 📚 **Learn:** An embedding is a fixed-size vector of meaning; cosine vs dot product vs L2, normalisation, dimensions vs storage cost, choosing models with MTEB, multilingual needs (Hindi/English). Read: [Simon Willison: Embeddings](https://simonwillison.net/2023/Oct/23/embeddings/), [sentence-transformers quickstart](https://sbert.net/docs/quickstart.html); browse the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard).
- 🛠️ **Do:** First, run `docker version` in your Codespace (Docker comes preinstalled there) so it is ready for Tuesday. Then embed 20 sentences (including paraphrases and Hindi/English pairs) locally with `all-MiniLM-L6-v2` and with an API or Ollama model (`nomic-embed-text`). Implement cosine similarity in NumPy and print the top-3 neighbours for 5 queries. Done when: you can show one case each model gets right that the other misses.

### Tuesday 01 Dec · 45 min — Vector databases, ANN indexes and Docker pgvector
- 📚 **Learn:** Exact (flat) vs approximate search; HNSW (graph; m, ef_search) vs IVF (clusters; lists, probes); recall vs latency vs memory; filtered-search pitfalls; options: pgvector, Qdrant, Chroma. Read: [pgvector README](https://github.com/pgvector/pgvector) (HNSW, IVFFlat, filtering), [Qdrant indexing](https://qdrant.tech/documentation/concepts/indexing/); install [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) (WSL2).
- 🛠️ **Do:** Run `docker run -d --name pgv -e POSTGRES_PASSWORD=pass -p 5432:5432 pgvector/pgvector:0.8.7-pg18`. Create `items(id, text, category, embedding vector(384))`, insert 1,000 embedded rows, then compare exact search vs an HNSW cosine index with `EXPLAIN ANALYZE`. Done when: both timings are recorded and the plan shows the HNSW index being used.

### Thursday 03 Dec · 45 min — FastAPI basics: routes, models, dependencies, tests
- 📚 **Learn:** Path and query params, pydantic request/response models, async endpoints, dependency injection with `Depends` (like Spring beans), auto OpenAPI docs at `/docs`, `TestClient`. Read: [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/), [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/), [Testing](https://fastapi.tiangolo.com/tutorial/testing/).
- 🛠️ **Do:** Create `05-semantic-search-api` with `fastapi[standard]`: `GET /health`, `POST /embed` (returns vector length and first 5 dimensions) and a stub `GET /search?q=&k=`. Load the embedding model once and inject it with `Depends`. Done when: `uv run fastapi dev` serves `/docs` and 3 TestClient tests pass.

### Friday 04 Dec · 45 min — Ingest a real dataset into pgvector
- 📚 **Learn:** Batch embedding, idempotent upserts, metadata in JSONB, connection handling with psycopg 3, `pgvector-python` type adapters, cosine operator class. Read: [pgvector-python](https://github.com/pgvector/pgvector-python) (psycopg 3 section); datasets: [Wiki movie plots](https://huggingface.co/datasets/vishnupriyavr/wiki-movie-plots-with-summaries) or [data job postings](https://huggingface.co/datasets/lukebarousse/data_jobs).
- 🛠️ **Do:** Write `ingest.py` that embeds 2,000-5,000 rows in batches of 64 and upserts them with metadata (year/genre or company/location), then creates an HNSW `vector_cosine_ops` index. Done when: row counts match, re-running ingest creates no duplicates, and a SQL nearest-neighbour query returns sensible results.

### Saturday 05 Dec · 45 min — BUILD: SemanticSearch API with FastAPI and pgvector
- 📚 **Learn:** Search API design: `q`, `k`, filters, pagination, scores, latency logging; measure quality with a few labelled queries (recall@k). Structure with routers: [FastAPI bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
- 🛠️ **Do:** Implement `GET /search?q=&k=&genre=&year_from=` (embed query, pgvector cosine top-k with SQL filters), `POST /documents` and `GET /stats`. Label 15 queries with expected IDs and compute recall@10. Write a README with curl examples and a Mermaid diagram. Done when: recall@10 is 0.8+ on your 15 queries, p95 latency is logged, and tag `v1.0-semantic-search` is pushed.

## 📦 Deliverable (by Saturday night)
`05-semantic-search-api/`: pgvector in Docker, idempotent ingest script, FastAPI search with metadata filters, 15-query eval (recall@10), README with architecture diagram.

## ✅ Self-check (Sunday test preview)
- Cosine similarity vs dot product vs Euclidean distance: when are they equivalent?
- How does HNSW work at a high level, and what do `m` and `ef_search` trade off?
- Why can filtered ANN search return fewer than k results, and how do you fix it?
- How do you choose an embedding model? What is MTEB?
- pgvector vs a dedicated vector DB like Qdrant: pros and cons?
- What must you do if you change the embedding model after indexing?

## 🚀 Stretch (optional)
Repeat the search with [Qdrant](https://qdrant.tech/documentation/) in Docker and compare recall and latency with pgvector on your 15 queries.
