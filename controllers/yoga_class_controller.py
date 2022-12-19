from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.yoga_class import Yoga_class
import repositories.yoga_class_repository as yoga_class_repository

yoga_classes_blueprint = Blueprint("yoga-classes", __name__)

@yoga_classes_blueprint.route("/yoga_classes")
def yoga_classes():
    yoga_classes = yoga_class_repository.select_all() # NEW
    return render_template("yoga_classes/index.html", yoga_classes = yoga_classes)

@yoga_classes_blueprint.route("/yoga_classes/<id>")
def show(id):
    yoga_class = yoga_class_repository.select(id)
    return render_template("yoga_classes/show.html", yoga_class = yoga_class)
