from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository
import repositories.student_repository as student_repository
import repositories.yoga_class_repository as yoga_class_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all() # NEW
    return render_template("sessions/index.html", sessions = sessions)

# NEW
# GET '/sessions/new'
@sessions_blueprint.route("/sessions/new", methods=['GET'])
def new_task():
    students = student_repository.select_all()
    yoga_classes = yoga_class_repository.select_all()
    return render_template("sessions/new.html", students = students, yoga_classes = yoga_classes)

# CREATE
# POST '/sessions'
@sessions_blueprint.route("/sessions",  methods=['POST'])
def create_task():
    student_id = request.form['student_id']
    yoga_class_id = request.form['yoga_class_id']
    booking_notes = request.form['booking_notes']
    student = student_repository.select(student_id)
    yoga_class = yoga_class_repository.select(yoga_class_id)
    session = Session(student, yoga_class, booking_notes)
    session_repository.save(session)
    return redirect('/sessions')

# DELETE
# DELETE '/visits/<id>'
@sessions_blueprint.route("/sessions/<id>/delete", methods=['POST'])
def delete_task(id):
    session_repository.delete(id)
    return redirect('/sessions')