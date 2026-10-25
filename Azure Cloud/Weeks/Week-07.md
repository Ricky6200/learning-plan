# ☁️ Azure Cloud · Week 07 — RBAC, subscriptions and governance at scale

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** Who can do what, where - and what nobody may ever do - is the other half of AZ-104's identity and governance domain and the first thing auditors check in a migration landing zone.

## 🗓️ Sessions

### Tuesday 08 Dec · 45 min — Azure RBAC: built-in roles, scopes, interpreting assignments
- 📚 **Learn:** Owner, Contributor, Reader, User Access Administrator and data-plane roles; scopes and inheritance; Azure roles vs Entra roles; reading effective access. Read [Secure your Azure resources with Azure RBAC](https://learn.microsoft.com/en-us/training/modules/secure-azure-resources-with-rbac/). Optional: [Azure roles vs Entra roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles).
- 🛠️ **Do:** Assign the Java group Reader on the subscription and Contributor on `rg-lab-w07`; give one QA user Storage Blob Data Reader on a storage account. Run `az role assignment list --all --assignee <upn> -o table` for each and write what they can and cannot do, including why Reader can't read blob data. Remove the assignments. Done when: 3 assignments + interpretation notes committed.

### Wednesday 09 Dec · 45 min — Azure Policy, initiatives, resource locks and tags
- 📚 **Learn:** Policy definitions, initiatives, assignments, effects (Deny, Audit, Modify, DeployIfNotExists), compliance and remediation; lock types; tag governance. Read the [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview). Optional: [Lock your resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources).
- 🛠️ **Do:** Assign the built-in 'Allowed locations' (Central India + South India) and 'Require a tag on resource groups' (costCenter) policies at subscription scope; prove both with non-compliant creates (expect RequestDisallowedByPolicy). Add a ReadOnly lock to an RG holding a storage account and observe what breaks (e.g., listing keys). Then remove the tag-policy assignment (or add `costCenter` to `new-lab.sh`) so later labs aren't blocked. Done when: 2 denials + lock behaviour are documented in `w07/policy.md` and no lab script fails on the tag rule.

### Friday 11 Dec · 45 min — Management groups, subscriptions, budgets, cost alerts and Advisor
- 📚 **Learn:** Management group hierarchy, moving resources between resource groups, budgets with action groups, cost alerts, Azure Advisor recommendations, and policy exemptions: Allowed locations will block Foundry models offered only outside India, so before AI W25 (12 Apr) you exempt that one resource group instead of deleting the policy. Read the [Management groups overview](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview). Optional: [Cost alerts](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending).
- 🛠️ **Do:** Create management group `mg-learning`, move your subscription under it, and re-assign 'Allowed locations' there (check inheritance in the compliance view). Create an RG-scoped budget that triggers an action-group email at 80%. Record 3 Advisor recommendations (or why there are none). Move a storage account between RGs with `az resource move` and compare resource IDs. Write the `az policy exemption create` command you'll need in April. Done when: MG tree, budget, Advisor notes, move output and the exemption command are committed.

### Saturday 12 Dec · 60 min — LAB: AZ-104 Lab 02a - custom roles and RBAC at scale
- 📚 **Learn:** Custom roles (Actions, NotActions, DataActions, AssignableScopes) assigned at management-group scope. Do the official [Lab 02a - Manage subscriptions and RBAC](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_02a_Manage_Subscriptions_and_RBAC_Entra.html). Optional, if time remains: the Modify-tag + remediation task in [Lab 02b - Manage governance via Azure Policy](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_02b-Manage_Governance_via_Azure_Policy.html).
- 🛠️ **Do:** Before starting, write your own `w07/custom-role.json` for a 'VM operator' (start, stop and restart VMs; read resource groups), then compare it with the lab's approach. Complete Lab 02a (management group, custom role, assignment); add Lab 02b's Modify + remediation task if time remains. Repeat one assignment in Az PowerShell in Cloud Shell (`New-AzRoleAssignment -SignInName <upn> -RoleDefinitionName Reader -ResourceGroupName <rg>`). Clean up the custom role, lab assignments and RGs. Done when: Lab 02a is done, the PowerShell assignment was listed and `custom-role.json` is committed.

## 📦 Deliverable (by Saturday night)
`w07/` RBAC interpretation notes, policy and lock experiments (tag policy removed afterwards), management group tree, budget with action group, Advisor notes, the April policy-exemption command, `custom-role.json` and one Az PowerShell role assignment.

## ✅ Self-check (Sunday test preview)
- A user is Reader on the subscription and Contributor on one RG: what can they do in that RG and elsewhere?
- Why can't a subscription Owner read blobs with `--auth-mode login` by default?
- Deny vs Audit vs Modify vs DeployIfNotExists: give one use case each.
- A ReadOnly lock on a storage account breaks which common operations, and why?
- What happens to policy and RBAC when you move a subscription to another management group, and when would you add a policy exemption instead of deleting an assignment?
- Budgets vs cost alerts vs Advisor: which can trigger automation through an action group?
- What does NotActions mean in a custom role, and how is it different from a deny assignment?

## 🚀 Stretch (optional)
Finish any Lab 02b tasks you skipped, then watch the first 30 minutes of Savill's [Anatomy of Azure Policy](https://www.youtube.com/watch?v=4wGns611G4w) and write a custom policy that audits VMs without an `owner` tag.
