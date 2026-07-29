from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.community import Community

community = Blueprint("community", __name__)

@community.route("/communities")
@login_required
def communities():

    communities = Community.query.order_by(
        Community.created_at.desc()
    ).all()

    return render_template(
        "dashboard/communities.html",
        communities=communities
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

        flash("Community Added Successfully!", "success")

        return redirect(url_for("community.communities"))

    return render_template("dashboard/add_community.html")