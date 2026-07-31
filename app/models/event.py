from app.extensions import db

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    event_date = db.Column(db.String(50), nullable=False)

    event_time = db.Column(db.String(30), nullable=False)

    venue = db.Column(db.String(150), nullable=False)

    organizer = db.Column(db.String(150), nullable=False)

    registration_link = db.Column(db.String(500))

    poster = db.Column(db.String(255), default="default_event.png")

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )