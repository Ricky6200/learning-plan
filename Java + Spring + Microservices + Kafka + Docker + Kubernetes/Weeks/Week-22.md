# ☕ Java Backend · Week 22 — CI/CD and DevSecOps with GitHub Actions

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Teams expect engineers to own the pipeline: automated tests, image builds, security gates and keyless cloud deploys. A green pipeline badge is strong resume evidence.

## 🗓️ Sessions

### Monday 22 Mar · 60 min — GitHub Actions basics: workflows, jobs, matrix, Maven caching
- 📚 **Learn:** Events/triggers, jobs, steps, runners, actions; `actions/setup-java` with Temurin 25 and Maven cache; matrix builds per module; artifacts; concurrency groups to cancel stale runs; least-privilege `permissions`. [GitHub Docs: Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart), [GitHub Docs: Building Java with Maven](https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-maven), [TechWorld with Nana: GitHub Actions (video)](https://www.youtube.com/watch?v=R8_veQiYBjI).
- 🛠️ **Do:** Create `.github/workflows/ci.yml`: on pull requests and pushes to main, run `./mvnw -B verify` for each service via a matrix, with Maven caching, JDK 25, `permissions: contents: read` and a concurrency group; upload Surefire reports as artifacts. Done when: a PR shows one green check per module and a second push cancels the stale run.

### Tuesday 23 Mar · 60 min — Testcontainers in CI, coverage reports, branch protection
- 📚 **Learn:** Docker is available on GitHub-hosted Ubuntu runners, so Testcontainers tests run as-is; speeding them up (reuse per class, parallel modules); publishing test and JaCoCo reports; required status checks and branch protection rules; fail fast on flaky tests rather than retrying blindly. [GitHub Docs: Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [GitHub Docs: Dependency caching](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching), [Testcontainers: Getting started for Java](https://testcontainers.com/guides/getting-started-with-testcontainers-for-java/).
- 🛠️ **Do:** Make all Testcontainers suites (Postgres, Redis, Kafka) pass in CI; publish JaCoCo HTML as an artifact and fail the job under 70%; protect `main` (PR required, CI checks required, no force-push). Open a PR with a deliberately failing test and confirm merge is blocked. Done when: the blocked PR screenshot is saved and the fixed PR merges.

### Wednesday 24 Mar · 60 min — Build and push images to GHCR with security scanning
- 📚 **Learn:** `docker/build-push-action` with Buildx and layer caching; tags from git (semver on tag, `sha-` on main) via metadata; `GITHUB_TOKEN` with `packages: write`; Trivy scan as a gate (fail on CRITICAL), SBOM upload; immutable image references for deploys. [GitHub Docs: Publishing Docker images](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images), [docker/build-push-action](https://github.com/docker/build-push-action), [aquasecurity/trivy-action](https://github.com/aquasecurity/trivy-action).
- 🛠️ **Do:** Add `images.yml`: on push to main and on `v*` tags, build all 5 images with cache, push to GHCR with `sha-<short>` and semver tags, scan each with Trivy (fail on CRITICAL, report HIGH), and attach an SBOM artifact. Done when: a tag push produces versioned images in GHCR and a deliberately vulnerable base image fails the job.

### Thursday 25 Mar · 60 min — Code quality and supply chain: Sonar, Dependabot, CodeQL, secrets
- 📚 **Learn:** Static analysis and quality gates with SonarQube Cloud (free for public repos); Dependabot version and security updates for Maven, Docker and Actions; CodeQL code scanning (default setup); secret scanning and push protection; pinning third-party actions. [GitHub Docs: CodeQL code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-code-scanning), [GitHub Docs: Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference), [SonarQube Cloud docs](https://docs.sonarsource.com/sonarqube-cloud/).
- 🛠️ **Do:** Enable CodeQL default setup and secret scanning; add `.github/dependabot.yml` for maven (each module), docker and github-actions with weekly schedules and grouped updates; connect SonarQube Cloud and add its PR analysis. Fix 3 real findings (Sonar or CodeQL) in one PR. Done when: the PR shows CodeQL, Sonar and CI checks and the quality gate passes.

### Friday 26 Mar · 60 min — Continuous delivery: environments, ephemeral cluster deploy, OIDC to Azure
- 📚 **Learn:** Environments with required reviewers and environment secrets; deploying with Helm from a workflow; ephemeral kind clusters in CI for smoke tests; OpenID Connect federation so workflows get short-lived Azure tokens without stored secrets; GitOps (Argo CD) as the pull-based alternative. [GitHub Docs: OIDC in Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure), [Microsoft Learn: GitHub Actions OIDC to Azure](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect), [Argo CD: Getting started](https://argo-cd.readthedocs.io/en/stable/getting_started/).
- 🛠️ **Do:** Add `cd.yml`: after images build on main, spin up kind in the runner (`helm/kind-action`), `helm upgrade --install` TicketVerse with the new tags and run the smoke script; add a `staging` environment with a required reviewer. Create an Entra app with a federated credential for your repo and run `azure/login` + `az account show`. Done when: the smoke test passes in CI and Azure login works with no client secret.

### Saturday 27 Mar · 60 min — BUILD: Full pipeline green from PR to deployable release
- 📚 **Learn:** Pipeline as a product: fast feedback first (unit tests), slower gates later (integration, scans, deploy), clear failure messages, reproducible builds, release notes from PR titles, status badges. [GitHub Docs: Actions documentation](https://docs.github.com/en/actions), [TechWorld with Nana: DevSecOps pipeline (video)](https://www.youtube.com/watch?v=gLJdrXPn0ns).
- 🛠️ **Do:** Demonstrate: a PR runs build + tests + coverage + CodeQL + Sonar; merging builds, scans and pushes images; the ephemeral cluster deploy + smoke test passes; a `v4.0.0` tag creates a GitHub Release with notes and images. Add badges and a pipeline diagram (Mermaid) to the README. Done when: one change flows from PR to tagged release with every check green.

## 📦 Deliverable (by Saturday night)
`.github/workflows` (ci, images, cd) with matrix builds, Testcontainers, coverage gate, GHCR images with Trivy + SBOM, CodeQL, Dependabot, SonarQube Cloud, ephemeral K8s smoke deploy, OIDC login to Azure, release `v4.0.0`.

## ✅ Self-check (Sunday test preview)
- How would you structure CI for a multi-module Maven repo to keep feedback fast?
- How do Testcontainers tests run on GitHub-hosted runners?
- Why is OIDC federation safer than storing a cloud client secret in GitHub?
- What should fail the pipeline: give three gates you configured and why.
- How do you tag container images so deployments are reproducible?
- Dependabot vs CodeQL vs secret scanning: what does each protect against?
- Push-based CD vs GitOps (Argo CD): trade-offs?

## 🚀 Stretch (optional)
Add a reusable workflow (`workflow_call`) shared by all services and measure the CI time saved.
