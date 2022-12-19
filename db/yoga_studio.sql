DROP TABLE sessions;
DROP TABLE yoga_classes;
DROP TABLE students;

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE yoga_classes (
  id SERIAL PRIMARY KEY,
  style VARCHAR(255),
  name VARCHAR(255)
);

CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  student_id INT REFERENCES students(id) ON DELETE CASCADE,
  yoga_class_id INT NOT NULL REFERENCES yoga_classes(id) ON DELETE CASCADE,
  booking_notes TEXT
);
