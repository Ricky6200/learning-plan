# 🤖 AI Engineering · Week 14 — Agents I: Tool Loops From Scratch

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Agentic features (tools, multi-step reasoning, memory) dominate 2026 AI job descriptions. Knowing the raw loop lets you use any framework safely and debug it under pressure. (Tue 26 Jan is Republic Day: a light session.)

## 🗓️ Sessions

### Monday 25 Jan · 45 min — Agent vs workflow and the augmented LLM
- 📚 **Learn:** Workflows follow predefined code paths; agents let the LLM choose the steps. Start with the simplest solution; the augmented LLM = model + retrieval + tools + memory; know when NOT to build an agent. Read: [Building effective agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents). Optional: [A practical guide to building agents (OpenAI, PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf).
- 🛠️ **Do:** Create `10-careerpilot/design.md`: list 6 CareerPilot tasks (parse JD, skill gap, prep plan, company research, mock interview, track applications) and classify each as single LLM call, workflow or agent with a one-line justification. Done when: the table exists and at least two tasks are deliberately not agents.

### Tuesday 26 Jan · 45 min — Workflow patterns: routing and parallelization (light)
- 📚 **Learn:** Prompt chaining with gates, routing (classify, then dispatch), parallelization (sectioning or voting), orchestrator-workers and evaluator-optimizer loops; each trades latency and cost for quality. Re-read the patterns section of [Building effective agents](https://www.anthropic.com/research/building-effective-agents). Optional: code shapes in [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) (read only).
- 🛠️ **Do:** Republic Day, so 20 minutes: implement routing in plain Python with `llmkit` (a message goes to `jd_parse`, `prep_plan` or `chit_chat`) and run it on 3 inputs, logging calls and tokens. Done when: all 3 inputs reach the right handler and the log shows calls and tokens per input.

### Thursday 28 Jan · 45 min — ReAct and a tool-calling agent loop without frameworks
- 📚 **Learn:** ReAct = reason, act, observe until done; native tool calling replaces text parsing; loop guardrails: max steps, tool allow-list, argument validation, errors returned as observations, final-answer detection. Read: [ReAct paper](https://arxiv.org/abs/2210.03629) (abstract and figure 1). Optional: [LLM Powered Autonomous Agents (Lilian Weng)](https://lilianweng.github.io/posts/2023-06-23-agent/) (planning, tool use).
- 🛠️ **Do:** Write `agent.py` (about 80 lines, no framework): call the model with tool schemas, execute requested tools, append results, stop on a final answer or after 6 steps. Tools: `search_jobs(query)` over local JSON, `get_skill_gap(job_id)`, `calc(expression)` with safe parsing. Done when: a 3-step task (find Java + AI jobs in Bengaluru, then my gap for the best one) completes with a printed trace.

### Friday 29 Jan · 45 min — Agent memory: short-term, long-term, context engineering
- 📚 **Learn:** Short-term memory (message window, running summary, trimming) vs long-term memory (profile facts, episodic logs, vector recall); context engineering: give the model the smallest high-signal context. Read: [Effective context engineering for AI agents (Anthropic)](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents). Optional: [LangChain memory concepts](https://docs.langchain.com/oss/python/concepts/memory).
- 🛠️ **Do:** Add a message window plus running summary, and a long-term `profile.json` the agent reads and updates through `remember(fact)` and `recall(topic)` tools (simple embedding search). Set a token budget per turn. Done when: a fresh session recalls your target role and skills, and prompts stay under your budget.

### Saturday 30 Jan · 45 min — BUILD: from-scratch CareerPilot agent with three tools
- 📚 **Learn:** Tool design: clear names and descriptions, typed arguments, small outputs, idempotency, error messages the model can act on; log every step for debugging. Read: [Writing effective tools for agents (Anthropic)](https://www.anthropic.com/research/writing-tools-for-agents).
- 🛠️ **Do:** Ship `10-careerpilot/agent_v0`: CLI agent with `search_jobs`, `skill_gap` and `save_application` (SQLite, using your W8 SQL), max-steps limit, tool allow-list, pydantic argument validation and JSONL traces. Write 8 scenario tests with expected tool sequences and run them. Done when: 6+ of 8 scenarios pass, traces show every step, and tag `v0.1-careerpilot-scratch` is pushed.

## 📦 Deliverable (by Saturday night)
`10-careerpilot/`: agent-vs-workflow design doc, a routing workflow, from-scratch tool loop with memory, 8 scenario tests and JSONL traces.

## ✅ Self-check (Sunday test preview)
- Workflow vs agent: how do you decide? Give an example of each.
- Describe the tool-calling loop and its stop conditions.
- What are the orchestrator-workers and evaluator-optimizer patterns?
- How do you prevent infinite loops and runaway cost in agents?
- Short-term vs long-term memory: how would you implement each?
- What makes a tool description good for an LLM?

## 🚀 Stretch (optional)
Implement the other two patterns from Tuesday (parallelization with `asyncio.gather` + a vote, evaluator-optimizer with at most two revisions), or complete Unit 1 of the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction).
