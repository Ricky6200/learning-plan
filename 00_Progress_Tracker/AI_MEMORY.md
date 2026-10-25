# 🧠 AI MEMORY — the AI mentor reads this FIRST in every new session

> **Why this file exists:** the AI (GitHub Copilot) loses its memory when a chat/context ends.
> Everything needed to continue *without starting from zero* lives in `00_Progress_Tracker/`.
> **Markdown is the source of truth.** PDFs are read-only copies.

---

## 1) Magic prompt — paste this at the start of every new session

```text
Read C:\Users\rkumar48\Personal_Learning\00_Progress_Tracker\AI_MEMORY.md and follow its
"Session start protocol". Then tell me where I am, my streak/XP, and today's tasks.
```

For the Sunday test, paste instead:

```text
Read 00_Progress_Tracker\AI_MEMORY.md and WEEKLY_TEST_PROTOCOL.md. Run my Week <N> test now.
```

---

## 2) Learner profile (facts given by the user — do not assume beyond this)

| Item | Value |
|---|---|
| User | rkumar48 · CSE graduate 2023 · ~3 yrs software experience (as of Oct 2026) · India (IST, UTC+05:30) |
| Current job | Java + Spring Boot (mostly maintenance / small features) + SQL DB with stored procedures |
| Java level | Understands code but **struggles to write complex code**. Self-rated weak in Core Java: OOP, methods, constructors, GC, multithreading |
| DSA level | Was good in college (C++), forgot everything → **beginner now (< 50 problems)**, weak on patterns. DSA language chosen: **Java** |
| Azure level | Very little hands-on; knows basics conceptually |
| AI preference | Python-first for AI engineering **+ Spring AI** to integrate AI into Java backends (user asked AI to decide; decided) |
| Time budget | ~7 months (30 weeks, Mon 26 Oct 2026 → Sun 23 May 2027), average 3.5–4 h/day → **Mon–Fri 3.5 h, Sat 4.5 h, Sun 3.5 h (weekly test)** ≈ 25.5 h/week |
| Wants | Daily tasks that are *not boring*, weekly tests across all 5 tracks, logged weak areas, PDFs + Markdown |
| Machines | **Company laptop** = main machine (fast; company AI tools such as GitHub Copilot; VS Code, IntelliJ). Software only via the company's software portal or IT; the corporate proxy blocks public PyPI downloads and free AI APIs; Python packages come from the company's JFrog Artifactory. **Personal laptop** = slower; used for AI coding from W4 (Codespaces), personal-Microsoft-account tasks (certification profile, exams, personal Azure labs) and job search. Company-specific details (internal addresses, test results, tool paths, account restrictions) live ONLY in **`COMPANY_ENVIRONMENT.local.md`** — local, never committed |
| Accounts | Personal GitHub = **Ricky6200** (works on the company laptop; personal repos in `C:\dev\personal`; push verified 24 Oct). Personal Microsoft account = certification profile, used on the personal laptop. The company provides the Azure exams (voucher process via L&D) |
| Setup status | Section 3 of `03_SETUP_YOUR_LAPTOP.md` (local only, not in Git) |

---

## 3) Goals — definition of done at Week 30 (Sun 23 May 2027)

1. **Java backend:** strong Core Java (OOP, collections internals, generics, streams, Java 8→25, concurrency, JVM/GC) + Spring Boot internals, JPA, transactions, security, testing, microservices, Kafka, Docker, Kubernetes, CI/CD. **Capstone "TicketVerse"** deployed on Azure.
2. **DSA:** 294 core + 202 bonus LeetCode problems across all major patterns (all free Blind 75, 137/143 free NeetCode 150), ≤ 2 new per day plus generated daily re-solves (spaced repetition), contests and mocks → solve the large majority of standard interview questions (Easy/Medium + common Hard) in 30–40 min.
3. **System Design:** LLD (SOLID, GoF patterns, ~18 machine-coding problems in Java) + HLD (fundamentals → distributed systems → ~20 case studies) + timed mocks.
4. **Azure:** AZ-900 ✅ → AZ-104 ✅ → AI-200 ✅ + migration lab + capstone deployment.
5. **AI Engineering:** LLM fundamentals → prompting/structured output → embeddings/RAG → evals → agents (LangGraph) → MCP → guardrails → LLMOps → OSS models/fine-tuning → Spring AI → Azure AI (Microsoft Foundry) → AI system design. Portfolio projects + AI features in TicketVerse.
6. **Career:** resume, LinkedIn/Naukri, STAR stories, mock interviews; start applying ~Week 20.

---

## 4) Key decisions (with reasons). Do NOT change without asking the user; log changes in Section 10.

