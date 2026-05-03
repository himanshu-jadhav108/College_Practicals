-- ============================================================
-- Created by HJ
-- Step 1: Create dependent table first (departments)
-- ============================================================
CREATE DATABASE practical01;
USE practical01;
CREATE TABLE departments (
    dept_id    INT PRIMARY KEY,
    dept_name  VARCHAR(100) NOT NULL
);

-- ============================================================
-- Step 2: Create employees table with all constraints
-- ============================================================

CREATE TABLE employees (
    emp_id        INT PRIMARY KEY,
    first_name    VARCHAR(50)  NOT NULL,
    last_name     VARCHAR(50)  NOT NULL,
    department_id INT,
    salary        DECIMAL(10,2) NOT NULL,
    hire_date     DATE NOT NULL,
    email         VARCHAR(100) UNIQUE NOT NULL,

    CONSTRAINT chk_salary CHECK (salary > 0),

    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES departments(dept_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================================
-- Step 3: Supporting database objects
-- ============================================================

-- Index for fast email lookups
CREATE INDEX idx_email ON employees (email);

-- Compound index for department + salary queries
CREATE INDEX idx_dept_salary ON employees (department_id, salary);

-- View: employees earning above 50,000
CREATE VIEW vw_high_salary AS
SELECT emp_id, first_name, last_name, salary
FROM employees
WHERE salary > 50000;

-- Sequence (Oracle/PostgreSQL)
-- CREATE SEQUENCE emp_seq START WITH 1 INCREMENT BY 1 NOCACHE;

-- Synonym (Oracle)
-- CREATE SYNONYM emp_syn FOR employees;

-- ============================================================
-- B. Seed Data
-- ============================================================

INSERT INTO departments VALUES
    (1, 'Engineering'),
    (2, 'Human Resources'),
    (3, 'Finance'),
    (4, 'Marketing');

INSERT INTO employees VALUES
    (1,  'John',    'Doe',      1, 65000.00, '2023-01-15', 'john.doe@example.com'),
    (2,  'Alice',   'Smith',    2, 55000.00, '2022-11-10', 'alice.smith@example.com'),
    (3,  'Bob',     'Johnson',  3, 48000.00, '2023-02-05', 'bob.johnson@example.com'),
    (4,  'Michael', 'Clark',    1, 78000.00, '2021-06-20', 'michael.clark@example.com'),
    (5,  'James',   'Anderson', 1, 69000.00, '2022-03-14', 'james.anderson@example.com'),
    (6,  'William', 'Martinez', 1, 86000.00, '2020-09-01', 'william.martinez@example.com'),
    (7,  'Evelyn',  'White',    4, 72000.00, '2021-11-30', 'evelyn.white@example.com'),
    (8,  'Ava',     'Garcia',   4, 64000.00, '2023-05-18', 'ava.garcia@example.com'),
    (9,  'Sophia',  'Brown',    2, 52000.00, '2022-07-22', 'sophia.brown@example.com'),
    (10, 'Liam',    'Wilson',   3, 43000.00, '2023-08-10', 'liam.wilson@example.com');

-- ============================================================
-- ALTER Operations
-- ============================================================

-- Add a new column
ALTER TABLE employees
ADD COLUMN phone VARCHAR(15);

-- Modify column type
ALTER TABLE employees
MODIFY COLUMN first_name VARCHAR(80) NOT NULL;

-- Add a constraint
-- ALTER TABLE employees
-- ADD CONSTRAINT chk_hire_date
-- CHECK (hire_date <= CURDATE());

-- Rename table
-- RENAME TABLE employees TO employee_records;

-- TRUNCATE (removes all rows, keeps structure)
-- TRUNCATE TABLE employee_records;

-- DROP table (removes structure)
-- DROP TABLE employee_records;

-- ============================================================
-- Queries
-- ============================================================

-- Employees with salary > 60,000
SELECT emp_id, first_name, last_name, salary
FROM employees
WHERE salary > 60000
ORDER BY salary DESC;

-- Employee count per department
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM departments d
LEFT JOIN employees e
    ON d.dept_id = e.department_id
GROUP BY d.dept_id, d.dept_name
ORDER BY total_employees DESC;

-- Use the view
SELECT *
FROM vw_high_salary
ORDER BY salary DESC;