-- Intro to DB
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Age INT,
    Address TEXT
);

CREATE TABLE Instructor (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Department VARCHAR(100) NOT NULL
);

CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    Credits INT NOT NULL,
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
);

CREATE TABLE Enrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    UNIQUE (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- seed
INSERT INTO Instructor (Name, Email, Department) VALUES
('Prof. Hitesh Rahangdale', 'hiteshr@mail.com', 'AIDS'),
('Prof. Shweta Kakade', 'skakade@mail.com', 'AIDS'),
('Prof. Kapeshkumar Kondekar', 'kakuko@mail.com', 'Computer Science');

INSERT INTO Student (Name, Email, Age, Address) VALUES
('Himanshu Jadhav', 'himanshu@mail.com', 20, 'Malegaon'),
('Durgesh Sonawane', 'dsonawane@mail.com', 21, 'Niphad'),
('Onkar Kharat', 'ok@mail.com', 19, 'Satara');

INSERT INTO Course (CourseName, Credits, InstructorID) VALUES
('DBMS', 4, 1),
('Data Science', 3, 2);

INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES
(1,1,CURDATE()),
(1,2,CURDATE()),
(2,1,CURDATE()),
(3,2,CURDATE());

-- queries
SELECT s.Name, c.CourseName
FROM Enrollment e
JOIN Student s ON e.StudentID = s.StudentID
JOIN Course c ON e.CourseID = c.CourseID;

SELECT c.CourseName, i.Name AS Instructor
FROM Course c
JOIN Instructor i ON c.InstructorID = i.InstructorID;

SELECT c.CourseName, COUNT(e.StudentID) AS TotalStudents
FROM Course c
LEFT JOIN Enrollment e ON c.CourseID = e.CourseID
GROUP BY c.CourseName;