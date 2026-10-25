# 🤖 AI Engineering · Week 27 — TicketVerse AI: Search, Booking Agent, Summaries

> 📅 **Mon 26 Apr 2027 → Sun 02 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 26](Week-26.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-27.md) · [Week 28 →](Week-28.md)

**Why this week:** Integrating AI into a real distributed system (semantic search, an agent that books safely, grounded summaries, evals and guardrails) is the story that wins 'Java + AI' offers. This week runs alongside Java W27, which adds the platform hooks (gateway route, JWT relay, Kafka topics, Helm values) for your `ticketverse-ai` service.

## 🗓️ Sessions

### Monday 26 Apr · 45 min — Semantic event search with PgVectorStore and Kafka sync
- 📚 **Learn:** Event search = embeddings of title + description + tags, structured filters (city, date, price) and a ranking blend (semantic score + popularity + date proximity); keep embeddings in sync by consuming the `catalog.shows.v1` events that Java W25 publishes. The full stack needs a 4-core codespace: start only the services you need and stop it after the session. Read: [PGvector store](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html) (metadata filters).
- 🛠️ **Do:** In `ticketverse-ai` add `GET /ai/search?q=&city=&date=`: backfill show embeddings, add a `@KafkaListener` on `catalog.shows.v1`, query PgVectorStore with metadata filters and blend in popularity. Label 10 queries and compute nDCG@10 with your W12 Python script. Done when: nDCG@10 is 0.7+ and a newly created show becomes searchable within seconds.

### Tuesday 27 Apr · 45 min — Booking agent via MCP tools with human confirmation
- 📚 **Learn:** Safe agentic booking: read tools (search, seats) vs write tools (hold, book) behind confirmation; two-phase flow: propose -> user confirms -> execute with an idempotency key (Java W15); user identity comes from the JWT the gateway relays (Java W27), never from the model. Read: [Spring AI tool calling](https://docs.spring.io/spring-ai/reference/api/tools.html) (tool context). Optional: [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).
- 🛠️ **Do:** Expose `holdSeats` and `confirmBooking` as tools/MCP tools where `confirmBooking` requires a server-issued confirmation token returned to the UI; the model can only propose. Forward the user's JWT to downstream services. Done when: the agent cannot book without the explicit confirm call and repeated confirms never double-book.

### Thursday 29 Apr · 45 min — Review summarization with citations and caching
- 📚 **Learn:** Map-reduce summarization over many reviews, aspect-based sentiment (sound, seating, value), structured output with cited review IDs to avoid invented claims, Redis caching invalidated by the `ReviewCreated` events from Java W25; treat review text as untrusted input (W18). Read: [Spring AI structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html). Optional: [Simon Willison on prompt injection](https://simonwillison.net/series/prompt-injection/).
- 🛠️ **Do:** Add `GET /ai/events/{id}/review-summary`: summarise review batches (map), merge them (reduce) into `ReviewSummary(summary, pros, cons, aspects, citedReviewIds)`, cache in Redis and invalidate on `ReviewCreated`. Done when: 3 events produce summaries whose cited review IDs exist and support the claims (spot-check).

### Friday 30 Apr · 45 min — Capstone evals and guardrails for TicketVerse AI
- 📚 **Learn:** Capstone eval suite: task success, tool-call accuracy, correct refusals, search nDCG, summary faithfulness; guardrails: input limits, indirect-injection tests via review text, PII redaction, per-user rate limits. Reuse your W12, W17 and W18 scripts. Read: [DeepEval task completion](https://deepeval.com/docs/metrics-task-completion). Optional: [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/).
- 🛠️ **Do:** Write 12 assistant scenarios (search, policy Q&A, booking with and without confirmation, malicious review text) and run them through a Python harness against the REST API; add the attack cases to the TicketVerse CI pipeline from Java W26. Done when: task success is 85%+, there are zero unconfirmed bookings, and the report is committed.

### Saturday 01 May · 45 min — BUILD: TicketVerse AI features integrated end-to-end
- 📚 **Learn:** Integration checklist: gateway route and JWT relay (Java W27), per-environment config, timeouts and fallbacks (Resilience4j around AI calls), dashboards, and a runbook for AI failures (provider down -> degrade gracefully). Read: [Spring AI observability](https://docs.spring.io/spring-ai/reference/observability/index.html).
- 🛠️ **Do:** On a 4-core codespace run the TicketVerse stack with `ticketverse-ai` behind the gateway and run the joint end-to-end script with Java W27 (search -> ask -> propose -> confirm). Fix integration bugs and update the architecture diagram and eval report. Done when: the end-to-end script passes on a fresh environment, the codespace is stopped, and tag `ticketverse-v2.0-ai` is pushed.

## 📦 Deliverable (by Saturday night)
TicketVerse with AI: semantic show search (nDCG@10 0.7+) synced from Kafka, an MCP/tool booking agent with confirmation and idempotency, cited review summaries with Redis caching, a 12-scenario eval with attack cases in CI and a passing end-to-end script.

## ✅ Self-check (Sunday test preview)
- How do you keep embeddings in sync with a changing catalog?
- How do you let an agent book tickets safely?
- What is an idempotency key, and why does the booking tool need one?
- How would you evaluate the TicketVerse assistant before release?
- What indirect prompt-injection risks do user reviews introduce?
- How does the AI service degrade when the LLM provider is down?

## 🚀 Stretch (optional)
Grow the eval to 20 scenarios, or add a 'similar events' recommendation endpoint using vector similarity over events a user previously booked.
