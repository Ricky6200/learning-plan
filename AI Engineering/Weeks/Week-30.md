# 🤖 AI Engineering · Week 30 — AI Interview Prep: Final Boss

> 📅 **Mon 17 May 2027 → Sun 23 May 2027** · Season 6 — Final Boss: The Offer · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 29](Week-29.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-30.md)

**Why this week:** Offers come from fluent explanations, fast coding under time pressure and crisp project stories. This week rehearses exactly what AI-engineer interviews test and ends with the final boss: a full mock interview.

## 🗓️ Sessions

### Monday 17 May · 45 min — Question-bank revision: ML, LLM basics, RAG, vector DBs, evals
- 📚 **Learn:** Revise the starred questions in `AI_INTERVIEW_QUESTION_BANK.md` (track folder) for ML fundamentals, LLM internals, tokenization/embeddings, prompting, RAG, vector databases and evals. Answer format: definition -> why it matters -> example from your project -> trade-off. Read: [ML interviews book (Chip Huyen)](https://huyenchip.com/ml-interviews-book/) (one chapter on your weakest area).
- 🛠️ **Do:** Answer 25 starred questions aloud (2 minutes max each), recording 5 of them. Mark each green/amber/red and rewrite weak answers as 5-line notes. Done when: 20+ of 25 are green and the red items are scheduled for Thursday review.

### Tuesday 18 May · 45 min — Agents, MCP, security, LLMOps revision and project deep-dives
- 📚 **Learn:** Revise starred questions on agents, MCP, security, LLMOps, fine-tuning, Spring AI and Azure AI. Prepare STAR-style project deep-dives: context, your design, metrics, trade-offs, failures, next steps. Refresh: [OWASP Top 10 for LLMs](https://genai.owasp.org/llm-top-10/). Optional: [Building effective agents](https://www.anthropic.com/research/building-effective-agents).
- 🛠️ **Do:** Write 3 one-page deep-dives (TicketVerse AI, DocuMind, CareerPilot) with 'numbers I can quote' and 5 likely follow-up questions each; rehearse one aloud for 5 minutes. Done when: all three are committed and each lists 3+ metrics.

### Thursday 20 May · 45 min — AI coding round: build a mini RAG in 45 minutes
- 📚 **Learn:** AI coding rounds often ask for a minimal RAG, agent or extractor in 45-60 minutes with docs allowed; interviewers watch structure, tests, error handling and how you check quality. Strategy: skeleton first, happy path, then evals and edge cases. Quick API refresher: [sentence-transformers quickstart](https://sbert.net/docs/quickstart.html).
- 🛠️ **Do:** Start a 45-minute timer and, from an empty folder, build a mini RAG over 3 text files: chunk, embed locally, retrieve top-3, answer with citations through a free API, 3 pytest tests and a 5-question check. Done when: it runs end-to-end within the time and you log what slowed you down.

### Friday 21 May · 45 min — Roadmap beyond Week 30 and target-company analysis
- 📚 **Learn:** Next 6 months: the AI-103 certification, deeper ML/DL (Karpathy's Zero to Hero, Raschka's LLM book), open-source contributions (LangGraph, Spring AI, MCP servers) and one specialisation (evals, inference or agents). Read: [AI-103: Azure AI Apps and Agents Developer](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/). Optional: [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).
- 🛠️ **Do:** Write `ROADMAP_NEXT.md`: 3 dated goals (certification, OSS contribution, deep-dive project), weekly hours, and 10 target companies/roles with the AI skills their JDs ask for, parsed and gap-analysed by your own JD Parser and CareerPilot. Done when: the roadmap is committed and all 10 JDs have gap reports.

### Saturday 22 May · 45 min — BOSS BATTLE: full AI-engineer mock interview
- 📚 **Learn:** Format: 10 minutes project deep-dive, 15 minutes rapid-fire concepts (ML basics, RAG, agents, evals, security, LLMOps), 15 minutes mini design (an AI feature for a product), 5 minutes your questions. Rubric /100: depth 30, clarity 20, trade-offs 20, metrics/evidence 20, communication 10. Reference: [What we learned from a year of building with LLMs](https://applied-llms.org/).
- 🛠️ **Do:** Run the mock with a peer or mentor (or an AI interviewer prompt you wrote, answering without notes) and record it. Score it with the rubric, list the top 5 improvements and update your resume with 3 numbers-backed project bullets. Done when: the score is 80+ (or a dated re-attempt within 7 days is booked) and the recording and scorecard are committed.

## 📦 Deliverable (by Saturday night)
Interview-ready kit: question bank with green/amber/red status, 3 project deep-dive one-pagers, a timed mini-RAG coding round, `ROADMAP_NEXT.md` with 10 analysed target JDs, a recorded final mock with scorecard and updated resume bullets.

## ✅ Self-check (Sunday test preview)
- Explain RAG end to end and how you evaluated it.
- When would you NOT use an agent?
- How do you secure an AI agent that can take actions?
- What did you fine-tune, and did it beat prompting? Why or why not?
- Precision vs recall: which mattered in your projects, and why?
- How would you design an LLM gateway for a company?
- How does Spring AI fit into a Java microservices architecture?
- How will you keep up with a field that changes every month?

## 🚀 Stretch (optional)
Do a second mock focused purely on AI system design with a different interviewer, and book the AI-103 exam when your notes from W25 show no red gaps.
