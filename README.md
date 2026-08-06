# 🎓 GCETHub - Campus Collaboration & Student Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📖 Project Overview

**GCETHub** is a centralized campus collaboration platform developed using **Flask**, **MySQL**, and **Bootstrap**. It enables students and administrators to manage announcements, study materials, placements, events, communities, and notifications from a single platform.

Instead of relying on multiple WhatsApp groups or disconnected communication channels, GCETHub provides a modern dashboard where students can stay informed about campus activities, academic resources, and career opportunities.

---

# ✨ Features

## 🔐 Authentication & Authorization

- User Registration & Login
- Secure Password Authentication
- Flask-Login Session Management
- Role-Based Access Control
  - 👨‍💼 Admin
  - 👨‍🎓 Student

---

## 📊 Dashboard

### Student Dashboard

- Profile Summary
- Statistics Cards
- Recent Activities
- Latest Announcements
- Upcoming Events
- Recent Placements

### Admin Dashboard

- Total Students
- Total Notes
- Total Placements
- Total Events
- Total Communities
- Total Announcements
- Latest Uploaded Content
- Platform Overview

---

## 📢 Announcements

- Add Announcement
- Edit Announcement
- Delete Announcement
- Search Announcements
- Preserve Formatting (Line breaks & spacing)
- Student View Access

---

## 👥 Communities

- Browse Communities
- Search Communities
- Create Community (Admin)
- Edit Community
- Delete Community
- Category Badges

---

## 📄 Study Notes

- Upload Notes
- View PDF
- Download PDF
- Search Notes
- Edit Notes
- Delete Notes

### Permissions

- Students can upload notes.
- Students can edit/delete **only their own notes**.
- Admin can manage all notes.

---

## 💼 Placements

- Job Listings
- Internship Listings
- Search by Company
- Search by Role
- Apply Links
- CRUD Operations (Admin)

---

## 📅 Events

- Upcoming Events
- Event Details
- Search Events
- Admin CRUD
- Student View Only

---

## 🔔 Notifications

Automatic notifications are generated whenever:

- New Announcement
- New Community
- New Placement
- New Event
- New Note

Features:

- Notification Badge
- Mark as Read
- Latest Notifications

---

## 👤 Profile

- View Profile
- Update Profile
- Upload Profile Picture
- Change Password

---

# 🎨 UI / UX Highlights

- Modern Glassmorphism Design
- Responsive Dashboard
- Reusable Components
- Responsive Sidebar
- Sticky Navigation
- Search Components
- Empty State Components
- Flash Message Components
- Mobile Friendly
- Bootstrap Icons
- Professional Cards & Widgets

---

# 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Backend | Python, Flask |
| Database | MySQL, SQLAlchemy |
| Authentication | Flask-Login |
| ORM | Flask-SQLAlchemy |
| Migration | Flask-Migrate |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Template Engine | Jinja2 |
| Icons | Bootstrap Icons |
| Version Control | Git, GitHub |
| IDE | VS Code |

---

# 📁 Project Structure

```
GCETHub/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   ├── utils/
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/payalgit933/GCETHub.git
cd GCETHub
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Database

Update **config.py**

```python
SQLALCHEMY_DATABASE_URI="mysql+pymysql://username:password@localhost/gcethub"

SECRET_KEY="your-secret-key"
```

Create Database

```sql
CREATE DATABASE gcethub;
```

Run Migration

```bash
flask db upgrade
```

---

## 5. Run Application

```bash
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🖼️ Screenshots

## Landing Page

(Add Screenshot)

---

## Student Dashboard

(Add Screenshot)

---

## Admin Dashboard

(Add Screenshot)

---

## Announcements

(Add Screenshot)

---

## Communities

(Add Screenshot)

---

## Notes Module

(Add Screenshot)

---

## Placements

(Add Screenshot)

---

## Events

(Add Screenshot)

---

## Notifications

(Add Screenshot)

---

# 🚀 Future Scope

- AI Campus Assistant
- Mobile Application
- Real-Time Chat
- Event Registration
- Email Notifications
- Global Search
- REST API
- Attendance Module
- Faculty Portal
- Analytics Dashboard

---

# 👨‍💻 Developer

**Payal Kumari**

MCA Student

Galgotias College of Engineering & Technology

Full Stack Developer

GitHub: https://github.com/payalgit933

---

# 🤝 Contributors

- **Payal Kumari** – Backend, Frontend, UI/UX, Database Integration

---

# 📄 License

This project is developed solely for **educational and academic purposes** as an MCA Mini Project.

---

⭐ If you like this project, consider giving it a star on GitHub!
