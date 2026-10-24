# 🤖 AI Engineering · Week 04 — LLM APIs and the TerminalGPT Boss

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Calling models reliably (streaming, retries, cost control, secrets) is the daily bread of an AI backend engineer and a common first task in AI coding interviews.

## 🗓️ Sessions

### Monday 16 Nov · 45 min — Provider landscape and your first free API calls
- 📚 **Learn:** Closed vs open-weight models; providers (OpenAI, Anthropic, Google, Azure OpenAI in Microsoft Foundry, Groq, OpenRouter, local Ollama); the OpenAI-compatible Chat Completions shape as lingua franca. Note: GitHub Models was retired on 30 Jul 2026. Read: [openai-python README](https://github.com/openai/openai-python) (Usage), [Gemini OpenAI-compatibility notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb).
- 🛠️ **Do:** Create free keys (Gemini in Google AI Studio, Groq console) and install [Ollama](https://ollama.com/download) with a 3-4B model (e.g., `llama3.2:3b`). Store keys in a git-ignored `.env`, load with python-dotenv, and call all three through the `openai` client by switching `base_url` and `model`. Done when: one script prints answers from 3 providers and `git status` shows `.env` is untracked.

### Tuesday 17 Nov · 45 min — Roles, multi-turn state and streaming
- 📚 **Learn:** Messages with roles (system/developer, user, assistant, tool); the API is stateless so you resend history; streaming arrives as server-sent chunks; `max_tokens`, `stop`, temperature. Read: [openai-python streaming](https://github.com/openai/openai-python#streaming-responses) and [Ollama OpenAI compatibility](https://ollama.com/blog/openai-compatibility) (same client, local model).
- 🛠️ **Do:** Write `chat_loop.py`: keep a `messages` list, stream tokens to the terminal as they arrive, support `/reset` and `/system <text>`, and trim history to the last N turns. Done when: a 5-turn chat remembers your name, output streams visibly, and `/reset` forgets it.

### Thursday 19 Nov · 45 min — Tokens, cost, retries, rate limits, timeouts
- 📚 **Learn:** Usage fields (prompt/completion tokens), cost = tokens x price; 429 vs 5xx, exponential backoff with jitter, client timeouts, fallbacks, idempotency. Read: [Counting tokens with tiktoken](https://developers.openai.com/cookbook/examples/how_to_count_tokens_with_tiktoken) and [tenacity](https://tenacity.readthedocs.io/) (retry, wait_exponential, stop_after_attempt).
- 🛠️ **Do:** Add a `CostMeter` that reads `usage` from responses (fall back to a tiktoken estimate when streams omit it) with prices from a `prices.toml` you fill in. Wrap calls in tenacity retries (3 attempts, exponential backoff, only on 429/5xx/timeouts). Simulate failure with a wrong `base_url`. Done when: each turn prints tokens and cost, and a forced failure retries then shows a clean error.

### Friday 20 Nov · 45 min — Provider abstraction, secrets hygiene, battle skeleton
- 📚 **Learn:** A thin provider layer (config-driven base_url, model, key env var) is dependency inversion, like a Java interface. Secrets: `.env` + `.gitignore`, never log keys, rotate on leak. Read: [python-dotenv](https://pypi.org/project/python-dotenv/) and [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/).
- 🛠️ **Do:** Create a reusable `llmkit/` package: `Settings` (pydantic-settings), `get_client(provider)` for gemini/groq/ollama/openrouter, and `chat(messages, stream=True)`. Write the TerminalGPT skeleton with TODOs and 3 pytest tests using a fake client. Done when: `uv run pytest` passes offline and switching provider is a one-line config change.

### Saturday 21 Nov · 45 min — BOSS BATTLE: TerminalGPT CLI chatbot in 45 minutes
- 📚 **Learn:** Rules: 45-minute timer, start from Friday's skeleton, docs allowed, no AI code generation, commit every 15 minutes. Scoring /100: streaming 25, memory 25, provider switch 20, cost meter 20, error handling 10. UI help: [Rich](https://rich.readthedocs.io/en/latest/).
- 🛠️ **Do:** Ship `03-terminalgpt`: streaming replies, conversation memory with `/reset`, `/model <provider>` hot switch, live token and cost meter, graceful 429/timeout handling and `/save` transcript to JSON. Record a 60-second terminal demo. Done when: you score 80+ on the rubric, tag `v1.0-terminalgpt` is pushed and the README has setup steps plus the demo.

## 📦 Deliverable (by Saturday night)
`03-terminalgpt/` tagged v1.0 plus the reusable `llmkit/` package (providers, settings, cost meter, retries) and a demo recording.

## ✅ Self-check (Sunday test preview)
- Why is the chat API stateless, and how do you implement conversation memory?
- How does streaming work over HTTP, and why does it improve perceived latency?
- Estimate monthly cost for 10k users x 20 messages/day x 800 tokens at a given price.
- Which errors should you retry, and why add jitter to backoff?
- How do you keep API keys out of Git, logs and screenshots?
- What does 'OpenAI-compatible API' mean, and where does compatibility break down?

## 🚀 Stretch (optional)
Add `/compare` that sends one prompt to two providers concurrently with asyncio and shows latency and cost side by side.
