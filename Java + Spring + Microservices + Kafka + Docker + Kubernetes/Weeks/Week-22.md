# ☕ Java Backend · Week 22 — Docker deep dive: full TicketVerse in containers

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Containers are how your code ships; interviewers ask about image layers, non-root images, JVM memory in containers and debugging a broken container. This week every service gets a production-grade image and the whole system starts with one command (milestone).

## 🗓️ Sessions

### Monday 22 Mar · 60 min — Production images: multi-stage, layers, non-root, pinned bases
- 📚 **Learn:** Build on W11: order layers from least to most changing, `.dockerignore`, a two-stage Dockerfile that extracts Boot layers (`-Djarmode=tools`) from the host-built jar, a non-root `USER`, pinned base image tags or digests, small runtime bases (JRE vs distroless) and why every MB matters on pull. Holi lite day: catalog-service alone is enough. Read: [Docker: Building best practices](https://docs.docker.com/build/building/best-practices/). Optional: [Docker: Multi-stage builds](https://docs.docker.com/build/building/multi-stage/).
- 🛠️ **Do:** Turn your W11 layered Dockerfile into a shared template for all 5 services: stage 1 extracts layers from the host-built jar, stage 2 copies them onto `eclipse-temurin:25-jre`, runs as a non-root user and pins the base tag. Compare image size and rebuild time after a one-line change with W18's single-`COPY` images. Done when: a table shows size and rebuild time per service and `docker run ... id` shows a non-root uid.

### Tuesday 23 Mar · 60 min — Images without Dockerfiles: Jib locally, Buildpacks in CI
- 📚 **Learn:** Jib builds layered images straight from Maven and uses the JVM truststore, so it works behind the corporate proxy (add `-Djavax.net.ssl.trustStoreType=Windows-ROOT` to `MAVEN_OPTS` if needed; pass the mirrored base with `-Djib.from.image=...` so the prefix stays out of the POM). Cloud Native Buildpacks (`spring-boot:build-image`) download tools inside containers, which the proxy breaks, so compare them on GitHub's runners. Read: [Jib on GitHub](https://github.com/GoogleContainerTools/jib). Optional: [Spring Boot: Buildpacks](https://docs.spring.io/spring-boot/reference/packaging/container-images/cloud-native-buildpacks.html).
- 🛠️ **Do:** Build catalog-service with `./mvnw jib:dockerBuild` (base `eclipse-temurin:25-jre` through the mirror) and compare size, build time and layers with Monday's image. Add a manual (`workflow_dispatch`) job to `ci.yml` that runs `spring-boot:build-image` on GitHub's runner and prints the image size. Set a `mem_limit` per service in compose (heap via `MaxRAMPercentage`, W11). Done when: `docs/containers.md` compares Dockerfile vs Jib vs Buildpacks and every service runs within its limit.

### Wednesday 24 Mar · 60 min — Compose deep dive: healthchecks, startup order, profiles, networks, volumes
- 📚 **Learn:** `depends_on` with `condition: service_healthy` (as in W11) across the whole stack; healthcheck commands for Postgres/Kafka/Redis/Keycloak; profiles (`infra`, `apps`, `obs`); `.env` and variable interpolation; user-defined bridge networks and DNS; named volumes vs bind mounts; resource limits. Read: [Docker: Control startup order](https://docs.docker.com/compose/how-tos/startup-order/). Optional: [Docker: Compose profiles](https://docs.docker.com/compose/how-tos/profiles/).
- 🛠️ **Do:** Refactor `compose.yaml`: healthchecks on every infra container, services start only after dependencies are healthy, profiles `infra`/`apps`/`obs`, secrets and ports in `.env`, named volumes for Postgres and Kafka, memory limits per service. Done when: `docker compose --profile infra --profile apps up -d` reaches all-healthy without manual restarts on two consecutive clean runs.

### Thursday 25 Mar · 60 min — Image security, secret scan, public repo, GHCR and tagging
- 📚 **Learn:** Vulnerability scanning and fixing by updating base images and dependencies; SBOMs (CycloneDX/SPDX); never bake secrets into images; tags = git semver + commit SHA, never `latest` in deployments; GitHub Container Registry. On free plans private GHCR storage is small and branch protection/code scanning need a public repo, so make `ticketverse` public only after a secret scan and a check that no company names or hostnames were ever committed. Read: [Trivy: First steps](https://trivy.dev/docs/latest/getting-started/). Optional: [GitHub Docs: Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).
- 🛠️ **Do:** Scan all five images with Trivy (`docker run aquasec/trivy image ...`; if its database download fails behind the corporate proxy, scan in a Codespace) and fix or document every HIGH/CRITICAL finding. Run gitleaks over the full history (`zricethezav/gitleaks` image) and grep for company names and hostnames, then make `ticketverse` public. Tag images `1.4.0` and `sha-<short>` and push them to `ghcr.io/<you>/ticketverse-*`. Done when: no unexplained CRITICAL finding remains, the secret scan is clean and images are visible in GHCR.

### Friday 26 Mar · 60 min — Linux and container troubleshooting: logs, exec, inspect, network
- 📚 **Learn:** Linux essentials: processes (`ps`, `top`), files and permissions, env vars, `curl`, `ss`, `nslookup`/`dig`, disk usage; container debugging with `docker logs`, `exec`, `inspect`, `stats`, `events`; reading exit codes (1, 137, 143). Watch: [Abhishek Veeramalla: Linux Zero to Hero (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvIBIRWcReRV-m2kgIW6V6gr) (first video). Optional: [Docker: Volumes](https://docs.docker.com/engine/storage/volumes/).
- 🛠️ **Do:** Ask a friend (or write a script) to inject 5 faults: wrong DB password env, port already in use, Keycloak not healthy, typo in a service hostname, memory limit too low. Diagnose each using only CLI tools and write a `docs/RUNBOOK.md` entry (symptom -> command -> cause -> fix). Done when: all 5 are fixed and each runbook entry has the exact command that revealed the cause.

### Saturday 27 Mar · 60 min — BUILD: Full TicketVerse system in Docker with one command
- 📚 **Learn:** Milestone checklist: start from `docker compose down -v` and a fresh clone; only README instructions allowed. Stack: gateway + 4 services + Postgres + Redis + Kafka + Keycloak + Prometheus + Grafana + Jaeger. Pass = all healthy + both saga paths + evidence; a failed first run counts only after a written root cause. Read: [Docker: Compose services reference](https://docs.docker.com/reference/compose-file/services/). Optional: [Spring Boot: Efficient container images](https://docs.spring.io/spring-boot/reference/packaging/container-images/efficient-images.html).
- 🛠️ **Do:** Bring the full stack up with one command; run the smoke script for the happy and payment-failure sagas; show the Jaeger trace of a booking and the Grafana dashboard; save `docker compose ps` and `docker stats` output in `docs/milestone-docker.md`; tag `v1.4.0`. Done when: everything passes on the first clean run (aim for under 60 minutes) and the evidence is committed.

## 📦 Deliverable (by Saturday night)
TicketVerse v1.4.0: hardened non-root images for all services, Dockerfile vs Jib vs Buildpacks comparison, profiled compose with healthchecks, Trivy reports, a clean secret scan and a public repo, images on GHCR (semver + sha tags), RUNBOOK, full-system milestone evidence.

## ✅ Self-check (Sunday test preview)
- How does Docker layer caching work, and how should a Java Dockerfile be ordered?
- Why run as a non-root user, and why pin base images?
- Jib vs Buildpacks vs a Dockerfile: when would you pick each, especially behind a corporate proxy?
- A container exits with code 137: what happened and how do you confirm it?
- Volumes vs bind mounts; how do containers in one compose project find each other?
- Why avoid `latest` tags in deployments? What is an SBOM?
- Walk through how you would debug a container stuck in a restart loop.

## 🚀 Stretch (optional)
Try JDK 25 AOT cache ([JEP 514](https://openjdk.org/jeps/514)) or Spring Boot's AOT cache support and measure startup time before and after. Extras: generate a CycloneDX SBOM for booking-service; try a distroless Java base image and compare size and debuggability.
