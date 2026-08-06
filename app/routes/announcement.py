from flask import Blueprint, render_template, request, redirect, url_for, flash,abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models.announcement import Announcement
from app.utils.notifications import create_notification

announcement = Blueprint("announcement", __name__)

from sqlalchemy import or_

@announcement.route("/announcements")
@login_required
def announcements():

    search = request.args.get("search", "")

    query = Announcement.query

    if search:
        query = query.filter(
            or_(
                Announcement.title.ilike(f"%{search}%"),
                Announcement.content.ilike(f"%{search}%")
            )
        )

    announcements = query.order_by(
        Announcement.created_at.desc()
    ).all()

    return render_template(
        "dashboard/announcements.html",
        announcements=announcements,
        search=search
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
        create_notification(
            title="New Announcement",
            message=title,
            type="announcement"
        )

        flash("Announcement Added Successfully!", "success")

        return redirect(url_for("announcement.announcements"))

    return render_template("dashboard/add_announcement.html")


@announcement.route("/announcement/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_announcement(id):

    if current_user.role != "admin":
        abort(403)

    announcement = Announcement.query.get_or_404(id)

    if request.method == "POST":

        announcement.title = request.form.get("title")
        announcement.content = request.form.get("content")

        db.session.commit()

        flash("Announcement updated successfully!", "success")

        return redirect(url_for("announcement.announcements"))

    return render_template(
        "dashboard/edit_announcement.html",
        announcement=announcement
    )

@announcement.route("/announcement/delete/<int:id>")
@login_required
def delete_announcement(id):

    if current_user.role != "admin":
        abort(403)

    announcement = Announcement.query.get_or_404(id)

    db.session.delete(announcement)
    db.session.commit()

    flash("Announcement deleted successfully!", "success")

    return redirect(url_for("announcement.announcements"))