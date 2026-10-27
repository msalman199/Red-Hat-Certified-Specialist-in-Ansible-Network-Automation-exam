<div align="center">

# 🧬 Multi-Vendor Configuration Generation with Jinja2

### Data-Driven Templates, Conditionals, Blocks & Macros

![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white)
![Juniper](https://img.shields.io/badge/Juniper-84B135?style=for-the-badge&logo=juniper-networks&logoColor=white)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [📖 Lab Summary](#-lab-summary)
- [🎯 Key Skills Practiced](#-key-skills-practiced)
- [🔑 Key Concepts](#-key-concepts)
- [🌍 Real-World Applications](#-real-world-applications)
- [🚀 Next Steps](#-next-steps)

---

## 📖 Lab Summary

> 💡 **Lab Environment:** This README summarizes the **Conclusion** of the lab. It covers what was built and learned, not the step-by-step tasks.

In this lab you built a data-driven configuration generation workflow using Jinja2, moving from a single vendor-specific template to a multi-vendor system that selects the correct template based on device metadata in YAML.

---

## 🎯 Key Skills Practiced

### 1️⃣ 🏗️ Multi-Vendor Template Selection

- 📄 Started with a **single vendor-specific template**
- 🔀 Progressed to a **multi-vendor system** that selects the correct template based on **device metadata in YAML**

### 2️⃣ 🧩 Core Jinja2 Features

- 🔤 Variables
- 🔁 `{% for %}` loops
- ❓ `{% if %}` conditionals with `is defined` checks
- 🛟 Default filters

### 3️⃣ 🧹 Handling Real-World Data Inconsistencies

Used conditionals to correctly handle inconsistencies such as **Juniper interfaces that lack a `unit` field**.

### 4️⃣ ♻️ Refactoring a Monolithic Template

- 🧱 Refactored a monolithic **Cisco template** into a **base template** with `{% block %}` sections
- 📦 Moved reusable logic into a **separate macro file** imported with `{% import %}`
- ✅ Confirmed the refactored version produced **equivalent output** to the original

---

## 🔑 Key Concepts

| 🧠 Concept | 📝 Description |
|-----------|----------------|
| **Data-Driven Configuration** | Generating device configurations from structured data rather than hand-written configs |
| **Device Metadata (YAML)** | Per-device data used to select the correct vendor template |
| **`{% for %}` Loop** | Iterates over data such as interfaces |
| **`{% if %}` / `is defined`** | Conditionals that handle missing fields safely |
| **Default Filter** | Supplies a fallback value when data is absent |
| **Base Template / `{% block %}`** | Parent template with overridable sections |
| **Macro File / `{% import %}`** | Reusable template logic kept in a separate file |
| **Output Equivalence Check** | Confirming a refactor renders the same result as the original |

---

## 🌍 Real-World Applications

| 🏢 Scenario | 💼 How This Lab Applies |
|------------|-------------------------|
| **Mixed-vendor networks** | One workflow selects the right template per device from its metadata |
| **Inconsistent device data** | `is defined` checks and default filters keep rendering correct when fields are missing |
| **Maintainable templates** | Base templates and macros replace monolithic templates |

---

## 🚀 Next Steps

1. ➕ Extend the framework with templates for **additional vendors or device roles**
2. 🤖 Integrate it into an **Ansible playbook** so Jinja2-rendered configurations can be pushed directly to lab devices in a controlled test environment

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Powered%20by-Al%20Nafi-0A66C2?style=for-the-badge)

</div>
