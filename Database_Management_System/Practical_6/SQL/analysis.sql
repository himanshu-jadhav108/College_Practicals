USE employee_management;

-- View employees before increment
SELECT full_name, salary FROM employees;

-- Call cursor-based salary increment
CALL sp_increment_it_salary();

-- Verify salary changes
SELECT full_name, salary FROM employees ORDER BY salary DESC;

-- Check audit logs
SELECT * FROM employee_audit ORDER BY changed_at DESC;

-- Aggregate salary by department
SELECT d.department_name,
       COUNT(e.employee_id) AS total_employees,
       SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC;

-- Performance check
EXPLAIN SELECT * FROM employees WHERE department_id = 1;