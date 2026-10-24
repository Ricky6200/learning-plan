# ☕ Java Backend · Week 24 — Spring AI assistant: Ask TicketVerse

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** Java backends are adding LLM features fast; showing ChatClient, tool calling, RAG and an MCP server inside a real secured microservice system sets you apart in Java + AI roles.

## 🗓️ Sessions

### Monday 05 Apr · 60 min — Spring AI 2.x ChatClient, model choice, prompts, streaming
- 📚 **Learn:** ChatModel vs ChatClient fluent API; system and user messages, prompt templates, options (temperature, max tokens); streaming responses; free model options: Ollama locally, Gemini free tier, OpenAI-compatible endpoints (Groq, OpenRouter) via the OpenAI starter's base URL (in Spring AI 2.0, Azure OpenAI also goes through the OpenAI module). [Spring AI: Chat Client API](https://docs.spring.io/spring-ai/reference/api/chatclient.html), [Spring AI: Ollama chat](https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html), [Dan Vega: Spring AI (playlist)](https://www.youtube.com/playlist?list=PLZV0a2jwt22uoDm3LNDFvN6i2cAVU_HTH).
- 🛠️ **Do:** Create `ai-assistant` service (Boot 4.1, Spring AI 2.0.x BOM) with `POST /api/assistant/chat` and a streaming variant; a system prompt that keeps the assistant to TicketVerse topics; model via Ollama or an OpenAI-compatible free endpoint chosen by profile; route it through the gateway with JWT. Done when: the same prompt works on two providers by switching only the profile.

### Tuesday 06 Apr · 60 min — Structured output, advisors and per-user chat memory
- 📚 **Learn:** Structured output into records (`.entity(BookingIntent.class)`), validation and retries on bad JSON; Advisors API (logging, memory, guard-style advisors) and ordering; chat memory with a conversation id and a JDBC-backed repository; token limits. [Spring AI: Structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html), [Spring AI: Advisors](https://docs.spring.io/spring-ai/reference/api/advisors.html), [Spring AI: Chat memory](https://docs.spring.io/spring-ai/reference/api/chat-memory.html).
- 🛠️ **Do:** Implement `extractIntent(text)` returning `BookingIntent(city, movie, date, seatCount, budget)`; test it with 10 phrasings including Hinglish ('kal shaam Pune mein 2 seats'); add a logging advisor and JDBC chat memory keyed by the JWT subject so follow-ups ('make it 3 seats') work. Done when: 8 of 10 phrasings parse correctly and memory survives an app restart.

### Wednesday 07 Apr · 60 min — Tool calling into catalog and booking APIs, with safety
- 📚 **Learn:** `@Tool` methods and tool descriptions; how the model chooses tools; read tools (search shows, check availability) vs write tools (hold seats) that need explicit user confirmation; passing the user's identity to downstream calls; limiting tool scope and validating arguments. [Spring AI: Tool calling](https://docs.spring.io/spring-ai/reference/api/tools.html), [Concept && Coding: Spring AI (Hindi playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c602ytEt7f_qVtlV7jNkdabL).
- 🛠️ **Do:** Add tools `searchShows(city, movie, date)`, `seatAvailability(showId)` and `holdSeats(showId, seatIds)` that call your services with the caller's token; `holdSeats` only runs after the user replies 'confirm'. Test: 'Find 2 seats for Dune tomorrow evening in Pune' -> options -> confirm -> hold created. Done when: logs show the tool calls and no hold happens without confirmation.

### Thursday 08 Apr · 60 min — RAG over FAQs and policies with PgVectorStore; evaluation
- 📚 **Learn:** ETL pipeline: document readers, token splitting, embeddings, PgVectorStore (pgvector on Postgres); retrieval advisors (`QuestionAnswerAdvisor` from the `spring-ai-vector-store-advisor` artifact / RetrievalAugmentationAdvisor), similarity threshold and top-k, metadata filters; grounding and citing sources; evaluating relevancy and faithfulness. [Spring AI: RAG](https://docs.spring.io/spring-ai/reference/api/retrieval-augmented-generation.html), [Spring AI: PGvector](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html), [Spring AI: Evaluation testing](https://docs.spring.io/spring-ai/reference/api/testing.html).
- 🛠️ **Do:** Write 10 short policy docs (cancellation, refunds, F&B, accessibility, kids, convenience fees) in Markdown; ingest them into PgVectorStore with metadata; answer 'Can I cancel 2 hours before the show?' citing the source doc; build a 10-question eval set and score answers with an evaluator. Done when: at least 8 of 10 answers are judged relevant and each cites a source.

### Friday 09 Apr · 60 min — MCP server exposing booking tools; LangChain4j awareness
- 📚 **Learn:** Model Context Protocol: hosts, clients, servers, tools/resources/prompts; Spring AI MCP server Boot starter with Streamable HTTP and server annotations; securing MCP endpoints; LangChain4j (AI Services, Spring Boot starter) as the other popular Java option. [Spring AI: MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html), [Spring AI: MCP server Boot starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html), [Dan Vega: MCP with Spring AI (video)](https://www.youtube.com/watch?v=MarSC2dFA9g).
- 🛠️ **Do:** Expose `searchShows`, `seatAvailability` and `getMyBookings` as MCP tools from `ai-assistant` (read-only), protected by a token; connect an MCP client (VS Code agent mode or MCP Inspector) and call each tool. Write a 10-line comparison of Spring AI vs LangChain4j in `docs/adr/ADR-004-ai-stack.md`. Done when: an external MCP client lists and successfully calls all 3 tools.

### Saturday 10 Apr · 60 min — BUILD: Ask TicketVerse v1 end to end
- 📚 **Learn:** Production concerns for LLM features: authentication, per-user rate limits, prompt-injection awareness (never let retrieved text trigger write tools), PII-safe logging, timeouts and fallbacks when the model is down, observability of model and tool calls, cost tracking. [Spring AI: Observability](https://docs.spring.io/spring-ai/reference/observability/index.html), [Spring AI: MCP server annotations](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-annotations-server.html).
- 🛠️ **Do:** Demo a scripted 6-turn conversation through the gateway: find a show, ask a policy question (RAG), pick seats, confirm (hold via tool), complete booking through the normal API, ask 'what did I book?'. Add a rate limit and a fallback message when the model times out; show model and tool spans in Jaeger or App Insights; tag `v6.0.0`. Done when: the demo passes twice and a video is linked in the README.

## 📦 Deliverable (by Saturday night)
`ai-assistant` service: ChatClient with switchable free providers, structured intent extraction, JDBC chat memory, guarded tool calling, PgVector RAG with eval set, MCP server, observability; Ask TicketVerse demo `v6.0.0`.

## ✅ Self-check (Sunday test preview)
- ChatClient vs ChatModel: what does the fluent API add?
- How does tool calling work end to end, and how did you prevent unwanted write actions?
- Walk through your RAG pipeline from Markdown files to a cited answer.
- How do you evaluate whether RAG answers are relevant and grounded?
- What is MCP, and how is an MCP tool different from a Spring AI @Tool?
- How do you handle model timeouts, rate limits and cost in production?
- What is prompt injection, and where could it hit TicketVerse?

## 🚀 Stretch (optional)
Rebuild `extractIntent` with [LangChain4j's Spring Boot integration](https://docs.langchain4j.dev/tutorials/spring-boot-integration) and compare code and accuracy.
