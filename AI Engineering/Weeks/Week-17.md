# 🤖 AI Engineering · Week 17 — Multi-Agent Systems and Framework Tour

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Interviewers ask when multi-agent designs are worth the cost and how to evaluate them. Knowing more than one framework lets you pick the right tool instead of the trendy one.

## 🗓️ Sessions

### Monday 15 Feb · 45 min — Multi-agent patterns: supervisor, hierarchical, handoffs
- 📚 **Learn:** Single agent + tools first; supervisor (central router), hierarchical teams, handoffs (an agent transfers control), subagents exposed as tools; costs: multiplied tokens, context sharing, error propagation. Read: [LangChain multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent). Optional: [How we built our multi-agent research system (Anthropic)](https://www.anthropic.com/research/multi-agent-research-system).
- 🛠️ **Do:** Design CareerPilot v1 in `multi_agent.md`: researcher (company and role research), planner (prep plan) and interviewer (mock Q&A with feedback) under a supervisor. Define each agent's tools, inputs, outputs and handoff rules, and estimate tokens per run vs a single agent. Done when: the doc has a Mermaid diagram and a 'why not single-agent?' justification.

### Tuesday 16 Feb · 45 min — Implement supervisor and subagents in LangGraph
- 📚 **Learn:** Supervisor as a routing node or subagents-as-tools; handoffs with `Command(goto=..., update=...)`; shared vs private state; give each agent only the tools it needs. Read: [Subagents: personal assistant tutorial](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant). Optional: [Handoffs: customer support tutorial](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs-customer-support).
- 🛠️ **Do:** Implement supervisor + researcher + planner in LangGraph (the interviewer comes Thursday). The researcher calls your MCP server through a small wrapper that turns the v2 `Client`'s tools into LangChain `StructuredTool`s; the planner reuses the W15 plan subgraph. Log which agent acted at each step. Done when: 'prepare me for a backend role at Company X' routes researcher -> planner -> supervisor final answer.

### Thursday 18 Feb · 45 min — Framework tour: the OpenAI Agents SDK
- 📚 **Learn:** Compare primitives across frameworks: OpenAI Agents SDK (agents, handoffs, guardrails, sessions, tracing), Microsoft Agent Framework 1.x (agents + graph workflows; successor to Semantic Kernel and AutoGen; you use it in W25), Pydantic AI (typed agents and outputs), CrewAI (role-based crews, awareness). Read: [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) (quickstart). Optional: [Pydantic AI](https://pydantic.dev/docs/ai/overview/).
- 🛠️ **Do:** Build the interviewer agent with the OpenAI Agents SDK on a free OpenAI-compatible endpoint (`OpenAIChatCompletionsModel`, plus `set_tracing_disabled(True)` since you have no OpenAI key) and run 3 questions with feedback. Start `frameworks.md` with rows for LangGraph and the Agents SDK: setup effort, typing, tracing, multi-agent support, when to use. Done when: the agent runs and the table has both rows.

### Friday 19 Feb · 45 min — Agent evaluation: task success, trajectories, tool-call accuracy
- 📚 **Learn:** Evaluate outcomes (task success) and process (trajectory match, tool-call accuracy, argument correctness, steps and cost); rubric-based LLM judging for open-ended outputs; keep a regression set. Read: [DeepEval tool correctness](https://deepeval.com/docs/metrics-tool-correctness). Optional course: [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents).
- 🛠️ **Do:** Write 10 scenarios with expected agents/tools and success criteria. `eval_agents.py` computes task success, tool-call accuracy (name + key arguments), average steps and tokens. Run it on the W15 single-agent graph and on the multi-agent version. Done when: a comparison table shows which design wins and at what cost.

### Saturday 20 Feb · 45 min — BUILD: CareerPilot v1 multi-agent demo and eval
- 📚 **Learn:** Integration checklist: supervisor with three working agents, human approval kept from W15, the 10-scenario eval, a demo and a README with the architecture and eval table. Optional (Hindi): [Krish Naik Hindi GenAI + Agentic AI playlist](https://www.youtube.com/playlist?list=PLTDARY42LDV567lWN_5BtoVGjMFKbthGu).
- 🛠️ **Do:** Wire the interviewer into the supervisor, run end-to-end on 2 real JDs, run `eval_agents.py`, record a 2-minute demo and update the README with architecture and eval table. Done when: task success is 75%+ on the 10 scenarios, the demo is linked, and tag `v1.0-careerpilot` is pushed.

## 📦 Deliverable (by Saturday night)
`10-careerpilot/` v1.0: supervisor multi-agent system (researcher, planner, interviewer) with human approval, `frameworks.md` comparison, a 10-scenario agent eval (task success, tool-call accuracy) and a demo video.

## ✅ Self-check (Sunday test preview)
- When is a multi-agent architecture justified over one agent with tools?
- Supervisor vs handoffs vs hierarchical teams: sketch and compare.
- How do you evaluate an agent's trajectory and tool calls?
- Compare LangGraph with the OpenAI Agents SDK: when would you choose each?
- What are the main failure modes of multi-agent systems?
- How do you control cost and latency in a multi-agent system?

## 🚀 Stretch (optional)
Build the interviewer a second time with Pydantic AI (typed `Feedback` output) and add its row to `frameworks.md`, or grow the eval to 12 scenarios.
