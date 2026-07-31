from app.extensions import db
from app.models.notification import Notification
from app.models.user import User


def create_notification(title, message, type):

    users = User.query.all()

    for user in users:
        notification = Notification(
            title=title,
            message=message,
            type=type,
            user_id=user.id
        )

        db.session.add(notification)

    db.session.commit()