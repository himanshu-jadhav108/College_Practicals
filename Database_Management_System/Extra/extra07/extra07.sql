-- ============================================================
-- Created by HJ
-- Practical: Triggers
-- ============================================================
CREATE DATABASE practical08;
USE practical08;
-- ============================================================
-- RESET (important for re-run)
-- ============================================================

DROP TABLE IF EXISTS student_log;
DROP TABLE IF EXISTS student;

-- ============================================================
-- A. Schema Definition
-- ============================================================

CREATE TABLE student (
    id    INT PRIMARY KEY,
    name  VARCHAR(50) NOT NULL,
    marks INT NOT NULL
);

CREATE TABLE student_log (
    log_id     INT PRIMARY KEY AUTO_INCREMENT,
    action     VARCHAR(10) NOT NULL,
    student_id INT,
    old_marks  INT,
    new_marks  INT,
    log_time   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message    VARCHAR(200)
);

-- ============================================================
-- DROP TRIGGERS (prevents duplicate error on re-run)
-- ============================================================

DROP TRIGGER IF EXISTS trg_before_insert_student;
DROP TRIGGER IF EXISTS trg_after_insert_student;
DROP TRIGGER IF EXISTS trg_before_update_student;
DROP TRIGGER IF EXISTS trg_after_update_student;
DROP TRIGGER IF EXISTS trg_before_delete_student;

-- ============================================================
-- C. Trigger Definitions
-- ============================================================

DELIMITER $$

-- TRIGGER 1: BEFORE INSERT
CREATE TRIGGER trg_before_insert_student
BEFORE INSERT ON student
FOR EACH ROW
BEGIN
    IF NEW.marks < 0 THEN
        SET NEW.marks = 0;
    END IF;
END$$

-- TRIGGER 2: AFTER INSERT
CREATE TRIGGER trg_after_insert_student
AFTER INSERT ON student
FOR EACH ROW
BEGIN
    INSERT INTO student_log (action, student_id, new_marks, message)
    VALUES (
        'INSERT',
        NEW.id,
        NEW.marks,
        CONCAT('Student inserted: ', NEW.name)
    );
END$$

-- TRIGGER 3: BEFORE UPDATE
CREATE TRIGGER trg_before_update_student
BEFORE UPDATE ON student
FOR EACH ROW
BEGIN
    IF NEW.marks > 100 THEN
        SET NEW.marks = 100;
    END IF;

    IF NEW.marks < 0 THEN
        SET NEW.marks = 0;
    END IF;
END$$

-- TRIGGER 4: AFTER UPDATE
CREATE TRIGGER trg_after_update_student
AFTER UPDATE ON student
FOR EACH ROW
BEGIN
    INSERT INTO student_log (action, student_id, old_marks, new_marks, message)
    VALUES (
        'UPDATE',
        NEW.id,
        OLD.marks,
        NEW.marks,
        CONCAT('Marks changed for: ', NEW.name)
    );
END$$

-- TRIGGER 5: BEFORE DELETE
CREATE TRIGGER trg_before_delete_student
BEFORE DELETE ON student
FOR EACH ROW
BEGIN
    INSERT INTO student_log (action, student_id, old_marks, message)
    VALUES (
        'DELETE',
        OLD.id,
        OLD.marks,
        CONCAT('Student deleted: ', OLD.name)
    );
END$$

DELIMITER ;

-- ============================================================
-- TEST THE TRIGGERS
-- ============================================================

-- BEFORE INSERT (marks = -10 → becomes 0)
INSERT INTO student (id, name, marks)
VALUES (1, 'Areeb', -10);

-- Normal insert
INSERT INTO student (id, name, marks)
VALUES (2, 'Rahul', 80);

-- BEFORE UPDATE (150 → becomes 100)
UPDATE student
SET marks = 150
WHERE id = 2;

-- DELETE trigger
DELETE FROM student
WHERE id = 1;

-- ============================================================
-- VERIFY RESULTS
-- ============================================================

SELECT * FROM student;

SELECT *
FROM student_log
ORDER BY log_time;