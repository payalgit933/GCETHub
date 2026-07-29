# 🎓 GCETHub - Campus Collaboration & Student Platform

![GCETHub Banner](static/banner.png)

## 🚀 Overview

**GCETHub** is a modern campus collaboration platform designed to bring students, faculty, and campus communities together in one place.

The platform solves the problem of scattered information across multiple WhatsApp groups and disconnected channels by providing a centralized space for:

* 📢 Campus announcements
* 👥 Student communities
* 📚 Notes and academic resources
* 💼 Placement opportunities
* 🎉 Events and activities
* 👤 Student profiles and networking

GCETHub aims to create a digital campus ecosystem where students can easily access important updates, collaborate with peers, and stay connected with college activities.

---

# ✨ Key Features

## 📢 Announcements Module

* Centralized college announcements
* Important notices and updates
* Organized information instead of multiple messaging groups

## 👥 Community Module

* Student communities based on interests and departments
* Peer collaboration and discussions
* Campus networking

## 📚 Notes & Resources

* Upload and access study materials
* Share academic resources
* Easy knowledge sharing among students

## 💼 Placement Module

* Placement updates
* Internship opportunities
* Career-related information

## 👤 Profile Module

* Student profile management
* Profile picture support
* Personal academic information display

Profile includes:

* Name
* Email
* Enrollment number
* Department
* Year
* Section
* Role

## 🔐 Authentication System

* User registration
* Secure login
* Role-based access
* Protected routes

---

# 🖥️ Screenshots

## Landing Page

Modern campus-focused landing page introducing GCETHub's vision.

![Landing Page](static/images/landing.png)

## Dashboard

Student dashboard providing quick access to campus features.

![Dashboard](static/images/dashboard.png)

## Profile Module

Student profile management interface.

![Profile](static/images/profile.png)

---

# 🛠️ Tech Stack

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login

## Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript
* Jinja2 Templates

## Database

* SQLite / SQLAlchemy

## Tools

* VS Code
* Git & GitHub
* Flask Development Server

---

# 📂 Project Structure

```
GCETHub/

│
├── app/
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── profile.py
│   │   ├── dashboard.py
│   │   └── ...
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── templates/
│   │   │
│   │   ├── dashboard/
│   │   │   ├── dashboard.html
│   │   │   ├── dashboard_base.html
│   │   │   └── profile.html
│   │   │
│   │   └── includes/
│   │       ├── navbar.html
│   │       └── sidebar.html
│   │
│   ├── static/
│   │   │
│   │   ├── images/
│   │   │
│   │   └── uploads/
│   │       └── profile_pics/
│   │
│   └── __init__.py
│
├── run.py
├── requirements.txt
└── README.md

```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/GCETHub.git
```

Move into project directory:

```bash
cd GCETHub
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python run.py
```

Application will start at:

```
http://127.0.0.1:5000/
```

---

# 🔐 Environment Configuration

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

---

# 🧩 Current Development Status

Completed:

✅ Landing page design
✅ Authentication system
✅ Dashboard layout
✅ Profile image handling
✅ Student profile module
✅ Database integration

In Progress:

🚧 Edit Profile
🚧 Upload Profile Picture
🚧 Change Password
🚧 Announcement Module
🚧 Community Module
🚧 Notes Sharing Module
🚧 Placement Module

---

# 🔮 Future Enhancements

## 🤖 AI-Based Campus Assistant

* Smart campus search
* Personalized recommendations
* Academic assistance

## 📱 Mobile Application

* Android/iOS application
* Push notifications
* Real-time updates

## 🔔 Notification System

* Instant announcement alerts
* Event reminders

## 💬 Real-Time Communication

* Student discussions
* Community chat
* Collaboration spaces

---

# 🎯 Project Vision

GCETHub focuses on building a connected digital campus where students can learn, collaborate, and grow together.

Instead of searching through multiple platforms, students get one unified platform for everything related to campus life.

---

# 👩‍💻 Developer

**Payal Kumari**

MCA Student | Full Stack Developer

Skills:

* Python
* Flask
* Django
* React
* JavaScript
* SQL

---

# 📄 License

This project is developed for educational and academic purposes.
