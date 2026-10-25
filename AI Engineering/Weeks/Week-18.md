# 🤖 AI Engineering · Week 18 — AI Security and Guardrails

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** Every enterprise AI review asks about prompt injection, data leakage and excessive agency. A tested guardrail suite separates you from demo-only candidates.

## 🗓️ Sessions

### Monday 22 Feb · 45 min — OWASP Top 10 for LLM Applications 2025 and agentic risks
- 📚 **Learn:** LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. Read: [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/). Optional: [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- 🛠️ **Do:** Threat-model DocuMind and CareerPilot in `SECURITY.md`: map each OWASP item to a concrete risk in your apps (poisoned PDF -> LLM01/LLM08, `update_status` tool -> LLM06, no token caps -> LLM10), rate likelihood and impact, and list one mitigation each. Done when: all 10 items are mapped with a next step.

### Tuesday 23 Feb · 45 min — Prompt injection, jailbreaks and the lethal trifecta
- 📚 **Learn:** Direct vs indirect injection (through documents, web pages, tool outputs, emails), jailbreaks, why keyword filters fail, and the lethal trifecta: private data + untrusted content + an exfiltration channel. Read: [The lethal trifecta (Simon Willison)](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/). Optional: [Azure Prompt Shields concepts](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection).
- 🛠️ **Do:** Attack your own DocuMind: plant 5 indirect injections in a PDF (hidden instructions, fake citations, 'send this to...' requests) and try 3 direct jailbreak prompts. Done when: `attacks.md` lists 8 attacks with success/fail and the root cause of each success.

### Thursday 25 Feb · 45 min — PII redaction, data leakage and output validation
- 📚 **Learn:** Detect and anonymise PII before logging or sending text to third-party APIs (India's DPDP Act 2023 expects personal data to be used only for a stated purpose); never put secrets in prompts; validate outputs (schema, allow-lists, citation checks) and never execute or render raw model output (XSS/SQL risks). Read: [Microsoft Presidio](https://microsoft.github.io/presidio/) (getting started). Optional: [LangChain guardrails](https://docs.langchain.com/oss/python/langchain/guardrails).
- 🛠️ **Do:** Create a `guardrails/` module: Presidio-based redaction (small spaCy model `en_core_web_sm` to save disk) for email, phone and a custom recognizer for Indian PAN format, plus citation verification (every cited chunk must exist). Done when: unit tests prove PII is masked before logging and fake citations are rejected.

### Friday 26 Feb · 45 min — Least privilege, human approval and cost caps
- 📚 **Learn:** Least-privilege tools (read vs write, scoped credentials), human approval for irreversible actions, per-run step/token/cost caps (LLM10), wrapping tool outputs as clearly delimited untrusted data, content-safety APIs as an extra layer. Read: [OWASP LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/). Optional: [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview).
- 🛠️ **Do:** Harden CareerPilot: split tools into read and write, require approval for writes, cap steps and tokens per run, and wrap tool outputs as delimited untrusted data. Re-run your successful attacks from Tuesday. Done when: at least 2 previously successful attacks now fail and the change is noted in `SECURITY.md`.

### Saturday 27 Feb · 45 min — BUILD: guardrails and injection test suite for CareerPilot
- 📚 **Learn:** Defence in depth: input checks, privilege separation, output validation, monitoring; treat attacks like unit tests so they can run in CI (W19). Automated red-teaming tools generate many attacks for you. Read: [promptfoo red teaming](https://www.promptfoo.dev/docs/red-team/) (quickstart; needs Node.js 22.22+). Optional course: [Red Teaming LLM Applications](https://www.deeplearning.ai/courses/red-teaming-llm-applications).
- 🛠️ **Do:** Create `security/attack_suite.yaml` with 15+ cases (direct, indirect, PII exfiltration, excessive agency, unbounded consumption) and a pytest or promptfoo runner reporting the block rate. Fix issues until 90%+ are blocked while the W17 task-success score drops by at most 5 points. Done when: the report is committed, `SECURITY.md` is updated and tag `v1.1-careerpilot-secure` is pushed.

## 📦 Deliverable (by Saturday night)
OWASP-mapped `SECURITY.md`, `guardrails/` module (PII redaction, citation validation), hardened tools with approvals and caps, a 15+ case attack suite with 90%+ blocked.

## ✅ Self-check (Sunday test preview)
- Name five OWASP Top 10 for LLM Applications 2025 risks with an example each.
- Direct vs indirect prompt injection: give a RAG example of the indirect kind.
- What is the lethal trifecta, and how do you break it?
- Why is 'add a stronger system prompt' not a security control?
- How do you keep PII out of logs, traces and third-party LLM calls?
- What is excessive agency, and how do least privilege and human approval address it?

## 🚀 Stretch (optional)
Grow the suite to 25+ cases, run a promptfoo OWASP preset or a [PyRIT](https://github.com/Azure/PyRIT) scan and compare the findings with your suite, or try Lakera's [Agent Breaker game](https://play.lakera.ai/agent-breaker).
