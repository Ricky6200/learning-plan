# 🧠 AI SESSION LOG (handoffs between AI sessions — append-only)

> Purpose: when a chat/context ends, the next AI session reads the **last entry** here to continue seamlessly.
> The AI must append an entry before a session ends (or when the conversation gets long).

**Template**
```text
### Session YYYY-MM-DD HH:MM IST — <short title>
- Position at start → end: Wn Day → Wn Day
- What we did: …
- Files changed: …
- Decisions made (also add to Section 10 of AI_MEMORY if structural): …
- Open items / doubts to revisit: …
- NEXT STEP when the user returns: …
```

---

### Session 2026-10-24 00:42 IST — Plan kick-off
- Position at start → end: pre-start → pre-start (Week 1 begins Mon 26 Oct 2026)
- What we did: Interviewed the learner (AI language, DSA level, work stack, start date, formats); verified Azure certification
  changes (AZ-204 retired → AI-200; AI-102 → AI-103), current versions (JDK 25 LTS, Spring Boot 4.1.x, Spring AI 2.0.x,
  Kafka 4.x, LangGraph 1.x), ingress-nginx retirement (→ Gateway API); built the full 26-week, 5-track plan, daily planner,
  tracker system, weekly test protocol, gamification, PDFs.
- Files changed: entire `Personal_Learning` structure created — 195 Markdown files + 8 PDFs (Master, Daily Planner, 5 tracks, Career).
- Verified state at handoff: DSA 325 core + 118 bonus LeetCode problems (all free, IDs checked against the catalog, no
  duplicates, no overloaded days) + 29 compiled & unit-tested Java templates; Java 156 sessions, AI 130, SD 104, Azure 104
  (all pass `validate_track.py`); 1,561 unique external links checked (only glassdoor.co.in returns 403 to bots — URL is correct).
- Late corrections applied everywhere: GitHub Models retired 30 Jul 2026 (D13); W23 target = Container Apps (D14);
  JUnit 6 / Testcontainers 2 / Spring AI 2.0 artifact renames / MCP SDK v2 (D15); Maven 3.9.x/3.10.x; festival notes
  (Diwali Sun 8 Nov = W2 test day → Mini Test allowed; Christmas, New Year, Republic Day, Holi) in the daily planner.
- Learner-facing caveats: PyPI blocked on office laptop (D12) → use a personal machine for AI/Docker; Microsoft Learn
  sandboxes are retired → Azure W1–W5 labs use Path A (employer VS subscription) or Path B (free account from W6 Tue).
- Decisions made: D1–D15 in AI_MEMORY.md.
- Open items: learner should do the setup checklist in `00_START_HERE.md` (Sun 25 Oct or during Week 1) and pick Azure Path A/B by W1 Friday.
- NEXT STEP when the user returns: greet, confirm setup done, start Week 1 Monday tasks from `01_Daily_Planner/Week-01.md`.

### Sessions 2026-10-24 18:58–21:30 IST — Laptop setup (before Week 1)
- Position: pre-start (Week 1 begins Mon 26 Oct 2026).
- Outcome: company laptop = main machine; personal laptop for AI coding from W4, personal-Microsoft-account tasks and job search (D16–D24). Personal GitHub Ricky6200 with a separate personal Git identity for repos in `C:\dev\personal` — push verified. Python 3.12 via the `py` launcher; pip gets connected to the company JFrog with a token via `tools/setup_jfrog_pip.py` (N4). JDK 25 expected before Week 2 (Corretto 21 fallback by Fri 6 Nov). Certifications: personal Microsoft Learn profile on the personal laptop, voucher codes from L&D, exams on the personal laptop (system test by 21 Nov). Azure: company Visual Studio credit + personal free account from Tue 1 Dec (personal laptop).
- Privacy split: company-specific details (internal addresses, proxy observations, test results) moved to `COMPANY_ENVIRONMENT.local.md`, which is gitignored together with `03_SETUP_YOUR_LAPTOP.md` and the PDFs. This folder is the private GitHub repo `learning-plan` (first commit prepared; the user pushes).
- Files: NEW `03_SETUP_YOUR_LAPTOP.md` (local), `COMPANY_ENVIRONMENT.local.md` (local), `tools/setup_jfrog_pip.py`, `.gitignore`; `00_START_HERE.md`, AI README/RESOURCES, SD LLD framework, Azure cost doc, test protocol ("§" → "Section"); AI_MEMORY (D12–D24); plan_source data (AI W1, Java W1 Mon, SD W1 Mon) + gen.py ENV_NOTES → regenerated; PDFs rebuilt.
- Open items: Section 3 of `03_SETUP_YOUR_LAPTOP.md` (N1, N3–N6, N8–N10, N12) and the first `git push` of `learning-plan`.
- 21:20 IST: read the company developer-portal pages (Artifactory set-up, repository naming, certificates) at the user's request → helper
  script now writes the company-standard pip config (shared Python repository + `trusted-host`) and sets up uv via `uv auth login`;
  re-tested safely (temp files, public index only). Company-specific details stay in `COMPANY_ENVIRONMENT.local.md`.
