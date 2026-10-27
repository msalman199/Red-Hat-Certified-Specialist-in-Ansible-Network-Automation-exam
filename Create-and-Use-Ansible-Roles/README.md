<div align="center">

# 🧩 Building and Testing Ansible Roles

### Custom Roles, Ansible Galaxy, Assertion-Based Testing & `ansible-lint`

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=apache&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [📖 Lab Summary](#-lab-summary)
- [🎯 Key Skills Practiced](#-key-skills-practiced)
- [🗂️ Role Directory Structure](#️-role-directory-structure)
- [🔑 Key Concepts](#-key-concepts)
- [🌍 Real-World Applications](#-real-world-applications)
- [🚀 Next Steps](#-next-steps)
- [🏁 Conclusion](#-conclusion)

---

## 📖 Lab Summary

> 💡 **Lab Environment:** This README summarizes the **Conclusion** of the lab. It covers what was built and learned, not the step-by-step tasks.

In this lab, you built a complete Ansible role from the ground up, moving through all seven standard role directories and wiring them together into a working `webserver` role. You then combined that custom role with a community role installed via `ansible-galaxy`, validated everything with an assertion-based test playbook, and documented the role with a README and an `ansible-lint` pass.

---

## 🎯 Key Skills Practiced

### 1️⃣ 🏗️ Building the `webserver` Role

The custom role was assembled across all seven standard role directories and does four things:

- 📦 Installs **Apache**
- 🔥 Configures the **firewall**
- 📄 Deploys a **Jinja2-templated** index page
- ✅ **Verifies its own deployment**

### 2️⃣ 🤝 Mixing In-House and Third-Party Automation

- 🌐 Installed a **community role** via `ansible-galaxy`
- 📋 Managed it through a `requirements.yml` file
- 🔗 Combined it with the custom role, demonstrating how production Ansible projects mix in-house and third-party automation

### 3️⃣ 🧪 Testing and Documentation

- ✔️ Validated the role with an **assertion-based test playbook**
- 📝 Documented the role with a **README**
- 🧹 Ran an **`ansible-lint`** pass

These practices keep roles reusable and maintainable in real automation pipelines.

---

## 🗂️ Role Directory Structure

| 📁 Directory | 🎯 Part of the Role |
|--------------|---------------------|
| `tasks` | Role tasks |
| `handlers` | Role handlers |
| `templates` | Jinja2 templates (e.g., the index page) |
| `files` | Static files |
| `vars` | Role variables |
| `defaults` | Default variables |
| `meta` | Role metadata |

---

## 🔑 Key Concepts

| 🧠 Concept | 📝 Description |
|-----------|----------------|
| **Ansible Role** | A reusable, self-contained unit of automation organized into standard directories |
| **Role Directory Structure** | The seven standard directories: `tasks`, `handlers`, `templates`, `files`, `vars`, `defaults`, `meta` |
| **Jinja2 Template** | Templating used to generate the index page deployed by the role |
| **ansible-galaxy** | Tool used to install community roles |
| **requirements.yml** | File that declares the community roles a project depends on |
| **Assertion-Based Testing** | A test playbook that validates the role's deployment using assertions |
| **ansible-lint** | Linting tool run against the role to check quality and maintainability |
| **Ansible Collections** | Packaging format for distributing roles (next step) |
| **Molecule** | Automated role-testing tool (next step) |

---

## 🌍 Real-World Applications

| 🏢 Scenario | 💼 How This Lab Applies |
|------------|-------------------------|
| **Reusable automation** | Roles package tasks, templates, and variables so the same automation can be reused across projects |
| **Mixed automation sources** | Production projects combine in-house roles with Galaxy community roles via `requirements.yml` |
| **Pipeline-ready quality** | Assertion-based tests, a README, and `ansible-lint` keep roles reusable and maintainable in automation pipelines |

---

## 🚀 Next Steps

1. 📦 Package roles into **Ansible Collections**
2. 🌐 Publish them to a **private or public Galaxy namespace**
3. 🧪 Incorporate automated testing tools such as **Molecule** to further harden roles before using them in production environments

---

## 🏁 Conclusion

With a working `webserver` role, a community role pulled in through `ansible-galaxy`, an assertion-based test playbook, and a documented, linted result, you have practiced the full lifecycle of a reusable Ansible role. You are ready to package roles into Ansible Collections, publish them to Galaxy, and harden them with Molecule before production use.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Powered%20by-Al%20Nafi-0A66C2?style=for-the-badge)

</div>
