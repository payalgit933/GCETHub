from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

from app.models.user import User
from app.models.announcement import Announcement
from app.models.community import Community
from app.models.note import Note
from app.models.placement import Placement

admin = Blueprint("admin", __name__)

@admin.route("/admin/dashboard")
@login_required
def admin_dashboard():

    if current_user.role != "admin":
        abort(403)

    data = {
        "users": User.query.count(),
        "students": User.query.filter_by(role="student").count(),
        "admins": User.query.filter_by(role="admin").count(),
        "announcements": Announcement.query.count(),
        "communities": Community.query.count(),
        "notes": Note.query.count(),
        "placements": Placement.query.count()
    }

    return render_template(
        "dashboard/admin_dashboard.html",
        data=data
    )