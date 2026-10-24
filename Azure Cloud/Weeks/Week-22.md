# ☁️ Azure Cloud · Week 22 — Key Vault and App Configuration for secure apps

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Leaked secrets cause real outages and breaches. AI-200 tests storing, retrieving and rotating secrets with Key Vault and centralizing settings and feature flags with App Configuration - day-one requirements for any production Spring Boot or Python service.

## 🗓️ Sessions

### Tuesday 23 Mar · 45 min — Key Vault: secrets, keys, certificates, RBAC and soft delete
- 📚 **Learn:** Vault objects (secrets, keys, certificates) and versions, Azure RBAC data roles (recommended) vs legacy access policies, soft delete (on by default, 7-90 day retention) and purge protection, retrieving secrets with the Python SDK and caching them. Use the [Key Vault overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview), the [Python secrets quickstart](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python) and [Soft-delete overview](https://learn.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview).
- 🛠️ **Do:** Create a vault with RBAC authorization (pick a unique name - deleted vault names stay reserved during retention) and grant yourself Key Vault Secrets Officer. In `py/kv_demo.py` set a secret, read it, update it (new version), list versions, and add a 5-minute in-process cache. Delete the secret, then recover it. Done when: the version list, a cache-hit log and recovery evidence are in `w22/`.

### Wednesday 24 Mar · 45 min — Secret rotation patterns and managed-identity retrieval
- 📚 **Learn:** Rotation patterns (two credentials with overlap, expiry dates, Event Grid near-expiry events triggering a rotation function), key auto-rotation policies, retrieval via managed identity, Key Vault references in App Service and Functions. Use the [rotation tutorial](https://learn.microsoft.com/en-us/azure/key-vault/secrets/tutorial-rotation), [Key Vault with Event Grid](https://learn.microsoft.com/en-us/azure/key-vault/general/event-grid-overview) and [Key Vault references](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references).
- 🛠️ **Do:** Design `w22/rotation.md` for TicketVerse's PostgreSQL password: two DB users (A/B), 30-day expiry, Event Grid near-expiry event -> Function that resets the inactive user's password and writes a new secret version -> app reloads. Then, in your W21 function app, replace one setting with a Key Vault reference and confirm it resolves. Done when: the rotation sequence diagram and the resolved-reference evidence are committed.

### Friday 26 Mar · 45 min — App Configuration: key-values, labels, feature flags, Key Vault references
- 📚 **Learn:** Key-values, labels per environment, feature flags and filters, Key Vault references (App Configuration stores a pointer; the app reads the secret), the Python provider, dynamic refresh with a sentinel key, App Configuration vs Key Vault. Use the [App Configuration overview](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview), the [Python provider quickstart](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-python-provider) and [Feature management](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management).
- 🛠️ **Do:** Create a Free-tier store; add `TicketVerse:Search:TopK` with labels dev and prod, a feature flag `AskTicketVerse`, and a Key Vault reference to your DB secret. In `py/appconfig_demo.py` load the `dev` label with DefaultAzureCredential, print the resolved secret's length (never the value), then toggle the flag and see it change after refresh. Done when: label switch, flag toggle and secret-resolution evidence are in `w22/`.

### Saturday 27 Mar · 60 min — LAB: Settings + secrets from App Configuration in a container app
- 📚 **Learn:** The exercises in Learn's [Manage application secrets with Key Vault](https://learn.microsoft.com/en-us/training/modules/manage-app-secrets-key-vault/) and [Manage application settings with App Configuration](https://learn.microsoft.com/en-us/training/modules/manage-app-settings-app-config/); Java bonus: [Key Vault references in Spring Boot](https://learn.microsoft.com/en-us/azure/azure-app-configuration/use-key-vault-references-spring-boot).
- 🛠️ **Do:** Complete the 'Retrieve settings and secrets from Azure App Configuration' exercise (~30 min). Then deploy a tiny FastAPI container to Container Apps with a user-assigned managed identity that reads the same settings and secret at startup - no secrets in environment variables. Delete the RG (the vault name stays reserved while soft-deleted). Done when: the exercise is done, the container app shows the setting values and the RG is deleted.

## 📦 Deliverable (by Saturday night)
`w22/` Key Vault version/caching/recovery evidence, rotation design, App Configuration label/flag/reference evidence, and a container app reading config + secrets through managed identity.

## ✅ Self-check (Sunday test preview)
- Key Vault RBAC vs access policies: why is RBAC the recommended model?
- What do soft delete and purge protection prevent, and how do they affect re-creating a vault with the same name?
- Describe a zero-downtime rotation for a database password.
- What belongs in App Configuration vs Key Vault, and how does a Key Vault reference work?
- How does a sentinel key make dynamic configuration refresh efficient?
- How should an app cache secrets, and what must happen when the secret rotates?

## 🚀 Stretch (optional)
Watch Savill's [Using Key Vault key rotation policies](https://www.youtube.com/watch?v=EA_Bc805k4k) and do Learn's [Manage secrets in Java applications](https://learn.microsoft.com/en-us/training/modules/manage-secrets-java-applications-zero-trust/).
