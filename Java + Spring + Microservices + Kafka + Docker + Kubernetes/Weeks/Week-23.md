# ☕ Java Backend · Week 23 — Kubernetes I: pods, deployments, services, config

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Kubernetes is the default runtime for Java microservices; interviewers expect you to explain the control loop, Deployments vs Pods, Services, probes and resource limits from hands-on use.

## 🗓️ Sessions

### Monday 29 Mar · 60 min — Kubernetes architecture, declarative model, kubectl, local cluster
- 📚 **Learn:** Control plane (API server, etcd, scheduler, controller manager) and nodes (kubelet, kube-proxy, container runtime); desired state and reconciliation loops; kubectl get/describe/logs/exec/apply; local clusters with kind. kubectl, kind and Helm ship with the company's WSL Ubuntu image (with Podman: `KIND_EXPERIMENTAL_PROVIDER=podman`); fallback: a 4-core Codespace (Docker-in-Docker + kind) pulling your public GHCR images, or Killercoda for plain manifests (it cannot see local images). Read: [Kubernetes: Components](https://kubernetes.io/docs/concepts/overview/components/). Optional: [kind: Quick start](https://kind.sigs.k8s.io/docs/user/quick-start/).
- 🛠️ **Do:** Create a kind cluster; list nodes and system pods; pull `nginx` through the mirror and load it into kind (`kind load docker-image`; on Podman `podman save` + `kind load image-archive`) because kind nodes cannot use your registry login, run it imperatively, then write a Pod YAML and `kubectl apply` it; use `describe`, `logs`, `exec` and `get -o yaml`; delete the pod and note nothing recreates it. Done when: you can draw the control plane and explain what happened at each step of `kubectl apply`.

### Tuesday 30 Mar · 60 min — ReplicaSets and Deployments: rolling updates and rollbacks
- 📚 **Learn:** Labels and selectors; a ReplicaSet keeps N pods; a Deployment manages ReplicaSets for rolling updates (`maxSurge`, `maxUnavailable`), revision history, `kubectl rollout status/undo`; why you never create bare pods in production. Read: [Kubernetes: Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). Optional: [Abhishek Veeramalla: Kubernetes (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvJdsW6A0jCz_3VaANuFMLpc).
- 🛠️ **Do:** Load your catalog-service image into kind (`kind load docker-image`; in a Codespace pull it from GHCR instead), write a Deployment with 3 replicas, delete a pod and watch it come back, roll out a new image tag and watch ReplicaSets change, then roll back. Done when: `kubectl rollout history` shows 2+ revisions and you can explain maxSurge/maxUnavailable with your numbers.

### Wednesday 31 Mar · 60 min — Services, cluster DNS, namespaces, port-forward
- 📚 **Learn:** Service types (ClusterIP, NodePort, LoadBalancer, headless) and endpoints; how kube-proxy routes; DNS names `<svc>.<ns>.svc.cluster.local`; namespaces for isolation; `kubectl port-forward` for local testing. Read: [Kubernetes: Service](https://kubernetes.io/docs/concepts/services-networking/service/). Optional: [Kubernetes: kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/).
- 🛠️ **Do:** Create namespace `ticketverse`; deploy catalog-service with a ClusterIP Service; run a temporary curl pod and call it by short and full DNS name; port-forward to call it from your laptop; scale to 3 and watch endpoints change. Done when: calls succeed by DNS and `kubectl get endpointslices` shows 3 pod IPs.

### Thursday 01 Apr · 60 min — ConfigMaps, Secrets and probes with Spring Boot health groups
- 📚 **Learn:** ConfigMaps and Secrets as env vars or files (Secrets are base64, not encrypted by default); startup, liveness and readiness probes and their failure behaviour; Spring Boot liveness/readiness health groups and graceful startup. Read: [Kubernetes: Configure probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/). Optional: [Kubernetes: ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/).
- 🛠️ **Do:** Move catalog-service settings into a ConfigMap and DB credentials into a Secret; add startup, liveness and readiness probes using `/actuator/health/liveness` and `/readiness`; break the DB password and observe readiness failing (no traffic) while liveness stays healthy. Done when: you can explain why a DB outage should fail readiness, not liveness.

### Friday 02 Apr · 60 min — Requests and limits, QoS classes, OOMKilled, JVM sizing in pods
- 📚 **Learn:** CPU/memory requests (scheduling) vs limits (enforcement); CPU throttling vs memory OOMKill; QoS classes (Guaranteed, Burstable, BestEffort); sizing the JVM heap with `MaxRAMPercentage` inside limits (W11 rules); ResourceQuota/LimitRange awareness. Read: [Kubernetes: Resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/). Optional: [Kubernetes: Debug pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/).
- 🛠️ **Do:** Set requests/limits for catalog-service, read its QoS class, then lower the memory limit until the pod is OOMKilled and read the reason in `kubectl describe`; fix with a sane limit and `-XX:MaxRAMPercentage=75`; watch CPU throttling under a quick load loop. Done when: `docs/k8s-sizing.md` records the limits you chose and why.

### Saturday 03 Apr · 60 min — BUILD: Catalog and booking services on local Kubernetes
- 📚 **Learn:** Plain manifests per service: Deployment, Service, ConfigMap, Secret, probes, resources; Postgres as a simple Deployment + PVC for now (StatefulSet next week); booking calls catalog through Service DNS. Read: [Kubernetes: Learn Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/). Optional: [Spring Guide: Spring Boot on Kubernetes](https://spring.io/guides/gs/spring-boot-kubernetes/).
- 🛠️ **Do:** In `k8s/`, write manifests for Postgres, catalog-service and booking-service (+ Redis); apply them to namespace `ticketverse`; port-forward booking-service and run the hold-and-book smoke test; perform a rolling update and a rollback of booking-service during traffic. Done when: all pods are Ready, the smoke test passes, and the update causes zero failed requests.

## 📦 Deliverable (by Saturday night)
`k8s/` manifests for catalog, booking, Redis and Postgres with ConfigMaps, Secrets, probes and resources; rollout/rollback demo; sizing notes; the kind (or Codespace) cluster workflow in the README.

## ✅ Self-check (Sunday test preview)
- What do the API server, etcd, scheduler and controller manager each do?
- Pod vs ReplicaSet vs Deployment: why not create pods directly?
- ClusterIP vs NodePort vs LoadBalancer: when do you use each?
- Liveness vs readiness vs startup probes: what happens when each fails?
- Requests vs limits; what happens when a container exceeds its memory limit vs its CPU limit?
- Are Kubernetes Secrets encrypted? How would you protect them properly?
- How does a rolling update avoid downtime, and how do you roll back?

## 🚀 Stretch (optional)
Repeat Monday on the [Killercoda Kubernetes playground](https://killercoda.com/playgrounds/scenario/kubernetes) without notes to test your recall.
