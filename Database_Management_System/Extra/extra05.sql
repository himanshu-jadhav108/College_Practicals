-- ============================================================
-- Created by HJ
-- Practical: Subqueries
-- ============================================================
CREATE DATABASE practical06;
USE practical06;
-- ============================================================
-- A. Schema Definition
-- ============================================================

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
    (1, 'Areeb', 85, 'Aurangabad'),
    (2, 'Rahul', 70, 'Pune'),
    (3, 'Sara',  90, 'Mumbai'),
    (4, 'Ali',   60, 'Pune'),
    (5, 'Zara',  95, 'Mumbai'),
    (6, 'John',  75, 'Delhi');

-- ============================================================
-- C. Subquery Examples
-- ============================================================

-- 1. Students with marks above average
SELECT name, marks
FROM student
WHERE marks > (SELECT AVG(marks) FROM student)
ORDER BY marks DESC;

-- 2. Student(s) with the highest marks
SELECT name, marks
FROM student
WHERE marks = (SELECT MAX(marks) FROM student);

-- 3. Students from the same city as Areeb
SELECT name, city
FROM student
WHERE city = (SELECT city FROM student WHERE name = 'Areeb')
  AND name <> 'Areeb';

-- 4. Students with more marks than Rahul
SELECT name, marks
FROM student
WHERE marks > (SELECT marks FROM student WHERE name = 'Rahul')
ORDER BY marks;

-- 5. EXISTS: Students whose marks exceed 90
SELECT name
FROM student s
WHERE EXISTS (
    SELECT 1
    FROM student s2
    WHERE s2.id = s.id AND s2.marks > 90
);

-- 6. IN operator: Students from Pune or Mumbai
SELECT name, city
FROM student
WHERE city IN ('Pune', 'Mumbai');

-- 7. ALL operator: Students with marks > ALL students in Pune
SELECT name, marks
FROM student
WHERE marks > ALL (
    SELECT marks
    FROM student
    WHERE city = 'Pune'
);

-- 8. ANY operator: Students with marks matching any Mumbai student
SELECT name, marks
FROM student
WHERE marks = ANY (
    SELECT marks
    FROM student
    WHERE city = 'Mumbai'
);

-- 9. Correlated subquery: Rank comparison
SELECT name, marks,
       (SELECT COUNT(*)
        FROM student s2
        WHERE s2.marks > s1.marks) + 1 AS rank_pos
FROM student s1
ORDER BY rank_pos;