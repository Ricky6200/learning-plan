# 🤖 AI Engineering · Week 23 — Spring AI I: ChatClient and Structured Output

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Java + Spring AI lets you add AI to the backends you already maintain, a rare and valuable combination in the Indian market where most AI engineers know only Python. The AI track owns the `ticketverse-ai` service; Java W27 later adds the platform hooks (gateway, JWT relay, Kafka topics).

## 🗓️ Sessions

### Monday 29 Mar · 45 min — Spring AI 2.x architecture and your first ChatClient
- 📚 **Learn:** Spring AI 2.0.x runs on Spring Boot 4.0/4.1: ChatModel and EmbeddingModel abstractions, the fluent `ChatClient` (like the RestClient of Java W13), auto-configured starters, provider swap via properties. LLM calls stay in Codespaces, because free model APIs are blocked on the company network. Read: [Spring AI getting started](https://docs.spring.io/spring-ai/reference/getting-started.html). Optional: [ChatClient API](https://docs.spring.io/spring-ai/reference/api/chatclient.html).
- 🛠️ **Do:** Open the TicketVerse repo in a 2-core codespace (devcontainer with the Java 25 feature). Generate `ticketverse-ai` on [start.spring.io](https://start.spring.io/) (Boot 4.1.x, Java 25, Web, Actuator, Spring AI Ollama starter for zero-key local runs) and add `GET /ai/hello?q=` using an injected `ChatClient.Builder`. Done when: the endpoint returns your local model's answer and `./mvnw verify` passes.

### Tuesday 30 Mar · 45 min — Prompt templates, system messages, options and streaming
- 📚 **Learn:** `PromptTemplate` with variables, system vs user messages, a default system prompt on the builder, per-request options (model, temperature, max tokens), streaming via `.stream().content()`. Primer: that returns a `Flux<String>` (Project Reactor), a lazy asynchronous stream of tokens that Spring MVC can send as `text/event-stream`; Java W27 covers Reactor properly. Read: [Prompts](https://docs.spring.io/spring-ai/reference/api/prompt.html). Optional: [Reactor reference](https://projectreactor.io/docs/core/release/reference/) (introduction).
- 🛠️ **Do:** Add `POST /ai/event-blurb` filling a template (event name, city, date, genre) into a 50-word promo, with the template in `src/main/resources/prompts/`. Add `GET /ai/stream?q=` returning server-sent events from the `Flux`. Done when: editing the template needs no code change and `curl -N` shows tokens arriving progressively.

### Thursday 01 Apr · 45 min — Structured output: mapping responses to Java records
- 📚 **Learn:** `.entity(MyRecord.class)` maps model output to records and lists via a generated JSON schema; provider-native structured output (`useProviderStructuredOutput()`) when supported; add Bean Validation and one retry. Compare with your W7 pydantic version. Read: [Structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html).
- 🛠️ **Do:** Create `record EventQuery(String city, LocalDate from, LocalDate to, List<String> genres, Integer maxPrice)` and `POST /ai/parse-query` turning 'comedy shows in Pune next weekend under 800' into it. Add validation, one retry and 5 JUnit tests with a Mockito-mocked or recorded model response. Done when: 5/5 sample queries map correctly and the tests pass offline.

### Friday 02 Apr · 45 min — Advisors, chat memory, cloud providers and observability
- 📚 **Learn:** Advisors intercept model calls (logging, memory, RAG, safeguards); `MessageChatMemoryAdvisor` with `MessageWindowChatMemory` and a JDBC repository; cloud providers via the OpenAI starter pointed at Groq or the Google GenAI starter for Gemini; Micrometer observations with `gen_ai` keys (Micrometer from Java W19). Read: [Advisors](https://docs.spring.io/spring-ai/reference/api/advisors.html). Optional: [Chat memory](https://docs.spring.io/spring-ai/reference/api/chat-memory.html).
- 🛠️ **Do:** Add `SimpleLoggerAdvisor` and per-conversation memory backed by Postgres (JDBC chat memory repository), exposed as `POST /ai/chat/{conversationId}`. Add a `cloud` profile using Groq ([Groq chat](https://docs.spring.io/spring-ai/reference/api/chat/groq-chat.html)) with the key from a Codespaces secret. Done when: memory survives a restart and switching profiles changes the provider without code changes.

### Saturday 03 Apr · 45 min — BUILD: ticketverse-ai service skeleton with chat and structured output
- 📚 **Learn:** Service design inside TicketVerse: one AI service, `ticketverse-ai`, behind the gateway; ports-and-adapters; profiles `local` (Ollama) and `cloud` (Groq/Gemini); timeouts and fallbacks with the Resilience4j you learned in Java W19. Examples: [spring-ai-examples](https://github.com/spring-projects/spring-ai-examples). Optional: [Spring AI for Beginners (Microsoft)](https://github.com/microsoft/Spring-AI-for-Beginners).
- 🛠️ **Do:** Ship `ticketverse-ai` v0.1: chat with memory, `/ai/parse-query`, the streaming endpoint, a logging advisor, two profiles, a Dockerfile and tests (mocked model or Testcontainers), plus a `ticketverse-ai` entry in the TicketVerse Compose file. On the 2-core codespace start only `ticketverse-ai` and Postgres. Done when: both containers run via Compose, tests are green and tag `ticketverse-ai-v0.1` is pushed.

## 📦 Deliverable (by Saturday night)
`ticketverse/ticketverse-ai` v0.1 (Spring Boot 4.1 + Spring AI 2.0): ChatClient endpoints, external prompt templates, streaming, record mapping, JDBC chat memory, local/cloud profiles, Dockerfile and a Compose entry.

## ✅ Self-check (Sunday test preview)
- What is `ChatClient`, and how does it relate to `ChatModel`?
- What does `.stream().content()` return, and how does it reach the browser?
- How does `.entity()` produce structured output in Spring AI?
- What are advisors? Name three built-in ones.
- How do you implement per-conversation memory that survives restarts?
- How do you switch from Ollama to a cloud model without code changes?

## 🚀 Stretch (optional)
Implement one endpoint with [LangChain4j](https://docs.langchain4j.dev/) AI Services in a branch and compare the API style, or add the [Google GenAI chat](https://docs.spring.io/spring-ai/reference/api/chat/google-genai-chat.html) profile for Gemini.
