# 🤖 AI Engineering · Week 24 — TicketVerse AI: Search, Booking Agent, Summaries

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** Integrating AI into a real distributed system (semantic search, an agent that books safely, grounded summaries, evals and guardrails) is the story that wins SDE-2 'Java + AI' offers. Runs alongside Java track W24.

## 🗓️ Sessions

### Monday 05 Apr · 45 min — Semantic event search with PgVectorStore and Kafka sync
- 📚 **Learn:** Event search = embeddings of title + description + tags, structured filters (city, date, price) and a ranking blend (semantic score + popularity + date proximity); keep embeddings in sync from catalog events (Kafka consumer on created/updated). Reuse: [PGvector store](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html) and your W8 hybrid ideas.
- 🛠️ **Do:** In `ticketverse-ai` add `GET /ai/search?q=&city=&date=`: backfill event embeddings, add a Kafka listener for updates, query PgVectorStore with metadata filters and blend in popularity. Label 15 queries and compute nDCG@10 with your Python eval script. Done when: nDCG@10 is 0.7+ and a newly created event becomes searchable within seconds.

### Tuesday 06 Apr · 45 min — Booking agent via MCP tools with human confirmation
- 📚 **Learn:** Safe agentic booking: read tools (search, seats) vs write tools (hold, book) behind confirmation; two-phase flow: propose -> user confirms -> execute with an idempotency key; user identity comes from the request context, never from the model. Read: [Spring AI tool calling](https://docs.spring.io/spring-ai/reference/api/tools.html) (tool context) and [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices).
- 🛠️ **Do:** Expose `holdSeats` and `confirmBooking` as tools/MCP tools where `confirmBooking` requires a server-issued confirmation token returned to the UI; the model can only propose. Forward the user's JWT to downstream services. Done when: the agent cannot book without the explicit confirm call and repeated confirms never double-book.

### Thursday 08 Apr · 45 min — Review summarization with citations and caching
- 📚 **Learn:** Map-reduce summarization over many reviews, aspect-based sentiment (sound, seating, value), structured output with cited review IDs to avoid invented claims, Redis caching with invalidation on new reviews; treat review text as untrusted input. Read: [Spring AI structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html) and [Simon Willison on prompt injection](https://simonwillison.net/series/prompt-injection/).
- 🛠️ **Do:** Add `GET /ai/events/{id}/review-summary`: summarise review batches (map), merge them (reduce) into `ReviewSummary(summary, pros, cons, aspects, citedReviewIds)`, cache in Redis and invalidate on new-review events. Done when: 3 events produce summaries whose cited review IDs exist and support the claims (spot-check).

### Friday 09 Apr · 45 min — Capstone evals and guardrails for TicketVerse AI
- 📚 **Learn:** Capstone eval suite: task success, tool-call accuracy, correct refusals, search nDCG, summary faithfulness; guardrails: input limits, indirect-injection tests via review text, PII redaction, per-user rate limits. Reuse W9/W14/W15 scripts. Read: [DeepEval task completion](https://deepeval.com/docs/metrics-task-completion) and the [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/).
- 🛠️ **Do:** Write 20 assistant scenarios (search, policy Q&A, booking with and without confirmation, malicious review text) and run them through a Python harness against the REST API; add the attack cases to CI. Done when: task success is 85%+, tool-call accuracy 90%+, zero unconfirmed bookings, and the report is committed.

### Saturday 10 Apr · 45 min — BUILD: TicketVerse AI features integrated end-to-end
- 📚 **Learn:** Integration checklist: gateway routes, auth propagation, Compose/Kubernetes manifests, per-environment config, timeouts and fallbacks, dashboards (Grafana + traces), and a runbook for AI failures (provider down -> degrade gracefully). Read: [Spring AI observability](https://docs.spring.io/spring-ai/reference/observability/index.html).
- 🛠️ **Do:** Run the full TicketVerse stack with `ticketverse-ai` behind the gateway: semantic search, assistant with tools + RAG, confirmed booking flow and review summaries. Fix integration bugs together with the Java track and update the architecture diagram and eval report. Done when: an end-to-end script (search -> ask -> propose -> confirm) passes on a fresh environment and tag `ticketverse-v2.0-ai` is pushed.

## 📦 Deliverable (by Saturday night)
TicketVerse with AI: semantic event search (nDCG@10 0.7+), tool/MCP booking agent with human confirmation and idempotency, cited review summaries, 20-scenario eval + attack cases in CI, end-to-end script.

## ✅ Self-check (Sunday test preview)
- How do you keep embeddings in sync with a changing catalog?
- How do you let an agent book tickets safely?
- What is an idempotency key, and why does the booking tool need one?
- How would you evaluate the TicketVerse assistant before release?
- What indirect prompt-injection risks do user reviews introduce?
- How does the AI service degrade when the LLM provider is down?

## 🚀 Stretch (optional)
Add a 'similar events' recommendation endpoint using vector similarity over events a user previously booked.
