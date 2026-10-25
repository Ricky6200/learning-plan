# 🤖 AI Engineering · Week 09 — Embeddings, pgvector and the SemanticSearch Boss

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Semantic search is the backbone of RAG, recommendations and de-duplication, and pgvector is the vector store you reuse all plan (AI-200 tests vector databases too). The season ends with a timed build of a search API. (Fri 25 Dec is Christmas: a light preparation session.)

## 🗓️ Sessions

### Monday 21 Dec · 45 min — Embeddings and similarity metrics
- 📚 **Learn:** An embedding is a fixed-size vector of meaning; cosine vs dot product vs L2, normalisation, dimensions vs storage cost, choosing models with MTEB, multilingual needs (Hindi/English). Install sentence-transformers with the CPU-only PyTorch index: the default CUDA wheels add several GB to your codespace. Read: [sentence-transformers quickstart](https://sbert.net/docs/quickstart.html). Optional: [Simon Willison: Embeddings](https://simonwillison.net/2023/Oct/23/embeddings/).
- 🛠️ **Do:** Configure the CPU-only torch index in `pyproject.toml` (see the [uv PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/)), then `uv add sentence-transformers`. Embed 20 sentences (paraphrases and Hindi/English pairs) with `all-MiniLM-L6-v2` and with Ollama `nomic-embed-text`. Implement cosine similarity in NumPy and print the top-3 neighbours for 5 queries. Done when: you can show one case each model gets right that the other misses.

### Tuesday 22 Dec · 45 min — Vector databases, ANN indexes and pgvector
- 📚 **Learn:** Exact (flat) vs approximate search; HNSW (a graph; `m`, `ef_search`) vs IVF (clusters; lists, probes); recall vs latency vs memory; filtered-search pitfalls; options: pgvector, Qdrant, Chroma. Read: [pgvector README](https://github.com/pgvector/pgvector) (indexing: HNSW and IVFFlat; filtering). Optional: [Qdrant indexing](https://qdrant.tech/documentation/concepts/indexing/).
- 🛠️ **Do:** Run `docker run -d --name pgv -e POSTGRES_PASSWORD=pass -p 5433:5432 pgvector/pgvector:0.8.7-pg18`. Create `items(id, text, category, embedding vector(384))`, insert 1,000 embedded rows and compare exact search with an HNSW `vector_cosine_ops` index using `EXPLAIN ANALYZE` (W8). Small tables may still be scanned: inside a transaction run `SET LOCAL enable_seqscan = off` to see the index plan. Done when: both timings are recorded and one plan shows the HNSW index.

### Thursday 24 Dec · 45 min — Ingest a real dataset into pgvector
- 📚 **Learn:** Batch embedding, idempotent upserts (W8's `ON CONFLICT`), metadata in JSONB, connection handling with psycopg 3, `pgvector-python` type adapters, the cosine operator class. Read: [pgvector-python](https://github.com/pgvector/pgvector-python) (Psycopg 3 section). Optional dataset: [Wiki movie plots](https://huggingface.co/datasets/vishnupriyavr/wiki-movie-plots-with-summaries).
- 🛠️ **Do:** Write `08-semantic-search-api/ingest.py` that embeds 2,000-5,000 rows (movie plots or [data job postings](https://huggingface.co/datasets/lukebarousse/data_jobs)) in batches of 64 and upserts them with metadata (year/genre or company/location), then creates an HNSW `vector_cosine_ops` index. Done when: row counts match, re-running ingest creates no duplicates, and a SQL nearest-neighbour query returns sensible results.

### Friday 25 Dec · 45 min — Search API design and a labelled query set (light)
- 📚 **Learn:** Search API design: `q`, `k`, filters, scores and latency logging. Quality is measured with labelled queries: recall@k = the share of expected results that appear in the top k. Organise the app with routers. Read: [FastAPI bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) (about 10 min).
- 🛠️ **Do:** Christmas, so 20 minutes: write `labels.json` with 10 queries and their expected row IDs (find them with keyword SQL queries), and a skeleton `app/` with routers `search.py` and `documents.py` returning stubs. Done when: the skeleton starts with `uv run fastapi dev` and `labels.json` has 10 queries, each with at least one expected ID.

### Saturday 26 Dec · 45 min — BOSS BATTLE: SemanticSearch API in 45 minutes
- 📚 **Learn:** Rules: 45-minute timer, start from Friday's skeleton, docs allowed, no AI code generation, commit every 15 minutes. Rubric /100: `/search` with k and 2 filters 30, `POST /documents` 15, recall@10 on your 10 labels 20, p95 latency logged 10, 3 tests 15, README with curl examples and a Mermaid diagram 10. Reference: [pgvector README](https://github.com/pgvector/pgvector) (querying).
- 🛠️ **Do:** Implement `GET /search?q=&k=&genre=&year_from=` (embed the query, pgvector cosine top-k with SQL filters, return scores), `POST /documents` and `GET /stats`; compute recall@10 on `labels.json` and log p95 latency over 50 queries. Done when: the rubric score is 80+, recall@10 is 0.8+, and tag `v1.0-semantic-search` is pushed.

## 📦 Deliverable (by Saturday night)
`08-semantic-search-api/`: CPU-only embedding setup, pgvector in Docker, idempotent ingest, FastAPI search with metadata filters, labelled recall@10 and a README with an architecture diagram (boss tag `v1.0-semantic-search`).

## ✅ Self-check (Sunday test preview)
- Cosine similarity vs dot product vs Euclidean distance: when are they equivalent?
- How does HNSW work at a high level, and what do `m` and `ef_search` trade off?
- Why can filtered ANN search return fewer than k results, and how do you fix it?
- How do you choose an embedding model? What is MTEB?
- pgvector vs a dedicated vector DB like Qdrant: pros and cons?
- What must you do if you change the embedding model after indexing?

## 🚀 Stretch (optional)
Repeat the search with [Qdrant](https://qdrant.tech/documentation/) in Docker and compare recall and latency with pgvector, or cluster 2,000 embeddings with `KMeans` (W4 stretch) and name the clusters.
