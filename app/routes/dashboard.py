from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.announcement import Announcement
from app.models.community import Community
from app.models.note import Note
from app.models.placement import Placement

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
@login_required
def home():
    stats = {
        "announcements": Announcement.query.count(),
        "communities": Community.query.count(),
        "notes": Note.query.count(),
        "placements": Placement.query.count(),
    }
    return render_template(
        "dashboard/dashboard.html",
        user=current_user,
        stats=stats
    )