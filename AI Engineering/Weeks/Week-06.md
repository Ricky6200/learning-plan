# 🤖 AI Engineering · Week 06 — LLM APIs, Codespaces and TerminalGPT

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Calling models reliably (streaming, retries, cost control, secrets) is the daily bread of an AI backend engineer and a common first task in AI coding interviews. From this week LLM calls run in GitHub Codespaces on your personal laptop, because free LLM APIs are blocked on the company network.

## 🗓️ Sessions

### Monday 30 Nov · 45 min — Codespaces setup and your first free API call
- 📚 **Learn:** A dev container (`.devcontainer/devcontainer.json`) defines your codespace's image, features (Docker-in-Docker, Node) and setup commands, so every rebuild is identical. Keys live in Codespaces secrets, exposed as environment variables, never in files. Budget: the free plan gives about 120 core-hours and 15 GB-month of storage per month, and a 2-core machine uses 2 core-hours per hour; keep one codespace, stop it after each session, and install PyTorch only from the CPU-only index (W9) because the default CUDA wheels add several GB. Read: [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers). Optional: [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces).
- 🛠️ **Do:** On the personal laptop: create free Gemini (Google AI Studio) and Groq keys and save them as Codespaces secrets for `ai-engineering-lab`. Add a devcontainer (image `mcr.microsoft.com/devcontainers/python:3.13`, docker-in-docker and node features, `postCreateCommand: pip install uv`), set your idle timeout to 10 minutes and open a codespace. Call Gemini through the `openai` client via its OpenAI-compatible `base_url`. Done when: a script prints a Gemini answer, no key is in any file, and the billing page shows your usage.

### Tuesday 01 Dec · 45 min — Roles, multi-turn state and streaming
- 📚 **Learn:** Messages with roles (system/developer, user, assistant, tool); the API is stateless, so you resend history; streaming arrives as chunks you iterate over (a generator, W3); `max_tokens`, `stop`, temperature. The OpenAI-compatible Chat Completions shape is the common language of Gemini, Groq, OpenRouter and Ollama. Read: [openai-python README](https://github.com/openai/openai-python) (usage and streaming responses). Optional: [Gemini OpenAI-compatibility notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_OpenAI_Compatibility.ipynb).
- 🛠️ **Do:** In a second terminal install Ollama for Friday ([Linux install](https://ollama.com/download/linux), then `ollama serve &` and `ollama pull llama3.2:1b`). Meanwhile write `chat_loop.py`: keep a `messages` list, stream tokens to the terminal as they arrive, support `/reset` and `/system <text>`, and trim history to the last N turns. Done when: a 5-turn chat remembers your name, output streams visibly, and `/reset` forgets it.

### Thursday 03 Dec · 45 min — Tokens, cost, retries, rate limits, timeouts
- 📚 **Learn:** Usage fields (prompt/completion tokens), cost = tokens x price; 429 vs 5xx, exponential backoff with jitter, client timeouts; retry only operations that are safe to repeat (the idempotency idea from SD W2). Read: [tenacity docs](https://tenacity.readthedocs.io/) (retry, wait_exponential, stop_after_attempt). Optional: [Counting tokens with tiktoken](https://developers.openai.com/cookbook/examples/how_to_count_tokens_with_tiktoken).
- 🛠️ **Do:** Add a `CostMeter` that reads `usage` from responses (fall back to a tiktoken estimate when streams omit it) with prices from a `prices.toml` you fill in. Wrap calls in tenacity retries (3 attempts, exponential backoff, only on 429/5xx/timeouts). Simulate failure with a wrong `base_url`. Done when: each turn prints tokens and cost, and a forced failure retries, then shows a clean error.

### Friday 04 Dec · 45 min — Provider abstraction: llmkit with Gemini, Groq and Ollama
- 📚 **Learn:** A thin provider layer (config-driven base_url, model and key variable) is dependency inversion behind a small interface, the same idea as coding to a Java interface (Java W3 Tue). Add a fallback list: on 429 or timeout, try the next provider. Secrets come from environment variables only; never log keys; rotate a leaked key at once. Read: [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) (usage). Optional: [Ollama OpenAI compatibility](https://ollama.com/blog/openai-compatibility).
- 🛠️ **Do:** Create a reusable `llmkit/` package: `Settings` (pydantic-settings), `get_client(provider)` for gemini/groq/ollama/openrouter, `chat(messages, stream=True)` and `chat_with_fallback(providers, messages)`. Write the TerminalGPT skeleton with TODOs and 3 pytest tests using a fake client (monkeypatch), one of which proves a fake 429 falls back to the next provider. Done when: `uv run pytest` passes offline and switching provider is a one-line config change.

### Saturday 05 Dec · 45 min — BUILD: TerminalGPT CLI chatbot
- 📚 **Learn:** Ship-it rules: 45-minute timer, start from Friday's skeleton, docs allowed, no AI code generation, commit every 15 minutes. Self-score /100: streaming 25, memory 25, provider switch 20, cost meter 20, error handling 10. UI help: [Rich](https://rich.readthedocs.io/en/latest/) (console and live display).
- 🛠️ **Do:** Ship `05-terminalgpt`: streaming replies, conversation memory with `/reset`, `/model <provider>` hot switch, live token and cost meter, graceful 429/timeout handling and `/save` transcript to JSON; add 5 offline tests (8+ in total). Stop the codespace when you finish. Done when: you self-score 80+, tag `v1.0-terminalgpt` is pushed and the README has setup steps plus a 60-second terminal recording or GIF.

## 📦 Deliverable (by Saturday night)
`05-terminalgpt/` tagged v1.0 with 8+ offline tests, the reusable `llmkit/` package (providers, settings, cost meter, retries, fallback), a working devcontainer and Codespaces secrets.

## ✅ Self-check (Sunday test preview)
- Why is the chat API stateless, and how do you implement conversation memory?
- How does streaming work over HTTP, and why does it improve perceived latency?
- Estimate monthly cost for 10k users x 20 messages/day x 800 tokens at a given price.
- Which errors should you retry, and why add jitter to backoff?
- How do you keep API keys out of Git, logs and screenshots, and how do Codespaces secrets help?
- What does 'OpenAI-compatible API' mean, and where does compatibility break down?
- How do you keep your codespace inside the free monthly quota?

## 🚀 Stretch (optional)
Add `/compare` that sends one prompt to two providers concurrently with asyncio and shows latency and cost side by side.
