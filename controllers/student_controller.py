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
    return render_template("students/show.html", student = student)
