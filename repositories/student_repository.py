from db.run_sql import run_sql
from models.yoga_class import Yoga_class
from models.student import Student

def save(student):
    sql = "INSERT INTO students (name) VALUES ( %s ) RETURNING id"
    values = [student.name]
    results = run_sql( sql, values )
    student.id = results[0]['id']
    return student


def select_all():
    students = []

    sql = "SELECT * FROM students"
    results = run_sql(sql)
    for row in results:
        student = Student(row['name'], row['id'])
        students.append(student)
    return students


def select(id):
    student = None
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'falsy' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        student = Student(result['name'], result['id'] )
    return student


def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)
