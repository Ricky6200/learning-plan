# 📚 Azure Track Resources (verified 24–25 Oct 2026)

Free first. Paid items are marked **(paid)**. Weekly sessions link one main resource (plus at most one optional link) and the
week's stretch lists the official modules and labs; this page is the map for all 30 weeks.

## 1. Primary — use these every week

### Official study guides, courses and learning paths
| Exam | Study guide (skills measured) | Official course | Self-paced learning paths (Microsoft Learn) |
|---|---|---|---|
| AZ-900 | [AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) | [AZ-900T00](https://learn.microsoft.com/en-us/training/courses/az-900t00) | [Cloud concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/) · [Architecture & services](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/) · [Management & governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/) (~5 h) |
| AZ-104 | [AZ-104 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) | [AZ-104T00](https://learn.microsoft.com/en-us/training/courses/az-104t00) | [Prerequisites](https://learn.microsoft.com/en-us/training/paths/az-104-administrator-prerequisites/) · [Identities & governance](https://learn.microsoft.com/en-us/training/paths/az-104-manage-identities-governance/) · [Storage](https://learn.microsoft.com/en-us/training/paths/az-104-manage-storage/) · [Compute](https://learn.microsoft.com/en-us/training/paths/az-104-manage-compute-resources/) · [Virtual networks](https://learn.microsoft.com/en-us/training/paths/az-104-manage-virtual-networks/) · [Monitor & back up](https://learn.microsoft.com/en-us/training/paths/az-104-monitor-backup-resources/) (~18 h) |
| AI-200 | [AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200) | [AI-200T00](https://learn.microsoft.com/en-us/training/courses/ai-200t00) | [Container hosting](https://learn.microsoft.com/en-us/training/paths/implement-container-app-hosting-azure/) · [Container Apps](https://learn.microsoft.com/en-us/training/paths/deploy-manage-apps-azure-container-apps/) · [AKS](https://learn.microsoft.com/en-us/training/paths/deploy-monitor-apps-azure-kubernetes-service/) · [Cosmos DB](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-cosmos-db/) · [PostgreSQL](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-database-postgresql/) · [Managed Redis](https://learn.microsoft.com/en-us/training/paths/enhance-ai-solutions-azure-managed-redis/) · [Backend services](https://learn.microsoft.com/en-us/training/paths/integrate-backend-services-ai-solutions/) · [Secrets & config](https://learn.microsoft.com/en-us/training/paths/manage-app-secrets-configuration/) · [Observe & troubleshoot](https://learn.microsoft.com/en-us/training/paths/observe-troubleshoot-apps/) (~36 h) |

### Core docs you'll keep open
- Azure CLI: [get started](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli) · [command reference](https://learn.microsoft.com/en-us/cli/azure/reference-index) · [querying output (JMESPath)](https://learn.microsoft.com/en-us/cli/azure/use-azure-cli-successfully-query)
- IaC: [Bicep overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) · [ARM template syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax) · Learn path [Fundamentals of Bicep](https://learn.microsoft.com/en-us/training/paths/fundamentals-bicep/) · [Bicep modules](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/modules) · [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/) · [Deployment stacks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks) (W28)
- KQL: [overview](https://learn.microsoft.com/en-us/kusto/query/) · [quick reference](https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference)
- Python: [Azure SDK for Python overview](https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview) · [Authenticate Python apps (DefaultAzureCredential)](https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/overview) · [azure-sdk-for-python on GitHub](https://github.com/Azure/azure-sdk-for-python)
- Java: [Azure for Java developers](https://learn.microsoft.com/en-us/azure/developer/java/) · [Spring Cloud Azure](https://learn.microsoft.com/en-us/azure/developer/java/spring-framework/) · [Passwordless Azure SQL for Java](https://learn.microsoft.com/en-us/azure/developer/java/spring-framework/migrate-sql-database-to-passwordless-connection) · [JDBC driver: Microsoft Entra authentication](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-using-azure-active-directory-authentication) (W27, W30)

### Video backbone
- **John Savill's Technical Training** — [channel](https://www.youtube.com/@NTFAQGuy) · [AZ-900 certification course playlist](https://www.youtube.com/playlist?list=PLlVtbbG169nED0_vMEniWBQjSoxTsBYS3) (one short video per objective, W1–W4) · [AZ-900 Study Cram](https://www.youtube.com/watch?v=tQp1YkB2Tgs) (W4–W5) · [AZ-104 Study Cram v2](https://www.youtube.com/watch?v=0Knf9nub4-k) (W15) · [AZ-104 study list playlist](https://www.youtube.com/playlist?list=PLlVtbbG169nGlGPWs9xaLKT1KfwqREHbs)
- **Microsoft Learn** — [AZ-900 course videos](https://www.youtube.com/playlist?list=PLahhVEj9XNTd6H2vpsvm_kBSMsMw9EMUL) · [AZ-104 course videos](https://www.youtube.com/playlist?list=PLahhVEj9XNTcj4dwEwRHozO3xcxI_UHYG) · AI-200 exam prep [1 containers](https://www.youtube.com/watch?v=XHOBLJQZBCU), [2 data](https://www.youtube.com/watch?v=haeOJ2K1UU4), [3 connect & consume](https://www.youtube.com/watch?v=oIalMs581A0), [4 secure & monitor](https://www.youtube.com/watch?v=K2F1uvc8Cr8)

## 2. Secondary / reference (look things up, design, migrate)

| Area | Resources |
|---|---|
| Architecture | [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) · [Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) · [Well-Architected Review assessment](https://learn.microsoft.com/en-us/assessments/azure-architecture-review/) · [Choose a compute service](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) · [Asynchronous messaging options](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging) · [Hub-spoke topology](https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke) · [Connect on-premises networks (hybrid)](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/) · [DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview) |
| Migration (your goal!) | [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) · [Select migration strategies](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/select-cloud-migration-strategy) · [Plan your migration](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/plan-migration) · [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) · [CSV-import assessment + business case](https://learn.microsoft.com/en-us/azure/migrate/tutorial-discover-import) · [AppCAT for Java](https://learn.microsoft.com/en-us/azure/migrate/appcat/java) ([AppCAT 7 quickstart](https://learn.microsoft.com/en-us/azure/migrate/appcat/appcat-7-quickstart)) · [Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/dms-overview) · [PostgreSQL migration service](https://learn.microsoft.com/en-us/azure/postgresql/migrate/migration-service/overview-migration-service-postgresql) ([online tutorial](https://learn.microsoft.com/en-us/azure/postgresql/migrate/migration-service/tutorial-migration-service-iaas-online)) |
| Azure SQL (W27, W30) | [What is Azure SQL?](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview) · [Azure SQL Database free tier](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-tier) · [SQL Server → Azure SQL Database migration guide](https://learn.microsoft.com/en-us/data-migration/sql-server/database/guide) · [SqlPackage](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-download) |
| Landing zones, governance and APIs (W28–W29) | [Landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) · [Design areas](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas) · [Subscription vending](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) · [Defender for Cloud secure score](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls) · [API Management: import and publish](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish) · [Terraform on Azure](https://learn.microsoft.com/en-us/azure/developer/terraform/overview) (awareness) |
| Java workloads | [Migrate Java apps to Azure](https://learn.microsoft.com/en-us/azure/developer/java/migration/migration-overview) · [Spring Boot → App Service](https://learn.microsoft.com/en-us/azure/developer/java/migration/migrate-spring-boot-to-app-service) · [Spring Boot → Container Apps](https://learn.microsoft.com/en-us/azure/developer/java/migration/migrate-spring-boot-to-azure-container-apps) · Learn path [Get started with Java on Azure](https://learn.microsoft.com/en-us/training/paths/get-started-java-azure/) |
| AI back ends | [RAG solution design guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) · [Cosmos DB vector search](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-search) · [pgvector on Azure PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-use-pgvector) · [Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview) · [Cache-aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside) |
| Limits & cost | [Subscription and service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) · [Pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) · [Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management) · see [COST_SAFETY_AND_ACCOUNT_SETUP.md](COST_SAFETY_AND_ACCOUNT_SETUP.md) |
| Exam logistics | [Exam duration & experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience) · [Retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy) · [Renewal](https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification) · see [CERTIFICATION_GUIDE.md](CERTIFICATION_GUIDE.md) |

## 3. Books (optional)

| Book | Use | Note |
|---|---|---|
| [Exam Ref AZ-104 Microsoft Azure Administrator, 2nd Edition](https://www.microsoftpressstore.com/store/exam-ref-az-104-microsoft-azure-administrator-9780138345938) — Charles Pluta, Microsoft Press (2024) **(paid)** | Structured reading for W6–W15 if you like books | Published before the Apr 2026 skills update — check the study guide's change log for what moved |
| *(none yet for AI-200)* | — | The exam launched in 2026; the official [AI-200T00 course](https://learn.microsoft.com/en-us/training/courses/ai-200t00) is the best "book" |

## 4. YouTube — English and Hindi options

| Language | Channel / playlist | Best for |
|---|---|---|
| English | [John Savill's Technical Training](https://www.youtube.com/@NTFAQGuy) · [Azure Master Class (v3 parts 1-7 + v2 modules)](https://www.youtube.com/playlist?list=PLlVtbbG169nGccbp8VSpAozu3w9xSQJoY) | Clear whiteboard deep dives; crams for every exam |
| English | [Microsoft Learn](https://www.youtube.com/@MicrosoftLearn) · [AZ-204-era course videos](https://www.youtube.com/playlist?list=PLahhVEj9XNTcQ-rtUyuly3KpWFP9xzp7A) | Official course walkthroughs; the AZ-204 episodes on Functions, Cosmos DB, Key Vault, App Configuration and Event Grid still help for AI-200 |
| English | [Adam Marczak - Azure for Everyone](https://www.youtube.com/@AdamMarczakYT) · [AZ-900 full course](https://www.youtube.com/playlist?list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM) | Short, beginner-friendly AZ-900 episodes (older recordings; concepts hold) |
| English (Indian creator) | [Abhishek Veeramalla](https://www.youtube.com/@AbhishekVeeramalla) · [Azure Zero to Hero](https://www.youtube.com/playlist?list=PLdpzxOOAlwvIcxgCUyBHVOcWs0Krjx9xR) | Practical, DevOps-flavoured Azure projects and interview questions |
| English | [Using pgvector with PostgreSQL on Azure (Pamela Fox, Microsoft)](https://www.youtube.com/watch?v=sCX_sB2dQHY) | W19 pgvector deep dive |
| Hindi | [Technical Guftgu - Azure/AZ-104 in Hindi](https://www.youtube.com/playlist?list=PLBGx66SQNZ8ZIxo2wu2x9eU9HHvjToHBp) ([channel](https://www.youtube.com/@TechnicalGuftgu)) | AZ-900/AZ-104 concepts explained in Hindi |
| Hindi | [AZ-900 Full Course in Hindi (2025)](https://www.youtube.com/playlist?list=PLks8W396lro4RpDs-teA87oaGH6nRU5Zf) | W1–W4 second explanation |
| Hindi | [New Azure Administrator AZ-104 (Hindi)](https://www.youtube.com/playlist?list=PLAwzouYxcpPiYRHVBsfDmzIiiak3xM_BS) | W6–W15 second explanation |
| Hindi | [AI-200 Full Course 2026 (Azure in Hindi)](https://www.youtube.com/playlist?list=PL5TTTZj-297nFs3InPjph4E-07ayWa8mG) | W16–W25 second explanation |

Community videos (especially the newer Hindi ones) are a *second* explanation — when they disagree with the study
guide or Learn docs, the official page wins.

## 5. Practice and labs

| Resource | What it is | When |
|---|---|---|
| [AZ-900 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/practice/assessment?assessment-type=practice&assessmentId=23) | Free, official question style | W4 Boss (run 1), W5 Tue (run 2) |
| [AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21) | Free, official | W9 Boss, W15 (runs 1–2 + go/no-go gate), W16 (run 3) |
| [AI-200 practice assessment (AI Skills Navigator)](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b) | Free, official; sign-in required | W19 lab (10 questions), W25 (runs 1–2), W26 (run 3) |
| [Exam sandbox](https://aka.ms/examdemo) | The real exam UI with sample question types | W5 Wed (repeat before AZ-104/AI-200 if needed) |
| [AZ-104 official labs](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/) | Step-by-step admin labs (Entra, RBAC/Policy, storage, VMs, web apps, containers, networking, backup, monitoring) | Saturdays W6–W8 (Labs 01, 02a, 07); stretches W7, W11–W13 (Labs 02b, 09a, 09c, 04, 06, 11) |
| AI-200 module exercises (inside each [AI-200T00](https://learn.microsoft.com/en-us/training/courses/ai-200t00) module) | ~30-minute guided Python exercises in your subscription | Saturdays W17, W18, W21, W24; stretches W18–W24 |
| [Microsoft Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/) (free) | Hosted, scenario-based lab assessments; 72-hour wait between attempts | Stretch goals (W6, W9, W12–W14, W19, W23) |
| [Exam Readiness Zone](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/) | Official exam-prep episodes | W15 |
| [Azurite](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite) | Free local Azure Storage emulator | W3 (Path B: VS Code extension on the company laptop; fallback `npx azurite` in a Codespace) |
| [GitHub Codespaces](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) | Cloud dev container from your `azure-labs` repo (free monthly quota; 2-core by default) | W3 Path B, W25 Boss (pgvector + Redis), W26–W30 (SQL Server 2022 source, SqlPackage, AppCAT) |
| [Well-Architected Review](https://learn.microsoft.com/en-us/assessments/azure-architecture-review/) | Free self-assessment that exports recommendations | W29 Wed |
| [Azure Samples on GitHub](https://github.com/Azure-Samples) | Reference code for almost every service | Any time you're stuck |

## 6. Tools to install (versions current on 24–25 Oct 2026)

Company laptop: Azure CLI, `az bicep build` and the Bicep, Azure Resources, Azure Functions, Azurite and Kubernetes VS Code
extensions (installed 26 Oct); personal Microsoft sign-in is blocked there.
Everything below except the CLI is installed on your **personal laptop** in W5 Sat, or lives in a Codespace.

| Tool | Version | Install / docs | First used |
|---|---|---|---|
| Azure CLI | 2.91.0 | [Install](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) | W1 |
| Bicep CLI | v0.48.1 (`az bicep install` / `az bicep upgrade`) | [Install Bicep tools](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/install) | W1, W10, W28 |
| VS Code + extensions (personal laptop) | Latest; [Azure Tools pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack), [Bicep](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep), Python | [VS Code](https://code.visualstudio.com/) | W5 Sat |
| PowerShell 7 + Az module | Az 16.4.0 (`Install-Module Az -Scope CurrentUser`) | [Install Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-azure-powershell) | W5 Sat (PowerShell steps W6–W14) |
| GitHub Codespaces (instead of local Docker) | Universal image + `azure-cli` dev container feature | [Codespaces billing and quota](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) | W3, W25, W26–W30 |
| AzCopy | v10.34.1 | [AzCopy v10](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10) | W8 |
| Azure Storage Explorer | v1.46.0 | [Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/) | W8 |
| PostgreSQL client (`psql`) | 16 or 17 | [PostgreSQL downloads](https://www.postgresql.org/download/) | W14, W18, W29 |
| JDK | JDK 25 on the personal laptop (Cloud Shell has a JDK + Maven for W11) | — | W14, W27, W30 |
| Python | 3.12 via [uv](https://docs.astral.sh/uv/) (`uv venv --python 3.12`), same version as the AI track; AI-200 exercises need 3.12+ | [python.org](https://www.python.org/downloads/) | W16 |
| Azure Functions Core Tools | 4.16.0 | [Develop locally with Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) | W21 |
| kubectl | v1.37.1 (or Cloud Shell / `az aks install-cli`; stay within one minor version of your cluster) | [Install tools](https://kubernetes.io/docs/tasks/tools/) | W23 |
| SqlPackage | Latest (`dotnet tool install -g microsoft.sqlpackage`, in the Codespace) | [Download SqlPackage](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-download) | W26 Sat, W27, W30 |
| AppCAT for Java | 7.x CLI | [AppCAT 7 quickstart](https://learn.microsoft.com/en-us/azure/migrate/appcat/appcat-7-quickstart) | W26 Sat, W27 |

**Python packages** (`uv pip install ...`, versions on PyPI on 24–25 Oct 2026): `azure-identity` 1.26.0 · `azure-mgmt-resource` 26.0.0 ·
`azure-storage-blob` 12.31.0 · `azure-cosmos` 4.17.1 · `psycopg[binary,pool]` 3.3.6 · `pgvector` 0.5.1 · `redis` 8.1.0 ·
`azure-servicebus` 7.15.0 · `azure-eventgrid` 4.22.1 · `confluent-kafka` 2.16.0 + `certifi` 2026.10.23 (W20 Kafka endpoint) ·
`azure-functions` 2.3.0 · `azure-keyvault-secrets` 4.11.3 · `azure-appconfiguration-provider` 2.5.0 ·
`microsoft-opentelemetry` 1.5.0 (the Microsoft OpenTelemetry Distro; existing apps may still use `azure-monitor-opentelemetry` 1.8.11).
Pin versions in `azure-labs/py/requirements.txt` so labs stay reproducible. Embeddings come from the AI track's local
models — Ollama `nomic-embed-text` (768 dimensions) or `all-MiniLM-L6-v2` via sentence-transformers (384) — downloaded on
the personal laptop or in a Codespace (not on the company network); size every vector field/column to match the model you use.
