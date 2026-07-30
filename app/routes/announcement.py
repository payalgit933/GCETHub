from flask import Blueprint, render_template, request, redirect, url_for, flash,abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models.announcement import Announcement

announcement = Blueprint("announcement", __name__)

@announcement.route("/announcements")
@login_required
def announcements():

    announcements = Announcement.query.order_by(
        Announcement.created_at.desc()
    ).all()

    return render_template(
        "dashboard/announcements.html",
        announcements=announcements
    )


@announcement.route("/announcement/add", methods=["GET", "POST"])
@login_required
def add_announcement():
    if current_user.role != "admin":
        abort(403)

    if request.method == "POST":

        title = request.form.get("title")

        content = request.form.get("content")

        new_post = Announcement(
            title=title,
            content=content
        )

        db.session.add(new_post)
        db.session.commit()

        flash("Announcement Added Successfully!", "success")

        return redirect(url_for("announcement.announcements"))

    return render_template("dashboard/add_announcement.html")