from app.extensions import db

class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    message = db.Column(db.Text, nullable=False)

    type = db.Column(db.String(30))

    icon = db.Column(db.String(50))

    is_read = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )