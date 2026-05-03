-- ============================================================
-- Created by HJ
-- Practical: Aggregate Queries
-- ============================================================

-- ============================================================
-- TABLE CREATION
-- ============================================================
CREATE DATABASE practical04;
USE practical04;

CREATE TABLE student (
    id    INT PRIMARY KEY,
    name  VARCHAR(50) NOT NULL,
    marks INT NOT NULL CHECK (marks BETWEEN 0 AND 100),
    city  VARCHAR(50) NOT NULL
);

-- ============================================================
-- B. Seed Data
-- ============================================================

INSERT INTO student (id, name, marks, city) VALUES
    (1,  'Areeb', 85, 'Aurangabad'),
    (2,  'Rahul', 70, 'Pune'),
    (3,  'Sara',  90, 'Mumbai'),
    (4,  'Ali',   60, 'Pune'),
    (5,  'Zara',  95, 'Mumbai'),
    (6,  'John',  75, 'Delhi'),
    (7,  'Priya', 88, 'Delhi'),
    (8,  'Aman',  55, 'Aurangabad'),
    (9,  'Neha',  92, 'Pune'),
    (10, 'Karan', 65, 'Mumbai');

-- ============================================================
-- C. Aggregate Queries
-- ============================================================

-- 1. Overall statistics
SELECT
    AVG(marks) AS avg_marks,
    SUM(marks) AS total_marks,
    MAX(marks) AS highest,
    MIN(marks) AS lowest,
    COUNT(*) AS total_students
FROM student;

-- 2. Average marks per city (GROUP BY)
SELECT
    city,
    AVG(marks) AS avg_marks
FROM student
GROUP BY city
ORDER BY avg_marks DESC;

-- 3. Cities with avg marks > 75 (HAVING)
SELECT
    city,
    AVG(marks) AS avg_marks
FROM student
GROUP BY city
HAVING AVG(marks) > 75
ORDER BY avg_marks DESC;

-- 4. Full summary per city
SELECT
    city,
    COUNT(*) AS total_students,
    SUM(marks) AS total_marks,
    AVG(marks) AS avg_marks,
    MAX(marks) AS top_score,
    MIN(marks) AS lowest_score
FROM student
GROUP BY city
ORDER BY total_students DESC;

-- 5. Cities where at least one student scored > 90
SELECT
    city,
    COUNT(*) AS bright_students
FROM student
WHERE marks > 90
GROUP BY city;