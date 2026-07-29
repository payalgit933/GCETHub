from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.note import Note
import os

note = Blueprint("note", __name__)

UPLOAD_FOLDER = "app/static/uploads/notes"


@note.route("/notes")
@login_required
def notes():

    notes = Note.query.order_by(Note.created_at.desc()).all()

    return render_template(
        "dashboard/notes.html",
        notes=notes
    )


@note.route("/notes/upload", methods=["GET", "POST"])
@login_required
def upload_note():

    if request.method == "POST":

        title = request.form.get("title")
        subject = request.form.get("subject")
        department = request.form.get("department")
        year = request.form.get("year")

        file = request.files.get("file")

        if not file:
            flash("Please select a PDF.", "danger")
            return redirect(url_for("note.upload_note"))

        filename = secure_filename(file.filename)

        file.save(os.path.join(UPLOAD_FOLDER, filename))

        new_note = Note(
            title=title,
            subject=subject,
            department=department,
            year=year,
            file_name=filename,
            uploaded_by=current_user.id
        )

        db.session.add(new_note)
        db.session.commit()

        flash("Note uploaded successfully!", "success")

        return redirect(url_for("note.notes"))

    return render_template("dashboard/upload_note.html")