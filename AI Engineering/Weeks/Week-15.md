# 🤖 AI Engineering · Week 15 — AI Security and Guardrails

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** Every enterprise AI review asks about prompt injection, data leakage and excessive agency. A tested guardrail suite separates you from demo-only candidates.

## 🗓️ Sessions

### Monday 01 Feb · 45 min — OWASP Top 10 for LLM Applications 2025 and agentic risks
- 📚 **Learn:** LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. Read: [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/); skim [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- 🛠️ **Do:** Threat-model DocuMind and CareerPilot in `SECURITY.md`: map each OWASP item to a concrete risk in your apps (poisoned PDF -> LLM01/LLM08, `update_status` tool -> LLM06, no token caps -> LLM10), rate likelihood and impact, and list one mitigation each. Done when: all 10 items are mapped with a next step.

### Tuesday 02 Feb · 45 min — Prompt injection, jailbreaks and the lethal trifecta
- 📚 **Learn:** Direct vs indirect injection (through documents, web pages, tool outputs, emails), jailbreaks, why keyword filters fail, and the lethal trifecta: private data + untrusted content + an exfiltration channel. Read: [The lethal trifecta (Simon Willison)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) and [Azure Prompt Shields concepts](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection).
- 🛠️ **Do:** Attack your own DocuMind: plant 5 indirect injections in a PDF (hidden instructions, fake citations, 'send this to...' requests) and try 5 direct jailbreak prompts. Optional warm-up: Lakera's [Agent Breaker game](https://play.lakera.ai/agent-breaker). Done when: `attacks.md` lists 10 attacks with success/fail and the root cause of each success.

### Thursday 04 Feb · 45 min — PII redaction, data leakage and output validation
- 📚 **Learn:** Detect and anonymise PII before logging or sending text to third-party APIs; never put secrets in prompts; validate outputs (schema, allow-lists, citation checks) and never execute or render raw model output (XSS/SQL risks). Read: [Microsoft Presidio](https://microsoft.github.io/presidio/) and [LangChain guardrails](https://docs.langchain.com/oss/python/langchain/guardrails).
- 🛠️ **Do:** Create a `guardrails/` module: Presidio-based redaction for logs and traces (email, phone, plus a custom recognizer for Indian phone and PAN formats), output schema validation, citation verification (every cited chunk must exist) and Markdown/HTML sanitising. Done when: unit tests prove PII is masked in traces and fake citations are rejected.

### Friday 05 Feb · 45 min — Least privilege, human approval, content safety, red-teaming tools
- 📚 **Learn:** Least-privilege tools (read vs write, scoped credentials), human approval for irreversible actions, per-run step/token/cost caps (LLM10), content-safety APIs, automated red-teaming with promptfoo or PyRIT. Read: [promptfoo red teaming](https://www.promptfoo.dev/docs/red-team/), [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview); awareness: [PyRIT](https://github.com/Azure/PyRIT).
- 🛠️ **Do:** Harden CareerPilot: split tools into read and write, require approval for writes, cap steps and tokens per run, and wrap tool outputs as delimited untrusted data. Install promptfoo (Node.js 22.22+) and run a small red-team config against your `/ask` endpoint. Done when: the promptfoo report is generated and 2+ previously successful attacks now fail.

### Saturday 06 Feb · 45 min — BUILD: guardrails and injection test suite for CareerPilot
- 📚 **Learn:** Defence in depth: input checks, privilege separation, output validation, monitoring; treat attacks like unit tests and run them in CI next week. Free course: [Red Teaming LLM Applications](https://www.deeplearning.ai/courses/red-teaming-llm-applications).
- 🛠️ **Do:** Create `security/attack_suite.yaml` with 25+ cases (direct, indirect, PII exfiltration, excessive agency, unbounded consumption) and a pytest or promptfoo runner reporting block rate. Fix issues until 90%+ are blocked while the W14 task-success score drops by at most 5 points. Done when: the report is committed, `SECURITY.md` is updated and tag `v1.1-careerpilot-secure` is pushed.

## 📦 Deliverable (by Saturday night)
OWASP-mapped `SECURITY.md`, `guardrails/` module (PII redaction, output and citation validation, sanitising), hardened tools with approvals and caps, 25+ case attack suite with 90%+ blocked.

## ✅ Self-check (Sunday test preview)
- Name five OWASP Top 10 for LLM Applications 2025 risks with an example each.
- Direct vs indirect prompt injection: give a RAG example of the indirect kind.
- What is the lethal trifecta, and how do you break it?
- Why is 'add a stronger system prompt' not a security control?
- How do you keep PII out of logs, traces and third-party LLM calls?
- What is excessive agency, and how do least privilege and human approval address it?

## 🚀 Stretch (optional)
Run a [PyRIT](https://github.com/Azure/PyRIT) scan or extend promptfoo with an OWASP preset and compare the findings with your suite.
