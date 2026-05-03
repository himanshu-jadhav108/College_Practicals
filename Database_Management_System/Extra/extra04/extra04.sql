-- ============================================================
-- Created by HJ
-- Practical: JOINs & Views
-- ============================================================
CREATE DATABASE practical05;
USE practical05;
-- ============================================================
-- A. Schema Definition
-- ============================================================

CREATE TABLE student (
    id   INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    sid     INT,
    subject VARCHAR(50) NOT NULL,
    marks   INT NOT NULL CHECK (marks BETWEEN 0 AND 100),

    CONSTRAINT fk_marks_student
        FOREIGN KEY (sid)
        REFERENCES student(id)
        ON DELETE CASCADE
);

-- ============================================================
-- B. Seed Data
-- ============================================================

INSERT INTO student (id, name, city) VALUES
    (1, 'Areeb', 'Aurangabad'),
    (2, 'Rahul', 'Pune'),
    (3, 'Sara',  'Mumbai'),
    (4, 'Ali',   'Delhi');

-- NOTE: Removed invalid sid=5 (breaks FK)
INSERT INTO marks (sid, subject, marks) VALUES
    (1, 'Math',    85),
    (1, 'Science', 80),
    (2, 'Math',    70),
    (3, 'Science', 90);

-- ============================================================
-- C. JOIN Queries
-- ============================================================

-- INNER JOIN
SELECT s.name, m.subject, m.marks
FROM student s
INNER JOIN marks m ON s.id = m.sid
ORDER BY s.name, m.subject;

-- LEFT JOIN
SELECT s.name, m.subject, m.marks
FROM student s
LEFT JOIN marks m ON s.id = m.sid
ORDER BY s.name;

-- RIGHT JOIN
SELECT s.name, m.subject, m.marks
FROM student s
RIGHT JOIN marks m ON s.id = m.sid
ORDER BY m.sid;

-- FULL OUTER JOIN (MySQL workaround)
SELECT s.name, m.subject, m.marks
FROM student s
LEFT JOIN marks m ON s.id = m.sid

UNION

SELECT s.name, m.subject, m.marks
FROM student s
RIGHT JOIN marks m ON s.id = m.sid;

-- SELF JOIN (students in same city)
SELECT a.name AS student1, b.name AS student2, a.city
FROM student a
JOIN student b 
    ON a.city = b.city AND a.id < b.id
ORDER BY a.city;

-- ============================================================
-- VIEW MANAGEMENT
-- ============================================================

CREATE VIEW vw_student_marks AS
SELECT s.id, s.name, s.city, m.subject, m.marks
FROM student s
INNER JOIN marks m ON s.id = m.sid;

-- Use the view
SELECT * FROM vw_student_marks
ORDER BY name, subject;

-- Update via view
UPDATE vw_student_marks
SET marks = 95
WHERE name = 'Sara' AND subject = 'Science';

-- Drop view
DROP VIEW IF EXISTS vw_student_marks;