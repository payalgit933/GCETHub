import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.extensions import db

profile = Blueprint("profile", __name__)

@profile.route("/profile")
@login_required
def my_profile():
    return render_template(
        "dashboard/profile.html",
        user=current_user
    )

# //edit profile route
@profile.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.name = request.form.get("name")
        current_user.department = request.form.get("department")
        current_user.year = request.form.get("year")
        current_user.section = request.form.get("section")

        db.session.commit()

        flash("Profile updated successfully!", "success")

        return redirect(url_for("profile.my_profile"))

    return render_template(
        "dashboard/edit_profile.html",
        user=current_user
    )

@profile.route("/profile/upload", methods=["POST"])
@login_required
def upload_profile_picture():

    file = request.files.get("profile_pic")

    if not file or file.filename == "":
        flash("Please select an image.", "warning")
        return redirect(url_for("profile.my_profile"))

    allowed = {"png", "jpg", "jpeg"}

    extension = file.filename.rsplit(".", 1)[1].lower()

    if extension not in allowed:
        flash("Only PNG, JPG and JPEG files are allowed.", "danger")
        return redirect(url_for("profile.my_profile"))

    filename = secure_filename(f"{current_user.id}.{extension}")

    upload_folder = os.path.join(
        current_app.root_path,
        "static",
        "uploads",
        "profile_pics"
    )

    os.makedirs(upload_folder, exist_ok=True)

    file.save(os.path.join(upload_folder, filename))

    current_user.profile_pic = filename

    db.session.commit()

    flash("Profile picture updated successfully!", "success")

    return redirect(url_for("profile.my_profile"))

@profile.route("/profile/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    if request.method == "POST":

        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        if not check_password_hash(current_user.password, current_password):
            flash("Current password is incorrect.", "danger")
            return redirect(url_for("profile.change_password"))

        if new_password != confirm_password:
            flash("New passwords do not match.", "warning")
            return redirect(url_for("profile.change_password"))

        current_user.password = generate_password_hash(new_password)

        db.session.commit()

        flash("Password changed successfully!", "success")

        return redirect(url_for("profile.my_profile"))

    return render_template("dashboard/change_password.html")