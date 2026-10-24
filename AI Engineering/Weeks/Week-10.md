# 🤖 AI Engineering · Week 10 — Production AI Backend: DocuMind v2

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Shipping AI means classic backend excellence (async APIs, auth, rate limits, caching, timeouts, observability, containers) applied to slow, costly, non-deterministic LLM calls.

## 🗓️ Sessions

### Monday 28 Dec · 45 min — FastAPI structure: routers, dependencies, async, config, logging
- 📚 **Learn:** Routers per feature, dependency-injected services (retriever, LLM client), lifespan startup for models and pools, `async def` vs threadpool for blocking libraries, pydantic-settings per environment, structured logging. Read: [Bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/), [Concurrency and async/await](https://fastapi.tiangolo.com/async/), [Logging HOWTO](https://docs.python.org/3/howto/logging.html).
- 🛠️ **Do:** Restructure DocuMind into `app/` (routers `ask`, `ingest`, `health`; `services/`; `config.py`). Load embedding and re-rank models once in lifespan, move secrets/config to env vars and add JSON logs with a request ID and latency. Done when: all existing tests pass, `/docs` shows grouped routes and every log line carries request_id and duration.

### Tuesday 29 Dec · 45 min — SSE streaming, API-key auth and rate limiting
- 📚 **Learn:** Stream tokens with Server-Sent Events (`EventSourceResponse`, native since FastAPI 0.135) and send citations as a final event; API-key or JWT auth via dependencies; per-key rate limits to protect cost. Read: [FastAPI Server-Sent Events](https://fastapi.tiangolo.com/tutorial/server-sent-events/), [FastAPI security](https://fastapi.tiangolo.com/tutorial/security/), [slowapi](https://github.com/laurentS/slowapi).
- 🛠️ **Do:** Add `POST /ask/stream` emitting `token` events then one `citations` event. Protect routes with an API-key header dependency and limit each key to 10 requests/minute. Test with `curl -N`. Done when: tokens stream live, a missing key returns 401 and the 11th request in a minute returns 429.

### Thursday 31 Dec · 45 min — Exact and semantic caching with Redis
- 📚 **Learn:** Exact cache (hash of normalised prompt + parameters) vs semantic cache (embedding similarity under a distance threshold); TTLs; cache keys must include model, prompt version and tenant/user scope; risk of wrong-context hits. Read: [RedisVL semantic cache guide](https://docs.redisvl.com/en/latest/user_guide/03_llmcache.html) (needs Redis 8+) and [Redis docs](https://redis.io/docs/latest/).
- 🛠️ **Do:** Run `redis:8` in Docker. Add an exact cache (key = sha256 of question + config, TTL 1 hour) and a RedisVL `SemanticCache` with a strict threshold. Send 10 repeated and 10 paraphrased questions and log hit rate, latency and tokens saved. Done when: savings are logged and you show one wrong semantic hit your threshold now prevents.

### Friday 01 Jan · 45 min — Timeouts, fallbacks, background ingestion, OpenTelemetry
- 📚 **Learn:** Timeouts on every external call, retries with backoff, provider fallback, circuit-breaker idea (like Resilience4j), background ingestion jobs with status, OpenTelemetry traces and metrics. Read: [Background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/), [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/), [FastAPI instrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html).
- 🛠️ **Do:** Add provider fallback (primary Gemini, fallback Groq on 429 or timeout), a 20-second overall request timeout, `POST /ingest` returning a job ID with `GET /jobs/{id}` status, and OpenTelemetry auto-instrumentation exporting to the console. Done when: breaking the primary key triggers fallback and an ingestion job moves queued -> running -> done.

### Saturday 02 Jan · 45 min — BUILD: DocuMind v2 dockerized with streaming and cache
- 📚 **Learn:** Container hygiene: slim base image, uv inside Docker, non-root user, healthcheck, `.dockerignore`, Docker Compose for app + pgvector + Redis, secrets via env files that never reach Git. Read: [FastAPI in containers](https://fastapi.tiangolo.com/deployment/docker/).
- 🛠️ **Do:** Write a multi-stage Dockerfile using uv and a `compose.yaml` (api, pgvector, redis). Run end-to-end: ingest PDFs, stream answers, see cache hits and rate limits. Add a smoke-test script and a 'Run in 3 commands' README section. Done when: `docker compose up` works from a clean clone, eval scores stay within 2% of v1, and tag `v2.0-documind` is pushed.

## 📦 Deliverable (by Saturday night)
`06-documind/` v2.0: modular FastAPI app with SSE streaming, API-key auth, rate limiting, exact + semantic Redis cache, timeouts/fallbacks, background ingestion, OpenTelemetry, Docker Compose.

## ✅ Self-check (Sunday test preview)
- How do you stream LLM tokens from FastAPI to a browser, and why SSE rather than WebSockets here?
- What must be part of a cache key for LLM responses?
- When is semantic caching dangerous?
- How would you protect an LLM-backed API from cost blow-ups?
- Why run blocking model inference in a threadpool or separate worker?
- What would you trace in an AI request to debug p95 latency?

## 🚀 Stretch (optional)
Build a tiny HTML page that uses the browser `EventSource` API to render streamed answers with clickable citations.
