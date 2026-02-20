-- Student above age 20 
SELECT * FROM students
WHERE age > 20;

-- Filter by Instructor
SELECT c.course_name, i.name 
FROM courses c 
JOIN instructors i ON c.instructor_id=i.instructor_id
WHERE i.name='Dr Jethalal Gada';

-- Sorting by Alphabetical
SELECT * FROM students
ORDER BY name;

-- Sorting by credits
SELECT * FROM courses
ORDER BY credits DESC;

-- Aggregation Student count per course
SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM enrollments e 
JOIN courses c ON e.course_id=c.course_id
GROUP BY c.course_name;

-- Aggregation Average Age
SELECT AVG(age) AS avg_age FROM students;

-- Nested Subqueries for student enrolled in Data Science
SELECT name 
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = (
        SELECT course_id FROM courses
        WHERE course_name="Data Science"
    )
);