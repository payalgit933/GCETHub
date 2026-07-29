from app.extensions import db

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    subject = db.Column(db.String(100), nullable=False)

    department = db.Column(db.String(50), nullable=False)

    year = db.Column(db.String(20), nullable=False)

    file_name = db.Column(db.String(255), nullable=False)

    uploaded_by = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())