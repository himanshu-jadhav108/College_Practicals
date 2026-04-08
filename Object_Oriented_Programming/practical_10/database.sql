CREATE DATABASE IF NOT EXISTS studentdb;
USE studentdb;

CREATE TABLE IF NOT EXISTS students ( 
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
course VARCHAR(100) NOT NULL,
marks DOUBLE NOT NULL
);

INSERT INTO students (name, course, marks)
VALUES
('Himanshu Jadhav', 'AIDS', 87.5),
('Sujal Bagad', 'Computer Science', 79.2);