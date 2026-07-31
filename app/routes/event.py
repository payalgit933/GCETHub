from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models.event import Event

event = Blueprint("event", __name__)


# ----------------------------
# View All Events
# ----------------------------
@event.route("/events")
@login_required
def events():

    events = Event.query.order_by(
        Event.created_at.desc()
    ).all()

    return render_template(
        "dashboard/events/events.html",
        events=events
    )


# ----------------------------
# Add Event
# ----------------------------
@event.route("/event/add", methods=["GET", "POST"])
@login_required
def add_event():

    if current_user.role != "admin":
        abort(403)

    if request.method == "POST":

        new_event = Event(
            title=request.form.get("title"),
            description=request.form.get("description"),
            event_date=request.form.get("event_date"),
            event_time=request.form.get("event_time"),
            venue=request.form.get("venue"),
            organizer=request.form.get("organizer"),
            registration_link=request.form.get("registration_link")
        )

        db.session.add(new_event)
        db.session.commit()

        flash("Event added successfully!", "success")

        return redirect(url_for("event.events"))

    return render_template("dashboard/events/add_event.html")


# ----------------------------
# Edit Event
# ----------------------------
@event.route("/event/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_event(id):

    if current_user.role != "admin":
        abort(403)

    event_obj = Event.query.get_or_404(id)

    if request.method == "POST":

        event_obj.title = request.form.get("title")
        event_obj.description = request.form.get("description")
        event_obj.event_date = request.form.get("event_date")
        event_obj.event_time = request.form.get("event_time")
        event_obj.venue = request.form.get("venue")
        event_obj.organizer = request.form.get("organizer")
        event_obj.registration_link = request.form.get("registration_link")

        db.session.commit()

        flash("Event updated successfully!", "success")

        return redirect(url_for("event.events"))

    return render_template(
        "dashboard/events/edit_event.html",
        event=event_obj
    )


# ----------------------------
# Delete Event
# ----------------------------
@event.route("/event/delete/<int:id>")
@login_required
def delete_event(id):

    if current_user.role != "admin":
        abort(403)

    event_obj = Event.query.get_or_404(id)

    db.session.delete(event_obj)
    db.session.commit()

    flash("Event deleted successfully!", "success")

    return redirect(url_for("event.events"))