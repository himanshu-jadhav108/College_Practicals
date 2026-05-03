-- ============================================================
-- Created by HJ
-- Practical: Procedures, Functions & Cursor
-- ============================================================
CREATE DATABASE practical07;
USE practical07;

-- ============================================================
-- A. Schema Definition
-- ============================================================

DROP TABLE IF EXISTS student;

CREATE TABLE student (
    id    INT PRIMARY KEY,
    name  VARCHAR(50) NOT NULL,
    marks INT NOT NULL CHECK (marks BETWEEN 0 AND 100)
);

-- ============================================================
-- B. Seed Data
-- ============================================================

INSERT INTO student (id, name, marks) VALUES
    (1, 'Areeb', 85),
    (2, 'Rahul', 70),
    (3, 'Sara',  90),
    (4, 'Ali',   60);

-- ============================================================
-- C. Procedures, Functions & Cursor
-- ============================================================

-- Drop if exists (prevents re-run errors)
DROP PROCEDURE IF EXISTS sp_display_students;
DROP PROCEDURE IF EXISTS sp_students_above_marks;
DROP FUNCTION IF EXISTS fn_get_grade;

-- ============================================================
-- STORED PROCEDURE: Display all students using a cursor
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_display_students()
BEGIN
    DECLARE v_done INT DEFAULT 0;
    DECLARE v_name VARCHAR(50);
    DECLARE v_marks INT;

    DECLARE cur_students CURSOR FOR
        SELECT name, marks FROM student ORDER BY marks DESC;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = 1;

    OPEN cur_students;

    read_loop: LOOP
        FETCH cur_students INTO v_name, v_marks;

        IF v_done = 1 THEN
            LEAVE read_loop;
        END IF;

        SELECT v_name AS student_name, v_marks AS student_marks;
    END LOOP;

    CLOSE cur_students;
END$$

DELIMITER ;

-- Call the procedure
CALL sp_display_students();

-- ============================================================
-- STORED PROCEDURE: Get students above a mark threshold
-- ============================================================

DELIMITER $$

CREATE PROCEDURE sp_students_above_marks(IN p_threshold INT)
BEGIN
    SELECT id, name, marks
    FROM student
    WHERE marks > p_threshold
    ORDER BY marks DESC;
END$$

DELIMITER ;

-- Call with parameter
CALL sp_students_above_marks(75);

-- ============================================================
-- SCALAR FUNCTION: Return letter grade
-- ============================================================

DELIMITER $$

CREATE FUNCTION fn_get_grade(p_marks INT)
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    DECLARE v_grade VARCHAR(10);

    IF p_marks >= 90 THEN 
        SET v_grade = 'A';
    ELSEIF p_marks >= 75 THEN 
        SET v_grade = 'B';
    ELSEIF p_marks >= 60 THEN 
        SET v_grade = 'C';
    ELSEIF p_marks >= 45 THEN 
        SET v_grade = 'D';
    ELSE 
        SET v_grade = 'F';
    END IF;

    RETURN v_grade;
END$$

DELIMITER ;

-- Use the function
SELECT name, marks, fn_get_grade(marks) AS grade
FROM student
ORDER BY marks DESC;