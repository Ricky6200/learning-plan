# ☕ Java Backend · Week 19 — Docker deep dive, Linux basics: Season 4 boss

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** Containers are how your code ships; interviewers ask about layers, multi-stage builds, JVM memory in containers and debugging a broken container, and the boss proves the whole system runs anywhere.

## 🗓️ Sessions

### Monday 01 Mar · 60 min — Images, layers, cache; multi-stage Dockerfiles for Spring Boot
- 📚 **Learn:** Image layers and the build cache (order instructions from least to most changing), `.dockerignore`, multi-stage builds (JDK build stage -> JRE runtime stage), Spring Boot layered jars and `jarmode=tools` extraction, small base images (JRE, distroless), pinning tags/digests. [Docker: Multi-stage builds](https://docs.docker.com/build/building/multi-stage/), [Docker: Building best practices](https://docs.docker.com/build/building/best-practices/), [Spring Boot: Dockerfiles](https://docs.spring.io/spring-boot/reference/packaging/container-images/dockerfiles.html).
- 🛠️ **Do:** Write a multi-stage Dockerfile for catalog-service (Temurin 25 JDK build stage, Temurin 25 JRE runtime, extracted layers, non-root user); compare image size and rebuild time after a one-line code change vs a naive single-stage `COPY target/*.jar`. Done when: a table shows size and rebuild times, and `docker run ... id` shows a non-root uid.

### Tuesday 02 Mar · 60 min — JVM in containers: memory flags, OOMKilled; Buildpacks and Jib
- 📚 **Learn:** Container-aware JVM: heap from `-XX:MaxRAMPercentage` (default 25% is too small), metaspace/threads/direct memory outside the heap, OOMKilled (exit 137) vs Java OOM; CPU limits and `availableProcessors`; image builds without Dockerfiles: Cloud Native Buildpacks (`spring-boot:build-image`) and Jib. [Baeldung: Docker memory and CPU limits](https://www.baeldung.com/ops/docker-memory-limit), [Spring Boot: Buildpacks](https://docs.spring.io/spring-boot/reference/packaging/container-images/cloud-native-buildpacks.html), [Jib on GitHub](https://github.com/GoogleContainerTools/jib).
- 🛠️ **Do:** Run catalog-service with `--memory=512m` and print `Runtime.getRuntime().maxMemory()` with default flags and with `-XX:MaxRAMPercentage=75`; force an OOMKilled with a too-small limit and read `docker inspect` State. Build the same service with Buildpacks and with Jib and compare size and build time to Monday's Dockerfile. Done when: the comparison table and the OOMKilled evidence are in `docs/containers.md`.

### Wednesday 03 Mar · 60 min — Compose deep dive: healthchecks, startup order, profiles, networks, volumes
- 📚 **Learn:** `depends_on` with `condition: service_healthy`; healthcheck commands for Postgres/Kafka/Redis/Keycloak; profiles (`infra`, `apps`, `obs`); `.env` and variable interpolation; user-defined bridge networks and DNS; named volumes vs bind mounts; resource limits. [Docker: Control startup order](https://docs.docker.com/compose/how-tos/startup-order/), [Docker: Compose profiles](https://docs.docker.com/compose/how-tos/profiles/), [Docker: Networking overview](https://docs.docker.com/engine/network/).
- 🛠️ **Do:** Refactor `compose.yaml`: healthchecks on every infra container, services start only after dependencies are healthy, profiles `infra`/`apps`/`obs`, secrets and ports in `.env`, named volumes for Postgres and Kafka, memory limits per service. Done when: `docker compose --profile infra --profile apps up -d` reaches all-healthy without manual restarts on two consecutive clean runs.

### Thursday 04 Mar · 60 min — Image security and registries: Trivy, SBOM, GHCR, tagging
- 📚 **Learn:** Vulnerability scanning and fixing by updating base images and dependencies; SBOMs (CycloneDX/SPDX); never bake secrets into images; registries and tagging (semver + git SHA, avoid `latest` in deployments); pushing to GitHub Container Registry. [Trivy: First steps](https://trivy.dev/docs/latest/getting-started/), [GitHub Docs: Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry), [TechWorld with Nana: Docker full course (video)](https://www.youtube.com/watch?v=3c-iBn73dDE).
- 🛠️ **Do:** Scan all five images with Trivy, fix or document every HIGH/CRITICAL finding, and generate a CycloneDX SBOM for booking-service; tag images as `0.19.0` and `sha-<short>` and push them to `ghcr.io/<you>/ticketverse-*` with a fine-grained token. Done when: no unexplained CRITICAL findings remain and images are visible in GHCR.

### Friday 05 Mar · 60 min — Linux and container troubleshooting: logs, exec, inspect, network
- 📚 **Learn:** Linux essentials: processes (`ps`, `top`), files and permissions, env vars, `curl`, `ss`, `nslookup`/`dig`, disk usage; container debugging with `docker logs`, `exec`, `inspect`, `stats`, `events`; reading exit codes (1, 137, 143). [Abhishek Veeramalla: Linux Zero to Hero (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvIBIRWcReRV-m2kgIW6V6gr), [Docker: Volumes](https://docs.docker.com/engine/storage/volumes/).
- 🛠️ **Do:** Ask a friend (or write a script) to inject 5 faults: wrong DB password env, port already in use, Keycloak not healthy, typo in a service hostname, memory limit too low. Diagnose each using only CLI tools and write a `docs/RUNBOOK.md` entry (symptom -> command -> cause -> fix). Done when: all 5 are fixed and each runbook entry has the exact command that revealed the cause.

### Saturday 06 Mar · 60 min — BOSS BATTLE: Whole TicketVerse via docker compose up, 60 min
- 📚 **Learn:** Rules: start from `docker compose down -v` and a fresh clone; 60 minutes; only README instructions allowed. Stack: gateway + 4 services + Postgres + Redis + Kafka + Keycloak + Prometheus + Grafana + Jaeger. Pass = all healthy + saga demo + evidence. [Docker: Compose services reference](https://docs.docker.com/reference/compose-file/services/), [Spring Boot: Efficient container images](https://docs.spring.io/spring-boot/reference/packaging/container-images/efficient-images.html).
- 🛠️ **Do:** Bring the full stack up with one command; run the smoke script for happy and payment-failure sagas; show the Jaeger trace of a booking and the Grafana dashboard; take `docker compose ps` and `docker stats` screenshots; tag `v3.1.0`. Done when: everything passes inside 60 minutes on the first clean run (a second attempt counts only after a written root cause).

## 📦 Deliverable (by Saturday night)
TicketVerse v3.1.0: optimized multi-stage images (non-root), container memory notes, Buildpacks/Jib comparison, profiled compose with healthchecks, Trivy reports + SBOM, images on GHCR, RUNBOOK, boss evidence.

## ✅ Self-check (Sunday test preview)
- How does Docker layer caching work, and how should a Java Dockerfile be ordered?
- Why use multi-stage builds and a JRE or distroless runtime image?
- A container exits with code 137: what happened and how do you confirm it?
- How should you size the JVM heap inside a 1 GB container?
- Volumes vs bind mounts; how do containers in one compose project find each other?
- Why avoid `latest` tags in deployments? What is an SBOM?
- Walk through how you would debug a container stuck in a restart loop.

## 🚀 Stretch (optional)
Try JDK 25 AOT cache ([JEP 514](https://openjdk.org/jeps/514)) or Spring Boot's AOT cache support and measure startup time before and after.
