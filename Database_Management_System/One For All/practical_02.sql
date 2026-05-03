-- Practical 02 Views ANd Index
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    grade VARCHAR(2)
);

-- indexes
CREATE INDEX idx_student_name ON students(name);
CREATE INDEX idx_enroll_student ON enrollments(student_id);
CREATE INDEX idx_enroll_course ON enrollments(course_id);

-- seed
INSERT INTO students (name, email, department) VALUES
('Himanshu', 'himanshu@mail.com', 'AIDS'),
('Sujal', 'sujal@mail.com', 'CS'),
('Onkar', 'onkar@mail.com', 'AIDS');

INSERT INTO courses (course_name, credits) VALUES
('DBMS', 4),
('Data Science', 3);

INSERT INTO enrollments VALUES
(1,1,'A'),
(1,2,'B'),
(2,1,'A'),
(3,2,'B');

-- view
CREATE VIEW student_course_view AS
SELECT
    s.name,
    c.course_name,
    e.grade
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- queries
SELECT * FROM student_course_view;

UPDATE enrollments
SET grade = 'A+'
WHERE student_id = 1 AND course_id = 2;

DELETE FROM enrollments
WHERE student_id = 2 AND course_id = 1;

EXPLAIN SELECT * FROM students WHERE name = 'Himanshu';

SHOW INDEX FROM students;

SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM enrollments;