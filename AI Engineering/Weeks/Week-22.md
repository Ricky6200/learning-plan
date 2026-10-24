# 🤖 AI Engineering · Week 22 — Azure AI: Foundry, AI Search, Container Apps

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Indian enterprises standardise on Azure. Microsoft Foundry, keyless auth and Azure AI Search are what AI-103/AI-200-style interviews and real projects expect, and this week feeds your Azure track.

## 🗓️ Sessions

### Monday 22 Mar · 45 min — Microsoft Foundry: projects, model catalog and deployments
- 📚 **Learn:** Foundry resource and project, model catalog, deployments and quotas (tokens per minute), Foundry Models including Azure OpenAI and partner models, endpoints and SDKs, playground to code. Read: [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) and the [Foundry code quickstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code); certification map: [AI-103](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/).
- 🛠️ **Do:** With Azure credits: create a Foundry project, deploy a small chat model and an embedding model, and call both from Python. Without credits: work through the quickstart code against your free provider behind an `azure` config stub. Done when: either a working Azure call or a reviewed code path plus notes is committed in `06-documind/azure/`.

### Tuesday 23 Mar · 45 min — Keyless authentication with managed identity
- 📚 **Learn:** Why API keys are risky; Microsoft Entra ID tokens via `DefaultAzureCredential` (az login locally, managed identity in Azure), `get_bearer_token_provider`, the 'Cognitive Services OpenAI User' role, no secrets in config. Read: [Keyless connections to Azure AI](https://learn.microsoft.com/en-us/azure/developer/ai/keyless-connections) and [Managed identities overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).
- 🛠️ **Do:** Add an `azure` provider to `llmkit` using `DefaultAzureCredential` and a bearer-token provider instead of a key. Use `az login` locally and document the role-assignment command. Done when: the Azure path runs keyless (or is unit-tested with a fake credential) and a repo search finds no Azure keys.

### Thursday 25 Mar · 45 min — Foundry Agent Service and Microsoft Agent Framework basics
- 📚 **Learn:** Foundry Agent Service: prompt agents vs hosted agents, built-in tools, conversations, tracing; Microsoft Agent Framework 1.x (`pip install agent-framework`): `Agent` with chat clients for Foundry, OpenAI, Ollama and others, tools, graph workflows. Read: [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) and [Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/).
- 🛠️ **Do:** Rebuild the CareerPilot interviewer as an Agent Framework `Agent` with one tool (question-bank lookup), running on Foundry (with credits) or a local Ollama client. Run 3 mock questions with feedback. Done when: it works and `frameworks.md` gains an Agent Framework row compared with your W14 versions.

### Friday 26 Mar · 45 min — Azure AI Search: vector, hybrid, semantic ranker, content safety
- 📚 **Learn:** Index schemas with vector fields, integrated vectorisation, hybrid queries (BM25 + vectors fused with RRF), the semantic ranker (re-ranking), agentic retrieval (preview); Azure AI Content Safety and Prompt Shields as input/output filters. Read: [Vector search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview), [Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview), [Semantic ranker](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview).
- 🛠️ **Do:** Map DocuMind v1 to Azure AI Search: write the index JSON (fields, vector profile, semantic configuration) and an `AzureSearchRetriever` implementing your retriever interface. With credits, run 10 golden questions; otherwise unit-test the query builder. Done when: index definition and retriever are committed and each option maps to a W8 concept.

### Saturday 27 Mar · 45 min — BUILD: DocuMind on Azure Container Apps (or architecture doc)
- 📚 **Learn:** Deploy containers to Azure Container Apps (revisions, scale rules, managed identity, Key Vault-backed secrets) with PostgreSQL + pgvector or Azure AI Search, and Azure Managed Redis for caching. Read: [Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview) and the [baseline Foundry chat reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat).
- 🛠️ **Do:** With credits: push the image to Azure Container Registry, deploy to Container Apps with managed identity to Foundry, configure env/secrets and run the smoke eval against the public URL. Without credits: write `AZURE_ARCHITECTURE.md` (diagram, services, identity flow, cost estimate). Done when: the public URL passes the smoke eval or the doc is checked against the reference; tag `v3.0-documind-azure`.

## 📦 Deliverable (by Saturday night)
DocuMind on Azure Container Apps with Foundry models via keyless auth and AI Search or pgvector, or a reviewed `AZURE_ARCHITECTURE.md` with Azure code paths; Agent Framework interviewer; AI Search index + retriever.

## ✅ Self-check (Sunday test preview)
- What is Microsoft Foundry, and how do projects, deployments and the model catalog relate?
- How does keyless auth with managed identity work for Foundry/Azure OpenAI models?
- Explain hybrid search with RRF and the semantic ranker in Azure AI Search.
- When would you use Foundry Agent Service vs your own LangGraph app on Container Apps?
- Where do Content Safety and Prompt Shields fit in a RAG pipeline?
- What does Microsoft Agent Framework replace, and what does it add?

## 🚀 Stretch (optional)
Compare this week's work with the [AI-200 certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/) and AI-103 skills outlines and list your gaps for post-plan prep.
