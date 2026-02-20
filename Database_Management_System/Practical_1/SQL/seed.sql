-- Insert Instructors
INSERT INTO Instructor (Name, Email, Department) VALUES
('Prof. Hitesh Rahangdale', 'hiteshr@mail.com', 'AIDS'),
('Prof. Shweta Kakade', 'skakade@mail.com', 'AIDS'),
('Prof. Kapeshkumar Kondekar', 'kakuko@mail.com', 'Computer Science');

-- Insert Students
INSERT INTO Student (Name, Email, Age, Address) VALUES
('Himanshu Jadhav', 'himanshu@mail.com', 20, 'Malegaon'),
('Durgesh Sonawane', 'dsonawane@mail.com', 21, 'Niphad'),
('Onkar Kharat', 'ok@mail.com', 19, 'Satara');

-- Insert Courses
INSERT INTO Course (CourseName, Credits, InstructorID) VALUES
('DBMS', 4, 1),
('Data Science', 3, 2);

-- Insert Enrollment
INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES
(1,1,CURDATE()),
(1,2,CURDATE()),
(2,1,CURDATE()),
(3,2,CURDATE());

