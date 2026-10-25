# ☁️ Azure Cloud · Week 22 — Key Vault, App Configuration and workload identity

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Leaked secrets cause real outages and breaches. AI-200 tests storing, retrieving and rotating secrets with Key Vault and centralizing settings with App Configuration, and every CI/CD pipeline - including Java's GitHub-to-Azure deploy - needs workload identity instead of stored passwords.

## 🗓️ Sessions

### Tuesday 23 Mar · 45 min — Key Vault: secrets, versions, RBAC, soft delete and rotation
- 📚 **Learn:** Vault objects (secrets, keys, certificates) and versions, Azure RBAC data roles (recommended) vs legacy access policies, soft delete (7-90 day retention) and purge protection, SDK retrieval with caching, and rotation: two credentials with overlap, expiry dates, a near-expiry Event Grid event triggering a rotation function, key auto-rotation policies. Read the [Python secrets quickstart](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python). Optional: the [rotation tutorial](https://learn.microsoft.com/en-us/azure/key-vault/secrets/tutorial-rotation).
- 🛠️ **Do:** Create a vault with RBAC authorization (unique name - deleted names stay reserved during retention) and grant yourself Key Vault Secrets Officer. In `py/kv_demo.py` set a secret with a 30-day expiry, read it, update it (new version), list versions and cache reads for 5 minutes; delete the secret, then recover it. Write the 5-step dual-credential rotation for TicketVerse's database password in `w22/rotation.md`. Done when: versions, a cache-hit log, recovery evidence and the rotation design are in `w22/`.

### Wednesday 24 Mar · 45 min — Workload identity: service principals, managed identities, GitHub OIDC
- 📚 **Learn:** Service principal (an app registration's identity, authenticated by a secret, certificate or federated credential) vs managed identity (Azure-managed, no secrets; system- or user-assigned) vs federated credential (trust a short-lived GitHub OIDC token instead of storing any secret). You'll reuse this in Java W26's CI/CD. Read [Use GitHub Actions to connect to Azure with OpenID Connect](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect). Optional: [Federate a user-assigned managed identity](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity).
- 🛠️ **Do:** Create user-assigned identity `id-gh-azure-labs`, give it Reader on one lab RG and add a federated credential: `az identity federated-credential create --issuer https://token.actions.githubusercontent.com --subject repo:<you>/azure-labs:ref:refs/heads/main --audiences api://AzureADTokenExchange`. Store the client, tenant and subscription IDs as repo secrets and push a 10-line workflow (`permissions: id-token: write`, `azure/login@v2`, then `az group list`). Done when: the run lists your RGs and no password or client secret exists anywhere.

### Friday 26 Mar · 45 min — App Configuration: key-values, labels, feature flags, Key Vault references
- 📚 **Learn:** Key-values, labels per environment, feature flags and filters, Key Vault references (App Configuration stores a pointer; the app reads the secret), the Python provider, dynamic refresh with a sentinel key, App Configuration vs Key Vault. Read the [Python provider quickstart](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-python-provider). Optional: [Feature management](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management).
- 🛠️ **Do:** Create a Free-tier store; add `TicketVerse:Search:TopK` with labels dev and prod, a feature flag `AskTicketVerse`, and a Key Vault reference to your DB secret. In `py/appconfig_demo.py` load the `dev` label with DefaultAzureCredential, print the resolved secret's length (never the value), then toggle the flag and see it change after refresh. Done when: label switch, flag toggle and secret-resolution evidence are in `w22/`.

### Saturday 27 Mar · 60 min — LAB: Container on App Service with managed identity and Key Vault
- 📚 **Learn:** App Service custom containers: pull from ACR with the app's managed identity (AcrPull + `acrUseManagedIdentityCreds`), `WEBSITES_PORT` for non-80 ports, app settings as environment variables, and Key Vault references (`@Microsoft.KeyVault(SecretUri=...)`) resolved through the same identity. Read [Configure a custom container](https://learn.microsoft.com/en-us/azure/app-service/configure-custom-container) (managed identity section). Optional: the AI-200 module [Deploy containers to Azure App Service](https://learn.microsoft.com/en-us/training/modules/deploy-containers-azure-app-service/).
- 🛠️ **Do:** Create a Basic ACR and `az acr import` an image - DocuMind from GHCR if you pushed it there, else `mcr.microsoft.com/azuredocs/aci-helloworld`. Create a Linux B1 web app from it with a system-assigned identity, grant AcrPull and set `acrUseManagedIdentityCreds` (`az webapp config set --generic-configurations`); set `WEBSITES_PORT` if needed, one plain setting and one Key Vault-referenced secret (grant Key Vault Secrets User). Check the log stream, the app URL and that the reference resolved. Delete the RG and purge the vault. Done when: the app runs with no registry or app secrets in settings.

## 📦 Deliverable (by Saturday night)
`w22/` Key Vault version/caching/recovery evidence and rotation design, an OIDC workflow run through a federated credential, App Configuration label/flag/reference evidence, and a container on App Service pulling from ACR and reading a Key Vault reference through managed identity.

## ✅ Self-check (Sunday test preview)
- Key Vault RBAC vs access policies: why is RBAC the recommended model?
- What do soft delete and purge protection prevent, and how do they affect re-creating a vault with the same name?
- Describe a zero-downtime rotation for a database password, and what an app that caches the secret must do when it rotates.
- Service principal vs managed identity vs federated credential: when would you use each?
- What belongs in App Configuration vs Key Vault, and how does a Key Vault reference work?
- How does App Service pull a container image from ACR without admin credentials?
- How does a sentinel key make dynamic configuration refresh efficient?

## 🚀 Stretch (optional)
Do the exercises in the official AI-200 modules [Manage application secrets with Key Vault](https://learn.microsoft.com/en-us/training/modules/manage-app-secrets-key-vault/) and [Manage application settings with App Configuration](https://learn.microsoft.com/en-us/training/modules/manage-app-settings-app-config/); then Savill's [Using Key Vault key rotation policies](https://www.youtube.com/watch?v=EA_Bc805k4k) or Learn's [Manage secrets in Java applications](https://learn.microsoft.com/en-us/training/modules/manage-secrets-java-applications-zero-trust/).
