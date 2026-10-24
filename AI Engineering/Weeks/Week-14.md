# 🤖 AI Engineering · Week 14 — Multi-Agent Systems and Framework Tour

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Interviewers ask when multi-agent designs are worth the cost and how to evaluate them. Knowing several frameworks lets you pick the right tool instead of the trendy one.

## 🗓️ Sessions

### Monday 25 Jan · 45 min — Multi-agent patterns: supervisor, hierarchical, handoffs
- 📚 **Learn:** Single agent + tools first; supervisor (central router), hierarchical teams, handoffs (an agent transfers control), subagents exposed as tools; costs: multiplied tokens, context sharing, error propagation. Read: [LangChain multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent) and [How we built our multi-agent research system (Anthropic)](https://www.anthropic.com/research/multi-agent-research-system).
- 🛠️ **Do:** Design CareerPilot v1 in `multi_agent.md`: researcher (company and role research), planner (prep plan) and interviewer (mock Q&A with feedback) under a supervisor. Define each agent's tools, inputs, outputs and handoff rules, and estimate tokens per run vs single agent. Done when: the doc has a Mermaid diagram and a 'why not single-agent?' justification.

### Tuesday 26 Jan · 45 min — Implement supervisor and subagents in LangGraph
- 📚 **Learn:** Supervisor as a routing node or subagents-as-tools; handoffs with `Command(goto=..., update=...)`; shared vs private state; give each agent only the tools it needs. Read the tutorials [Subagents: personal assistant](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant) and [Handoffs: customer support](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs-customer-support).
- 🛠️ **Do:** Implement supervisor + researcher + planner in LangGraph (interviewer comes Thursday). The researcher uses your search tools or MCP server; the planner reuses the W12 plan subgraph. Log which agent acted at each step. Done when: 'prepare me for a backend role at Company X' routes researcher -> planner -> supervisor final answer.

### Thursday 28 Jan · 45 min — Framework tour: Agents SDK, Agent Framework, Pydantic AI
- 📚 **Learn:** Compare primitives: OpenAI Agents SDK (agents, handoffs, guardrails, sessions, tracing), Microsoft Agent Framework 1.x (agents + graph workflows; successor to Semantic Kernel and AutoGen), Pydantic AI (typed agents and outputs), CrewAI (role-based crews, awareness). Read: [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), [Microsoft Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/), [Pydantic AI](https://pydantic.dev/docs/ai/overview/).
- 🛠️ **Do:** Build the interviewer agent twice: with the OpenAI Agents SDK (`OpenAIChatCompletionsModel` on a free OpenAI-compatible endpoint, `set_tracing_disabled(True)` if you have no OpenAI key) and with Pydantic AI (typed `Feedback` output). Same prompt, same 3 questions. Fill `frameworks.md`: setup effort, typing, tracing, multi-agent support, when to use. Done when: both versions run and the table ends with a recommendation.

### Friday 29 Jan · 45 min — Agent evaluation: task success, trajectories, tool-call accuracy
- 📚 **Learn:** Evaluate outcomes (task success) and process (trajectory match, tool-call accuracy, argument correctness, steps and cost); rubric-based LLM judging for open-ended outputs; keep a regression set. Read: [DeepEval tool correctness](https://deepeval.com/docs/metrics-tool-correctness) and [RAGAS metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) (agent and tool-use section); optional course: [Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents).
- 🛠️ **Do:** Write 12 scenarios with expected agents/tools and success criteria. `eval_agents.py` computes task success, tool-call accuracy (name + key arguments), average steps and tokens. Run it on the W12 single-agent graph and the multi-agent version. Done when: a comparison table shows which design wins and at what cost.

### Saturday 30 Jan · 45 min — BOSS BATTLE: CareerPilot v1 multi-agent demo and mini eval
- 📚 **Learn:** Rules: 45 minutes starting from Tuesday/Thursday code; deliver a supervisor with 3 working agents, human approval kept, and the 12-scenario eval. Rubric /100: routing 25, three agents functional 25, human-in-the-loop 15, eval run + table 25, demo/README 10. Hindi recap: [Krish Naik Hindi GenAI + Agentic AI playlist](https://www.youtube.com/playlist?list=PLTDARY42LDV567lWN_5BtoVGjMFKbthGu).
- 🛠️ **Do:** Wire the interviewer into the supervisor, run end-to-end on 2 real JDs, run `eval_agents.py`, record a 2-minute demo and update the README with architecture and eval table. Done when: rubric score is 80+, task success is 75%+ on the 12 scenarios and tag `v1.0-careerpilot` is pushed.

## 📦 Deliverable (by Saturday night)
`07-careerpilot/` v1.0: supervisor multi-agent system (researcher, planner, interviewer) with human approval, `frameworks.md` comparison, 12-scenario agent eval (task success, tool-call accuracy) and a demo video.

## ✅ Self-check (Sunday test preview)
- When is a multi-agent architecture justified over one agent with tools?
- Supervisor vs handoffs vs hierarchical teams: sketch and compare.
- How do you evaluate an agent's trajectory and tool calls?
- Compare LangGraph, OpenAI Agents SDK and Microsoft Agent Framework.
- What are the main failure modes of multi-agent systems?
- How do you control cost and latency in a multi-agent system?

## 🚀 Stretch (optional)
Port the planner to [Microsoft Agent Framework workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/overview) to prepare for the W22 Foundry work.
