<div align="center">

# 🔁 Ansible Loops and Conditionals

### Loop Constructs, Conditional Logic & Explicit Failure Handling

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
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
- [🚀 Next Steps](#-next-steps)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Lab Summary

In this lab, you built a series of Ansible playbooks that progressively introduced **loop constructs, conditional logic, and the combination of both** to automate realistic system administration tasks such as package installation, configuration management, and deployment readiness checks.

---

## 🏆 Key Skills Practiced

| # | 🎯 Skill | ✅ Description |
|---|----------|----------------|
| 1 | 🔁 **Loops** | Looped over simple lists, lists of dictionaries, and registered results |
| 2 | 🔀 **Conditionals** | Used conditionals driven by Ansible facts, custom variables, and command output to control exactly when tasks execute |
| 3 | 🧩 **Combined Logic** | Combined loops and conditionals to automate package installation, configuration management, and deployment readiness checks |
| 4 | 🛡️ **Explicit Failure Handling** | Replaced blanket `ignore_errors: yes` usage with explicit prerequisite checks and documented `failed_when: false` conditions |

---

## 🔑 Key Concepts

| 📘 Concept | 📝 Description |
|-----------|----------------|
| **Loop Constructs** | Repeating a task over simple lists, lists of dictionaries, or registered results |
| **Conditional Logic** | Controlling when tasks execute based on facts, custom variables, or command output |
| **Registered Results** | Task output captured and used as loop or conditional input |
| **`ignore_errors: yes`** | Blanket error suppression, replaced in this lab with more explicit handling |
| **Prerequisite Checks** | Explicit checks that replace blanket error suppression |
| **`failed_when: false`** | A documented condition for handling expected failure cases |

---

## 🌍 Real-World Applications

Replacing blanket `ignore_errors: yes` with explicit prerequisite checks and documented `failed_when: false` conditions is a more maintainable and honest way to handle expected failure cases in **production-quality playbooks**.

---

## 🚀 Next Steps

To continue building on these skills:

1. 🧬 Practice writing custom Jinja2 templates driven by loop variables
2. 🏷️ Explore `loop_control` options such as `label` for cleaner output
3. 🧱 Study Ansible's `block`/`rescue`/`always` error-handling constructs as a complement to conditional logic

---

## 🏁 Conclusion

You have built playbooks that combine loops and conditionals to automate realistic system administration tasks, and handled expected failures explicitly rather than suppressing errors.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cyber_Security_Education-0A66C2?style=for-the-badge)

**🎉 Lab Complete — Keep Automating!**

</div>
