from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.placement import Placement
from flask import abort

placement = Blueprint("placement", __name__)


@placement.route("/placements")
@login_required
def placements():

    placements = Placement.query.order_by(
        Placement.created_at.desc()
    ).all()

    return render_template(
        "dashboard/placements.html",
        placements=placements
    )


@placement.route("/placement/add", methods=["GET", "POST"])
@login_required
def add_placement():

    if current_user.role != "admin":
        abort(403)

    if request.method == "POST":

        company = request.form.get("company")
        role = request.form.get("role")
        package = request.form.get("package")
        location = request.form.get("location")
        eligibility = request.form.get("eligibility")
        deadline = request.form.get("deadline")
        apply_link = request.form.get("apply_link")

        new_placement = Placement(
            company=company,
            role=role,
            package=package,
            location=location,
            eligibility=eligibility,
            deadline=deadline,
            apply_link=apply_link
        )

        db.session.add(new_placement)
        db.session.commit()

        flash("Placement added successfully!", "success")

        return redirect(url_for("placement.placements"))

    return render_template("dashboard/add_placement.html")