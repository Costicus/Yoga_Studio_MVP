from flask import Flask, render_template

from controllers.session_controller import sessions_blueprint
from controllers.yoga_class_controller import yoga_classes_blueprint
from controllers.student_controller import students_blueprint

app = Flask(__name__)

app.register_blueprint(sessions_blueprint)
app.register_blueprint(yoga_classes_blueprint)
app.register_blueprint(students_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)