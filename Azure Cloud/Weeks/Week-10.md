# ☁️ Azure Cloud · Week 10 — ARM templates, Bicep and virtual machines I

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Infrastructure as code is how real teams deploy and a big part of AZ-104's compute domain (20-25%): reading and modifying ARM/Bicep, then building VMs with the right size, disks and encryption, is core admin and DevOps interview material.

## 🗓️ Sessions

### Tuesday 29 Dec · 45 min — Interpret, modify and export ARM templates
- 📚 **Learn:** Template structure (parameters, variables, resources, outputs, functions, dependsOn), deployment scopes and modes (incremental vs complete), exporting a template from a resource group or deployment. Use [Template structure and syntax](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/syntax), [Export template in the portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal) and [AZ-104 Lab 03b - ARM templates](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_03b-Manage_Azure_Resources_by_Using_ARM_Templates.html).
- 🛠️ **Do:** Create a storage account in the portal, export its template and annotate each section (`w10/exported.json` + notes). Modify it: a `skuName` parameter with allowedValues, a name variable using `uniqueString(resourceGroup().id)`, and an output for the blob endpoint. Deploy twice with `az deployment group create` and show the outputs are identical (idempotency). Done when: the annotated and modified template is deployed twice.

### Wednesday 30 Dec · 45 min — Bicep: author, modify, what-if and decompile
- 📚 **Learn:** Bicep syntax (param, var, resource, module, output, decorators, parent/child), `what-if`, `az bicep decompile`, Bicep vs ARM JSON. Use [What is Bicep?](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview), [Decompile ARM JSON to Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/decompile) and [Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if).
- 🛠️ **Do:** Decompile Tuesday's template to `w10/main.bicep`, fix the warnings by hand, and add a blob container using the `parent` property. Run `az deployment group what-if` and explain every create, modify and no-change line in comments. Deploy, then delete the RG. Done when: `main.bicep`, the what-if output and a 5-line 'ARM vs Bicep' note are committed.

### Friday 01 Jan · 45 min — VM sizes, disks and encryption at host
- 📚 **Learn:** VM size families (B, D, E, F), resizing and deallocation, managed disk types (Standard HDD/SSD, Premium SSD v1/v2, Ultra), data disks, encryption options (server-side encryption, encryption at host, Azure Disk Encryption). Use [Introduction to Azure virtual machines](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-virtual-machines/), [Managed disk encryption options](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) and [Enable encryption at host (CLI)](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli).
- 🛠️ **Do:** Run `az feature register --namespace Microsoft.Compute --name EncryptionAtHost` and wait until it shows Registered. Use `az vm list-skus` to pick a small size in your region that supports encryption at host. Write `w10/vm-checklist.md`: name, region/zone, size, image, SSH auth, disks, NIC/NSG, auto-shutdown, tags. (1 Jan is a holiday - shift if needed.) Done when: the feature is registered and the checklist is committed.

### Saturday 02 Jan · 60 min — LAB: Deploy a Linux VM with Bicep (data disk, encryption at host)
- 📚 **Learn:** VM building blocks in Bicep (VNet, subnet, NSG, public IP, NIC, VM), cloud-init `customData`, data disks and `securityProfile.encryptionAtHost`. Use [Create an Ubuntu VM with Bicep](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-bicep) and [Manage disks with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-disks).
- 🛠️ **Do:** Write `w10/vm.bicep` by adapting the quickstart (understand each block - don't paste blindly): Ubuntu, your chosen size, SSH key, NSG allowing port 22 only from your IP, a 32 GB data disk and `encryptionAtHost: true`. Deploy, SSH in, find the disk with `lsblk`, format and mount it, then run `nuke-lab.sh 10`. Done when: Bicep, deployment output and `lsblk`/`df -h` evidence are committed and the RG is deleted.

## 📦 Deliverable (by Saturday night)
`w10/` annotated ARM template, `main.bicep` + what-if output, VM checklist, and `vm.bicep` with deployment evidence.

## ✅ Self-check (Sunday test preview)
- Incremental vs complete deployment mode: what can complete mode delete?
- What does dependsOn do, and why does Bicep rarely need it?
- How do you convert an exported ARM template to Bicep, and what usually needs manual cleanup?
- Encryption at host vs Azure Disk Encryption vs server-side encryption: what does each encrypt, and where?
- Why must a VM sometimes be deallocated to resize it, and what happens to a dynamic public IP?
- Which disk type would you choose for a PostgreSQL VM vs a dev box, and why?

## 🚀 Stretch (optional)
Refactor `vm.bicep` into `network.bicep` and `vm.bicep` modules with a `.bicepparam` file, and add an auto-shutdown schedule resource.
