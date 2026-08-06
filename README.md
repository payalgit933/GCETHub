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

GCETHub/├── app/│   ├── models/        # SQLAlchemy database models (User, Note, Event, etc.)│   ├── routes/        # Blueprint route handlers (Auth, Notes, Admin, etc.)│   ├── static/        # Static assets (Custom CSS, JavaScript, Images, Uploads)│   ├── templates/     # Jinja2 HTML templates & layout partials│   ├── utils/         # Helpers, custom decorators, & upload handlers│   ├── extensions.py  # Flask extensions initialization (db, login_manager)│   └── init.py    # Application factory├── migrations/        # Database migration scripts (Alembic)├── config.py          # Environment settings & credentials setup├── run.py             # Application entry point├── requirements.txt   # Python dependency list└── README.md          # Project documentation
---

## ⚙️ Getting Started

Follow these steps to set up **GCETHub** locally on your machine.

### Prerequisites
* **Python 3.10+** installed
* **MySQL Server** installed and running

---

### Step 1: Clone the Repository
```bash
git clone [https://github.com/payalgit933/GCETHub.git](https://github.com/payalgit933/GCETHub.git)
cd GCETHub
Step 2: Set Up Virtual EnvironmentOn Windows:Bashpython -m venv venv
venv\Scripts\activate
On macOS / Linux:Bashpython3 -m venv venv
source venv/bin/activate
Step 3: Install DependenciesBashpip install -r requirements.txt
Step 4: Configure Database & EnvironmentCreate a MySQL database:SQLCREATE DATABASE gcethub;
Update configuration settings in config.py:PythonSQLALCHEMY_DATABASE_URI = "mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/gcethub"
SECRET_KEY = "your-custom-secret-key"
Step 5: Run Database MigrationsBashflask db upgrade
Step 6: Launch ApplicationBashpython run.py
🚀 Access the platform by opening your browser at http://127.0.0.1:5000🖼️ ScreenshotsStudent DashboardAdmin AnalyticsAcademic NotesPlacement Portal🚀 Future Roadmap[x] Core Authentication & Role-Based Access Control[x] Announcements, Notes, Placements, Events & Community Modules[x] Automatic In-App Notifications[ ] 🤖 AI Campus Assistant: Smart Q&A bot for syllabus & college FAQs[ ] 💬 Real-Time Community Chat: Instant messaging for student clubs[ ] 📊 Academic Tracker: Personal attendance and marks manager[ ] 📱 Mobile Application: Cross-platform Flutter / React Native client[ ] 📧 Automated Email Digests: Priority alerts for high-stakes notices👨‍💻 Developer & CreditsDeveloped with ❤️ by Payal KumariMCA Student @ Galgotias College of Engineering & TechnologyFull Stack Developer🌐 GitHub: @payalgit933💼 Project Repository: GCETHub Repository📄 LicenseThis project was developed solely for educational and academic purposes as an MCA Mini Project at Galgotias College of Engineering & Technology.⭐ If you find this project helpful, please give it a star on GitHub! ⭐
