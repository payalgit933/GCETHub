from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.community import Community
from app.utils.notifications import create_notification

community = Blueprint("community", __name__)

from sqlalchemy import or_
@community.route("/communities")
@login_required
def communities():

    search = request.args.get("search", "")

    query = Community.query

    if search:
        query = query.filter(
            or_(
                Community.name.ilike(f"%{search}%"),
                Community.category.ilike(f"%{search}%"),
                Community.description.ilike(f"%{search}%")
            )
        )

    communities = query.order_by(
        Community.created_at.desc()
    ).all()

    return render_template(
        "dashboard/communities.html",
        communities=communities,
        search=search
    )

@community.route("/community/add", methods=["GET", "POST"])
@login_required
def add_community():

    if current_user.role != "admin":
        return "Unauthorized", 403

    if request.method == "POST":

        name = request.form.get("name")
        description = request.form.get("description")
        category = request.form.get("category")

        new_community = Community(
            name=name,
            description=description,
            category=category
        )

        db.session.add(new_community)
        db.session.commit()
        create_notification(
            title="New Community",
            message=name,
            type="community"
        )

        flash("Community Added Successfully!", "success")

        return redirect(url_for("community.communities"))

@community.route("/community/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_community(id):

    if current_user.role != "admin":
        abort(403)

    community = Community.query.get_or_404(id)

    if request.method == "POST":

        community.name = request.form.get("name")
        community.description = request.form.get("description")
        community.category = request.form.get("category")

        db.session.commit()

        flash("Community updated successfully!", "success")

        return redirect(url_for("community.communities"))

    return render_template(
        "dashboard/edit_community.html",
        community=community
    )


@community.route("/community/delete/<int:id>")
@login_required
def delete_community(id):

    if current_user.role != "admin":
        abort(403)

    community = Community.query.get_or_404(id)

    db.session.delete(community)
    db.session.commit()

    flash("Community deleted successfully!", "success")

    return redirect(url_for("community.communities"))

    return render_template("dashboard/add_community.html")