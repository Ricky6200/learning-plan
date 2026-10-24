# 🤖 AI Engineering · Week 11 — Agents I: Tool Loops From Scratch

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** Agentic features (tools, multi-step reasoning, memory) dominate 2026 AI job descriptions. Knowing the raw loop lets you use any framework safely and debug it under pressure.

## 🗓️ Sessions

### Monday 04 Jan · 45 min — Agent vs workflow and the augmented LLM
- 📚 **Learn:** Workflows follow predefined code paths; agents let the LLM choose steps. Start with the simplest solution; the augmented LLM = model + retrieval + tools + memory; know when NOT to build an agent. Read: [Building effective agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents); skim [A practical guide to building agents (OpenAI, PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- 🛠️ **Do:** Create `07-careerpilot/design.md`: list 6 CareerPilot tasks (parse JD, skill gap, prep plan, company research, mock interview, track applications) and classify each as single LLM call, workflow or agent with a one-line justification. Done when: the table exists and at least two tasks are deliberately not agents.

### Tuesday 05 Jan · 45 min — Workflow patterns: chaining, routing, parallelization, evaluator-optimizer
- 📚 **Learn:** Prompt chaining with gates, routing (classify then dispatch), parallelization (sectioning or voting), orchestrator-workers, evaluator-optimizer loops; each trades latency and cost for quality. Re-read the patterns section of [Building effective agents](https://www.anthropic.com/research/building-effective-agents); see code shapes in [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) (read only).
- 🛠️ **Do:** Implement 3 patterns in plain Python with `llmkit`: routing (message to jd_parse, prep_plan or chit_chat), parallelization (3 concurrent skill-gap critiques via `asyncio.gather` plus a vote) and evaluator-optimizer (draft, critique, revise at most twice). Done when: each pattern runs on 3 inputs and you log calls and tokens per pattern.

### Thursday 07 Jan · 45 min — ReAct and a tool-calling agent loop without frameworks
- 📚 **Learn:** ReAct = reason, act, observe until done; native tool calling replaces text parsing; loop guardrails: max steps, tool allow-list, argument validation, errors returned as observations, final-answer detection. Read: [ReAct paper](https://arxiv.org/abs/2210.03629) (abstract, figure 1) and [LLM Powered Autonomous Agents (Lilian Weng)](https://lilianweng.github.io/posts/2023-06-23-agent/) (planning, tool use).
- 🛠️ **Do:** Write `agent.py` (about 80 lines, no framework): call the model with tool schemas, execute requested tools, append results, stop on a final answer or after 6 steps. Tools: `search_jobs(query)` over local JSON, `get_skill_gap(job_id)`, `calc(expression)` with safe parsing. Done when: a 3-step task (find Java + AI jobs in Bengaluru, then my gap for the best one) completes with a printed trace.

### Friday 08 Jan · 45 min — Agent memory: short-term, long-term, context engineering
- 📚 **Learn:** Short-term memory (message window, running summary, trimming) vs long-term memory (profile facts, episodic logs, vector recall); context engineering: give the model the smallest high-signal context. Read: [LangChain memory concepts](https://docs.langchain.com/oss/python/concepts/memory) and [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).
- 🛠️ **Do:** Add a message window plus running summary, and a long-term `profile.json` the agent reads and updates through `remember(fact)` and `recall(topic)` tools (simple embedding search). Set a token budget per turn. Done when: a fresh session recalls your target role and skills, and prompts stay under your budget.

### Saturday 09 Jan · 45 min — BUILD: from-scratch CareerPilot agent with three tools
- 📚 **Learn:** Tool design: clear names and descriptions, typed arguments, small outputs, idempotency, error messages the model can act on; log every step for debugging. Read: [Writing effective tools for agents (Anthropic)](https://www.anthropic.com/research/writing-tools-for-agents).
- 🛠️ **Do:** Ship `07-careerpilot/agent_v0`: CLI agent with `search_jobs`, `skill_gap` and `save_application` (SQLite), max-steps limit, tool allow-list, pydantic argument validation and JSONL traces. Write 8 scenario tests with expected tool sequences and run them. Done when: 6+ of 8 scenarios pass, traces show every step, and tag `v0.1-careerpilot-scratch` is pushed.

## 📦 Deliverable (by Saturday night)
`07-careerpilot/`: agent-vs-workflow design doc, three workflow patterns, from-scratch tool loop with memory, 8 scenario tests and JSONL traces.

## ✅ Self-check (Sunday test preview)
- Workflow vs agent: how do you decide? Give an example of each.
- Describe the tool-calling loop and its stop conditions.
- What are the orchestrator-workers and evaluator-optimizer patterns?
- How do you prevent infinite loops and runaway cost in agents?
- Short-term vs long-term memory: how would you implement each?
- What makes a tool description good for an LLM?

## 🚀 Stretch (optional)
Complete Unit 1 of the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction) and compare its agent loop with yours.
