from app.extensions import db

class Placement(db.Model):
    __tablename__ = "placements"

    id = db.Column(db.Integer, primary_key=True)

    company = db.Column(db.String(100), nullable=False)

    role = db.Column(db.String(100), nullable=False)

    package = db.Column(db.String(50), nullable=False)

    location = db.Column(db.String(100), nullable=False)

    eligibility = db.Column(db.String(150), nullable=False)

    deadline = db.Column(db.Date, nullable=False)

    apply_link = db.Column(db.String(500), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())