- 21:45 IST: first N4 attempt failed (clipboard held the run command; old paste fallback dropped the URL line). Helper now waits for
  the JFrog copy (or a paste), checks the token is complete, supports `--repo` with fallback and explains 401/403/404 exactly;
  40/40 offline tests (fake tokens, local fake index). A token was partly visible in a screenshot → user told to revoke it and make
  a new one. Next: user revokes, re-runs N4 with the new command, then pushes `learning-plan`.
- 22:06 IST: **pip works through the company JFrog** (shared repository, `trusted-host`; `requests` installed; uv available there).
  Expiry check (decodes only the token's expiry field, never the token) showed `pip.ini` holds the exposed token (the user re-copied
  the old box) → N4b: revoke today's tokens, re-run, generate a NEW token; then the AI re-checks the expiry and deletes the
  `pip.ini.bak-*` copy that will hold the old token. After that: uv (N9, optional), `git push` of `learning-plan`.
- 22:12 IST: **N4 done.** Re-run with a NEW token (expiry differs from the exposed one); the exposed token is revoked (one test request
  → 401); the backup holding it was deleted. Next: uv (N9, optional), `git push` of `learning-plan` (N11).
- 22:30 IST: **uv set up (N9, user approved):** pip `--user` install from the company JFrog (0.13.5); user PATH += user Scripts
  folder (REG_EXPAND_SZ kept, backup in the session folder, WM_SETTINGCHANGE sent); helper `--uv` (now writes `system-certs`,
  pins uv's global Python to 3.12); tested `uv venv` (3.12) + `uv pip install requests` through JFrog. Next: user opens a new
  terminal → `uv --version`; restart VS Code; `git push` of `learning-plan` (N11).
- 22:40 IST: user confirmed `uv --version` works in a new terminal and pushed `learning-plan` (local `main` = `origin/main`). User asked
  for a summary and which JDK 25 vendor → D20 vendor note (any company-provided JDK 25; Temurin/Microsoft preferred; Oracle OK).
  **Setup status at end of Sat 24 Oct:** done = accounts, Python 3.12, VS Code, Azure CLI, Git identity + push, pip→JFrog, uv, plan
  backup. Open = N1 (JDK 25, by Fri 6 Nov else Corretto 21), N12 (L&D, Mon), N6 (policy), N5 + N8 (personal laptop), N10 (VS
  credit), N3 (Docker + WSL2 by Sun 27 Dec). **Next session: Week 1 starts Mon 26 Oct** (`01_Daily_Planner/Week-01.md`).
- 22:55 IST: user listed requestable JDKs (Temurin ≤21, Microsoft OpenJDK ≤21, Amazon Corretto up to 25) → **D20: Amazon Corretto
  25**. Updated the setup guide (N1, Section 5 paths, request text), Java/SD resource pages, TicketVerse spec, Java W1 resource link,
  planner reminders W1/W2/W6; regenerated planner + week files and PDFs. User to submit the Corretto 25 request.
- 23:05 IST: "AWS Corretto 25" turned out to be directly installable in the Company Portal → user installing it. Baseline recorded
  (local file): `java`/`mvn` = JDK 11, JAVA_HOME unset. **Next (when the user says installed):** verify the Corretto folder and
  version; check whether the installer changed system JAVA_HOME/PATH (if `mvn` moved to 25 → user JAVA_HOME = JDK 11); TLS test
  with Corretto 25 (Maven Central, Spring Initializr, company JFrog) → company-cert step if PKIX errors.
- 23:15 IST: **Corretto 25 installed (N1 done).** Installer had made 25 the system default (system JAVA_HOME + first in PATH) → set
  user `JAVA_HOME` = JDK 11 (work Maven back on 11, verified); per-window override → 25 (verified). Maven on 25 downloads through the
  company JFrog (76 jars, empty cache, BUILD SUCCESS). Corretto's own trust store fails on intercepted sites (PKIX) →
  `-Djavax.net.ssl.trustStoreType=Windows-ROOT` fixes it (verified). Plan updated so Week 1 uses Corretto 25. User asked about the
  Visual Studio IDE licence (trial until 22 Jan 2027): not needed — only a VS subscription's Azure credit matters (N10, Path A).
  Open setup items: N12 (L&D, Mon), N6 (policy), N3 (Docker + WSL2), N5 + N8 (personal laptop), N10 (VS subscription credit).
- 23:45 IST: user confirmed a work project (JDK 11) still builds. Scanned the whole plan for tools: the VS Code allow-list policy
  blocks the Azure tools/Azurite/Kubernetes extensions (D25) → Azure W1 Sat uses `az bicep build`, Azure W3 Sat Azurite in a
  Codespace, AI W6 Mon Docker inside the Codespace. Created **AI_MEMORY Section 11 (install & reminder schedule)** + session-start
  check; planner lead-time reminders (W1, W3, W7, W9, W14, W18, W20); chat commands (AI_MEMORY Section 9 + START_HERE).
  **Next session = Mon 26 Oct, Week 1 Day 1**: start with the magic prompt; remind N3/N13/N12/N6/N14 (Section 11).
- NEXT STEP: ask whether N4 printed `[OK] pip works through JFrog` and whether `learning-plan` was pushed; then start Week 1 Monday.
