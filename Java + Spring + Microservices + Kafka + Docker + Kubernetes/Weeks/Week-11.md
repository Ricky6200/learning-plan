# ☕ Java Backend · Week 11 — Docker for Java, then JVM internals and GC

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** You met Docker in AI W8; now package Java the right way (JRE base, layered images, container-aware memory) and look inside the JVM, because GC and memory-leak questions appear in every SDE-2 loop and Spring, Testcontainers and Kubernetes all build on this.

## 🗓️ Sessions

### Monday 04 Jan · 60 min — Docker for Java I: recap, company mirror, Boot jar image, layers
- 📚 **Learn:** 10-minute recap of AI W8 (image, container, port, volume, Compose). Company laptop: Podman in the WSL Ubuntu image runs every `docker` command as `podman` (`alias docker=podman`; Compose via `podman-compose`). Java specifics: pull through the company's mirror in JFrog (log in once; keep the prefix in a git-ignored `.env`); run on a JRE base (`eclipse-temurin:25-jre`); build the jar on the host and `COPY` it, because Maven inside an image build hits the corporate proxy; layered jars keep dependencies in cacheable layers. Read: [Spring Boot: Efficient container images](https://docs.spring.io/spring-boot/reference/packaging/container-images/efficient-images.html). Optional: [Spring Boot: Dockerfiles](https://docs.spring.io/spring-boot/reference/packaging/container-images/dockerfiles.html).
- 🛠️ **Do:** Generate a tiny app on start.spring.io (Boot 4.1.x, Java 25, web + actuator; Boot is taught properly in W13) into `java-mastery/docker-lab` and `./mvnw package`. Dockerfile v1: `FROM eclipse-temurin:25-jre`, `COPY target/*.jar app.jar`, `ENTRYPOINT ["java", "-jar", "/app.jar"]`; build `hello:1` and run it with `-p 8080:8080`. Dockerfile v2: stage 1 runs `java -Djarmode=tools -jar app.jar extract --layers --destination extracted`, stage 2 copies the layer folders. Change one line of code and compare rebuild times. Done when: `/actuator/health` answers from the container and v2 rebuilds faster.

