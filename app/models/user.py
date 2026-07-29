from app.extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    enrollment = db.Column(db.String(30), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    department = db.Column(db.String(50))

    year = db.Column(db.String(20))

    section = db.Column(db.String(10))

    role = db.Column(db.String(20), default="student")

    profile_pic = db.Column(db.String(255), default="default.png")

    phone = db.Column(db.String(20))

    bio = db.Column(db.Text)

    skills = db.Column(db.Text)

    github = db.Column(db.String(255))

    linkedin = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, server_default=db.func.now())