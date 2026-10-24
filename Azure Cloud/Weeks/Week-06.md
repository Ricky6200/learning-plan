# ☁️ Azure Cloud · Week 06 — Entra ID users, groups, licenses and SSPR

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Identity and governance is 20-25% of AZ-104, and every migration starts in Entra ID: creating users and groups, inviting partner (B2B) users and enabling self-service password reset are daily admin tasks that interviewers probe.

## 🗓️ Sessions

### Tuesday 01 Dec · 45 min — Activation day: subscription, guardrails, Entra ID P2 trial
- 📚 **Learn:** Activation checklist from COST_SAFETY_AND_ACCOUNT_SETUP.md (sign-up, budget + alerts first, tags, default region); Entra licensing - dynamic groups and SSPR for cloud users need Entra ID P1 or higher. Use [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing), [Sign up for Entra ID P1/P2](https://learn.microsoft.com/en-us/entra/fundamentals/get-started-premium) and [Understand Microsoft Entra ID](https://learn.microsoft.com/en-us/training/modules/understand-azure-active-directory/).
- 🛠️ **Do:** Path B: sign up for the Azure free account (note the date: the credit ends 30 days later) and immediately run your W1 guardrails: budget with 50/80/100% alerts, action group email, test `new-lab.sh` and `nuke-lab.sh`. Both paths: start the Microsoft Entra ID P2 trial in the Entra admin center and note its end date. Done when: budget visible in Cost Management, trial active, and both dates recorded in `w06/notes.md`.

### Wednesday 02 Dec · 45 min — Users, groups, properties and dynamic membership
- 📚 **Learn:** Cloud vs synced vs guest users, key properties (usage location, department), bulk create, security vs Microsoft 365 groups, assigned vs dynamic membership, restoring deleted users. Use [Create, configure, and manage identities](https://learn.microsoft.com/en-us/training/modules/create-configure-manage-identities/), [How to manage groups](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups) and [Dynamic membership rules](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-membership).
- 🛠️ **Do:** In the Entra admin center (or with a bulk-create CSV) create 6 users - 2 each in Java, QA and Ops - with department and usage location India; one security group per department; and a dynamic group with the rule `user.department -eq "Java"`. Delete one user and restore it. Done when: `az ad user list --query '[].userPrincipalName' -o table` output and the dynamic group's members are captured in `w06/`.

### Friday 04 Dec · 45 min — Group licensing, B2B guests and self-service password reset
- 📚 **Learn:** Group-based licensing (needs usage location), external identities (B2B invitation, guest vs member, external collaboration settings), SSPR scope, authentication methods and registration. Use Microsoft Learn's [identities video](https://www.youtube.com/watch?v=UUkshXoGOD8), [Add B2B collaboration users](https://learn.microsoft.com/en-us/entra/external-id/add-users-administrator) and [Enable SSPR](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr).
- 🛠️ **Do:** Assign the P2 trial license to the Java group and confirm a member inherits it; invite a personal Gmail or Outlook address as a B2B guest and accept the invitation in a private window; enable SSPR for a pilot group with 2 methods and reset a pilot user's password. Done when: license inheritance, the guest's 'Accepted' state and a successful SSPR reset are evidenced in `w06/`.

### Saturday 05 Dec · 60 min — LAB: AZ-104 Lab 01 - manage Entra ID identities
- 📚 **Learn:** The official lab on users, groups and guest invitations: [AZ-104 Lab 01 - Manage Entra ID identities](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_01-Manage_Entra_ID_Identities.html), plus [What is B2B collaboration?](https://learn.microsoft.com/en-us/entra/external-id/what-is-b2b) for the guest-user concepts behind it.
- 🛠️ **Do:** Complete Lab 01 in your tenant, typing commands instead of pasting them. Then write `w06/group-setup.sh` (10-15 lines) that creates a group and adds two existing users with `az ad group create` and `az ad group member add`, and run it. Clean up lab users and groups (keep your admin account). Done when: lab finished, script committed, and `az ad group list -o table` shows only the groups you intend to keep.

## 📦 Deliverable (by Saturday night)
Subscription active with budget + alerts; Entra ID P2 trial on; `w06/` evidence (users, dynamic group, licensing, B2B guest, SSPR reset) and `group-setup.sh`.

## ✅ Self-check (Sunday test preview)
- Security group vs Microsoft 365 group: when would you use each?
- Why can group-based licensing fail for a user without a usage location?
- How does a B2B guest authenticate, and how do member and guest user types differ?
- Which license do dynamic membership groups require? Write a rule for all users in the Ops department.
- How do you restore a deleted user, and for how long is that possible?
- Which SSPR authentication methods would you require for administrators vs normal users, and why?

## 🚀 Stretch (optional)
Watch Savill's [Beginners Guide to Entra ID](https://www.youtube.com/watch?v=UP2kzp14WA0); optionally attempt the hosted Applied Skills lab [Get started with identities and access using Microsoft Entra](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/).
