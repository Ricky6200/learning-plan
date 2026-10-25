# ☕ Java Backend · Week 26 — CI/CD and DevSecOps with GitHub Actions

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-26.md) · [Week 27 →](Week-27.md)

**Why this week:** Teams expect engineers to own the pipeline: automated tests, image builds, security gates and keyless cloud deploys. A green pipeline badge is strong resume evidence. AI-200 exam week: Friday and Saturday are deliberately lighter.

## 🗓️ Sessions

### Monday 19 Apr · 60 min — GitHub Actions deeper: matrix per service, caching, concurrency
- 📚 **Learn:** Events/triggers, jobs, steps, runners, actions; growing your W14 `ci.yml`: `actions/setup-java` (Temurin 25, Maven cache), a matrix per service, artifacts, concurrency groups that cancel stale runs, least-privilege `permissions`. Read: [GitHub Docs: Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) (jobs, strategy, concurrency). Optional: [TechWorld with Nana: GitHub Actions (video)](https://www.youtube.com/watch?v=R8_veQiYBjI).
- 🛠️ **Do:** Extend `.github/workflows/ci.yml`: on pull requests and pushes to main, run `./mvnw -B verify` for each service via a matrix, with Maven caching, JDK 25, `permissions: contents: read` and a concurrency group; upload Surefire reports as artifacts. Done when: a PR shows one green check per module and a second push cancels the stale run.

### Tuesday 20 Apr · 60 min — Testcontainers in CI, coverage reports, branch protection
- 📚 **Learn:** Docker is available on GitHub-hosted Ubuntu runners, so Testcontainers tests run as-is (no mirror needed there); speeding them up (reuse per class, parallel modules); publishing test and JaCoCo reports; required status checks and branch protection (on free plans this needs a public repo, which `ticketverse` is since W22); fail fast on flaky tests rather than retrying blindly. Read: [GitHub Docs: About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). Optional: [GitHub Docs: Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching).
- 🛠️ **Do:** Make all Testcontainers suites (Postgres, Redis, Kafka) pass in CI; publish JaCoCo HTML as an artifact and fail the job under 70%; protect `main` (PR required, CI checks required, no force-push). Open a PR with a deliberately failing test and confirm merge is blocked. Done when: the blocked PR screenshot is saved and the fixed PR merges.

### Wednesday 21 Apr · 60 min — Build and push images to GHCR with security scanning
- 📚 **Learn:** `docker/build-push-action` with Buildx and layer caching (the runner builds the jar first, then your W22 Dockerfile); tags from git (semver on tag, `sha-` on main) via metadata; `GITHUB_TOKEN` with `packages: write`; Trivy scan as a gate (fail on CRITICAL), SBOM upload; immutable image references for deploys. Read: [GitHub Docs: Publishing Docker images](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images). Optional: [aquasecurity/trivy-action](https://github.com/aquasecurity/trivy-action).
- 🛠️ **Do:** Add `images.yml`: on push to main and on `v*` tags, build all 5 images with cache, push to GHCR with `sha-<short>` and semver tags, scan each with Trivy (fail on CRITICAL, report HIGH), and attach an SBOM artifact. Done when: a tag push produces versioned images in GHCR and a deliberately vulnerable base image fails the job.

### Thursday 22 Apr · 60 min — Code quality and supply chain: Sonar, Dependabot, CodeQL, secrets
- 📚 **Learn:** Static analysis and quality gates with SonarQube Cloud (free for public repos); Dependabot version and security updates for Maven, Docker and Actions; CodeQL code scanning (default setup) and secret scanning with push protection, free for public repositories like yours; pinning third-party actions. Read: [GitHub Docs: CodeQL code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning). Optional: [GitHub Docs: Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
- 🛠️ **Do:** Enable CodeQL default setup and secret scanning; add `.github/dependabot.yml` for maven (each module), docker and github-actions with weekly schedules and grouped updates; connect SonarQube Cloud and add its PR analysis. Fix 3 real findings (Sonar or CodeQL) in one PR. Done when: the PR shows CodeQL, Sonar and CI checks and the quality gate passes.

### Friday 23 Apr · 60 min — CD basics: environments, ephemeral kind deploy, OIDC to Azure (light)
- 📚 **Learn:** Environments with required reviewers and environment secrets; deploying with Helm from a workflow; ephemeral kind clusters in CI for smoke tests; OpenID Connect federation gives workflows short-lived Azure tokens without stored secrets (you created the federated credential in Azure W22 Wed); GitOps (Argo CD) as the pull-based alternative. Read: [GitHub Docs: OIDC in Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure). Optional: [Argo CD: Getting started](https://argo-cd.readthedocs.io/en/stable/getting_started/).
- 🛠️ **Do:** Add `cd.yml`: after images build on main, spin up kind in the runner (`helm/kind-action`), `helm upgrade --install` TicketVerse with the new tags and run the smoke script; add a `staging` environment with a required reviewer; run `azure/login` with your Azure W22 federated credential, then `az account show`. AI-200 week: if time is short, do only the OIDC login. Done when: Azure login works with no client secret (and, if done, the kind smoke test passes in CI).

### Saturday 24 Apr · 60 min — BUILD: One change from PR to tagged release (light day, AI-200 week)
- 📚 **Learn:** Pipeline as a product: fast feedback first (unit tests), slower gates later (integration, scans, deploy), clear failure messages, reproducible builds, release notes generated from PR titles, status badges. Read: [GitHub Docs: Automatically generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes). Optional: [TechWorld with Nana: DevSecOps pipeline (video)](https://www.youtube.com/watch?v=gLJdrXPn0ns).
- 🛠️ **Do:** Open a small PR (e.g. a new `/actuator/info` field) and watch build + tests + coverage + CodeQL + Sonar; merge it so images are built, scanned and pushed; tag `v2.1.0` to create a GitHub Release with generated notes; add badges and a Mermaid pipeline diagram to the README. Done when: one change flows from PR to tagged release with every check green.

## 📦 Deliverable (by Saturday night)
`.github/workflows` (ci, images, cd) with matrix builds, Testcontainers, coverage gate, GHCR images with Trivy + SBOM, CodeQL, Dependabot, SonarQube Cloud, ephemeral K8s smoke deploy, OIDC login to Azure, release `v2.1.0`.

## ✅ Self-check (Sunday test preview)
- How would you structure CI for a multi-module Maven repo to keep feedback fast?
- How do Testcontainers tests run on GitHub-hosted runners?
- Why is OIDC federation safer than storing a cloud client secret in GitHub?
- What should fail the pipeline: give three gates you configured and why.
- How do you tag container images so deployments are reproducible?
- Dependabot vs CodeQL vs secret scanning: what does each protect against?
- Push-based CD vs GitOps (Argo CD): trade-offs?

## 🚀 Stretch (optional)
Add a reusable workflow (`workflow_call`) shared by all services and measure the CI time saved. Extra: let Argo CD (W24 stretch) deploy from Git instead of `cd.yml`.
