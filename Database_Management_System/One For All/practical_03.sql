-- SQL QUeries with Filtering and Sorting 
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS enrollments, courses, students, instructors;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT,
    department VARCHAR(50)
);

CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- seed
INSERT INTO students (name,email,age,department) VALUES
('Himanshu Jadhav','himanshu@mail.com',21,'AIDS'),
('Durgesh Sonawane','dsonawane@mail.com',19,'ENTC'),
('Omkar Shedage','omkarshedage@mail.com',22,'AIDS'),
('Sujit Bera','berasujit@mail.com',20,'CS');

INSERT INTO instructors (name,department) VALUES
('Dr Jethalal Gada','AI'),
('Prof Tarak Mehta','IT');

INSERT INTO courses (course_name,credits,instructor_id) VALUES
('DBMS',4,1),
('Data Science',3,1),
('Embedded System',3,2);

INSERT INTO enrollments (student_id,course_id,grade) VALUES
(1,1,'A'),
(1,2,'B'),
(2,1,'A'),
(3,2,'A'),
(4,3,'B');

-- queries
SELECT * FROM students
WHERE age > 20;

SELECT c.course_name, i.name
FROM courses c
JOIN instructors i ON c.instructor_id = i.instructor_id
WHERE i.name = 'Dr Jethalal Gada';

SELECT * FROM students
ORDER BY name;

SELECT * FROM courses
ORDER BY credits DESC;

SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
GROUP BY c.course_name;

SELECT AVG(age) AS avg_age FROM students;

SELECT name
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT course_id FROM courses
        WHERE course_name = 'Data Science'
    )
);

SELECT * FROM students;
SELECT * FROM instructors;
SELECT * FROM courses;
SELECT * FROM enrollments;