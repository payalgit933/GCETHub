<div align="center">

# 🎓 GCETHub

### *Unified Campus Collaboration & Student Portal*

A modern, centralized platform empowering students and administrators with real-time academic resources, event coordination, placement opportunities, and campus announcements.

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

---

</div>

## 📌 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Role-Based Access Control](#-role-based-access-control)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
- [Screenshots](#-screenshots)
- [Future Roadmap](#-future-roadmap)
- [Developer & Credits](#-developer--credits)
- [License](#-license)

---

## 📖 About the Project

**GCETHub** replaces fragmented communication channels (like scattered WhatsApp groups and offline notice boards) with a single, streamlined Web Portal. Designed specifically for **Galgotias College of Engineering & Technology**, GCETHub bridges the communication gap between students and administration.

> 💡 **Why GCETHub?**
> * **Centralized Knowledge:** Study materials, official announcements, and career listings hosted in one organized place.
> * **Real-Time Notifications:** Dynamic alerts triggered for new activities.
> * **Modern UI:** Built with a glassmorphism design language using Bootstrap 5 for seamless mobile and desktop experiences.

---

## ✨ Key Features

### 📢 Announcements & Campus Updates
* **Rich Formatting:** Preserves line breaks and structural layouts for clear notice reading.
* **Search & Filter:** Quickly locate official notices by keyword or subject.

### 📄 Academic Resource Center (Notes)
* **Peer-to-Peer Sharing:** Students and admins can upload PDF study notes.
* **In-Browser Preview:** View materials directly within the portal without downloading.
* **Granular Permissions:** Authors can edit/delete their own notes; admins hold universal moderation rights.

### 💼 Career & Placement Cell
* **Opportunities Board:** Live feeds for full-time job roles and internship opportunities.
* **Direct Applications:** Integrated links for fast application workflows.
* **Filter Options:** Search opportunities by role, company, or requirement.

### 👥 Campus Communities & Clubs
* **Club Discovery:** Explore active student societies, technical chapters, and interest groups.
* **Category Badges:** Visual identifiers for tech, cultural, and sports clubs.

### 📅 Events & Calendar
* **Campus Happenings:** Centralized listing for hackathons, workshops, and cultural fests.
* **Detailed Breakdown:** Schedule, venue details, and registration links.

### 🔔 Smart Notification System
* Auto-generated notification badges for new uploads, events, placements, and notices.
* One-click "Mark as Read" functionality.

---

## 🔐 Role-Based Access Control

| Feature / Action | 👨‍🎓 Student | 👨‍💼 Admin |
| :--- | :---: | :---: |
| View Announcements, Events & Placements | Read-Only | Full CRUD |
| Upload & Share Study Notes | ✅ | ✅ |
| Edit / Delete Notes | Own Notes Only | All Notes |
| Create & Manage Communities | View Only | Full CRUD |
| Dashboard Access | Personalized Student View | System-Wide Analytics |

---

## 🛠️ Tech Stack

<details>
<summary><b>Click to expand technology details</b></summary>

| Layer | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3.13, Flask 3.x |
| **Database & ORM** | MySQL, Flask-SQLAlchemy, Flask-Migrate |
| **Authentication** | Flask-Login, Werkzeug Security |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3, Jinja2 Templates |
| **Icons & Visuals** | Bootstrap Icons, Custom Glassmorphism CSS |
| **Tooling** | Git, GitHub, VS Code |

</details>

---

## 📂 Project Architecture
