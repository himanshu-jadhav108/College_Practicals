-- Students with their courses
SELECT s.Name, c.CourseName
FROM Enrollment e
JOIN Student s ON e.StudentID = s.StudentID
JOIN Course c ON e.CourseID = c.CourseID;

-- Courses with instructors
SELECT c.CourseName, i.Name AS Instructor
FROM Course c
JOIN Instructor i ON c.InstructorID = i.InstructorID;

-- Student count per course
SELECT c.CourseName, COUNT(e.StudentID) AS TotalStudents
FROM Course c
LEFT JOIN Enrollment e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;