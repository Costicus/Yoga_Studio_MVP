import pdb
from models.yoga_class import Yoga_class
from models.student import Student
from models.session import Session

import repositories.yoga_class_repository as yoga_class_repository
import repositories.student_repository as student_repository
import repositories.session_repository as session_repository

session_repository.delete_all()
yoga_class_repository.delete_all()
student_repository.delete_all()

student1 = Student('Oxy')
student_repository.save(student1)

student2 = Student('Roxy')
student_repository.save(student2)

student3 = Student('Toxy')
student_repository.save(student3)

yoga_class1 = Yoga_class('Hatha-Yoga', 'Cave-1')
yoga_class_repository.save(yoga_class1)

yoga_class2 = Yoga_class('Ashtanga-Yoga', 'Cave-2')
yoga_class_repository.save(yoga_class2)

yoga_class3 = Yoga_class('Raja-Yoga', 'Cave-3')
yoga_class_repository.save(yoga_class3)

session1 = Session(student1, yoga_class1, 'blah')
session_repository.save(session1)

session2 = Session(student3, yoga_class2, 'blah blah')
session_repository.save(session2)

session3 = Session(student2, yoga_class3, 'blah blah blah')
session_repository.save(session3)

pdb.set_trace()
