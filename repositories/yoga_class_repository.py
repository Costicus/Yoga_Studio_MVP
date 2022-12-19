from db.run_sql import run_sql
from models.yoga_class import Yoga_class
from models.student import Student

def save(yoga_class):
    sql = "INSERT INTO yoga_classes(name, style) VALUES ( %s, %s ) RETURNING id"
    values = [yoga_class.name, yoga_class.style]
    results = run_sql(sql, values)
    yoga_class.id = results[0]['id']
    return yoga_class


def select_all():
    yoga_classes = []

    sql = "SELECT * FROM yoga_classes"
    results = run_sql(sql)

    for row in results:
        yoga_class = Yoga_class(row['name'], row['style'], row['id'])
        yoga_classes.append(yoga_class)
    return yoga_classes


def select(id):
    yoga_class = None
    sql = "SELECT * FROM yoga_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        yoga_class = Yoga_class(result['name'], result['style'], result['id'] )
    return yoga_class


def delete_all():
    sql = "DELETE FROM yoga_classes"
    run_sql(sql)