### Tuesday 05 Jan · 60 min — Docker for Java II: container-aware JVM memory, Testcontainers
- 📚 **Learn:** The JVM reads container limits: by default the max heap is 25% of the memory limit and `availableProcessors()` follows `--cpus`; `-XX:MaxRAMPercentage=75` gives the heap more while leaving room for metaspace, thread stacks and direct buffers; pass flags via `JAVA_TOOL_OPTIONS`; going over the limit gets the container OOMKilled (exit 137), not a Java `OutOfMemoryError`. Testcontainers pulls through the mirror with `hub.image.name.prefix` in `~/.testcontainers.properties`; on Podman, run the tests inside WSL with `DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock` and `TESTCONTAINERS_RYUK_DISABLED=true`. Read: [Microsoft Learn: Containerize your Java applications](https://learn.microsoft.com/en-us/azure/developer/java/containers/overview). Optional: [Testcontainers: Image name substitution](https://java.testcontainers.org/features/image_name_substitution/).
- 🛠️ **Do:** Log `maxMemory()` and `availableProcessors()` at startup of Monday's app. Run it with `--memory=512m --cpus=1`, first with default flags, then with `JAVA_TOOL_OPTIONS=-XX:MaxRAMPercentage=75`; then shrink the limit until the container dies and check `docker inspect --format '{{.State.OOMKilled}}'`. Create `~/.testcontainers.properties` with your mirror prefix and run one test that starts a `PostgreSQLContainer` and runs `select 1` through plain JDBC (`DriverManager`; JDBC in depth in W14). Done when: `notes/containers.md` has a heap/CPU table and the Testcontainers test is green.

### Wednesday 06 Jan · 60 min — JVM I: class loading, delegation, runtime data areas, JIT
- 📚 **Learn:** Loading, linking (verify, prepare, resolve) and initialization; bootstrap/platform/application loaders and parent delegation; heap, metaspace, thread stacks/frames, PC register, code cache; interpreter + C1/C2 tiered JIT, inlining, escape analysis. Read: [Baeldung: Class loaders](https://www.baeldung.com/java-classloaders). Optional: [Baeldung: JVM run-time data areas](https://www.baeldung.com/java-jvm-run-time-data-areas).
- 🛠️ **Do:** Print the loader chain for your class, `String` and `java.sql.Connection`; write a custom `ClassLoader` that loads a `.class` from a folder and show two loaders produce two different `Class` objects. Compare the recursion depth reached before `StackOverflowError` (your W1 Thu demo) with `-Xss256k` vs `-Xss2m`; count loaded classes with `-Xlog:class+load`. Done when: notes explain every output.

### Thursday 07 Jan · 60 min — JVM II: GC roots, generations, G1, generational ZGC
- 📚 **Learn:** Reachability and GC roots; mark-sweep-compact; the generational hypothesis (eden, survivor, old); minor vs full GC; stop-the-world pauses; Serial, Parallel, G1 (default, region-based, pause goal), ZGC (generational by default since JDK 23); GC logging with `-Xlog:gc*`. Read: [dev.java: GC in Java](https://dev.java/learn/jvm/tool/garbage-collection/java-specifics/). Optional: [Concept && Coding: Memory and GC (Hindi video)](https://www.youtube.com/watch?v=vz6vSZRuS2M).
- 🛠️ **Do:** Write `Allocator` creating short-lived and long-lived objects; run it with `-Xmx256m -Xlog:gc` under G1, then `-XX:+UseZGC`, then `-XX:+UseParallelGC`; compare pause times and GC counts in a table. Explain one G1 log line field by field. Done when: the table and annotated log are in `notes/gc.md`.

### Friday 08 Jan · 60 min — JVM III: memory leaks, OOM types, histograms and JFR
- 📚 **Learn:** Leak patterns (static collections, unbounded caches, listeners, ThreadLocal in pools, inner-class references); OOM types (Java heap space, GC overhead limit, Metaspace, unable to create native thread, direct buffer); JDK-only tools, since VisualVM, Eclipse MAT and JMC need IT approval: `jcmd <pid> GC.class_histogram` (diff two snapshots), `-XX:+HeapDumpOnOutOfMemoryError`, `jcmd <pid> JFR.start`, `jfr summary`, `jfr view hot-methods` and `allocation-by-class`. Read: [Baeldung: Memory leaks](https://www.baeldung.com/java-memory-leaks). Optional: [Inside Java: the jfr view command](https://inside.java/2023/09/26/sip082/).
- 🛠️ **Do:** Write `LeakyCache` (a static HashMap that grows per simulated request) and run it with `-Xmx128m -XX:+HeapDumpOnOutOfMemoryError`; take two `jcmd <pid> GC.class_histogram` snapshots a minute apart and find the growing class; record `jcmd <pid> JFR.start duration=60s filename=leak.jfr` and run `jfr view allocation-by-class leak.jfr`. Fix it with your W5 `LruCache`. Done when: the histogram diff and the JFR view point at the same class and the fixed app runs 5 minutes without OOM.

### Saturday 09 Jan · 60 min — BUILD: Containerised Java app + Postgres via Compose, tuned JVM
- 📚 **Learn:** Compose as in AI W8 Sat (services, named volume, healthcheck + `depends_on: condition: service_healthy`, a git-ignored `.env`); write images as `${MIRROR:-}postgres:18` so the mirror prefix lives only in `.env`; service names are DNS names (`jdbc:postgresql://db:5432/app`); configuration through environment variables; `mem_limit` plus `-XX:MaxRAMPercentage` keeps the JVM inside its box and `-Xlog:gc` shows how it copes. Read: [Docker: Compose services reference](https://docs.docker.com/reference/compose-file/services/). Optional: [Docker: Control startup order](https://docs.docker.com/compose/how-tos/startup-order/).
- 🛠️ **Do:** In a new plain Maven folder `docker-lab/heartbeat` (no Spring), write an app that reads `DB_URL/DB_USER/DB_PASSWORD`, inserts a heartbeat row every second with JDBC and keeps the last 1,000 rows in your W5 `LruCache`. Dockerfile on `eclipse-temurin:25-jre` (copy dependencies with `dependency:copy-dependencies`, run with `-cp`); `compose.yaml` with `app` + `db` (named volume, healthcheck), `mem_limit: 384m` and `JAVA_TOOL_OPTIONS=-XX:MaxRAMPercentage=75 -Xlog:gc`. Done when: `docker compose up` shows rows growing, GC lines appear in `docker compose logs app`, and a clean `down`/`up` keeps the data.

## 📦 Deliverable (by Saturday night)
`docker-lab`: Boot jar image (single vs layered, rebuild timings), container heap/CPU table with OOMKilled evidence, first Testcontainers test through the mirror, Compose heartbeat app + Postgres with tuned JVM flags; JVM notes: class loaders, GC comparison table, histogram + JFR evidence for the leak.

## ✅ Self-check (Sunday test preview)
- Why build the jar on the host and run it on a JRE base image? What do layered jars buy you?
- Where does the company's Docker mirror prefix live, and why must it never be committed?
- How does the JVM size its heap inside a 512 MB container, and what does `-XX:MaxRAMPercentage=75` change?
- A container exits with code 137: what happened and how do you confirm it?
- Explain parent delegation in class loading. Why does it matter for security?
- What are GC roots? Minor vs full GC? Why is G1 the default and when would you pick ZGC?
- Name four OutOfMemoryError types. How do you find a leak with only `jcmd` and `jfr`?

## 🚀 Stretch (optional)
Run TripPlanner (W9) with JFR and explore threads and CPU with `jfr view` (or [JDK Mission Control](https://adoptium.net/jmc/) if IT approves it). Extras: `docker system df` and a safe prune; run Monday's image with `--cpus=1 --memory=1g`, print the chosen GC with `-XX:+PrintCommandLineFlags` and explain why the JVM may pick Serial GC in a small container.
