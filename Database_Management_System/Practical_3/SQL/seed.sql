INSERT INTO students (name,email,age,department) VALUES
('Himanshu Jadhav','himanshu@mail.com',21,'AIDS'),
('Durgesh Sonawane','dsonawane@mail.com',19,'ENTC'),
('Omkar Shedage','omkarshedage@mail.com',22,'AIDS'),
('Sujit Bera','berasujit@mail.com',20,'CS');

INSERT INTO instructors (name,department) VALUES
('Dr Jethalal Gada','AI'),
('Prof Tarak Mehta','IT');

INSERT INTO courses (course_name,credits,instructor_id) VALUES
('DBMS',4,1),
('Data Science',3,1),
('Embedded System',3,2);

INSERT INTO enrollments (student_id,course_id,grade) VALUES
(1,1,'A'),
(1,2,'B'),
(2,1,'A'),
(3,2,'A'),
(4,3,'B');