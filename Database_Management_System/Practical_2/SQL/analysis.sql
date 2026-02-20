CREATE VIEW student_course_view AS 
SELECT 
s.student_id,
s.name,
c.course_name,
e.grade
FROM students s 
JOIN enrollments e ON s.student_id=e.student_id
JOIN courses c ON e.course_id=c.course_id;


SELECT * FROM student_course_view;