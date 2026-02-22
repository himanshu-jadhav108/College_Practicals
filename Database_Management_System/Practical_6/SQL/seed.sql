USE employee_management;

INSERT INTO departments (department_name, location) VALUES
('IT', 'Mumbai'),
('HR', 'Pune'),
('Finance', 'Bangalore');

INSERT INTO employees (full_name, email, hire_date, salary, department_id) VALUES
('Anya Forger', 'anya.f@spyxfamily.com', '2022-03-15', 60000, 1),
('Eren Yeager', 'eren_yeager@aot.com', '2021-07-10', 75000, 1),
('Kamado Tanjiro', 'tanjiro@demonslayer.com', '2023-01-05', 50000, 2),
('Naruto Uzumaki', 'naruto@konhoa.com', '2020-11-20', 82000, 3);
