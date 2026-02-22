# Database Management System Practicals – SPPU 2024

This folder contains **DBMS practical codes** covering database design, SQL queries, normalization, and transaction management as per **SPPU 2024 pattern**.

---

## 📌 Overview

This repository focuses on:
- **SQL Queries** – Data Definition Language (DDL), Data Manipulation Language (DML), and Data Control Language (DCL)
- **Database Design** – ER diagrams, normalization (1NF, 2NF, 3NF, BCNF)
- **Advanced SQL** – Joins, subqueries, views, stored procedures, and triggers
- **Transaction Management** – ACID properties, concurrency control, and locking mechanisms
- **Database Performance** – Indexing, query optimization, and execution plans

---
## 📁 Folder Structure

```
Database_Management_System/
├── README_DBMS.md
├── temperory.txt
├── MiniProjects/
│   ├── ERD/
│   ├── Notes/
│   │   └── README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_1/ to Practical_9/
│   ├── ERD/
│   ├── Notes/
│   │   └── README.md
│   ├── Screenshots/
│   └── SQL/
│       ├── analysis.sql
│       ├── schema.sql
│       └── seed.sql
├── Screenshots/
└── Trial/
    ├── ERD/
    ├── Notes/
    └── SQL/
```

---
## 🚀 How to Use

1. **Navigate to the Database_Management_System folder**:
```bash
cd Database_Management_System
```

2. **Set up your database** (MySQL, PostgreSQL, or SQLite):
```bash
# For MySQL
mysql -u username -p database_name < script.sql
```

3. **Run SQL scripts or Python programs**:
```bash
python practical_name.py
```

---

## 📚 Practical List

1. **[Practical 1: Database Setup and Creation](Practical_1/)**  
   Setup and create a database using MySQL/PostgreSQL. Covers entities like Student, Course, Instructor, Enrollment, and their relationships.

2. **[Practical 2: Views and Indexing](Practical_2/)**  
   Optimizing a Student Course Management System using views and indexing for faster query performance.

3. **[Practical 3: SQL Queries with Filters and Sorting](Practical_3/)**  
   Perform advanced querying using filtering, sorting, aggregation, and nested subqueries.

4. **[Practical 4: Multi-Table Joins](Practical_4/)**  
   Implement multi-table joins in a Customer Order Management System using INNER JOIN, LEFT JOIN, etc.

5. **[Practical 5: PL/SQL Procedures and Functions](Practical_5/)**  
   Design a Sales Management System using stored procedures and functions for data handling.

6. **[Practical 6: Triggers and Cursors](Practical_6/)**  
   Develop an Employee Management System with triggers for audit logging and cursors for salary updates.

7. **[Practical 7: [In Progress]](Practical_7/)**  
   [Description to be added]

8. **[Practical 8: [In Progress]](Practical_8/)**  
   [Description to be added]

9. **[Practical 9: MySQL Database Backup and Recovery](Practical_9/)**  
   Demonstrate backup and recovery operations in a Library Management System.

Additionally, there are **[MiniProjects](MiniProjects/)** and **[Trial](Trial/)** folders for advanced exercises.

---

## 🛠 Dependencies

- Python 3.x
- mysql-connector-python (for MySQL)
- psycopg2 (for PostgreSQL)
- sqlite3 (built-in for SQLite)
- pandas (for data analysis with SQL)

---

## 📖 Topics Covered

- Table creation and manipulation
- Query optimization
- Normalization and denormalization
- Views and Indexes
- Stored procedures and triggers
- Transaction control

---

## 👨‍💻 Maintainer
Maintained by **Himanshu Jadhav**  
Second-Year Engineering Student (AI & Data Science)  
[GitHub](https://github.com/himanshu-jadhav108) • [LinkedIn](https://www.linkedin.com/in/himanshu-jadhav-328082339) • [Instagram](https://www.instagram.com/himanshu_jadhav_108?igsh=MWYxamppcTBlY3Rl) • [Portfolio](https://himanshu-jadhav-portfolio.vercel.app/)

---

✅ Each practical is modular and well-commented for easy understanding.
