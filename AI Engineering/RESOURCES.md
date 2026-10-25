# 📚 AI Engineering — Resources (verified 24–25 Oct 2026)

Every link below was checked on 24–25 Oct 2026. **Free unless marked (paid).** Week numbers refer to the 30-week plan (26 Oct 2026 → 23 May 2027) and show where each resource is used.

> ⚠️ **GitHub Models was retired on 30 Jul 2026.** Skip any tutorial that depends on it; use Gemini / Groq / Ollama / OpenRouter via the OpenAI-compatible client (see README Section 6).

---

## 1. Primary (daily use)

| Resource | Use it for | Weeks |
|---|---|---|
| [Python tutorial (official)](https://docs.python.org/3/tutorial/) | Syntax, data structures, classes, modules, errors | W1–W3 |
| [uv docs](https://docs.astral.sh/uv/) | Python versions, projects, lockfiles, `uv run`, Docker and PyTorch guides | W1 → all |
| [Pydantic docs](https://docs.pydantic.dev/latest/) | Validation, settings, JSON Schema for structured outputs | W2, W7 → all |
| [NumPy for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) · [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | Arrays, vectorised maths, DataFrames for evals and data prep | W3 → all |
| [scikit-learn getting started](https://scikit-learn.org/stable/getting_started.html) | Splits, baselines, metrics, cross-validation, TF-IDF pipelines | W4, W7 |
| [GitHub Codespaces: dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers) | Your cloud dev machine for every LLM session (secrets, timeout, quota) | W6 → all |
| [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | APIs, dependencies, SSE streaming, testing, Docker | W8, W9, W13 |
| [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html) · [Docker concepts](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) | SQL, upserts, indexes and EXPLAIN; containers, volumes, Compose | W8 → all |
| [openai-python](https://github.com/openai/openai-python) | One client for every OpenAI-compatible provider | W6 → all |
| [Gemini API cookbook](https://github.com/google-gemini/cookbook) | Free-tier quickstarts: OpenAI compatibility, streaming, JSON, function calling, embeddings, PDFs, audio | W6 → W22 |
| [Ollama](https://ollama.com/) · [model library](https://ollama.com/library) | Local models, embeddings, vision, benchmarks | W6, W9, W20, W22 |
| [LangChain docs](https://docs.langchain.com/oss/python/langchain/overview) · [LangGraph docs](https://docs.langchain.com/oss/python/langgraph/overview) | RAG building blocks, agents, graphs, persistence, interrupts, agentic RAG | W10, W14–W17, W29 |
| [LangChain Academy: Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) | Structured LangGraph course (modules 1–4) | W15 |
| [MCP docs](https://modelcontextprotocol.io/docs/learn/architecture) · [MCP Python SDK v2 docs](https://py.sdk.modelcontextprotocol.io/) | Protocol concepts, `MCPServer`, `Client`, testing, authorization | W16, W29 |
| [Building effective agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents) | Workflow vs agent, the 5 patterns | W14, W26, W30 |
| [Langfuse docs](https://langfuse.com/docs) | Tracing, prompt management, evals (free Hobby cloud or self-host) | W12, W19 |
| [RAGAS metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) · [DeepEval](https://deepeval.com/docs/getting-started) | RAG and agent evaluation metrics | W12, W17, W27 |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | AI security vocabulary and threat modelling | W18, W27, W30 |
| [Spring AI reference](https://docs.spring.io/spring-ai/reference/) | ChatClient, advisors, tools, RAG, MCP, observability (2.0.x) | W23–W28 |
| [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) | Azure AI platform (formerly Azure AI Foundry) | W25 |

---

## 2. Secondary / reference (by topic)

**Python for Java developers (W1–W2)**
- [Learn X in Y minutes: Python](https://learnxinyminutes.com/python/) · [Python vs Java (Real Python)](https://realpython.com/java-vs-python/) · [List comprehensions](https://realpython.com/list-comprehension-python/) · [Async IO in Python](https://realpython.com/async-io-python/)
- [Type hints cheat sheet (mypy)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) · [httpx async](https://www.python-httpx.org/async/) · [pytest](https://docs.pytest.org/en/stable/getting-started.html) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/en/latest/) · [Ruff](https://docs.astral.sh/ruff/)
- Corporate proxy (company laptop): [pip-system-certs](https://pypi.org/project/pip-system-certs/) (makes Python trust the OS certificate store) · [truststore](https://truststore.readthedocs.io/en/latest/) (the library underneath, if you prefer one explicit call)
- [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) (full free course, if you want more depth)

**Python III & data (W3)**
- [Generators and yield (Real Python)](https://realpython.com/introduction-to-python-generators/) · [itertools](https://docs.python.org/3/library/itertools.html) · [Functional programming HOWTO](https://docs.python.org/3/howto/functional.html) · [Primer on decorators (Real Python)](https://realpython.com/primer-on-python-decorators/) · [contextlib](https://docs.python.org/3/library/contextlib.html)
- [typing module](https://docs.python.org/3/library/typing.html) · [Enum HOWTO](https://docs.python.org/3/howto/enum.html) · [Logging HOWTO](https://docs.python.org/3/howto/logging.html) · [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [NumPy: absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html) · [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html) · [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · [Open-Meteo historical weather API](https://open-meteo.com/en/docs/historical-weather-api)

**ML fundamentals (W4)**
- scikit-learn: [Getting started](https://scikit-learn.org/stable/getting_started.html) · [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) · [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) · [Feature extraction (TF-IDF)](https://scikit-learn.org/stable/modules/feature_extraction.html) · [Pipelines](https://scikit-learn.org/stable/modules/compose.html) · [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) · [Text classification example](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html) · [Under- vs overfitting example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)
- Google ML Crash Course: [Accuracy, precision, recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) · [Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting) · [Dividing datasets](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) · [Logistic regression](https://developers.google.com/machine-learning/crash-course/logistic-regression)
- Dataset: [SMS Spam Collection (UCI)](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) — download it in the browser

**Codespaces & environment (W6, W9)**
- [Introduction to dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers) · [Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces) · [Idle timeout](https://docs.github.com/en/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces) · [Codespaces billing and free quota](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)
- [Ollama on Linux](https://ollama.com/download/linux) · [uv + PyTorch (CPU-only index)](https://docs.astral.sh/uv/guides/integration/pytorch/)

**Backend foundations: Docker, SQL, FastAPI (W8, W13)**
- Docker: [What is a container?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) · [What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/) · [Compose quickstart](https://docs.docker.com/compose/gettingstarted/) · [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/) · [FastAPI in containers](https://fastapi.tiangolo.com/deployment/docker/)
- SQL: [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial-sql.html) · [INSERT … ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html) · [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) · [psycopg 3 basic usage](https://www.psycopg.org/psycopg3/docs/basic/usage.html) · [Use The Index, Luke](https://use-the-index-luke.com/)
- FastAPI: [First steps](https://fastapi.tiangolo.com/tutorial/first-steps/) · [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) · [Server-Sent Events](https://fastapi.tiangolo.com/tutorial/server-sent-events/) · [Security reference (APIKeyHeader)](https://fastapi.tiangolo.com/reference/security/) · [slowapi](https://github.com/laurentS/slowapi)

**How LLMs work (W5)**
- [3Blue1Brown: Neural networks series](https://www.3blue1brown.com/topics/neural-networks) · [Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U) · [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [Transformer Explainer (interactive)](https://poloclub.github.io/transformer-explainer/) · [LLM Visualization](https://bbycroft.net/llm)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1) · [Tokenizers chapter](https://huggingface.co/learn/llm-course/chapter6/1) · [tiktoken](https://github.com/openai/tiktoken) · [Tiktokenizer playground](https://tiktokenizer.vercel.app/)
- [How to generate text (sampling)](https://huggingface.co/blog/how-to-generate) · [Illustrating RLHF](https://huggingface.co/blog/rlhf) · [Understanding reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) · [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
- Papers (abstract + figures are enough): [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

**Prompting, structured output, tool calling (W7)**
- [Anthropic prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) · [OpenAI prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) · [Prompting Guide techniques](https://www.promptingguide.ai/techniques) · [GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)
- [OpenAI structured outputs](https://platform.openai.com/docs/guides/structured-outputs) · [Instructor](https://python.useinstructor.com/) · [Ollama structured outputs](https://ollama.com/blog/structured-outputs) · [LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output)
- [OpenAI cookbook](https://developers.openai.com/cookbook) · [Claude cookbooks](https://github.com/anthropics/claude-cookbooks) · [Calling functions with chat models](https://developers.openai.com/cookbook/examples/how_to_call_functions_with_chat_models)

**Embeddings & vector databases (W9)**
- [sentence-transformers (SBERT)](https://sbert.net/) · [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) · [Embeddings explained (Simon Willison)](https://simonwillison.net/2023/Oct/23/embeddings/)
- [pgvector](https://github.com/pgvector/pgvector) · [pgvector-python](https://github.com/pgvector/pgvector-python) · [pgvector Docker image](https://hub.docker.com/r/pgvector/pgvector) · [Qdrant docs](https://qdrant.tech/documentation/) · [Chroma docs](https://docs.trychroma.com/docs/overview/introduction) · [FAISS](https://github.com/facebookresearch/faiss)

**RAG (W10–W11, W29)**
- [LangChain retrieval concepts](https://docs.langchain.com/oss/python/deepagents/retrieval) · [LangChain semantic search tutorial](https://docs.langchain.com/oss/python/langchain/knowledge-base) · [LangGraph agentic RAG](https://docs.langchain.com/oss/python/langgraph/agentic-rag)
- [RAG From Scratch (code)](https://github.com/langchain-ai/rag-from-scratch) · [RAG_Techniques notebooks](https://github.com/NirDiamant/RAG_Techniques) · [Contextual Retrieval (Anthropic)](https://www.anthropic.com/research/contextual-retrieval) · [GraphRAG](https://microsoft.github.io/graphrag/) · [LlamaIndex](https://github.com/run-llama/llama_index)
- Parsing: [Docling](https://github.com/docling-project/docling) · [MarkItDown](https://github.com/microsoft/markitdown) · [pymupdf4llm](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
- Re-ranking: [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) · Papers: [RAG](https://arxiv.org/abs/2005.11401) · [HyDE](https://arxiv.org/abs/2212.10496) · [Lost in the Middle](https://arxiv.org/abs/2307.03172) · [Corrective RAG](https://arxiv.org/abs/2401.15884)
- Multi-hop: [RAG from scratch, Part 7: decomposition](https://www.youtube.com/watch?v=h0OPWlEOank)

**Evals & observability (W12, W19)**
- [Your AI product needs evals](https://hamel.dev/blog/posts/evals/) · [LLM evals FAQ](https://hamel.dev/blog/posts/evals-faq/) · [Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/) · [What we learned from a year of building with LLMs](https://applied-llms.org/)
- [Langfuse evaluation](https://langfuse.com/docs/evaluation/overview) · [Arize Phoenix](https://arize.com/docs/phoenix) · [OpenTelemetry Python getting started](https://opentelemetry.io/docs/languages/python/getting-started/) · [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) · [promptfoo](https://www.promptfoo.dev/docs/intro/)

**Agents & multi-agent (W14–W17)**
- [A practical guide to building agents (OpenAI, PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) · [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) · [ReAct paper](https://arxiv.org/abs/2210.03629)
- Anthropic engineering: [Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) · [Writing tools for agents](https://www.anthropic.com/research/writing-tools-for-agents) · [Multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system)
- Frameworks: [LangChain multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent) · [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) · [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) · [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) · [Pydantic AI](https://pydantic.dev/docs/ai/overview/) · [CrewAI](https://docs.crewai.com/)

**MCP & agent protocols (W16, W29)**
- [MCP spec 2026-07-28: key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog) · [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) · [MCP Inspector](https://github.com/modelcontextprotocol/inspector) · [Reference servers](https://github.com/modelcontextprotocol/servers)
- [Python SDK v2: testing](https://py.sdk.modelcontextprotocol.io/get-started/testing/) · [Python SDK v2: authorization (TokenVerifier)](https://py.sdk.modelcontextprotocol.io/run/authorization/) · [MCP authorization spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index)
- [VS Code: use MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) · [A2A protocol](https://a2a-protocol.org/latest/) · [LangChain MCP adapters](https://docs.langchain.com/oss/python/langchain/mcp) (0.3.x still requires `mcp<2`: keep your v2 server in its own uv project)

**AI security (W18)**
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · [OWASP LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) · [Prompt injection series (Simon Willison)](https://simonwillison.net/series/prompt-injection/) · [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- [Microsoft Presidio (PII)](https://microsoft.github.io/presidio/) · [promptfoo red teaming](https://www.promptfoo.dev/docs/red-team/) · [PyRIT](https://github.com/Azure/PyRIT) · [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) · [Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)
- Guardrail frameworks (awareness): [LangChain guardrails](https://docs.langchain.com/oss/python/langchain/guardrails) · [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/latest) · [Guardrails AI](https://guardrailsai.com/guardrails/docs)

**LLMOps, cost & gateways (W19, W26, W28)**
- [Building a GenAI platform (Chip Huyen)](https://huyenchip.com/2024/07/25/genai-platform.html) · [LiteLLM](https://docs.litellm.ai/docs/) · [RouteLLM](https://github.com/lm-sys/RouteLLM) · [RedisVL](https://docs.redisvl.com/en/latest/) · [promptfoo GitHub Action](https://www.promptfoo.dev/docs/integrations/github-action/) · [GitHub Actions for Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python) · [PostgreSQL service containers](https://docs.github.com/en/actions/tutorials/use-containerized-services/create-postgresql-service-containers)
- Public demo and load tests: [Hugging Face Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker) · [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html)

**Open-source models, inference & fine-tuning (W20–W21)**
- [Hugging Face Hub docs](https://huggingface.co/docs/hub/index) · [Model cards](https://huggingface.co/docs/hub/model-cards) · [Licenses](https://huggingface.co/docs/hub/repositories-licenses) · [GGUF](https://huggingface.co/docs/hub/gguf) · [Transformers pipelines](https://huggingface.co/docs/transformers/pipeline_tutorial) · [Quantization overview](https://huggingface.co/docs/transformers/main/en/quantization/overview)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) · [vLLM docs](https://docs.vllm.ai/en/latest/) · [vLLM & PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) · [Continuous batching](https://www.anyscale.com/blog/continuous-batching-llm-inference) · [KV caching explained](https://huggingface.co/blog/not-lain/kv-caching) · [Artificial Analysis](https://artificialanalysis.ai/)
- [Unsloth docs](https://docs.unsloth.ai/) · [Unsloth notebooks](https://docs.unsloth.ai/get-started/unsloth-notebooks) · [TRL](https://huggingface.co/docs/trl/index) · [PEFT LoRA guide](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora) · [LoRA](https://arxiv.org/abs/2106.09685) · [QLoRA](https://arxiv.org/abs/2305.14314) · [DPO](https://arxiv.org/abs/2305.18290) · [LoRA tips (Raschka)](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms)

**Multimodal & document AI (W22)**
- [Ollama vision models](https://ollama.com/blog/vision-models) · [Whisper](https://github.com/openai/whisper) · [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [Diffusers](https://huggingface.co/docs/diffusers/index)
- Azure (awareness): [Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) · [Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) · [Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview)

**Spring AI & Java (W23–W28)**
- Spring AI 2.0: [ChatClient](https://docs.spring.io/spring-ai/reference/api/chatclient.html) · [Advisors](https://docs.spring.io/spring-ai/reference/api/advisors.html) · [Structured output](https://docs.spring.io/spring-ai/reference/api/structured-output.html) · [Chat memory](https://docs.spring.io/spring-ai/reference/api/chat-memory.html) · [Tools](https://docs.spring.io/spring-ai/reference/api/tools.html) · [PGvector](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html) · [ETL](https://docs.spring.io/spring-ai/reference/api/etl-pipeline.html) · [RAG](https://docs.spring.io/spring-ai/reference/api/retrieval-augmented-generation.html) · [MCP](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html) · [Observability](https://docs.spring.io/spring-ai/reference/observability/index.html) · [Evaluation](https://docs.spring.io/spring-ai/reference/api/testing.html)
- Providers: [Groq chat](https://docs.spring.io/spring-ai/reference/api/chat/groq-chat.html) · [Google GenAI chat (Gemini)](https://docs.spring.io/spring-ai/reference/api/chat/google-genai-chat.html) · [OpenAI chat](https://docs.spring.io/spring-ai/reference/api/chat/openai-chat.html) · Streaming returns a `Flux`: [Reactor reference](https://projectreactor.io/docs/core/release/reference/)
- [spring-ai-examples](https://github.com/spring-projects/spring-ai-examples) · [Spring AI for Beginners (Microsoft)](https://github.com/microsoft/Spring-AI-for-Beginners) · [awesome-spring-ai](https://github.com/spring-ai-community/awesome-spring-ai) · [Dan Vega's Spring AI workshop](https://github.com/danvega/spring-ai-workshop) · [LangChain4j](https://docs.langchain4j.dev/)

**Azure AI (W25, W28)**
- [Foundry code quickstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) · [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) · [Keyless connections](https://learn.microsoft.com/en-us/azure/developer/ai/keyless-connections) · [Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- Azure AI Search: [Vector](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) · [Hybrid](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) · [RRF ranking](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking) · [Semantic ranker](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) · [Agentic retrieval](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)
- [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview) · [Managed identity in Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/managed-identity) · [Secrets in Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets) · [AI gateway in API Management](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities) · Certs: [AI-200](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/) (exam in W26; its skills outline covers containers, data services, messaging and monitoring, not Foundry) · [AI-103](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/)

**AI system design**
- [Azure Architecture Center: AI/ML](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/) · [Baseline Foundry chat architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) · [Secure multitenant RAG](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag) · [RAG design & evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) · [Qdrant distributed deployment](https://qdrant.tech/documentation/guides/distributed_deployment/)

---

## 3. Books (optional)

| Book | Why | When | Cost |
|---|---|---|---|
| Chip Huyen — *AI Engineering* (O'Reilly, 2025) · [companion repo](https://github.com/chiphuyen/aie-book) | The best single book on evals, RAG, agents, inference optimisation and AI system design | W12, W19, W26 | (paid) |
| Sebastian Raschka — [*Build a Large Language Model (From Scratch)*](https://www.manning.com/books/build-a-large-language-model-from-scratch) · [code](https://github.com/rasbt/LLMs-from-scratch) | Deep intuition for tokenizers, attention, pretraining and fine-tuning by coding a GPT | W5 stretch, after W30 | (paid; code free) |
| Jay Alammar & Maarten Grootendorst — *Hands-On Large Language Models* (O'Reilly) · [code](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | Visual, practical: embeddings, semantic search, RAG, fine-tuning | W5, W9–W11, W21 | (paid; code free) |
| Chip Huyen — [*Introduction to ML Interviews* (free online)](https://huyenchip.com/ml-interviews-book/) | ML fundamentals for interview rounds | W4, W30 | Free |

---

## 4. YouTube (English + Hindi)

| Channel · video/playlist | Language | Topic | Weeks |
|---|---|---|---|
| Andrej Karpathy · [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | English | Best 1-hour LLM overview | W5 |
| Andrej Karpathy · [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | English | Pretraining → SFT → RL, in depth (3.5 h) | W5–W7 stretch |
| Andrej Karpathy · [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) · [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) · [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) | English | Practical usage, tokenization, training pipeline | W5–W7 |
| Andrej Karpathy · [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | English | Build neural nets/GPT from scratch (post-plan deep dive) | after W30 |
| 3Blue1Brown · [Neural networks playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (incl. [Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U), [Transformers](https://www.youtube.com/watch?v=wjZofJX0v4M), [Attention](https://www.youtube.com/watch?v=eMlx5fFNoYc), [LLMs explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs)) | English | Visual intuition for gradient descent, backprop, transformers, attention | W5 |
| LangChain · [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) | English | Short videos per RAG technique (Part 7 = multi-hop decomposition) | W10–W11, W29 |
| freeCodeCamp · [Learn RAG From Scratch](https://www.youtube.com/watch?v=sVcwVQRHIc8) · [Learn Python (full course)](https://www.youtube.com/watch?v=rfscVS0vtbw) | English | RAG in one sitting; Python basics | W1, W10–W11 |
| Corey Schafer · [Python OOP tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) | English | Classes, inheritance, properties | W2 |
| Telusko · [Python for Beginners](https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3) · [Spring AI tutorial #1](https://www.youtube.com/watch?v=4nBG848oArI) | English (Indian) | Python basics; Spring AI intro | W1, W23 |
| Dan Vega · [Spring AI playlist](https://www.youtube.com/playlist?list=PLZV0a2jwt22uoDm3LNDFvN6i2cAVU_HTH) | English | Spring AI features, RAG, tools, MCP | W23–W24 |
| Krish Naik · [Complete RAG playlist](https://www.youtube.com/playlist?list=PLZoTAELRMXVM8Pf4U67L4UuDRgV4TNX9D) · [MCP Agentic AI crash course](https://www.youtube.com/watch?v=MDBG2MOp4Go) | English (Indian) | RAG pipelines; MCP with Python | W10–W11, W16 |
| CodeWithHarry · [Python for Beginners (100 Days of Code)](https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg) | Hindi | Python from zero | W1–W3 |
| Chai aur Code · [Chai aur Python](https://www.youtube.com/playlist?list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s) · [Java Spring Boot project with RAG and GenAI](https://www.youtube.com/watch?v=R8VBA_KtUo0) | Hindi | Python; Spring Boot + RAG | W1–W3, W24 |
| CampusX · [Generative AI using LangChain](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) | Hindi | LangChain, RAG | W7–W11 |
| CampusX · [Agentic AI using LangGraph](https://www.youtube.com/playlist?list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL) | Hindi | LangGraph agents, persistence, HITL | W14–W17 |
| CampusX · [Model Context Protocol](https://www.youtube.com/playlist?list=PLKnIA16_Rmva_oZ9F4ayUu9qcWgF7Fyc0) | Hindi | MCP concepts, servers, clients | W16 |
| Krish Naik Hindi · [GenAI crash course with LangChain](https://www.youtube.com/watch?v=7qqGnuRrWxg) · [Complete GenAI & Agentic AI playlist](https://www.youtube.com/playlist?list=PLTDARY42LDV567lWN_5BtoVGjMFKbthGu) | Hindi | LangChain v1 basics, agents, RAG | W7–W17 |

> Framework videos age fast. If a video's code fails, trust the official docs linked in `learn` (versions: LangChain/LangGraph 1.x, MCP SDK v2, Spring AI 2.0).

---

## 5. Practice & labs

| Practice | What | Weeks |
|---|---|---|
| [CodingBat Python](https://codingbat.com/python) · [Exercism Python](https://exercism.org/tracks/python) · [Kaggle Learn Python](https://www.kaggle.com/learn/python) · [HackerRank Python](https://www.hackerrank.com/domains/python) | Python katas (write code daily) | W1–W3 |
| [Anthropic prompt-engineering interactive tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Hands-on prompting exercises | W7 |
| [Lakera Agent Breaker](https://play.lakera.ai/agent-breaker) | Prompt-injection game | W18 |
| DeepLearning.AI short courses (free): [Prompt engineering for developers](https://www.deeplearning.ai/courses/chatgpt-prompt-eng) · [How transformer LLMs work](https://www.deeplearning.ai/courses/how-transformer-llms-work) · [Vector databases](https://www.deeplearning.ai/courses/vector-databases-embeddings-applications) · [Building & evaluating advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag) · [AI agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph) · [MCP with Anthropic](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic) · [Evaluating AI agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) · [Red teaming LLM apps](https://www.deeplearning.ai/courses/red-teaming-llm-applications) · [Finetuning LLMs](https://www.deeplearning.ai/courses/finetuning-large-language-models) · [Post-training of LLMs](https://www.deeplearning.ai/courses/post-training-of-llms) · [Agentic AI (Andrew Ng)](https://www.deeplearning.ai/courses/agentic-ai) | 1–2 h guided notebooks | W5–W21 |
| Hugging Face courses: [all courses](https://huggingface.co/learn) · [Agents course](https://huggingface.co/learn/agents-course/unit0/introduction) · [MCP course](https://huggingface.co/learn/mcp-course/unit0/introduction) · [smol course (fine-tuning)](https://huggingface.co/learn/smol-course/unit0/1) | Free courses with exercises/certificates | W5, W14, W16, W21 |
| Microsoft open curricula: [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) · [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) · [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners) · [Spring AI for Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | Lesson-by-lesson repos | W6–W25 |
| [Google Colab](https://colab.research.google.com/) · [Kaggle notebooks](https://www.kaggle.com/docs/notebooks) | Free GPUs for local-model and fine-tuning work | W20–W21 |
| Project idea hubs: [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) · [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub) · [LLM course roadmap (mlabonne)](https://github.com/mlabonne/llm-course) | Inspiration + reference implementations | any |
| Datasets: [SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) · [Wiki movie plots](https://huggingface.co/datasets/vishnupriyavr/wiki-movie-plots-with-summaries) · [Data job postings](https://huggingface.co/datasets/lukebarousse/data_jobs) · APIs: [Open-Meteo](https://open-meteo.com/en/docs) (+ [historical](https://open-meteo.com/en/docs/historical-weather-api)) · [Arbeitnow jobs](https://www.arbeitnow.com/api/job-board-api) | Free data for builds | W2–W4, W9, W16, W21 |

---

## 6. Tools to install (versions checked 24–25 Oct 2026)

| Tool | Version to use | How | First used |
|---|---|---|---|
| Python | **3.12.x on the company laptop** (W1–W5) · **3.13.x in Codespaces** (W6+; 3.14 works for most libs, 3.15 is too new for several AI libs) | Company Portal (`py`) · devcontainer image `mcr.microsoft.com/devcontainers/python:3.13` | W1 · W6 |
| uv | 0.13.x | Company laptop: already installed via the company JFrog (Section 4 of `03_SETUP_YOUR_LAPTOP.md`) · Codespaces: `pip install uv` in `postCreateCommand` | W1 |
| pip-system-certs | 5.3 (uses truststore) | `uv add pip-system-certs` — only on the company laptop, for Python code that calls internet HTTPS | W2 |
| VS Code + Python, Pylance, Jupyter extensions | latest | [VS Code](https://code.visualstudio.com/) | W1 |
| Git | latest | [git-scm](https://git-scm.com/downloads) | W1 |
| Ruff · mypy | 0.17.x · 2.x | `uvx ruff check .` · `uvx mypy file.py` | W2 · W3 |
| NumPy · pandas · matplotlib · scikit-learn | 2.5 · 3.1 · 3.11 · 1.9 | `uv add ...` (through the company JFrog) | W3 · W4 |
| GitHub Codespaces | free plan: about 120 core-hours + 15 GB-month storage per month | [dev containers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers); 2-core default, 4-core only for W27–W28 | W6 |
| Ollama | 0.40.x | [Linux install](https://ollama.com/download/linux) inside the codespace, then `ollama serve &` | W6 |
| Docker | preinstalled in the codespace (devcontainer feature `docker-in-docker`) | `docker run ...` · `docker compose up` | W8 |
| PostgreSQL · pgvector image | `postgres:18` · `pgvector/pgvector:0.8.7-pg18` | `docker run ... postgres:18` · `docker run ... pgvector/pgvector:0.8.7-pg18` | W8 · W9 |
| PyTorch (via sentence-transformers) | CPU-only build | CPU index in `pyproject.toml` ([uv PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/)) | W9 |
| Redis | 8.x (`redis:8`) — includes the query engine RedisVL needs | `docker run -d -p 6379:6379 redis:8` | W13 |
| Node.js | 22.22+ (promptfoo needs ≥ 22.22) | devcontainer feature `node` | W18 |
| promptfoo | latest | `npx promptfoo@latest` | W18 |
| JDK / Spring | JDK 25 LTS · Spring Boot 4.1.x · **Spring AI 2.0.x** (2.0.2; 2.1 is RC) · LangChain4j 1.22 (awareness) | [start.spring.io](https://start.spring.io/) · devcontainer feature `java` | W23 |
| Azure CLI | latest | devcontainer feature `azure-cli`, then `az login --use-device-code` (personal account) | W25 |
| Locust · OBS Studio | 2.47 · latest | `uv add --dev locust` · [OBS](https://obsproject.com/) | W28 |

**Key Python packages (PyPI, 24–25 Oct 2026):** `openai` 3.x · `google-genai` 2.x · `langchain` 1.4 · `langgraph` 1.2 · `langgraph-checkpoint-sqlite` 3.x · `langchain-postgres` 0.0.x · `mcp[cli]` 2.3 · `langchain-mcp-adapters` 0.3 (still requires `mcp<2`) · `fastapi[standard]` 0.162 · `pydantic` 2.14 · `pydantic-settings` 2.16 · `httpx` 0.28 · `pip-system-certs` 5.3 · `pytest` 9.1 · `tenacity` 9.2 · `numpy` 2.5 · `pandas` 3.1 · `scikit-learn` 1.9 · `tiktoken` 0.14 · `sentence-transformers` 6.2 · `transformers` 5.x · `pgvector` 0.5 + `psycopg` 3.3 · `redisvl` 0.28 · `slowapi` 0.1 · `ragas` 0.4 · `deepeval` 4.3 · `langfuse` 5.x · `opentelemetry-sdk` 1.45 · `openai-agents` 0.24 · `agent-framework` 1.23 · `pydantic-ai` 2.x · `trl` 1.16 · `peft` 0.21 · `unsloth` 2026.10 · `faster-whisper` 1.2 · `docling` 2.x · `presidio-analyzer` 2.2 · `typer` 0.27 · `rich` 15 · `locust` 2.47.

**Accounts to create:** Google AI Studio (Gemini key) · GroqCloud · Hugging Face · Langfuse Cloud Hobby (optional; or self-host) · Google Colab / Kaggle · OpenRouter (optional) · GitHub Codespaces on your personal GitHub account (W6) · Azure (W25: your personal pay-as-you-go account with budgets, set up in the Azure track).
