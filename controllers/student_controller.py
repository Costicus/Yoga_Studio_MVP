from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.student import Student
import repositories.student_repository as student_repository

students_blueprint = Blueprint("students", __name__)

@students_blueprint.route("/students")
def students():
    students = student_repository.select_all() # NEW
    return render_template("students/index.html", students = students)

@students_blueprint.route("/students/<id>")
def show(id):
    student = student_repository.select(id)
    # sessions = yoga_class_repository.get_by_student(student)
    return render_template("students/show.html", student = student, yoga_classes = "")

@students_blueprint.route("/students/new")
def new_student():
    return render_template("/students/new.html")

@students_blueprint.route("/students", methods=['POST'])
def save_newstudent():
    student_name = request.form['name']
    student_to_save = Student(student_name)
    student_repository.save(student_to_save)
    return redirect("/students")
