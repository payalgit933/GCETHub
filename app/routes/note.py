from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.note import Note
from app.utils.notifications import create_notification
import os

note = Blueprint("note", __name__)

UPLOAD_FOLDER = "app/static/uploads/notes"

from sqlalchemy import or_
@note.route("/notes")
@login_required
def notes():

    search = request.args.get("search", "")

    query = Note.query

    if search:
        query = query.filter(
            or_(
                Note.title.ilike(f"%{search}%"),
                Note.subject.ilike(f"%{search}%"),
                Note.department.ilike(f"%{search}%")
            )
        )

    notes = query.order_by(
        Note.created_at.desc()
    ).all()

    return render_template(
        "dashboard/notes.html",
        notes=notes,
        search=search,
        result_count=len(notes),
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

        create_notification(
            title="New Note Uploaded",
            message=title,
            type="notes"
        )

        flash("Note uploaded successfully!", "success")

        return redirect(url_for("note.notes"))

    return render_template("dashboard/upload_note.html")


@note.route("/notes/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_note(id):

    note = Note.query.get_or_404(id)

    if current_user.role != "admin" and note.uploaded_by != current_user.id:
        abort(403)

    if request.method == "POST":

        note.title = request.form.get("title")
        note.subject = request.form.get("subject")
        note.department = request.form.get("department")
        note.year = request.form.get("year")

        db.session.commit()

        flash("Note updated successfully!", "success")

        return redirect(url_for("note.notes"))

    return render_template(
        "dashboard/edit_note.html",
        note=note
    )


@note.route("/notes/delete/<int:id>")
@login_required
def delete_note(id):

    note = Note.query.get_or_404(id)

    if current_user.role != "admin" and note.uploaded_by != current_user.id:
        abort(403)

    db.session.delete(note)
    db.session.commit()

    flash("Note deleted successfully!", "success")

    return redirect(url_for("note.notes"))