# ☁️ Azure Cloud · Week 19 — pgvector, Managed Redis + RAG data-layer Boss

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** pgvector tuning, RAG retrieval with metadata filters and Redis caching are what make AI features fast and affordable in production - and they are heavily weighted in AI-200. The Season 4 Boss builds a real RAG data layer on Azure.

## 🗓️ Sessions

### Tuesday 02 Mar · 45 min — pgvector on Azure: enable, store, HNSW vs IVFFlat
- 📚 **Learn:** Allowlisting `vector` in `azure.extensions`, `CREATE EXTENSION vector`, vector columns, distance operators (<->, <=>, <#>), HNSW (m, ef_construction, ef_search) vs IVFFlat (lists, probes), DiskANN awareness. Use [Vector search with pgvector](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-use-pgvector), [Optimize pgvector performance](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-optimize-performance-pgvector) and Learn's [Implement vector search with Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/training/modules/implement-vector-search-azure-database-postgresql/).
- 🛠️ **Do:** Allowlist and create the extension; load 5,000 document chunks with embeddings (reuse DocuMind or SemanticSearch data from the AI track; `vector(768)` for nomic-embed-text, `vector(384)` for MiniLM). Measure a top-5 cosine query with no index, with HNSW and with IVFFlat (lists about rows/1000); then vary `hnsw.ef_search` and `ivfflat.probes` and record latency vs recall against the exact result. Done when: a 6-row timing/recall table is in `w19/pgvector.md`.

### Wednesday 03 Mar · 45 min — RAG retrieval with metadata filters, sizing and connections
- 📚 **Learn:** Retrieval that combines vector similarity with SQL metadata filters (tenant, date, source), how filters interact with approximate indexes, memory for index builds (`maintenance_work_mem`), compute/memory/storage sizing for vector workloads, connection optimization. Use Learn's [Optimize vector search in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/training/modules/optimize-vector-search-azure-database-postgresql/), [Compute options](https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute) and Pamela Fox's [pgvector on Azure](https://www.youtube.com/watch?v=sCX_sB2dQHY).
- 🛠️ **Do:** Write `py/retrieve.py` with `retrieve(question, source=None, after=None, k=5)`: embed the question and run one parameterized SQL query combining `ORDER BY embedding <=> %s` with WHERE filters; add a B-tree index on the filter column and compare plans. Then write a sizing note: index size vs RAM, and when to move from B1ms to General Purpose. Done when: the function returns filtered results and the note is in `w19/`.

### Friday 05 Mar · 45 min — Azure Managed Redis: caching, expiration, invalidation, vector index
- 📚 **Learn:** Tiers (Memory Optimized, Balanced, Compute Optimized, Flash Optimized), Entra auth, redis-py, cache-aside with TTL, invalidation on write, key design, vector indexing with the RediSearch module (added only at creation time). Use [What is Azure Managed Redis?](https://learn.microsoft.com/en-us/azure/redis/overview), the [cache-aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside) and Learn's [Implement vector storage in Azure Managed Redis](https://learn.microsoft.com/en-us/training/modules/implement-vector-storage-azure-managed-redis/).
- 🛠️ **Do:** Create the smallest Balanced SKU with RediSearch enabled (note creation time and hourly price; delete it today). With redis-py: cache `retrieve()` results under `rag:<hash>` with a 10-minute TTL, measure hit vs miss latency, invalidate the key when a source document changes, and build a small vector index (FT.CREATE, DIM matching your model) to run a KNN query over 100 embeddings. Done when: hit/miss timings, invalidation test and KNN output are in `w19/redis.md`; cache deleted.

### Saturday 06 Mar · 60 min — BOSS BATTLE: Azure RAG data layer (pgvector + Redis) + 20 questions
- 📚 **Learn:** Season 4 integration: vector search, metadata filters, pooling and Redis cache-aside. Use your `py/retrieve.py`, the [Azure RAG design guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) for review, and the [AI-200 practice assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b) on AI Skills Navigator (sign-in required).
- 🛠️ **Do:** 40-minute build: start Azure Managed Redis (smallest SKU, RediSearch) first, then PostgreSQL (B1ms, pgvector, HNSW) in `rg-boss-s4`; load 1,000 chunks; expose `ask(question, source)` that serves repeats from cache with a TTL and logs DB vs cache latency; prove invalidation. 20 minutes: 20 AI-200 practice questions on data services, logging misses. Delete the RG. Done when: the demo log and score are committed and the RG is deleted.

## 📦 Deliverable (by Saturday night)
`w19/` pgvector timing/recall table, `retrieve.py` with filters, Redis cache-aside + vector-index evidence, the Boss demo log and the practice-question score.

## ✅ Self-check (Sunday test preview)
- HNSW vs IVFFlat: which builds slower, which needs data before building, and which parameters trade recall for speed?
- Why must you allowlist an extension on Azure Database for PostgreSQL before CREATE EXTENSION?
- How can metadata filters hurt recall with an approximate vector index, and how do you mitigate it?
- What is cache-aside, and how do you invalidate a cached RAG answer when a source document changes?
- Which Azure Managed Redis tier would you pick for a small dev cache vs a large vector index, and why?
- How would you size memory for a vector workload in PostgreSQL?

## 🚀 Stretch (optional)
Attempt the hosted Applied Skills lab [Build AI-powered solutions by using Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/credentials/applied-skills/build-ai-powered-solutions-by-using-microsoft-azure-database-for-postgresql/) or watch Savill's [Azure Managed Redis Deep Dive](https://www.youtube.com/watch?v=jIpJplSaFQM).
