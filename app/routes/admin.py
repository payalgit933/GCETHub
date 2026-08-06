from flask import Blueprint, render_template, abort, url_for
from flask_login import login_required, current_user

from app.models.user import User
from app.models.announcement import Announcement
from app.models.community import Community
from app.models.note import Note
from app.models.placement import Placement
from app.models.event import Event

admin = Blueprint("admin", __name__)


def _format_date(dt):
    if dt:
        return dt.strftime("%d %b %Y")
    return "—"


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
        "placements": Placement.query.count(),
        "events": Event.query.count(),
    }

    latest_announcements = [
        {
            "title": item.title,
            "date": _format_date(item.created_at),
            "action_url": url_for("announcement.edit_announcement", id=item.id),
            "action_text": "Manage",
        }
        for item in Announcement.query.order_by(
            Announcement.created_at.desc()
        ).limit(5).all()
    ]

    latest_placements = [
        {
            "title": f"{item.company} — {item.role}",
            "date": _format_date(item.created_at),
            "action_url": url_for("placement.edit_placement", id=item.id),
            "action_text": "Manage",
        }
        for item in Placement.query.order_by(
            Placement.created_at.desc()
        ).limit(5).all()
    ]

    latest_events = [
        {
            "title": item.title,
            "date": item.event_date,
            "action_url": url_for("event.edit_event", id=item.id),
            "action_text": "Manage",
        }
        for item in Event.query.order_by(
            Event.created_at.desc()
        ).limit(5).all()
    ]

    latest_notes = [
        {
            "title": item.title,
            "date": _format_date(item.created_at),
            "action_url": url_for("note.edit_note", id=item.id),
            "action_text": "Manage",
        }
        for item in Note.query.order_by(
            Note.created_at.desc()
        ).limit(5).all()
    ]

    return render_template(
        "dashboard/admin_dashboard.html",
        data=data,
        latest_announcements=latest_announcements,
        latest_placements=latest_placements,
        latest_events=latest_events,
        latest_notes=latest_notes,
    )