| # | Decision | Reason / evidence (verified Oct 2026) |
|---|---|---|
| D1 | Start **Mon 26 Oct 2026**; **30 weeks** (extended from 26 on 25 Oct 2026 — see D26), ends **Sun 23 May 2027**; Week N starts 26-Oct-2026 + 7·(N−1) days; Sunday = weekly test | User chose; user approved ~7 months for a solid, synced plan |
| D2 | Azure path **AZ-900 (exam W5) → AZ-104 (exam W16) → AI-200 (exam W26)**; AI-103 optional after plan | **AZ-204 retired 31 Jul 2026**, replaced by **AI-200 "Developing AI Cloud Solutions on Azure"** (Azure AI Cloud Developer Associate; skills measured as of 7 Oct 2026; expects Python, containers, Cosmos DB, PostgreSQL+pgvector, Managed Redis, Service Bus/Event Grid, Functions, Key Vault, App Config, OpenTelemetry/KQL). **AI-102 retired 30 Jun 2026 → AI-103**. AZ-900 updated 20 Jul 2026; AZ-104 updated 17 Apr 2026. AI-200 placed last because it depends on Python, Docker/K8s, vector DBs learned earlier in other tracks |
| D3 | Versions: **JDK 25 LTS**, **Spring Boot 4.1.x** (use newest stable when project starts), **Spring AI 2.0.x**, **Kafka 4.x (KRaft only)**, LangChain 1.x / LangGraph 1.x, MCP Python SDK 2.x, Microsoft Agent Framework 1.x | Checked Maven Central / PyPI / Adoptium on 24 Oct 2026 |
| D4 | Kubernetes ingress taught via **Gateway API** | **ingress-nginx retired March 2026** (Kubernetes blog) |
| D5 | Azure portal naming: **Microsoft Foundry** (formerly Azure AI Foundry/AI Studio) | Renamed at Ignite Nov 2025 |
| D6 | Capstone **TicketVerse** = AI-powered movie/event ticket booking platform (monolith → microservices → Kafka saga → Docker → K8s → Azure → AI assistant) | Maps directly to classic LLD (BookMyShow) + HLD (Ticketmaster) interview questions; rich concurrency (seat locking) |
| D7 | AI projects (30-week layout): TerminalGPT (W6) · SemanticSearch API (W9) · DocuMind RAG (W10–W13) · CareerPilot agent + MCP (W14–W19) · FineTune Lab (W21) · Doc/Resume extractor (W22) · Spring AI `ticketverse-ai` service, owned by the AI track (W23–W24) · TicketVerse AI features (W27, with Java W27 platform hooks) · capstone demo (W28) | CareerPilot also helps the user's own job hunt |
| D8 | DSA in Java, pattern-by-pattern, 13 core problems/week (+ bonus), spaced repetition (D+1, D+7, D+21) | Beginner restart; quality > quantity |
| D9 | Markdown = source of truth with checkboxes; PDFs regenerated via `00_Progress_Tracker/tools/build_pdfs.py` | User chose Markdown + PDF |
| D10 | Gamification: XP, levels, streaks, badges, 6 Seasons (W1–4, W5–9, W10–15, W16–20, W21–25, W26–30) with Boss Battles at **W4, W9, W15, W20, W25, W30** (every track's Saturday in those weeks is a timed `BOSS BATTLE:`; exam weeks are never boss weeks) | User asked for a non-boring, exciting path |
| D11 | Added a 6th folder **Career & Interview Prep** and a gap analysis (`02_GAP_ANALYSIS_What_You_Were_Missing.md`) | User asked "suggest what I am missing" |
| D12 | Environment constraint: on the company laptop, public PyPI downloads are **blocked by the corporate proxy** (verified 24 Oct 2026) → Python packages come from the company's JFrog (D19); the PDF tool is dependency-free (stdlib + Edge headless) | Don't bypass security controls |
| D13 | **GitHub Models was retired 30 Jul 2026** → free LLM options are Gemini (AI Studio) free tier, Groq, OpenRouter `:free` models, Ollama (local). Python: **3.12** on the company laptop (Company Portal; uv Python downloads disabled), 3.13 is fine in Codespaces | GitHub changelog 2026-07-01 |
| D14 | TicketVerse Azure deploy target = **Azure Container Apps** (scale-to-zero, cheapest; AI-200 skill), done in **Java W28** with the infrastructure provisioned by **Azure W28 Sat** (Bicep). AKS is practised in the Azure W23 Friday lab (1 node, then stop/delete) | Cost + exam alignment |
| D15 | Library facts to keep consistent: **JUnit 6** (Jupiter API = JUnit 5), **Testcontainers 2.0.x**, Jackson 3 (`tools.jackson`), Hibernate 7.4, Spring Security 7.1 (all managed by Boot 4.1.x); Spring AI 2.0 GA: advisor artifact renamed `spring-ai-vector-store-advisor`, no separate Azure OpenAI starter (use OpenAI module); MCP Python SDK v2 renamed `FastMCP` → `MCPServer`; MCP spec revision 2026-07-28 (stateless) | Verified on Maven Central / PyPI / docs, 24 Oct 2026 |
| D16 | **Machine split** (recommended 24 Oct; pending the user's policy check): company laptop = DSA, Java, SD, Azure, Python basics (AI W1–W3), mentor chats & tests. Personal laptop *as a browser* (GitHub Codespaces / Colab) = AI-track coding that calls LLMs from **W6 (Mon 30 Nov)**, CareerPilot, all job-search activity. **Mode B** if pushing to personal GitHub from the company laptop is blocked/not allowed: write code in Codespaces on the personal laptop | Free AI APIs blocked on company network; job search must stay off company devices; user prefers company laptop |
| D17 | Never help the user bypass company controls (no download-and-run scripts, proxies/VPNs, or routing blocked AI APIs through cloud machines opened on the company laptop). Approved channels only: Company Portal, Artifactory, IT requests — otherwise use the personal laptop | Security/policy compliance |
| D18 | Repos on **personal GitHub** (personal email, HTTPS push), not company GitLab. `Personal_Learning` to be backed up as a private repo `learning-plan` once the push test passes. Microsoft Learn / certification profile on a **personal Microsoft account** | Portfolio visibility + portability when leaving |
| D19 | Python on the company laptop = **3.12** at `C:\Program Files\Python312` (default for `py`; plain `python` = old 3.9) + `venv` + pip via the company JFrog, configured to the **company developer-portal standard**: the shared Python repository for not-yet-onboarded users + `trusted-host` for the JFrog host, written by `tools/setup_jfrog_pip.py` (run it **first** — it waits for the Set Me Up copy; `--repo <shared repository>` with automatic fallback to the copied repository; repository name/URLs in `COMPANY_ENVIRONMENT.local.md`). **Working since 24 Oct** (shared repository; uv is available there too) with a fresh token; the token exposed in a screenshot was revoked (verified: JFrog refuses it). Token renewal due before 24 Oct 2027. pip must work by Mon 2 Nov (AI W2); AI W1 works without packages | PyPI blocked; follow the company standard |
| D20 | JDK: **Amazon Corretto 25 installed 24 Oct** from the Company Portal (`C:\Program Files\Amazon Corretto\jdk25.0.0_36`, build 25+36; folder name changes with portal updates) = the learning-project JDK **from Week 1**, via the IntelliJ per-project SDK (+ Maven runner/importer "Use Project JDK") or per-window `$env:JAVA_HOME`. Its installer set the system `JAVA_HOME` and put its `bin` first on the system PATH → the AI set the **user** `JAVA_HOME` = `C:\Program Files\Java\jdk-11` so `mvn` (work) stays on JDK 11 (verified); plain `java`/`javac` = 25 (system PATH, admin needed to change). Maven on Corretto 25 verified (the user's Maven settings mirror everything to the company JFrog). Corretto's `cacerts` lacks the corporate proxy root → programs calling internet HTTPS directly get PKIX errors → use `-Djavax.net.ssl.trustStoreType=Windows-ROOT` (verified; no admin). **Vendor:** Corretto was the only JDK 25 offered (Temurin and Microsoft OpenJDK only up to 21); same Java SE 25, so the plan's Dockerfiles/GitHub Actions stay on Temurin 25. Never self-download on the company laptop. **Containers: Podman** — the company standard (Docker isn't allowed on company laptops); it is pre-installed in the company's WSL Ubuntu image, which also ships kubectl, kind and Helm. Self-service from Company Portal (the laptop already has the developer profile; WSL not installed yet on 25 Oct). Same CLI (`alias docker=podman`, Compose via `podman-compose`); images through the company JFrog mirror after `podman login`; Testcontainers runs inside WSL (`DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock`, `TESTCONTAINERS_RYUK_DISABLED=true`); kind with `KIND_EXPERIMENTAL_PROVIDER=podman`. Needed by **Mon 4 Jan (Java W11)**; Kubernetes tools by **Mon 29 Mar (Java W23)**; Codespaces fallback. Exact steps in the local setup guide (N3) | JUnit 6 / Spring Boot 4 need Java 17+; don't break work builds |
| D21 | Azure accounts: **company Visual Studio subscription credit** (Professional = $50/month, capped, refreshes monthly) or company sandbox, if allowed, for W1–W5 and post-free-credit labs — on the office laptop; **personal free account on Tue 1 Dec (W6), used on the personal laptop** (personal Microsoft sign-in is blocked on the office laptop) for AZ-104 identity labs (needs own tenant / Global Admin) and the TicketVerse W28 portfolio deploy | Identity labs impossible in a corporate directory; avoid bill risk |
| D22 | Certifications: the company provides the AZ-900/AZ-104/AI-200 exams. Account linking is impossible (personal account blocked on the office laptop, work account blocked on the personal laptop) and not needed: the Learn profile = **personal** Microsoft account, created and used on the **personal laptop**; ask L&D for **voucher codes** redeemable on the personal profile (if they insist on the work account, ask Microsoft certification support to move the cert before leaving). Online exams (Pearson VUE OnVUE) on the personal laptop — system test by Sat 21 Nov (Azure W4, booking day). AZ-900 never expires; associate certs renew yearly via a free online assessment | Certifications must stay with the user; Pearson recommends personal computers |
| D23 | Git on the company laptop (**set up and verified 24 Oct**): personal repos under `C:\dev\personal` with `includeIf gitdir/i` → `~/.gitconfig-personal` (GitHub noreply email); clone URLs include `Ricky6200@`; Git Credential Manager sign-in via device code in **Chrome** (Edge holds the work GitHub session). SSH :22 is blocked → HTTPS only. `Personal_Learning` is NOT under `C:\dev\personal` — when creating the `learning-plan` repo, add `include.path = ~/.gitconfig-personal` to its local config | Global git email is the work address; two GitHub identities on one machine |
| D24 | uv: **installed 24 Oct** (0.13.5) from the company JFrog with `py -3.12 -m pip install --user uv`; the user Scripts folder (`%APPDATA%\Python\Python312\Scripts`) appended to the **user** PATH (registry type REG_EXPAND_SZ kept; old value backed up in the session folder); configured to the company standard with `setup_jfrog_pip.py --uv`: `%APPDATA%\uv\uv.toml` with the index URL **without credentials** (+ `system-certs` — uv ≥0.13 renamed `native-tls`, `python-preference = only-system`, `python-downloads = never`), credentials via `uv auth login` (token on stdin; stored in `%APPDATA%\uv\credentials`), and `uv python pin --global 3.12` (else uv picks the PATH's 3.9). Verified: `uv venv` → 3.12, `uv pip install requests` through JFrog. Plan's uv commands work as written; `uv python install` is not used | User wanted uv; Company Portal doesn't have it |
| D25 | **VS Code extensions on the company laptop are allow-listed by company policy.** Allowed (verified 24 Oct): Python, Pylance, Jupyter, Docker DX (`docker.docker`), Remote-WSL, Mermaid, draw.io, Ruff, YAML. **Blocked:** the `ms-azuretools` publisher (Bicep, Azure Resources, Azure Functions, Container Tools), Azurite, Kubernetes tools → Bicep via the `az bicep` CLI (works), Azurite and Functions Core Tools in a Codespace / on the personal laptop; the user asks IT to allow-list them (request text in the local setup guide) | Company policy; keep the plan runnable without them |
| D26 | **30-week restructure (25 Oct 2026).** Five independent track audits (each rated its track 7–7.5/10: content strong, sessions overloaded, some cross-track "used before taught" gaps) → one merged spec. Inserted weeks: Java W10 core gaps (I/O, NIO.2, reflection, Mockito), W12 Spring Core, W18 microservices split, W25 loose ends; AI W3 Python III, W4 ML fundamentals, W8 Docker/SQL/FastAPI, W29 advanced/buffer; SD W10 timed LLD, W21 batch-vs-stream + job scheduler, W28–W29 mocks; Azure W27–W30 migration + IaC + capstone; DSA W27–W30 hard bank, company sets, OA, final speed-run (W26 = light re-solve week). Daily DSA re-solves generated automatically (weekdays 1 from D+7; Saturday 1–2 Easy/Medium from D+21; least-re-solved first). Session rule: one concept + one exercise; one main resource; "Done when" | User asked for a full cross-check and accepted ~7 months for a solid, in-sync plan |

---

## 5) Folder map

```text
Personal_Learning/
├─ 00_START_HERE.md                     ← master guide (how the system works)
├─ 01_MASTER_CALENDAR.md                ← 30 weeks × 5 tracks with dates, bosses, exams
├─ 02_GAP_ANALYSIS_What_You_Were_Missing.md
├─ 03_SETUP_YOUR_LAPTOP.md              ← laptop setup guide + setup status (Section 3) — LOCAL ONLY (gitignored)
├─ 00_Progress_Tracker/                 ← AI memory + logs (THIS folder)
│   ├─ AI_MEMORY.md  PROGRESS_DASHBOARD.md  DAILY_LOG.md  AI_SESSION_LOG.md
│   ├─ WEEKLY_TEST_PROTOCOL.md  TEST_SCOREBOARD.md  WEAKNESS_TRACKER.md
│   ├─ Weekly_Tests/Week-XX-Test.md     ← created on each Sunday (questions, answers, grading)
│   ├─ COMPANY_ENVIRONMENT.local.md     ← company-specific environment facts — LOCAL ONLY (gitignored)
│   └─ tools/build_pdfs.py              ← regenerate PDFs after edits
│       tools/plan_source/              ← plan data + generator (gen.py needs --force; RE-PLANNING ONLY — it overwrites checkboxes)
│       tools/setup_jfrog_pip.py        ← connects pip (and `--uv`) to the company JFrog; token never printed
├─ .gitignore                           ← this folder = private GitHub repo `learning-plan`; *.local.md, 03 guide and PDFs stay local
├─ 01_Daily_Planner/Week-01.md … Week-30.md   ← the DAILY checklist (all 5 tracks per day)
├─ Java + Spring + Microservices + Kafka + Docker + Kubernetes/  (README, RESOURCES, ROADMAP, Weeks/, Project_TicketVerse/)
├─ DSA/              (README, RESOURCES, ROADMAP, PATTERNS_CHEATSHEET, REVISION_TRACKER, Weeks/)
├─ System Design/    (README, RESOURCES, ROADMAP, frameworks, Weeks/)
├─ Azure Cloud/      (README, RESOURCES, ROADMAP, CERTIFICATION_GUIDE, Weeks/)
├─ AI Engineering/   (README, RESOURCES, ROADMAP, PROJECTS, Weeks/)
└─ Career & Interview Prep/
```

---

## 6) Session start protocol (the AI MUST follow, in order)

1. Read: **this file** → `PROGRESS_DASHBOARD.md` → `WEAKNESS_TRACKER.md` → last entry of `AI_SESSION_LOG.md` → current `01_Daily_Planner/Week-XX.md` → `COMPANY_ENVIRONMENT.local.md` (if it exists) → (until every item is ✅) the setup status in Section 3 of `03_SETUP_YOUR_LAPTOP.md` — ask about pending items and update that table.
2. Work out today's **calendar** Week/Day (Week 1 = Mon 26 Oct 2026). Compare with the **actual** position in `PROGRESS_DASHBOARD.md` (the learner may be behind/ahead). Use the actual position for tasks.
3. Open the session with: Season · Week · Day · streak · XP/level · today's checklist (from Daily_Planner) · any **remediation** items due from `WEAKNESS_TRACKER.md` · any **reminders due from Section 11** (remind-from date ≤ today and not ✅).
4. During the session: teach, review code, quiz. When the learner reports completion → tick the checkbox in Daily_Planner, append to `DAILY_LOG.md`, update XP in the dashboard.
5. On Sunday (or when asked): run the test exactly per `WEEKLY_TEST_PROTOCOL.md`; save it to `Weekly_Tests/Week-XX-Test.md`; update `TEST_SCOREBOARD.md`, `WEAKNESS_TRACKER.md`, dashboard; add remediation items into next week's Daily_Planner "Fix-it" section.
6. Before the session ends or context gets long: append a **handoff** entry to `AI_SESSION_LOG.md` (what happened, open items, next step) and update the dashboard. Never leave progress only in chat.

---

## 7) Catch-up rules (if the learner falls behind)

- **Missed 1 day:** do that day's DSA + Java on the next day's DSA/Java slots; push rotating-track items to Sunday's 30-min buffer.
- **Missed 2–4 days:** finish **Core** items only; skip "Stretch"; still take the Sunday test on what was covered.
- **Behind ≥ 1 full week:** do NOT silently shift everything. Propose a re-plan to the user (compress Stretch, merge review days, move exam dates) and record it in Section 10.
- Certification exam dates (W5, W16, W26) are fixed anchors; move them only with the user's agreement.
- Festivals/office crunch weeks: allowed "Lite Week" = DSA 1 problem/day + Java 45 min + Sunday test (record in log).

---

## 8) XP & levels (keep consistent everywhere)

| Action | XP |
|---|---|
| Each completed daily block (DSA / Java / AI / SD / Azure) | +10 |
| LeetCode problem solved: Easy / Medium / Hard (first time) | +5 / +10 / +20 |
| Re-solve from revision list (≤ target time) | +5 |
| Weekly test | + (overall % score) e.g. 78% → +78 |
| Boss Battle cleared | +300 |
| Certification passed | +500 |
| Project milestone shipped (tagged release / deployed) | +200 |
| 7-day streak | +50 (30-day: +250) |

Levels: L1 Trainee 0 · L2 Code Cadet 500 · L3 Junior Dev 1,500 · L4 SDE-1 3,000 · L5 SDE-2 5,000 · L6 Senior SDE 7,500 · L7 Staff Engineer 10,000 · L8 Principal Architect 13,000.

---

## 9) Rules for the AI mentor

- Never invent progress, scores, or hours — ask the learner.
- Be honest and specific about weaknesses; always attach a concrete remediation (exact problems, topics, resources, due date).
- Prefer making the learner **write code** (the core gap). Review it like a senior engineer (correctness, edge cases, complexity, naming, tests).
- Don't restructure the plan silently; propose → get approval → log in Section 10.
- When facts may have changed (cert syllabi, versions), verify on the web before advising.
- Keep tracker files lean: when `DAILY_LOG.md` exceeds ~400 lines, move old months to `DAILY_LOG_ARCHIVE_<yyyy-mm>.md`.
- **Privacy split:** this folder is backed up to the user's private GitHub repo `learning-plan`. Company-specific facts (internal hostnames, proxy/security observations, endpoint test results, internal tool versions) go ONLY into `COMPANY_ENVIRONMENT.local.md` (gitignored, with `03_SETUP_YOUR_LAPTOP.md` and the PDFs). Every tracked file — including this one and `AI_SESSION_LOG.md` — must stay generic ("company laptop", "corporate proxy", "company JFrog"). Commit only when the user asks, and let the user run `git push`.
- Never handle secrets: tokens and passwords go from the user's browser/clipboard straight into local config files (see `tools/setup_jfrog_pip.py`), never into chat or tracked files. Never test company systems with fake credentials (risk of account lockout).
- **If a secret shows up in a screenshot or message** (even partly): never repeat it, tell the user to revoke it and generate a new one (only the exposed one — older tokens may be in use), and remind them to crop/blur credential boxes before sharing.
- **The AI's own terminal uses the Copilot app's bundled Git with its own GitHub credential helper (the user's work account).** So the AI must never `push`/`fetch`/`clone` personal repos — that would use the wrong identity, and it can't see private personal repos anyway. The user runs those commands in their own terminal; the AI may run local-only Git commands (`init`, `add`, `commit`, `status`, `log`).
- After editing Markdown plans, regenerate PDFs: `python "00_Progress_Tracker\tools\build_pdfs.py"`.
- **Chat commands** (the learner may type these; also listed in `00_START_HERE.md`): `start` (= magic prompt: position, today's blocks, fix-its, reminders) · `doubt: …` (explain simply with an example; a doubt that repeats goes to `WEAKNESS_TRACKER.md`) · `teach: <topic>` (10-min lesson + 3 check questions) · `hint: <problem>` (hint ladder — pattern → approach → pseudo-code; no full code unless `solution:`; the learner marks it 🟡/🔴 in the DSA revision tracker) · `review: <repo/path/paste>` (senior-level code review) · `quiz: <topic>` (5 questions, scored, not logged as a test) · `log today: …` (tick the planner, append `DAILY_LOG.md`, XP/streak, carry-overs, doubts) · `test week <N>` (Sunday test per `WEEKLY_TEST_PROTOCOL.md`) · `status` (dashboard summary) · `behind` (catch-up plan per Section 7) · `lite day` (minimum viable day) · `remind` (Section 11 items) · `wrap up` (handoff entry in `AI_SESSION_LOG.md`).

---

## 10) Decisions & changes log (append-only)

| Date | Change | Reason | Approved by user? |
|---|---|---|---|
| 2026-10-24 | Initial 26-week plan created (D1–D11) | Kick-off session | Yes (scope & preferences given in kick-off) |
| 2026-10-24 | Environment decisions D16–D21; added `03_SETUP_YOUR_LAPTOP.md`; AI W1, Java W1 Mon, SD W1 Mon adapted (pip/venv, current JDK); planner environment reminders (W1, W2, W4, W5, W9, W18) | User's laptop situation (company laptop preferred; Company Portal installs; proxy blocks) | Recommended — user asked for steps; policy check pending |
| 2026-10-24 | D19/D20 updated (`py` launcher, JFrog Set Me Up, Corretto 21 now, JDK 25 by 6 Dec); D22 (certification profile), D23 (git identity setup); setup guide rewritten (status N1–N11); "§" replaced with "Section" in all docs; planner reminder added for W6 (JDK 25) | User's follow-up: Python 3.12/VS Code/Azure CLI installed, Corretto 21 available, personal GitHub Ricky6200, company-paid exams | Yes — user is following the steps |
| 2026-10-24 | Push test verified; D20 (JDK 25 before W2, Corretto 21 fallback by 6 Nov), D21 (personal Azure labs on the personal laptop), D22 (no account linking; voucher codes; OnVUE on the personal laptop, system test by 21 Nov), D23 (verified), D24 (uv via JFrog); Java W1 Mon + SD W1 Mon back to JDK 11 for Week 1; planner notes W1/W2/W3 (new)/W5/W6 updated; setup guide rewritten (N12 L&D added) | User: push done, JDK 25 before W2, uv tab seen in JFrog, personal/work Microsoft sign-ins blocked across laptops | Yes — user reported these facts |
| 2026-10-24 | Privacy split: company-specific details moved to `COMPANY_ENVIRONMENT.local.md`; `.gitignore` (local files + PDFs); folder prepared as private repo `learning-plan` (first commit; user pushes); `tools/setup_jfrog_pip.py` for N4 | User created the `learning-plan` repo and asked for help with the JFrog token | Yes — user asked to set up the repo and pip |
| 2026-10-24 | Read the company developer portal (Artifactory set-up, repository naming, certificates) at the user's request → D19/D24 aligned to the company standard (shared Python repository, `trusted-host`, uv via `uv auth login`); helper script updated and re-tested; certificate note added for new JDKs; details kept in the local file | User shared the developer-portal link and asked to follow it | Yes — user asked |
| 2026-10-24 | First N4 attempt failed (the clipboard held the run command; the old paste fallback dropped the URL line of a 2-line paste). Helper rewritten: waits for the JFrog copy or a paste, rejects cut-off tokens, `--repo` with fallback, exact 401/403/404 messages; 40 offline tests passed (fake tokens, local fake index, never JFrog). Token partly visible in a screenshot → user advised to revoke it; new secrets rule in Section 9 | User reported the failure with screenshots | Yes — user asked for help |
| 2026-10-24 | N4 (pip, fresh token; exposed one revoked — verified), N9 (uv; D24: `system-certs`, global Python 3.12 pin) and N11 (`learning-plan` pushed) done; D20 vendor note (any company-provided JDK 25; Temurin/Microsoft preferred; Oracle OK) | User finished the setup steps and asked which JDK 25 to take | Yes — user asked |
| 2026-10-24 | D20 vendor decided: **Amazon Corretto 25** (only JDK 25 in the company catalogue). Java/SD resource pages, TicketVerse spec, Java W1 resource link and planner reminders (W1, W2, W6) updated; Docker/CI stay Temurin 25 | User listed the requestable JDKs and asked for a final pick | Yes — user asked |
| 2026-10-24 | **Corretto 25 installed** (N1 done) → D20 rewritten: learning on 25 from Week 1; user `JAVA_HOME` = JDK 11 keeps work Maven on 11 (installer had switched it); Maven-through-JFrog verified on 25; `Windows-ROOT` trust store for PKIX. Java W1 Mon + SD W1 Mon now use Corretto 25 (the old SD text paired JDK 11 with JUnit 6, which needs 17+); planner W1/W2 reminders updated, W6 reminder removed. N10: the plan doesn't need the Visual Studio IDE; only a VS subscription's Azure credit matters (Path A) | User installed Corretto 25 and asked about the Visual Studio licence | Yes — user asked; JAVA_HOME change announced beforehand |
| 2026-10-24 | D25 (VS Code extension allow-list); **Section 11 reminder schedule** + session-start check; chat commands (Section 9 + `00_START_HERE.md`); plan fixes: Azure W1 Sat (`az bicep build` instead of the blocked extension), Azure W3 Sat (Azurite in a Codespace), AI W6 Mon (Docker inside the Codespace, no Docker Desktop install); planner lead-time reminders W1, W3, W7, W9, W14, W18, W20 | User asked for every pending install/IT request with reminders, and how to run the days from Week 1 | Yes — user asked |
| 2026-10-25 | **D26: plan restructured to 30 weeks** (ends Sun 23 May 2027; exams unchanged W5/W16/W26; bosses W4, W9, W15, W20, W25, W30). All 5 tracks rewritten and validated (Java 180 / AI 150 / SD 120 / Azure 120 sessions; DSA 294 core + 202 bonus, ≤ 2 new a day); generator: daily re-solves planned least-re-solved first (Saturday 1–2, Easy/Medium), contest Sundays W10–W18 + W22–W28 (not boss weeks), mocks from W15, W28 Saturday order Azure → Java → AI (teardown) → SD; cross-track scan clean (only deliberate primers); docs + roadmaps (`ROADMAP.md`) regenerated; employer words moved out of the repo into git-ignored `forbidden_words.local.md` | User asked for a full cross-check (complete, basic → advanced, in sync) and accepted ~7 months | Yes — user asked |
| 2026-10-25 | **D20 containers → Podman.** The company docs say Podman is the only supported container engine (no Docker); it ships pre-installed in the company's WSL Ubuntu image together with kubectl, kind and Helm. Developer profile confirmed (PC name), WSL not installed yet. The Docker and kubectl IT requests were replaced by self-service steps (Section 11, local guide N3); Java W11 Mon/Tue and W23 Mon, the Java/SD resources and planner notes W1/W7/W9/W10/W14/W21 were updated (Testcontainers inside WSL via the Podman socket; kind with the Podman provider). VS Code Python + Jupyter extensions installed | User found the company Podman docs and shared the extension screenshots | Yes — user asked |

---

## 11) Install & reminder schedule — the AI checks this at every session start (Section 6, step 3)

Announce every row whose **Remind from** date ≤ today and isn't ✅; mark ✅ when the learner confirms (also in Section 3 of the local setup guide).

| Remind from | What | Needed by | Where | Fallback | Status |
|---|---|---|---|---|---|
| Mon 26 Oct | VS Code **Python + Jupyter** extensions ✅ (installed 25 Oct) · `pip install ipykernel` in the AI venv | AI W1 Mon (26 Oct) | company laptop | — | ⏳ |
| Mon 26 Oct | Send the **L&D message** (exam vouchers + Visual Studio subscription Azure credit) | before booking AZ-900 (Sat 21 Nov) | — | company exam process | ⏳ |
| Mon 26 Oct | **Install the company's WSL Ubuntu image** from Company Portal (self-service; developer profile ✅) → import it, `podman --version`, `podman login` to JFrog, run `hello-world` through the mirror (local guide N3) | Sun 3 Jan (Java W11, Mon 4 Jan) | company laptop | Codespace | ⏳ |
| Mon 26 Oct | **Ask IT to allow-list VS Code extensions:** `ms-azuretools` (Bicep, Azure Resources, Functions, Container Tools), `azurite.azurite`, `ms-kubernetes-tools.vscode-kubernetes-tools` | nice-to-have from Azure W1 Sat (31 Oct) | company laptop | `az bicep build` · Codespace | ⏳ |
| Mon 26 Oct | Policy check: personal GitHub from the company laptop (N6) | this week | — | — | ⏳ |
| Sat 31 Oct | `az bicep install` (Azure CLI works through the proxy — verified) | Azure W1 Sat | company laptop | Codespace | ⏳ |
| Mon 16 Nov | Personal laptop: Codespace test (N8) + free Gemini and Groq API keys | AI W6 (Mon 30 Nov) | personal laptop | — | ⏳ |
| Mon 9 Nov | Personal laptop: Microsoft Learn profile (N5) + Pearson OnVUE system test | Sat 21 Nov (book AZ-900) | personal laptop | test centre | ⏳ |
| Sat 14 Nov | Azurite lab in a Codespace (`npx azurite`) | Azure W3 Sat | Codespace | dry-run | ⏳ |
| Mon 23 Nov | Read `Azure Cloud/COST_SAFETY_AND_ACCOUNT_SETUP.md`; create the personal Azure free account on Tue 1 Dec | Tue 1 Dec (Azure W6) | personal laptop | — | ⏳ |
| Mon 14 Dec | Podman ready for Java: `podman-compose` and a JDK 25 + Maven inside WSL (Testcontainers tests run there) — the mentor walks through it | Sun 3 Jan | company laptop (WSL) | Codespace | ⏳ |
| Mon 28 Dec | Testcontainers on Podman: one `PostgreSQLContainer` test green inside WSL (`DOCKER_HOST` to the Podman socket, Ryuk disabled, mirror prefix in `~/.testcontainers.properties`) | Mon 4 Jan (Java W11) | company laptop (WSL) | Codespace | ⏳ |
| Mon 28 Dec | VisualVM / JDK Mission Control (optional) | Java W11 Wed (6 Jan) | company laptop | JDK `jcmd` + `jfr` | ⏳ |
| Mon 25 Jan | Check kubectl, kind and Helm in the WSL image; test `KIND_EXPERIMENTAL_PROVIDER=podman kind create cluster` with node images through the mirror | Sun 28 Mar (Java W23, Mon 29 Mar) | company laptop (WSL) | Codespace / Cloud Shell / Killercoda | ⏳ |
| Mon 8 Mar | Azure Functions Core Tools (`func`) in a Codespace or on the personal laptop | Azure W21 (Mon 15 Mar) | personal | — | ⏳ |
| Mon 19 Apr | Codespaces quota check — TicketVerse AI (AI W27) needs a 4-core Codespace for a week | AI W27 (Mon 26 Apr) | personal laptop | 2-core + fewer services | ⏳ |
| When assigned | Visual Studio subscription → my.visualstudio.com → Benefits → Azure credit → Activate (Path A) | — | — | Path B (free account) | ⏳ |
| Mon 11 Oct 2027 | Renew the JFrog token (Set Me Up → helper with `--repo`, then `--uv`) | 24 Oct 2027 | company laptop | — | ⏳ |
