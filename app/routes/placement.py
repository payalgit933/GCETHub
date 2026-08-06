from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from sqlalchemy import or_

from app.extensions import db
from app.models.placement import Placement
from app.utils.notifications import create_notification

placement = Blueprint("placement", __name__)


@placement.route("/placements")
@login_required
def placements():
    search = request.args.get("search", "")

    query = Placement.query

    if search:
        query = query.filter(
            or_(
                Placement.company.ilike(f"%{search}%"),
                Placement.role.ilike(f"%{search}%")
            )
        )

    placements = query.order_by(
        Placement.created_at.desc()
    ).all()

    return render_template(
        "dashboard/placements.html",
        placements=placements,
        search=search,
        result_count=len(placements),
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
        create_notification(
            title="New Placement Opportunity",
            message=company,
            type="placements"
        )

        flash("Placement added successfully!", "success")

        return redirect(url_for("placement.placements"))

    return render_template("dashboard/add_placement.html")


@placement.route("/placement/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_placement(id):
    if current_user.role != "admin":
        abort(403)

    placement = Placement.query.get_or_404(id)

    if request.method == "POST":
        placement.company = request.form.get("company")
        placement.role = request.form.get("role")
        placement.location = request.form.get("location")
        placement.package = request.form.get("package")
        placement.apply_link = request.form.get("apply_link")
        placement.deadline = request.form.get("deadline")

        db.session.commit()

        flash("Placement updated successfully!", "success")

        return redirect(url_for("placement.placements"))

    return render_template(
        "dashboard/edit_placement.html",
        placement=placement
    )


@placement.route("/placement/delete/<int:id>")
@login_required
def delete_placement(id):
    if current_user.role != "admin":
        abort(403)

    placement = Placement.query.get_or_404(id)

    db.session.delete(placement)
    db.session.commit()

    flash("Placement deleted successfully!", "success")

    return redirect(url_for("placement.placements"))
