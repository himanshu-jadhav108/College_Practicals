-- Trigger and Coursor
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS employee_audit, employees, departments;
SET FOREIGN_KEY_CHECKS = 1;

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
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE employee_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    action_type VARCHAR(10),
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- index
CREATE INDEX idx_employee_department ON employees(department_id);

-- triggers
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

-- procedure
DELIMITER //
CREATE PROCEDURE sp_increment_it_salary()
BEGIN
    UPDATE employees
    SET salary = salary * 1.10
    WHERE department_id IN (
        SELECT department_id
        FROM departments
        WHERE department_name = 'IT'
    );
END //
DELIMITER ;

-- seed
INSERT INTO departments (department_name, location) VALUES
('IT','Mumbai'),
('HR','Pune'),
('Finance','Bangalore');

INSERT INTO employees (full_name, email, hire_date, salary, department_id) VALUES
('Anya Forger','anya.f@spyxfamily.com','2022-03-15',60000,1),
('Eren Yeager','eren@aot.com','2021-07-10',75000,1),
('Kamado Tanjiro','tanjiro@ds.com','2023-01-05',50000,2),
('Naruto Uzumaki','naruto@naruto.com','2020-11-20',82000,3);

-- queries
SELECT full_name, salary FROM employees;

CALL sp_increment_it_salary();

SELECT full_name, salary FROM employees ORDER BY salary DESC;

SELECT * FROM employee_audit ORDER BY changed_at DESC;

SELECT d.department_name,
COUNT(e.employee_id) AS total_employees,
SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC;

EXPLAIN SELECT * FROM employees WHERE department_id = 1;