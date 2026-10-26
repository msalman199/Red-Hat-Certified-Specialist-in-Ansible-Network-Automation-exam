<div align="center">

# 🪜 Ansible Variable Hierarchy and Precedence

### vars, group_vars, host_vars, vars_files, extra_vars & assert Validation

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
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
- [📊 Variable Precedence](#-variable-precedence)
- [🌍 Real-World Applications](#-real-world-applications)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Lab Summary

In this lab, students built a small but complete **Ansible variable hierarchy**, combining playbook-level `vars`, inventory variables, `group_vars`, `host_vars`, and external `vars_files` into a single set of playbooks, and confirmed how each layer contributes to the final value seen by a task.

Students then used `extra_vars` on the command line to override those layers at runtime and verified the override took effect on every host, and used the `assert` module to validate that required variables were defined and held values consistent with the actual configuration data in `host_vars`.

---

## 🏆 Key Skills Practiced

| # | 🎯 Skill | ✅ Description |
|---|----------|----------------|
| 1 | 🧱 **Layered Variable Hierarchy** | Combined playbook-level `vars`, inventory variables, `group_vars`, `host_vars`, and external `vars_files` into a single set of playbooks |
| 2 | 🔎 **Layer Contribution Analysis** | Confirmed how each layer contributes to the final value seen by a task |
| 3 | ⚡ **Runtime Overrides** | Used `extra_vars` on the command line to override those layers and verified the override took effect on every host |
| 4 | ✅ **Variable Validation** | Used the `assert` module to validate that required variables were defined and held values consistent with the configuration data in `host_vars` |

---

## 🔑 Key Concepts

| 📘 Concept | 📝 Description |
|-----------|----------------|
| **Playbook `vars`** | Variables defined at the playbook level |
| **Inventory Variables** | Variables defined in the inventory |
| **`group_vars`** | Variables applied to groups of hosts |
| **`host_vars`** | Variables applied to individual hosts |
| **`vars_files`** | External files of variables loaded by a playbook |
| **`extra_vars`** | Command-line variables used for deliberate runtime overrides |
| **Variable Precedence** | The ordering that determines which variable source supplies the final value |
| **`assert` Module** | Validates that critical variables are defined and hold expected values |

---

## 📊 Variable Precedence

The key takeaway is Ansible's variable precedence, from highest to lowest as presented in this lab:

| 🥇 Priority | 📦 Source |
|------------|-----------|
| 1 (highest) | Command-line `extra_vars` — always wins |
| 2 | More specific sources like `host_vars` and `vars_files` |
| 3 (lowest) | General defaults set in `group_vars` or the playbook itself |

---

## 🌍 Real-World Applications

When designing real automation:

- 🗂️ Keep environment-specific values in `host_vars`/`group_vars` or dedicated `vars_files`
- ⚡ Reserve `extra_vars` for deliberate runtime overrides
- 🛡️ Always validate critical variables with `assert` before they are used in tasks that change system state

---

## 🏁 Conclusion

You have built a complete variable hierarchy, seen how `extra_vars` overrides every other layer, and used `assert` to guard critical variables before they affect system state.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cyber_Security_Education-0A66C2?style=for-the-badge)

**🎉 Lab Complete — Keep Automating!**

</div>
