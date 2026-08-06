from datetime import datetime

from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

from app.models.announcement import Announcement
from app.models.community import Community
from app.models.note import Note
from app.models.placement import Placement
from app.models.event import Event

dashboard = Blueprint("dashboard", __name__)


def _format_date(dt):
    if dt:
        return dt.strftime("%d %b %Y")
    return "—"


@dashboard.route("/dashboard")
@login_required
def home():
    now = datetime.now()
    month_start = datetime(now.year, now.month, 1)
    today = now.strftime("%Y-%m-%d")

    stats = {
        "announcements": Announcement.query.count(),
        "communities": Community.query.count(),
        "notes": Note.query.count(),
        "placements": Placement.query.count(),
        "events": Event.query.count(),
    }

    uploads_this_month = Note.query.filter(
        Note.created_at >= month_start
    ).count()

    upcoming_events = Event.query.filter(
        Event.event_date >= today
    ).order_by(Event.event_date.asc()).limit(5).all()

    activity_items = []

    for item in Announcement.query.order_by(
        Announcement.created_at.desc()
    ).limit(3).all():
        activity_items.append({
            "type": "announcement",
            "icon": "bi-megaphone-fill",
            "label": "Announcement",
            "title": item.title,
            "date": _format_date(item.created_at),
            "sort_key": item.created_at,
            "url": url_for("announcement.announcements"),
        })

    for item in Note.query.order_by(Note.created_at.desc()).limit(3).all():
        activity_items.append({
            "type": "note",
            "icon": "bi-journal-text",
            "label": "Note uploaded",
            "title": item.title,
            "date": _format_date(item.created_at),
            "url": url_for("note.notes"),
        })

    for item in Event.query.order_by(Event.created_at.desc()).limit(3).all():
        activity_items.append({
            "type": "event",
            "icon": "bi-calendar-event",
            "label": "Event",
            "title": item.title,
            "date": item.event_date,
            "sort_key": item.created_at,
            "url": url_for("event.events"),
        })

    for item in Placement.query.order_by(
        Placement.created_at.desc()
    ).limit(3).all():
        activity_items.append({
            "type": "placement",
            "icon": "bi-briefcase-fill",
            "label": "Placement",
            "title": f"{item.company} — {item.role}",
            "date": _format_date(item.created_at),
            "sort_key": item.created_at,
            "url": url_for("placement.placements"),
        })

    activity_items.sort(
        key=lambda x: x.get("sort_key") or datetime.min,
        reverse=True
    )
    latest_activity = activity_items[:8]

    return render_template(
        "dashboard/dashboard.html",
        user=current_user,
        stats=stats,
        uploads_this_month=uploads_this_month,
        upcoming_events=upcoming_events,
        latest_activity=latest_activity,
    )
