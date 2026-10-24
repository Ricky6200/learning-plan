# ☕ Java Backend · Week 16 — Resilience and observability: survive and see failures

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Distributed systems fail partially; interviewers ask how you stop cascades (timeouts, retries, circuit breakers, idempotency) and how you debug across services (metrics, traces, logs).

## 🗓️ Sessions

### Monday 08 Feb · 60 min — Timeouts, retries with backoff and jitter, idempotency keys
- 📚 **Learn:** Retry only idempotent or idempotency-keyed operations; exponential backoff with jitter; retry budgets and retry storms; `Idempotency-Key` header stored with the response; Resilience4j Retry vs Spring Framework 7 built-in `@Retryable`. [Resilience4j: Retry](https://resilience4j.readme.io/docs/retry), [Spring Framework: Resilience features](https://docs.spring.io/spring-framework/reference/core/resilience.html), [microservices.io: Idempotent consumer](https://microservices.io/patterns/communication-style/idempotent-consumer.html).
- 🛠️ **Do:** Add an `idempotency_key` table to booking-service: a repeated `POST /api/bookings` with the same `Idempotency-Key` returns the original response; wrap payment calls in Retry (3 attempts, exponential backoff + jitter, retry only on timeouts/5xx). Done when: a test sends the same request 3 times and gets one booking, and logs show backoff gaps growing.

### Tuesday 09 Feb · 60 min — Circuit breaker, time limiter and graceful fallbacks
- 📚 **Learn:** Circuit breaker states (CLOSED, OPEN, HALF_OPEN), count vs time sliding windows, failure-rate and slow-call thresholds, wait duration; TimeLimiter for async calls; meaningful fallbacks (booking stays PAYMENT_PENDING) vs hiding errors; Boot 4 starter `resilience4j-spring-boot4` plus actuator. [Resilience4j: CircuitBreaker](https://resilience4j.readme.io/docs/circuitbreaker), [Martin Fowler: Circuit breaker](https://martinfowler.com/bliki/CircuitBreaker.html), [Java Techie: Resilience4j circuit breaker (video)](https://www.youtube.com/watch?v=b6R4dElDtRc).
- 🛠️ **Do:** Wrap `PaymentClient` with `@CircuitBreaker(name = "payment", fallbackMethod = ...)`: 50% failure rate over 10 calls opens it, 10 s wait, 3 half-open trial calls; the fallback marks the booking PAYMENT_PENDING. Expose the `circuitbreakers` actuator endpoint. Done when: forcing payment failures shows CLOSED -> OPEN -> HALF_OPEN -> CLOSED in the actuator output.

### Wednesday 10 Feb · 60 min — Rate limiter and bulkhead: protect yourself and dependencies
- 📚 **Learn:** RateLimiter (permits per refresh period, timeout) to protect expensive endpoints; Bulkhead (semaphore vs fixed thread pool) to isolate a slow dependency so it cannot exhaust request threads; HTTP 429 with `Retry-After`; layering order of resilience decorators. [Resilience4j: RateLimiter](https://resilience4j.readme.io/docs/ratelimiter), [Resilience4j: Bulkhead](https://resilience4j.readme.io/docs/bulkhead), [Daily Code Buffer: Resilience4j tutorial (video)](https://www.youtube.com/watch?v=9AXAUlp3DBw).
- 🛠️ **Do:** Limit `POST /api/shows/{id}/holds` to 5 requests/second per instance (return 429 ProblemDetail with `Retry-After`); add a semaphore Bulkhead of 10 around payment calls. Fire 50 concurrent requests from a small virtual-thread Java client and count 2xx vs 429 vs bulkhead rejections. Done when: the numbers match your configured limits.

### Thursday 11 Feb · 60 min — Metrics with Micrometer, Prometheus and Grafana dashboards
- 📚 **Learn:** Micrometer meters (counter, timer, gauge, distribution summary), tags and cardinality limits, `/actuator/prometheus`, histograms for p95/p99, RED and USE methods; Prometheus scraping and PromQL basics; Grafana panels. [Micrometer: Concepts](https://docs.micrometer.io/micrometer/reference/concepts.html), [Spring Boot: Metrics](https://docs.spring.io/spring-boot/reference/actuator/metrics.html), [Prometheus: Getting started](https://prometheus.io/docs/prometheus/latest/getting_started/).
- 🛠️ **Do:** Add Prometheus and Grafana to compose (profile `obs`); add custom metrics `bookings_confirmed_total`, `seat_hold_failures_total` and a timer around confirm; build a Grafana dashboard: request rate, error rate, p95 latency per endpoint, bookings/min, circuit-breaker state. Done when: the dashboard JSON is committed and panels move during a smoke-test run.

### Friday 12 Feb · 60 min — Distributed tracing with OpenTelemetry and Jaeger; structured logs
- 📚 **Learn:** Traces, spans, attributes; W3C `traceparent` propagation across HTTP; Micrometer Observation + OpenTelemetry bridge exporting OTLP (Boot 4 `spring-boot-starter-opentelemetry`); Jaeger v2 as OTLP backend; sampling; structured JSON logs with traceId for correlation. [OpenTelemetry: Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/), [Spring Boot: Tracing](https://docs.spring.io/spring-boot/reference/actuator/tracing.html), [Dan Vega: Spring Boot 4 OpenTelemetry (video)](https://www.youtube.com/watch?v=6_Y41z7OIv8).
- 🛠️ **Do:** Add Jaeger (all-in-one, OTLP) to compose; export traces from all 5 services with sampling 1.0 locally; enable structured JSON console logs including traceId/spanId. Make one booking through the gateway and find its trace. Done when: one trace shows gateway -> booking -> catalog -> payment spans and the same traceId appears in each service's logs.

### Saturday 13 Feb · 60 min — BUILD: Chaos test: kill payment, prove resilience with evidence
- 📚 **Learn:** Chaos experiment format: steady-state hypothesis, inject failure, observe, roll back, learn; what good degradation looks like (fast failures, no thread exhaustion, honest status codes, recovery without restarts). [microservices.io: Circuit breaker](https://microservices.io/patterns/reliability/circuit-breaker.html), [Jaeger: Getting started](https://www.jaegertracing.io/docs/latest/getting-started/).
- 🛠️ **Do:** Run a 5-minute booking load loop; `docker compose stop payment-service` for 2 minutes, then start it. Capture: circuit-breaker transitions, Grafana error-rate and p95 panels, a Jaeger trace of a short-circuited call, bookings left PAYMENT_PENDING then reconciled. Write `docs/CHAOS_REPORT.md` with screenshots. Done when: p95 of other endpoints stays within 2x baseline and the system recovers without restarts; tag `v2.0.0`.

## 📦 Deliverable (by Saturday night)
TicketVerse with idempotency keys, retries with jitter, circuit breaker + fallback, rate limiter, bulkhead, Prometheus/Grafana dashboard, OpenTelemetry traces in Jaeger, JSON logs, and a chaos report.

## ✅ Self-check (Sunday test preview)
- Which operations are safe to retry, and how do idempotency keys make POST safe?
- Explain circuit breaker states and the settings you chose for payment.
- Bulkhead vs rate limiter: what does each protect?
- Why must metric tags have low cardinality? Give a bad example.
- How does trace context propagate from the gateway to the booking service?
- Counter vs gauge vs timer: one TicketVerse example each.
- What did your chaos test prove, and what would you improve next?

## 🚀 Stretch (optional)
Add a Grafana alert rule (error rate > 5% for 2 min) and test it by stopping catalog-service.
