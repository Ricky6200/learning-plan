# 🤖 AI Engineering · Week 16 — LLMOps: Observability, Prompts, CI Eval Gates

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Models, prompts and data change weekly in production AI. Traces, versioned prompts, eval gates and cost control are what make AI features safe to ship continuously. (AZ-104 exam week: keep sessions tight.)

## 🗓️ Sessions

### Monday 08 Feb · 45 min — Observability with Langfuse and OTel GenAI conventions
- 📚 **Learn:** Trace inputs/outputs (masked), model, parameters, tokens, cost, latency, tool calls, user and session IDs; sampling; OpenTelemetry GenAI semantic conventions (`gen_ai.*` attributes) for vendor-neutral telemetry; dashboards for p50/p95 latency, cost per day and error rate. Read: [OTel GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) and [Langfuse docs](https://langfuse.com/docs).
- 🛠️ **Do:** Make DocuMind and CareerPilot send traces with session/user IDs, model, tokens and cost, with PII masked by your W15 module. Build a Langfuse dashboard for p95 latency, cost per day and error rate. Done when: the dashboard shows 50+ traces from both apps and you can find the most expensive request.

### Tuesday 09 Feb · 45 min — Prompt management, versioning and rollback
- 📚 **Learn:** Prompts as versioned artifacts with labels (production, staging), templating, linking prompt versions to traces and eval results, instant rollback; Git-only prompts vs a prompt registry. Read: [Langfuse prompt management](https://langfuse.com/docs/prompt-management/overview).
- 🛠️ **Do:** Move DocuMind's answer prompt and CareerPilot's planner prompt into Langfuse prompt management (or a local `prompts/` registry with semver if offline). Fetch by label at runtime with a cached fallback and tag traces with the prompt version. Create v2 of one prompt. Done when: moving the `production` label from v1 to v2 changes behaviour without a redeploy and traces show the version.

### Thursday 11 Feb · 45 min — Evals in CI: a regression gate on pull requests
- 📚 **Learn:** Offline evals as tests: a small fast smoke set on every PR, a bigger nightly set, thresholds per metric; reduce judge flakiness (temperature 0, deterministic checks first, cached calls). Read: [Building and testing Python with GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/python), [promptfoo GitHub Action](https://www.promptfoo.dev/docs/integrations/github-action/), [DeepEval getting started](https://deepeval.com/docs/getting-started).
- 🛠️ **Do:** Create `.github/workflows/eval.yml`: on PR run unit tests, a 10-question DocuMind smoke eval (recall@5 plus a faithfulness check) and 10 attack cases; fail if recall@5 drops more than 0.05 below the committed baseline or the block rate falls under 90%. Store keys as GitHub secrets. Done when: a PR with a deliberately worse prompt is blocked.

### Friday 12 Feb · 45 min — Cost and latency optimization; feedback loops
- 📚 **Learn:** Levers: shorter prompts and context, `max_tokens`, prompt/context caching (stable prefix first), model routing and cascades, batching, streaming for time-to-first-token, semantic cache; A/B tests and user feedback (thumbs, edits). Read: [Building a GenAI platform (Chip Huyen)](https://huyenchip.com/2024/07/25/genai-platform.html) (router, gateway, cache) and the [Gemini context caching notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Caching.ipynb).
- 🛠️ **Do:** Implement a 2-tier cascade in DocuMind: a small fast model answers first; escalate to a stronger model when the retrieval score is low or a self-check fails. Add a thumbs up/down endpoint stored with the trace ID. Compare cost and quality vs a single model on 20 questions. Done when: a table shows savings and quality delta, and feedback appears on traces.

### Saturday 13 Feb · 45 min — BUILD: GitHub Actions eval gate for DocuMind and CareerPilot
- 📚 **Learn:** Release discipline: eval summary as a PR artifact or comment, committed baselines, nightly full evals, cost-budget alerts, a written gate policy. Reference: [LLM evals FAQ](https://hamel.dev/blog/posts/evals-faq/) (CI and judges sections).
- 🛠️ **Do:** Finish the pipeline: the PR job (smoke evals, attack suite, unit tests) publishes a Markdown summary; a nightly job runs the full 30-item DocuMind and 12-scenario CareerPilot evals and uploads reports. Document the policy in `LLMOPS.md`. Done when: two PRs demonstrate a pass and a fail, and tag `llmops-v1` is pushed.

## 📦 Deliverable (by Saturday night)
Langfuse dashboards for both apps, labelled prompt versions, `eval.yml` PR gate plus nightly evals, cascade routing with measured savings, feedback capture and `LLMOPS.md`.

## ✅ Self-check (Sunday test preview)
- What would you log for every LLM call, and what must you never log?
- How do you version prompts and roll back safely?
- Design an eval gate for a RAG app: what runs per PR vs nightly?
- Explain model cascades/routing and how you would prove they help.
- How does prompt caching work, and how should prompts be structured to benefit?
- What are the OpenTelemetry GenAI semantic conventions and why use them?

## 🚀 Stretch (optional)
Run an A/B test routing 50% of traffic to prompt v2 for a week, collect feedback scores and decide with data.
