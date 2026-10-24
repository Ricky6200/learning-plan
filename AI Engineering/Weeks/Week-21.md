# 🤖 AI Engineering · Week 21 — Spring AI II: Tools, RAG and MCP

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** Tool calling, RAG and MCP in Spring AI turn TicketVerse into an AI-powered product and give you Java-side answers in AI system interviews.

## 🗓️ Sessions

### Monday 15 Mar · 45 min — Tool calling with @Tool on Spring beans
- 📚 **Learn:** `@Tool` and `@ToolParam` on bean methods, tool definitions sent to the model, `returnDirect`, tool context for passing user identity safely, exception handling; start with read-only tools. The model never runs code; your application does. Read: [Tool calling](https://docs.spring.io/spring-ai/reference/api/tools.html).
- 🛠️ **Do:** Create `ShowTools` with `@Tool searchShows(city, date, genre)` and `@Tool checkSeats(showId)` calling TicketVerse catalog and booking APIs (or stubs if not ready). Register them with `.tools(showTools)` and ask 'Any comedy shows in Pune on Saturday with 2 seats together?'. Done when: logs show both tools called with correct arguments and the answer uses tool data.

### Tuesday 16 Mar · 45 min — Embeddings, VectorStore and PgVectorStore
- 📚 **Learn:** `EmbeddingModel`, the portable `VectorStore` API, `PgVectorStore` (HNSW, cosine distance, dimensions must match your embedding model), metadata filter expressions. Read: [Vector databases](https://docs.spring.io/spring-ai/reference/api/vectordbs.html) and [PGvector store](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html); model option: [nomic-embed-text](https://ollama.com/library/nomic-embed-text) (768 dimensions).
- 🛠️ **Do:** Add the pgvector store starter, set dimensions to match your embedding model, and index 30 TicketVerse FAQ and policy snippets (refunds, cancellations, accessibility) with a `category` metadata field. Query with and without a filter. Done when: `similaritySearch` returns relevant snippets and the `category == 'refund'` filter works.

### Thursday 18 Mar · 45 min — ETL pipeline and RAG advisors
- 📚 **Learn:** ETL: `DocumentReader` (PDF, Markdown, Tika) -> `TokenTextSplitter` -> `VectorStore`; RAG via `QuestionAnswerAdvisor` (artifact `spring-ai-vector-store-advisor`) or the modular `RetrievalAugmentationAdvisor` (artifact `spring-ai-rag`: query transformers, retrievers, augmenters). Read: [ETL pipeline](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html) and [Retrieval Augmented Generation](https://docs.spring.io/spring-ai/reference/api/retrieval-augmented-generation.html).
- 🛠️ **Do:** Write policies as Markdown, ingest them via ETL at startup (idempotently), and add `POST /ai/ask-policy` using `QuestionAnswerAdvisor` with a similarity threshold; then try `RetrievalAugmentationAdvisor` with a query-rewrite transformer. Done when: 10 policy questions are answered with sources and an off-topic question gets a polite refusal.

### Friday 19 Mar · 45 min — MCP server and client with Spring AI; LangChain4j awareness
- 📚 **Learn:** Spring AI MCP Boot starters: a server (WebMVC, Streamable HTTP) exposing `@McpTool`/`@McpResource` methods, and a client starter that consumes external MCP servers as tools; LangChain4j is the alternative Java AI library (AI Services, tools, RAG). Read: [MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html), [MCP server annotations](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-annotations-server.html), [LangChain4j docs](https://docs.langchain4j.dev/).
- 🛠️ **Do:** Expose `searchShows` and `checkSeats` as MCP tools from `ticketverse-ai` over Streamable HTTP and call them from VS Code and MCP Inspector. Then add the MCP client starter so `ticketverse-ai` consumes one external server (your W13 `careerpilot-mcp` over HTTP or a reference server) as tools. Done when: VS Code chat searches TicketVerse shows through MCP and Spring logs show both server-side and client-side MCP tool calls.

### Saturday 20 Mar · 45 min — BUILD: Ask TicketVerse assistant with tools and RAG
- 📚 **Learn:** Assistant design: show search -> tools, policy questions -> RAG, booking -> not allowed yet; system prompt rules, memory per user, guardrails (`SafeGuardAdvisor`, input length limits), evaluation with Spring AI evaluators. Read: [Evaluation testing](https://docs.spring.io/spring-ai/reference/api/testing.html); Hindi option: [Chai aur Code Spring Boot + RAG project](https://www.youtube.com/watch?v=R8VBA_KtUo0).
- 🛠️ **Do:** Ship `POST /ai/assistant/{conversationId}` combining memory, tools, RAG advisor, logging and safeguards. Add 15 evaluation cases using `RelevancyEvaluator`/`FactCheckingEvaluator` or JUnit assertions on tool calls. Update Compose and the README with a sequence diagram. Done when: 12+ of 15 cases pass, booking requests are refused with guidance and tag `ticketverse-ai-v0.2` is pushed.

## 📦 Deliverable (by Saturday night)
`ticketverse-ai` v0.2: `@Tool` show search and seat check, PgVectorStore FAQ/policy RAG via ETL and advisors, MCP server exposure, assistant endpoint with memory and guardrails, 15-case evaluation.

## ✅ Self-check (Sunday test preview)
- How does Spring AI's `@Tool` work end to end?
- QuestionAnswerAdvisor vs RetrievalAugmentationAdvisor: when do you use which?
- How do you keep embedding dimensions consistent between the model and PgVectorStore?
- How do you expose Spring beans as MCP tools?
- How would you stop the assistant from booking tickets without confirmation?
- Spring AI vs LangChain4j: how would you choose for a team?

## 🚀 Stretch (optional)
Rebuild the assistant with LangChain4j AI Services in a branch and compare code size, features and testing support.
