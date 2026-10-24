# 🤖 AI Engineering · Week 20 — Spring AI I: ChatClient and Structured Output

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Java + Spring AI lets you add AI to the backends you already maintain, a rare and valuable combination in the Indian market where most AI engineers know only Python.

## 🗓️ Sessions

### Monday 08 Mar · 45 min — Spring AI 2.x architecture and your first ChatClient
- 📚 **Learn:** Spring AI 2.0.x runs on Spring Boot 4.0/4.1: ChatModel and EmbeddingModel abstractions, the fluent `ChatClient` (like RestClient), auto-configured starters, provider swap via properties. Read: [Spring AI getting started](https://docs.spring.io/spring-ai/reference/getting-started.html) and [ChatClient API](https://docs.spring.io/spring-ai/reference/api/chatclient.html); English video: [Dan Vega Spring AI playlist](https://www.youtube.com/playlist?list=PLZV0a2jwt22uoDm3LNDFvN6i2cAVU_HTH).
- 🛠️ **Do:** Generate `ticketverse-ai` on [start.spring.io](https://start.spring.io/) (Boot 4.1.x, Java 25, Web, Actuator, Spring AI Ollama starter for zero-key local runs). Add `GET /ai/hello?q=` using an injected `ChatClient.Builder`. Done when: the endpoint returns a local model's answer and the project builds with `./mvnw verify`.

### Tuesday 09 Mar · 45 min — Prompt templates, system messages, options and streaming
- 📚 **Learn:** `PromptTemplate` with variables, system vs user messages, default system prompt on the builder, per-request options (model, temperature, max tokens), streaming as `Flux<String>` via `.stream().content()`. Read: [Prompts](https://docs.spring.io/spring-ai/reference/api/prompt.html) and the streaming section of [ChatClient API](https://docs.spring.io/spring-ai/reference/api/chatclient.html).
- 🛠️ **Do:** Add `POST /ai/event-blurb` filling a template (event name, city, date, genre) into a 50-word promo, with the template in `src/main/resources/prompts/`. Add `GET /ai/stream?q=` returning server-sent events. Done when: editing the template needs no code change and `curl -N` shows tokens arriving progressively.

### Thursday 11 Mar · 45 min — Structured output: mapping responses to Java records
- 📚 **Learn:** `.entity(MyRecord.class)` maps model output to records and lists via a generated JSON schema; provider-native structured output (`useProviderStructuredOutput()`) when supported; add Bean Validation and a retry. Read: [Structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html) and compare with your W5 pydantic version.
- 🛠️ **Do:** Create `record EventQuery(String city, LocalDate from, LocalDate to, List<String> genres, Integer maxPrice)` and `POST /ai/parse-query` turning 'comedy shows in Pune next weekend under 800' into it. Add validation, one retry and 5 JUnit tests with a mocked or recorded model response. Done when: 5/5 sample queries map correctly and tests pass offline.

### Friday 12 Mar · 45 min — Advisors, chat memory, cloud providers and observability
- 📚 **Learn:** Advisors intercept model calls (logging, memory, RAG, safeguards); `MessageChatMemoryAdvisor` with `MessageWindowChatMemory` and a JDBC repository; cloud providers via the OpenAI starter (Groq, Azure/Foundry) or the Google GenAI starter (Gemini); Micrometer observations with `gen_ai` keys. Read: [Advisors](https://docs.spring.io/spring-ai/reference/api/advisors.html), [Chat memory](https://docs.spring.io/spring-ai/reference/api/chat-memory.html), [Observability](https://docs.spring.io/spring-ai/reference/observability/index.html).
- 🛠️ **Do:** Add `SimpleLoggerAdvisor` and per-conversation memory backed by Postgres (JDBC chat memory repository), exposed as `POST /ai/chat/{conversationId}`. Add a `cloud` profile using Groq or Gemini with keys from env vars. Check Actuator metrics for `gen_ai` observations. Done when: memory survives a restart and switching profiles changes the provider without code changes.

### Saturday 13 Mar · 45 min — BUILD: ticketverse-ai service skeleton with chat and structured output
- 📚 **Learn:** Service design inside TicketVerse: a separate `ticketverse-ai` microservice behind the gateway, ports-and-adapters, profiles `local` (Ollama) and `cloud` (Gemini/Groq), timeouts and fallbacks with Resilience4j from your Java track. Examples: [spring-ai-examples](https://github.com/spring-projects/spring-ai-examples) and [Spring AI for Beginners (Microsoft)](https://github.com/microsoft/Spring-AI-for-Beginners).
- 🛠️ **Do:** Ship `ticketverse-ai` v0.1: chat with memory, `/ai/parse-query`, streaming endpoint, logging advisor, two profiles, Dockerfile, tests (mocked model or Testcontainers) and README. Add it to the TicketVerse Docker Compose. Done when: it runs in Compose next to the other services, tests are green and tag `ticketverse-ai-v0.1` is pushed.

## 📦 Deliverable (by Saturday night)
`ticketverse/ticketverse-ai` v0.1 (Spring Boot 4.1 + Spring AI 2.0): ChatClient endpoints, external prompt templates, streaming, record mapping, JDBC chat memory, observability, local/cloud profiles and a Dockerfile.

## ✅ Self-check (Sunday test preview)
- What is `ChatClient`, and how does it relate to `ChatModel`?
- How does `.entity()` produce structured output in Spring AI?
- What are advisors? Name three built-in ones.
- How do you implement per-conversation memory that survives restarts?
- How do you switch from Ollama to a cloud model without code changes?
- What observability does Spring AI provide out of the box?

## 🚀 Stretch (optional)
Implement one endpoint with [LangChain4j](https://docs.langchain4j.dev/) AI Services in a branch and compare the API style.
