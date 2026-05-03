-- ============================================================
-- Created by HJ
-- Practical 03: DML, DCL & TCL
-- ============================================================

-- Reset (so script can run multiple times safely)
DROP DATABASE IF EXISTS practical03;

CREATE DATABASE practical03;
USE practical03;

-- ============================================================
-- TABLE CREATION
-- ============================================================

CREATE TABLE student (
    id    INT PRIMARY KEY,
    name  VARCHAR(50) NOT NULL,
    marks INT NOT NULL CHECK (marks BETWEEN 0 AND 100),
    city  VARCHAR(50) NOT NULL
);

-- ============================================================
-- SEED DATA
-- ============================================================

INSERT INTO student (id, name, marks, city) VALUES
    (1, 'Areeb', 85, 'Aurangabad'),
    (2, 'Rahul', 70, 'Pune'),
    (3, 'Sara',  90, 'Mumbai');

-- ============================================================
-- DML OPERATIONS
-- ============================================================

-- UPDATE: Give bonus marks
UPDATE student
SET marks = marks + 5
WHERE id = 2;

-- DELETE: Remove a student
DELETE FROM student
WHERE id = 1;

-- ============================================================
-- QUERIES
-- ============================================================

-- Arithmetic operator
SELECT name, marks, marks + 10 AS bonus_marks
FROM student;

-- Logical operator
SELECT *
FROM student
WHERE marks > 80 AND city = 'Mumbai';

-- Set operator
SELECT name AS value FROM student
UNION
SELECT city AS value FROM student;

-- Pattern matching
SELECT *
FROM student
WHERE name LIKE 'S%';

-- String functions
SELECT UPPER(name) AS upper_name,
       LENGTH(name) AS name_length
FROM student;

-- ============================================================
-- DCL (User & Role Management)
-- NOTE: May require admin/root privileges
-- ============================================================

-- Create application user (ignore error if already exists)
CREATE USER IF NOT EXISTS 'app_user'@'localhost' IDENTIFIED BY 'SecurePass@123';

-- Grant permissions (must include database.table)
GRANT SELECT, INSERT ON practical03.student TO 'app_user'@'localhost';

-- Revoke insert privilege
REVOKE INSERT ON practical03.student FROM 'app_user'@'localhost';

-- Role-based access
CREATE ROLE IF NOT EXISTS 'student_read_role';

GRANT SELECT ON practical03.student TO 'student_read_role';
GRANT 'student_read_role' TO 'app_user'@'localhost';

-- ============================================================
-- TCL (Transactions)
-- ============================================================

START TRANSACTION;

-- Sara gets 100
UPDATE student SET marks = 100 WHERE id = 3;

SAVEPOINT sp1;

-- Rahul temporarily set to 50
UPDATE student SET marks = 50 WHERE id = 2;

-- Undo Rahul change only
ROLLBACK TO SAVEPOINT sp1;

COMMIT;

-- Final verification
SELECT * FROM student;