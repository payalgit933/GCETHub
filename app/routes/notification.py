from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.notification import Notification
from app.extensions import db

notification = Blueprint("notification", __name__)

@notification.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    for n in notifications:
        if not n.is_read:
            n.is_read = True

    db.session.commit()

    return render_template(
        "dashboard/notifications.html",
        notifications=notifications
    )