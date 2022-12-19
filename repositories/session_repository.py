from db.run_sql import run_sql
from models.session import Session
import repositories.student_repository as student_repository
import repositories.yoga_class_repository as yoga_class_repository

def save(session):
    sql = "INSERT INTO sessions (student_id, yoga_class_id, booking_notes) VALUES ( %s, %s, %s ) RETURNING id"
    values = [session.student.id, session.yoga_class.id, session.booking_notes]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session


def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        student = student_repository.select(row['student_id'])
        yoga_class = yoga_class_repository.select(row['yoga_class_id'])
        session = Session(student, yoga_class, row['booking_notes'], row['id'])
        sessions.append(session)
    return sessions


def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)
