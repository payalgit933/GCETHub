from flask import Blueprint, render_template
from flask_login import login_required
from app.models.notification import Notification

notification = Blueprint("notification", __name__)

@notification.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.order_by(
        Notification.created_at.desc()
    ).all()

    return render_template(
        "dashboard/notifications.html",
        notifications=notifications
    )