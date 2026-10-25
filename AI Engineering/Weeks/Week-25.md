# 🤖 AI Engineering · Week 25 — Azure AI: Foundry, AI Search and the Cloud Boss

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** Indian enterprises standardise on Azure. Microsoft Foundry, keyless auth and Azure AI Search are what AI-103-style interviews and real projects expect (the AI-200 exam itself focuses on data, containers, messaging and monitoring). The season ends with a timed, cost-safe cloud deployment.

## 🗓️ Sessions

### Monday 12 Apr · 45 min — Microsoft Foundry: projects, models and a keyless call
- 📚 **Learn:** Foundry resource and project, model catalog, deployments and quotas (tokens per minute), Foundry Models including Azure OpenAI, endpoints and SDKs. Keyless auth: `DefaultAzureCredential` + `get_bearer_token_provider` and the 'Cognitive Services OpenAI User' role (managed identity from Azure W22). Cost-safe: pay-per-token deployments, your Azure W9 budget alerts, delete everything after Saturday. Read: [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry). Optional: [Keyless connections to Azure AI](https://learn.microsoft.com/en-us/azure/developer/ai/keyless-connections).
- 🛠️ **Do:** In a codespace, `az login --use-device-code` with your personal account, create a resource group and a Foundry project, and deploy the smallest chat model offered in your region plus a small embedding model. Assign yourself the role above and add an `azure` provider to `llmkit` that calls both keylessly. Done when: both calls work with no key in code or settings, and a repo search finds no Azure keys.

### Tuesday 13 Apr · 45 min — Foundry Agent Service and Microsoft Agent Framework basics
- 📚 **Learn:** Foundry Agent Service: prompt agents vs hosted agents, built-in tools, conversations, tracing. Microsoft Agent Framework 1.x (`pip install agent-framework`): agents with chat clients for Foundry, OpenAI, Ollama and others, tools, graph workflows; the successor to Semantic Kernel and AutoGen. Read: [Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/). Optional: [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview).
- 🛠️ **Do:** Rebuild the CareerPilot interviewer as an Agent Framework agent with one tool (question-bank lookup), running on your Foundry deployment. Run 3 mock questions with feedback. Done when: it works and `frameworks.md` gains an Agent Framework row compared with your W17 versions.

### Thursday 15 Apr · 45 min — Azure AI Search: vector, hybrid and semantic ranker
- 📚 **Learn:** Index schemas with vector fields, integrated vectorisation, hybrid queries (BM25 + vectors fused with RRF, as in W11), the semantic ranker (re-ranking), agentic retrieval; the Free tier is enough for practice. Content Safety and Prompt Shields can filter inputs and outputs (W18). Read: [Hybrid search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview). Optional: [Semantic ranker](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview).
- 🛠️ **Do:** Create a Free-tier search service, write the index JSON (fields, vector profile) and an `AzureSearchRetriever` implementing your retriever interface; upload your DocuMind chunks with embeddings from the Foundry embedding deployment. Run 10 golden questions. Done when: the retriever returns hybrid results and each index option in your notes maps to a W11 concept.

### Friday 16 Apr · 45 min — Deployment script: Container Apps with managed identity
- 📚 **Learn:** Deploy containers to Azure Container Apps (revisions, scale rules, system-assigned managed identity, secrets) as you practised in Azure W23; grant the app's identity the Foundry role so no API key is ever stored; script everything so creation and teardown are repeatable. Read: [Managed identities in Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity). Optional: [Baseline Foundry chat reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat).
- 🛠️ **Do:** Write `09-documind/azure/deploy.sh` (az CLI: registry, push the image, Container Apps environment and app with a system-assigned identity, role assignment, environment variables) and `teardown.sh`. Dry-run with a public hello-world image. Done when: the hello app answers on its public URL and `teardown.sh` removes the registry and the app.

### Saturday 17 Apr · 45 min — BOSS BATTLE: DocuMind on Azure in 45 minutes
- 📚 **Learn:** Rules: 45-minute timer, start from Friday's scripts, docs allowed, no AI code generation. Rubric /100: working public URL 30, keyless auth (no secrets anywhere) 20, 10-question smoke eval against the URL 20, `AZURE_ARCHITECTURE.md` with diagram and identity flow 15, teardown and cost note 15. Reference: [Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview).
- 🛠️ **Do:** Run `deploy.sh` with the DocuMind image using the Foundry model through managed identity and the Azure AI Search retriever, run the 10-question smoke eval against the public URL, screenshot it, write `AZURE_ARCHITECTURE.md`, then run `teardown.sh` and delete the search service and Foundry project. Done when: the rubric score is 80+, nothing is left running in the portal, and tag `v3.0-documind-azure` is pushed.

## 📦 Deliverable (by Saturday night)
DocuMind on Azure Container Apps with a Foundry model via keyless auth and an Azure AI Search retriever (boss tag `v3.0-documind-azure`), deploy/teardown scripts, `AZURE_ARCHITECTURE.md` and an Agent Framework interviewer.

## ✅ Self-check (Sunday test preview)
- What is Microsoft Foundry, and how do projects, deployments and the model catalog relate?
- How does keyless auth with managed identity work for Foundry/Azure OpenAI models?
- Explain hybrid search with RRF and the semantic ranker in Azure AI Search.
- When would you use Foundry Agent Service vs your own LangGraph app on Container Apps?
- Where do Content Safety and Prompt Shields fit in a RAG pipeline?
- How did you keep this week's Azure bill close to zero?

## 🚀 Stretch (optional)
Compare this week's work with the [AI-103 certification](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/) skills and list your gaps for post-plan preparation.
