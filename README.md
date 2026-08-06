# GCETHub - Campus Collaboration & Student Platform

![GCETHub Banner](app/static/images/banner.png)

## Project Overview

**GCETHub** is a campus collaboration platform built with Flask and MySQL. It centralizes announcements, communities, study notes, placements, events, and notifications in one place for students and administrators.

Instead of scattered WhatsApp groups and disconnected channels, GCETHub gives students a single dashboard for campus updates, academic resources, and career opportunities.

---

## Features

### Authentication & Roles
- User registration and secure login
- Role-based access control (Admin / Student)
- Protected routes with Flask-Login

### Dashboard
- Student dashboard with statistics, quick links, and activity widgets
- Admin dashboard with platform metrics and latest content previews
- Uploads-this-month counter, upcoming events, and latest activity feed

### Announcements
- Create, read, update, and delete (admin)
- Search with result counts and clear search
- Students can view all announcements
- **Formatting preserved** — line breaks and spacing from the editor are kept when announcements are displayed

### UI / UX
- **Glassmorphism design** — frosted-glass surfaces with backdrop blur across dashboard, auth, and landing pages
- **Glossy card effects** — subtle highlights, gradients, and depth on stat cards, list items, and forms
- **Modern sidebar & navbar** — sticky glass navbar, collapsible sidebar on mobile, active route highlighting
- **Responsive layout** — optimized for desktop and mobile viewports

### Communities
- Browse and search student communities
- Admin CRUD with category badges

### Study Notes
- Upload, view PDF, download, edit, and delete
- Students can manage only their own notes
- Admins can manage all notes

### Placements
- Job and internship listings with apply links
- Search by company or role
- Admin CRUD

### Events
- Campus event listings with date, time, and venue
- Responsive table with sticky headers
- Admin CRUD

### Notifications
- Broadcast alerts when new content is added
- Unread notification badge in navbar

### Profile
- View and edit profile details
- Profile picture upload
- Change password

---

## Technologies

| Layer | Stack |
|-------|-------|
| Backend | Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate |
| Frontend | HTML5, CSS3 (Glassmorphism), Bootstrap 5, Bootstrap Icons, Jinja2 |
| Database | MySQL (via PyMySQL) |
| Tools | Git, VS Code |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/GCETHub.git
cd GCETHub
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Update `config.py` with your MySQL credentials:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost/gcethub"
SECRET_KEY = "your-secret-key"
```

Create the database:

```sql
CREATE DATABASE gcethub;
```

Run migrations:

```bash
flask db upgrade
```

### 5. Run the application

```bash
python run.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### Writing Announcements

When creating or editing an announcement, use line breaks and spacing as you would in a document. The platform preserves your formatting when displaying content to students — paragraphs, bullet lists, and multi-line notices all render exactly as written.

---

## Folder Structure

```
GCETHub/
├── app/
│   ├── __init__.py              # Application factory
│   ├── extensions.py            # db, login_manager, migrate
│   ├── models/                  # SQLAlchemy models
│   │   ├── user.py
│   │   ├── announcement.py
│   │   ├── community.py
│   │   ├── note.py
│   │   ├── placement.py
│   │   ├── event.py
│   │   └── notification.py
│   ├── routes/                  # Blueprint route handlers
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── admin.py
│   │   ├── announcement.py
│   │   ├── community.py
│   │   ├── note.py
│   │   ├── placement.py
│   │   ├── event.py
│   │   ├── profile.py
│   │   └── notification.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/
│   │   ├── dashboard/
│   │   └── includes/            # Reusable partials (flash, search, empty state)
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── uploads/
│   └── utils/
│       └── notifications.py
├── migrations/                  # Alembic migration files
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Screenshots

### Landing Page
![Landing Page](app/static/images/banner.png)

### Student Dashboard
![Dashboard](app/static/images/dashboard.png)

### Profile
![Profile](app/static/images/profile.png)

### Admin Dashboard
<!-- Add screenshot: app/static/images/admin_dashboard.png -->

### Announcements
<!-- Add screenshot: app/static/images/announcements.png -->

### Events
<!-- Add screenshot: app/static/images/events.png -->

---

## Future Scope

- **AI Campus Assistant** — Smart search and personalized recommendations
- **Mobile Application** — Android/iOS app with push notifications
- **Real-time Chat** — Community discussions and direct messaging
- **Advanced Analytics** — Usage trends and engagement metrics for admins
- **Email Notifications** — Alerts for announcements, events, and placements
- **Global Search** — Search across all modules from a single input
- **Event Registration** — In-app RSVP and attendance tracking
- **API Layer** — REST API for third-party integrations

---

## Developer

**Payal Kumari** — MCA Student | Full Stack Developer

---

## License

This project is developed for educational and academic purposes.
