CREATE DATABASE IF NOT EXISTS employee_management;
USE employee_management;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    department_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON DELETE RESTRICT
);

CREATE TABLE employee_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    action_type VARCHAR(10),
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_employee_department ON employees(department_id);

DELIMITER //

CREATE TRIGGER trg_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit(employee_id, action_type, new_salary)
    VALUES (NEW.employee_id, 'INSERT', NEW.salary);
END //

CREATE TRIGGER trg_employee_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit(employee_id, action_type, old_salary, new_salary)
    VALUES (OLD.employee_id, 'UPDATE', OLD.salary, NEW.salary);
END //

CREATE TRIGGER trg_employee_delete
AFTER DELETE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit(employee_id, action_type, old_salary)
    VALUES (OLD.employee_id, 'DELETE', OLD.salary);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_increment_it_salary()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_id INT;
    DECLARE emp_salary DECIMAL(10,2);

    DECLARE emp_cursor CURSOR FOR
        SELECT employee_id, salary
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        WHERE d.department_name = 'IT';

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN emp_cursor;

    salary_loop: LOOP
        FETCH emp_cursor INTO emp_id, emp_salary;
        IF done THEN
            LEAVE salary_loop;
        END IF;

        UPDATE employees
        SET salary = emp_salary * 1.10
        WHERE employee_id = emp_id;

    END LOOP;

    CLOSE emp_cursor;
END //

DELIMITER ;