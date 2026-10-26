<div align="center">

# 🧬 Ansible Jinja2 Templates for Configuration Generation

### Device & Application Configs, Filters, Loops, Conditionals & Output Verification

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Red Hat](https://img.shields.io/badge/Red_Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cyber_Security_Lab-0A66C2?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [🎯 Lab Summary](#-lab-summary)
- [🏆 Key Skills Practiced](#-key-skills-practiced)
- [🔑 Key Concepts](#-key-concepts)
- [🌍 Real-World Applications](#-real-world-applications)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Lab Summary

In this lab you built and rendered **two Jinja2 templates in Ansible**, a network device configuration and an application configuration file, both driven from a single shared variables file.

You practiced core Jinja2 filters such as `upper`, `trim`, `selectattr`, and `map`, and used loops and conditionals to control what content appears in the generated output based on data values like `active` status and `environment`.

By running `ansible-playbook --syntax-check` before execution and then using `grep` to confirm specific lines and counts in the rendered files, you verified that the templating logic produced exactly the output the source data implied.

---

## 🏆 Key Skills Practiced

| # | 🎯 Skill | ✅ Description |
|---|----------|----------------|
| 1 | 🖧 **Template Rendering** | Built and rendered two Jinja2 templates: a network device configuration and an application configuration file |
| 2 | 🗃️ **Shared Data Source** | Drove both templates from a single shared variables file |
| 3 | 🔧 **Jinja2 Filters** | Practiced core filters such as `upper`, `trim`, `selectattr`, and `map` |
| 4 | 🔁 **Loops & Conditionals** | Controlled generated content based on data values like `active` status and `environment` |
| 5 | ✅ **Syntax Checking** | Ran `ansible-playbook --syntax-check` before execution |
| 6 | 🔎 **Output Verification** | Used `grep` to confirm specific lines and counts in the rendered files |

---

## 🔑 Key Concepts

| 📘 Concept | 📝 Description |
|-----------|----------------|
| **Jinja2 Template** | A template file that Ansible renders into a generated configuration file |
| **Shared Variables File** | A single data source driving multiple templates |
| **`upper` / `trim` Filters** | Jinja2 filters for transforming string values |
| **`selectattr` / `map` Filters** | Jinja2 filters for selecting and transforming items in data collections |
| **Loops & Conditionals** | Template logic controlling which content appears in the output |
| **`--syntax-check`** | `ansible-playbook` option that validates a playbook before execution |
| **Output Verification with `grep`** | Confirming specific lines and counts in rendered files against the source data |

---

## 🌍 Real-World Applications

Verifying that templating logic produces exactly the output the source data implies is the core skill needed to **debug and trust Jinja2-driven configuration generation in real Ansible projects**.

---

## 🏁 Conclusion

You have built Jinja2 templates driven by shared data, shaped their output with filters, loops, and conditionals, and verified the rendered results with syntax checks and `grep`.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cyber_Security_Education-0A66C2?style=for-the-badge)

**🎉 Lab Complete — Keep Automating!**

</div>
