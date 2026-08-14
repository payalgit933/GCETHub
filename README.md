<div align="center">

# 🎓 GCETHub

### Campus Collaboration & Student Portal

A modern campus management platform built using **Flask, MySQL, Bootstrap, and Jinja2** that centralizes announcements, study materials, placements, events, communities, and notifications into one unified portal.

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)](https://getbootstrap.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)](https://www.mysql.com/)
[![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)](#)

</div>

---

## 📌 Table of Contents

- [📖 About](#-about)
- [✨ Features](#-features)
  - [🔐 Authentication](#-authentication)
  - [📊 Dashboard](#-dashboard)
  - [📢 Announcements](#-announcements)
  - [👥 Communities](#-communities)
  - [📄 Study Notes](#-study-notes)
  - [💼 Placements](#-placements)
  - [📅 Events](#-events)
  - [🔔 Notifications](#-notifications)
  - [👤 Profile](#-profile)
- [🔒 Role-Based Access](#-role-based-access)
- [🎨 UI / UX Highlights](#-ui--ux-highlights)
- [🛠 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙ Installation](#-installation)
- [📸 Screenshots](#-screenshots)
- [🚀 Future Scope](#-future-scope)
- [👩‍💻 Developer](#-developer)
- [📜 License](#-license)

---

## 📖 About

**GCETHub** is a centralized campus collaboration platform developed for students and administrators.

Instead of relying on multiple WhatsApp groups, emails, and notice boards, GCETHub provides a **single dashboard** where students can access:

* 📢 Announcements
* 📄 Study Notes
* 💼 Placements
* 📅 Events
* 👥 Student Communities
* 🔔 Notifications

The system provides **role-based access** so administrators can manage campus content while students can securely access academic resources.

---

## ✨ Features

### 🔐 Authentication
* User Registration
* Secure Login
* Logout
* Password Hashing
* Role-Based Access (Admin / Student)

---

### 📊 Dashboard

#### Student Dashboard
* Total Notes
* Total Events
* Total Placements
* Total Communities
* Total Announcements
* Upcoming Events Widget
* Latest Activity Widget
* Personalized Statistics

#### Admin Dashboard
* Overall Platform Statistics
* Latest Uploads
* Recent Announcements
* Recent Placements
* Recent Events
* Upload Statistics

---

### 📢 Announcements
* Add Announcement (Admin)
* Edit Announcement (Admin)
* Delete Announcement (Admin)
* Search Announcements
* Rich Text Formatting
* Line Break Preservation
* Students can View Only

---

### 👥 Communities
* Browse Communities
* Search Communities
* Category Badges
* Create Community (Admin)
* Edit Community (Admin)
* Delete Community (Admin)

> ℹ️ *Students have **read-only access**.*

---

### 📄 Study Notes
* Upload PDF
* View PDF
* Download Notes
* Search Notes
* Edit Own Notes
* Delete Own Notes

#### Permissions
* **Students:** Upload Notes, Edit Only Their Own Notes, Delete Only Their Own Notes
* **Admin:** Full Control

---

### 💼 Placements
* Internship Listings
* Job Listings
* Company Details
* Apply Links
* Search Placements

* **Admin can:** Add, Edit, Delete
* **Students can:** View, Search, Apply

---

### 📅 Events
* Campus Events
* Venue
* Date
* Time
* Organizer
* Registration Links
* Search Events

* **Admin:** CRUD Operations
* **Students:** View Only

---

### 🔔 Notifications
Automatic notifications when new:
* Announcement
* Placement
* Note
* Event

are added.

#### Features
* Notification Badge
* Read Status
* Recent Notifications

---

### 👤 Profile
* Profile Picture Upload
* Change Profile Picture
* Edit Profile
* Change Password

---

## 🔒 Role-Based Access

| Feature | Student | Admin |
| :--- | :---: | :---: |
| View Announcements | ✅ | ✅ |
| Add Announcement | ❌ | ✅ |
| Edit Announcement | ❌ | ✅ |
| Delete Announcement | ❌ | ✅ |
| View Communities | ✅ | ✅ |
| Add Community | ❌ | ✅ |
| Edit Community | ❌ | ✅ |
| Delete Community | ❌ | ✅ |
| Upload Notes | ✅ | ✅ |
| Edit Own Notes | ✅ | ✅ |
| Delete Own Notes | ✅ | ✅ |
| Edit All Notes | ❌ | ✅ |
| Delete All Notes | ❌ | ✅ |
| View Placements | ✅ | ✅ |
| Add Placement | ❌ | ✅ |
| Edit Placement | ❌ | ✅ |
| Delete Placement | ❌ | ✅ |
| View Events | ✅ | ✅ |
| Add Event | ❌ | ✅ |
| Edit Event | ❌ | ✅ |
| Delete Event | ❌ | ✅ |

---

## 🎨 UI / UX Highlights

* Modern Glassmorphism Design
* Responsive Layout
* Bootstrap 5
* Sticky Navigation Bar
* Sidebar Navigation
* Search Bars Across Modules
* Empty State Components
* Latest Activity Widgets
* Statistic Cards
* Mobile Friendly Design

---

## 🛠 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Backend** | Flask |
| **Language** | Python 3.13 |
| **Database** | MySQL |
| **ORM** | Flask-SQLAlchemy |
| **Authentication** | Flask-Login |
| **Migration** | Flask-Migrate |
| **Frontend** | HTML5 |
| **Styling** | CSS3 |
| **UI Framework** | Bootstrap 5 |
| **Icons** | Bootstrap Icons |
| **Template Engine** | Jinja2 |
| **Version Control** | Git & GitHub |

---

## 📂 Project Structure

```text
GCETHub
│
├── app
│   ├── models
│   ├── routes
│   ├── static
│   │   ├── css
│   │   ├── images
│   │   └── uploads
│   ├── templates
│   │   ├── auth
│   │   ├── dashboard
│   │   └── includes
│   ├── utils
│   ├── extensions.py
│   └── __init__.py
│
├── migrations
├── config.py
├── requirements.txt
├── run.py
└── README.md

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/payalgit933/GCETHub.git
cd GCETHub
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Configure Database

Create Database

```sql
CREATE DATABASE gcethub;
```

Update `config.py`

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/gcethub"

SECRET_KEY = "your-secret-key"
```

---

## 5. Run Migrations

```bash
flask db upgrade
```

---

## 6. Start Application

```bash
python run.py runserver
```

Open

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## Landing Page

> Add screenshot

```
![Student Dashboard](ss/dashboard.png)
```

---

## Student Dashboard

> Add screenshot

```
ss/dashboard.png
```

---

## Admin Dashboard

> Add screenshot

```
ss/admin_dashboard.png
```

---

## Notes Module

> Add screenshot

```
ss/notes.png
```

---

## Placements

> Add screenshot

```
ss/placements.png
```

---

## Events

> Add screenshot

```
ss/events.png
```

---

## Communities

> Add screenshot

```
ss/communities.png
```

---

## Profile

> Add screenshot

```
ss/profile.png
```

---

# 🚀 Future Scope

- 🤖 AI Campus Assistant
- 💬 Real-Time Chat
- 📱 Android Application
- 📧 Email Notifications
- 📊 Advanced Analytics
- 🔎 Global Search
- 📅 Event Registration
- 📚 Attendance Management
- 🎓 Result & GPA Tracking
- REST API Integration

---

# 👩‍💻 Developer

**Payal Kumari**

MCA Student

Galgotias College of Engineering & Technology

**GitHub**

https://github.com/payalgit933

Project Repository

https://github.com/payalgit933/GCETHub

---

# 📜 License

This project was developed as an **MCA Mini Project** for educational and academic purposes.

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a Star ⭐

</div>
