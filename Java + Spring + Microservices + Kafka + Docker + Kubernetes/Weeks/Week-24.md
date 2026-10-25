# ☕ Java Backend · Week 24 — Kubernetes II: Gateway API, autoscaling, state, Helm

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** Real clusters need traffic entry, autoscaling, stateful workloads, access control and packaging; Gateway API replaced ingress-nginx (retired March 2026), so modern answers use it.

## 🗓️ Sessions

### Monday 05 Apr · 60 min — Gateway API: GatewayClass, Gateway, HTTPRoute with Envoy Gateway
- 📚 **Learn:** Why Ingress gave way to Gateway API (role-oriented, portable, richer routing) and the ingress-nginx retirement; GatewayClass (infra provider), Gateway (listeners), HTTPRoute (path/header matching, weights, filters); implementations like Envoy Gateway or NGINX Gateway Fabric. If Helm charts or images cannot be pulled behind the corporate proxy, use the 4-core Codespace. Read: [Kubernetes: Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/). Optional: [Envoy Gateway: Quickstart](https://gateway.envoyproxy.io/docs/tasks/quickstart/).
- 🛠️ **Do:** Install Envoy Gateway on kind with Helm; create a Gateway and HTTPRoutes sending `/api/events` to catalog-service and `/api/bookings` to booking-service; add a header-based route to a `v2` deployment and a 90/10 weighted split. Done when: curl through the Gateway reaches both services and the weighted split shows roughly 10% v2 responses over 100 calls.

### Tuesday 06 Apr · 60 min — Horizontal Pod Autoscaler with metrics-server and load
- 📚 **Learn:** metrics-server (its image comes from registry.k8s.io, part of the IT request; else use the Codespace); HPA on CPU utilization (needs requests), min/max replicas, stabilization windows and scale-down behaviour; why JVM warm-up and memory-based scaling are tricky; VPA and KEDA awareness for event-driven scaling (Kafka lag). Read: [Kubernetes: HPA walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/). Optional: [Kubernetes: Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).
- 🛠️ **Do:** Install metrics-server on kind (with `--kubelet-insecure-tls`), create an HPA for catalog-service (min 1, max 5, 60% CPU), generate load with a busy loop pod, and record replicas over time with `kubectl get hpa -w`; then stop load and watch scale-down. Done when: a timeline of scale-out and scale-in is saved in `docs/k8s-hpa.md`.

### Wednesday 07 Apr · 60 min — StatefulSets, PV/PVC, Jobs and CronJobs
- 📚 **Learn:** StatefulSets (stable names, ordered rollout, per-pod PVCs via volumeClaimTemplates); PersistentVolumes, claims and StorageClasses; why managed databases beat self-run ones in the cloud; Jobs for one-off work (migrations) and CronJobs for schedules (cleanup). Read: [Kubernetes: StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). Optional: [Kubernetes: CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/).
- 🛠️ **Do:** Convert Postgres to a StatefulSet with a volumeClaimTemplate; insert data, delete the pod and prove data survives; add a Job that runs Flyway migrations before deploy and a CronJob that calls booking-service's `/actuator/health` every 5 minutes as a stand-in (W25 builds the real cleanup endpoint and you point the CronJob at it). Done when: data persists across pod deletion and the CronJob history shows successful runs.

### Thursday 08 Apr · 60 min — RBAC, Kustomize awareness, troubleshooting broken workloads
- 📚 **Learn:** ServiceAccounts, Roles/ClusterRoles, RoleBindings, least privilege, `kubectl auth can-i`; Kustomize overlays (dev/prod) vs Helm values; reading Events and statuses: CrashLoopBackOff, ImagePullBackOff, OOMKilled, Pending, failing readiness. Read: [Kubernetes: RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). Optional: [Kubernetes: Debug running pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/).
- 🛠️ **Do:** Create a read-only ServiceAccount for a 'support' role and verify with `kubectl auth can-i`. Inject 5 failures (bad image tag, crashing command, tiny memory limit, impossible CPU request, wrong readiness path) and fix each using only `get`, `describe`, `logs`, `events`. Done when: `docs/RUNBOOK.md` gains 5 Kubernetes entries with the decisive command for each.

### Friday 09 Apr · 60 min — Helm charts: templates, values, install, upgrade, rollback
- 📚 **Learn:** Chart layout (Chart.yaml, values.yaml, templates/, `_helpers.tpl`); Go templating, `include`, `toYaml`, conditionals; per-environment values files; `helm lint`, `helm template`, `install`, `upgrade --install`, `rollback`, `history`; Helm 4 is current and keeps chart compatibility. Read: [Helm: Chart template guide](https://helm.sh/docs/chart_template_guide/getting_started/). Optional: [Helm: Quickstart](https://helm.sh/docs/intro/quickstart/).
- 🛠️ **Do:** `helm create` a chart for catalog-service and adapt it: image repo/tag, replicas, resources, probes, env from ConfigMap/Secret, HTTPRoute template toggled by a value; lint and template it; install, upgrade with a new tag, then roll back. Done when: `helm history` shows 3 revisions and `helm template` output matches your hand-written manifests.

### Saturday 10 Apr · 60 min — BUILD: TicketVerse Helm chart on local Kubernetes
- 📚 **Learn:** Umbrella chart with one subchart per service (or one generic service chart reused with values), shared labels and helpers, values-dev.yaml, infra (Postgres StatefulSet, Redis, Kafka in KRaft mode, Keycloak) kept simple for local use; the full chart may need the 4-core Codespace. Read: [Helm: Chart best practices](https://helm.sh/docs/chart_best_practices/). Optional: [Gateway API: HTTP routing guide](https://gateway-api.sigs.k8s.io/guides/user-guides/http-routing/).
- 🛠️ **Do:** Create `charts/ticketverse` deploying gateway, catalog, booking, payment-mock, notification and infra plus HTTPRoutes; `helm upgrade --install tv charts/ticketverse -f values-dev.yaml -n ticketverse`; run the saga smoke test through the Gateway API entry point. Done when: one Helm command brings up the system on a fresh kind cluster and both saga paths pass.

## 📦 Deliverable (by Saturday night)
Gateway API routing (incl. weighted split), HPA timeline, Postgres StatefulSet, migration Job + stand-in CronJob, RBAC + troubleshooting runbook, `charts/ticketverse` umbrella chart running the full saga on kind.

## ✅ Self-check (Sunday test preview)
- Why did the ecosystem move from Ingress to Gateway API? Name its three core resources.
- How does HPA decide the replica count, and why must requests be set?
- StatefulSet vs Deployment: when do you need each?
- Job vs CronJob: one TicketVerse use case each.
- What do CrashLoopBackOff and ImagePullBackOff mean, and what is your first command for each?
- Helm vs Kustomize: how do they differ?
- How would you do a canary release with Gateway API?

## 🚀 Stretch (optional)
Install Argo CD on kind and let it sync `charts/ticketverse` from Git (GitOps preview for W26).
