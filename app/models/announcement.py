from app.extensions import db

class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted_by = db.Column(db.String(100), default="Admin")
    created_at = db.Column(db.DateTime, server_default=db.func.now())