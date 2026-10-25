# 🤖 AI Engineering · Week 13 — Production AI Backend: DocuMind v2

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** Shipping AI means classic backend excellence (async APIs, streaming, auth, rate limits, caching, containers) applied to slow, costly, non-deterministic LLM calls. Tracing with OpenTelemetry follows in W19.

## 🗓️ Sessions

### Monday 18 Jan · 45 min — FastAPI structure: routers, lifespan, settings, logging
- 📚 **Learn:** Routers per feature, dependency-injected services (retriever, LLM client), lifespan startup for models and connection pools, `async def` vs a threadpool for blocking libraries (the same thread-pool idea as Java W8), pydantic-settings per environment, structured logging with a request ID. Read: [Concurrency and async/await (FastAPI)](https://fastapi.tiangolo.com/async/) (the 'in a hurry' part and the path-operation rules). Optional: [Logging HOWTO](https://docs.python.org/3/howto/logging.html).
- 🛠️ **Do:** Restructure DocuMind into `app/` (routers `ask`, `ingest`, `health`; `services/`; `config.py`). Load embedding and re-rank models once in lifespan, move secrets/config to env vars and add JSON logs with a request ID and latency. Done when: all existing tests pass, `/docs` shows grouped routes and every log line carries request_id and duration.

### Tuesday 19 Jan · 45 min — Streaming answers with Server-Sent Events
- 📚 **Learn:** SSE streams events over an ordinary HTTP response (`text/event-stream`). FastAPI 0.135+ supports it natively: `yield` items from an async generator (W3) with `response_class=EventSourceResponse`, and send a final `ServerSentEvent(event='citations', ...)`; clients resume with `Last-Event-ID`. One-way server push is all a chat answer needs, so SSE beats WebSockets here. Read: [FastAPI Server-Sent Events](https://fastapi.tiangolo.com/tutorial/server-sent-events/).
- 🛠️ **Do:** Add `POST /ask/stream` that yields `token` events while the LLM streams, then one `citations` event, with a 25-second overall timeout that emits an `error` event. Test with `curl -N`. Done when: tokens appear progressively, the citations event arrives last, and a deliberately slow fake provider produces the error event.

### Thursday 21 Jan · 45 min — Exact and semantic caching with Redis
- 📚 **Learn:** Redis primer: an in-memory key-value store; `SET key value EX 3600` stores a value with a time-to-live, `GET key` reads it. Exact cache (hash of the normalised prompt + parameters) vs semantic cache (embedding similarity under a distance threshold); keys must include model, prompt version and user scope; wrong-context hits are the main risk (caching concepts from SD W4). Read: [RedisVL LLM cache guide](https://docs.redisvl.com/en/latest/user_guide/03_llmcache.html) (needs Redis 8+).
- 🛠️ **Do:** Run `redis:8` in Docker. Add an exact cache (key = sha256 of question + config, TTL 1 hour) and a RedisVL `SemanticCache` with a strict threshold. Send 10 repeated and 10 paraphrased questions and log hit rate, latency and tokens saved. Done when: savings are logged and you show one wrong semantic hit your threshold now prevents.

### Friday 22 Jan · 45 min — Protecting cost: API keys and rate limits
- 📚 **Learn:** Authentication = who is calling (here an `X-API-Key` header checked by a dependency); authorization = what that caller may do. Per-key rate limits stop runaway cost: a token bucket (SD W11) allows short bursts, then answers 429 with `Retry-After`. Provider fallback already lives in your `llmkit`. Read: [slowapi](https://github.com/laurentS/slowapi) (README quickstart). Optional: [FastAPI security reference](https://fastapi.tiangolo.com/reference/security/) (APIKeyHeader).
- 🛠️ **Do:** Protect `/ask` and `/ask/stream` with an `APIKeyHeader` dependency (valid keys from settings) and limit each key to 10 requests per minute. Write 3 tests: missing key -> 401, valid key -> 200, 11th request within a minute -> 429. Done when: the tests pass and `curl` without a key is rejected.

### Saturday 23 Jan · 45 min — BUILD: DocuMind v2 dockerized with streaming and cache
- 📚 **Learn:** Container hygiene beyond W8: a multi-stage build (dependencies in a builder stage, slim runtime stage), uv inside Docker, a non-root user, a healthcheck, `.dockerignore`, Compose for app + pgvector + Redis, secrets via env files that never reach Git. Read: [FastAPI in containers](https://fastapi.tiangolo.com/deployment/docker/). Optional: [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/) (multi-stage builds).
- 🛠️ **Do:** Write a multi-stage Dockerfile using uv and a `compose.yaml` (api, pgvector, redis). Run end-to-end: ingest PDFs, stream answers, see cache hits and rate limits. Add a smoke-test script and a 'Run in 3 commands' README section. Done when: `docker compose up` works from a clean clone, eval scores stay within 2% of v1, and tag `v2.0-documind` is pushed.

## 📦 Deliverable (by Saturday night)
`09-documind/` v2.0: modular FastAPI app with SSE streaming, API-key auth, per-key rate limiting, exact + semantic Redis cache, multi-stage Docker image and Compose stack.

## ✅ Self-check (Sunday test preview)
- How do you stream LLM tokens from FastAPI to a browser, and why SSE rather than WebSockets here?
- What must be part of a cache key for LLM responses?
- When is semantic caching dangerous?
- How would you protect an LLM-backed API from cost blow-ups?
- Why run blocking model inference in a threadpool or separate worker?
- What does a multi-stage Dockerfile save you, and why run as a non-root user?

## 🚀 Stretch (optional)
Add `POST /ingest` as a background job with `GET /jobs/{id}` status, or a `GET /ask/stream?q=` variant plus a tiny HTML page that renders streamed answers with the browser `EventSource` API.
