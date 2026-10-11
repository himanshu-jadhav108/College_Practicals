# 🗄️ Database Management System Practicals – SPPU 2024

> **Second-Year Engineering | AI & Data Science | Savitribai Phule Pune University**

![SQL](https://img.shields.io/badge/SQL-MySQL%20%7C%20PostgreSQL%20%7C%20SQLite-blue?logo=mysql&logoColor=white)
![NoSQL](https://img.shields.io/badge/NoSQL-MongoDB-green?logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![SPPU](https://img.shields.io/badge/University-SPPU%202024-orange)

---

## 📌 Overview

This repository contains **DBMS practical codes** as per the **SPPU 2024 curriculum**, covering relational and non-relational database concepts, query design, optimization techniques, and transaction management.

### Key Focus Areas

| Area | Topics |
|------|--------|
| **SQL Foundations** | DDL, DML, DCL, TCL |
| **Database Design** | ER Diagrams, Normalization (1NF → BCNF) |
| **Advanced SQL** | Joins, Subqueries, Views, Stored Procedures, Triggers, Cursors |
| **Transaction Management** | ACID Properties, Concurrency Control, Locking |
| **Performance Tuning** | Indexing, Query Optimization, Execution Plans |
| **NoSQL** | MongoDB CRUD, Indexing, Aggregation Pipelines |

---

## 📁 Folder Structure

```
Database_Management_System/
├── README_DBMS.md               ← You are here
├── .gitignore
├── Practical_1/                 ← Database Setup & Creation (SQL)
│   ├── ERD/
│   ├── Notes/README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_2/                 ← Views & Indexing (SQL)
│   ├── ERD/
│   ├── Notes/README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_3/                 ← Filters, Sorting & Aggregation (SQL)
│   ├── ERD/
│   ├── Notes/README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_4/                 ← Multi-Table Joins (SQL)
│   ├── ERD/
│   ├── Notes/README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_5/                 ← PL/SQL Procedures & Functions
│   ├── ERD/
│   ├── Notes/README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_6/                 ← Triggers & Cursors
│   ├── ERD/
│   ├── Notes/README.md
│   ├── Screenshots/
│   └── SQL/
├── Practical_7/                 ← NoSQL Indexing (MongoDB)
│   ├── NoSQL/
│   │   └── practical07_playground.mongodb.js
│   ├── Notes/README.md
│   └── Screenshots/
├── Practical_8/                 ← NoSQL Aggregation Pipelines (MongoDB)
│   ├── NoSQL/
│   │   └── aggregation_queries.js
│   ├── Notes/README.md
│   └── Screenshots/
├── Practical_9/                 ← Backup & Recovery (MySQL)
│   ├── ERD/
│   ├── Notes/
│   ├── Screenshots/
│   └── SQL/
├── MiniProjects/                ← Advanced Exercises & ERDs
│   ├── ERD/
│   ├── Notes/
│   ├── Screenshots/
│   └── SQL/
└── Trial/                       ← Experimental / Scratch Work
    ├── ERD/
    ├── Notes/
    └── SQL/
```

Each **SQL Practical** contains:
```
Practical_N/
├── ERD/              ← Entity-Relationship Diagrams
├── Notes/
│   └── README.md     ← Practical description, theory & ER diagram
├── Screenshots/      ← Query output screenshots
└── SQL/              ← SQL scripts
    ├── schema.sql    ← Table creation
    ├── seed.sql      ← Sample data insertion
    └── queries.sql   ← Queries & analysis
```

Each **NoSQL Practical** contains:
```
Practical_N/
├── NoSQL/
│   └── *.mongodb.js  ← MongoDB playground scripts
├── Notes/
│   └── README.md     ← Practical description & theory
└── Screenshots/      ← Query output screenshots
```

---

## 📚 Practical List

### 🔹 SQL Practicals

| # | Title | Key Concepts |
|---|-------|-------------|
| 1 | [Database Setup & Creation](Practical_1/) | DDL, ER Mapping, Student–Course–Instructor schema |
| 2 | [Views & Indexing](Practical_2/) | `CREATE VIEW`, `CREATE INDEX`, query optimization |
| 3 | [Filters, Sorting & Aggregation](Practical_3/) | `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, subqueries |
| 4 | [Multi-Table Joins](Practical_4/) | `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, Customer–Order schema |
| 5 | [PL/SQL Procedures & Functions](Practical_5/) | `CREATE PROCEDURE`, `CREATE FUNCTION`, Sales Management System |
| 6 | [Triggers & Cursors](Practical_6/) | `CREATE TRIGGER`, cursors, audit logging, Employee Management |
| 9 | [Backup & Recovery](Practical_9/) | `mysqldump`, restore, Library Management System |

### 🔹 NoSQL Practicals (MongoDB)

| # | Title | Key Concepts |
|---|-------|-------------|
| 7 | [NoSQL Indexing](Practical_7/) | `createIndex()`, compound indexes, nested field indexes, `getIndexes()`, `dropIndex()` |
| 8 | [NoSQL Aggregation Pipelines](Practical_8/) | `$group`, `$unwind`, `$sort`, `$limit`, hashtag analytics, Social Media dataset |

---

## 🚀 Getting Started

### SQL Practicals

**1. Connect to your database:**
```bash
# MySQL
mysql -u username -p

# PostgreSQL
psql -U username -d database_name
```

**2. Run the SQL scripts in order:**
```sql
-- Step 1: Create schema
SOURCE Practical_N/SQL/schema.sql;

-- Step 2: Insert seed data
SOURCE Practical_N/SQL/seed.sql;

-- Step 3: Run analysis queries
SOURCE Practical_N/SQL/analysis.sql;
```

**3. Or use Python to connect and execute:**
```bash
python practical_name.py
```

### NoSQL Practicals (MongoDB)

**1. Start MongoDB shell:**
```bash
mongosh
```

**2. Select or create your database:**
```js
use practicalDB
```

**3. Run MongoDB playground scripts:**
```bash
# Practical 7 - Indexing
mongosh < Practical_7/NoSQL/practical07_playground.mongodb.js

# Practical 8 - Aggregation
mongosh < Practical_8/NoSQL/aggregation_queries.js
```

---

## 🛠️ Dependencies

### Python (SQL Practicals)
```bash
pip install mysql-connector-python psycopg2 pandas
```

| Package | Purpose |
|---------|---------|
| `mysql-connector-python` | Connect to MySQL |
| `psycopg2` | Connect to PostgreSQL |
| `sqlite3` | Built-in SQLite support |
| `pandas` | Data analysis & result formatting |

### NoSQL Practicals
- **MongoDB** (v6.x or later) — [Download](https://www.mongodb.com/try/download/community)
- **mongosh** — MongoDB Shell

---

## 📖 Topics Covered

- ✅ Table creation, alteration, and deletion (DDL)  
- ✅ Data insertion, updating, and deletion (DML)  
- ✅ User privileges and access control (DCL)  
- ✅ ER diagram design and relational mapping  
- ✅ Normalization — 1NF, 2NF, 3NF, BCNF  
- ✅ Views and materialized query optimization  
- ✅ Indexing strategies (single-column, compound, nested)  
- ✅ Stored procedures and user-defined functions  
- ✅ Triggers for audit logging and automation  
- ✅ Cursors for row-by-row processing  
- ✅ Transaction control (COMMIT, ROLLBACK, SAVEPOINT)  
- ✅ Backup and recovery strategies  
- ✅ MongoDB CRUD operations  
- ✅ MongoDB aggregation pipelines and analytics  

---

## 👨‍💻 Maintainer

**Himanshu Jadhav**  
Second-Year Engineering Student — AI & Data Science | SPPU  

[![GitHub](https://img.shields.io/badge/GitHub-himanshu--jadhav108-black?logo=github)](https://github.com/himanshu-jadhav108)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Himanshu%20Jadhav-blue?logo=linkedin)](https://www.linkedin.com/in/himanshu-jadhav-328082339)
[![Instagram](https://img.shields.io/badge/Instagram-himanshu__jadhav__108-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/himanshu_jadhav_108?igsh=MWYxamppcTBlY3Rl)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blueviolet?logo=vercel)](https://himanshu-jadhav-portfolio.vercel.app/)

---

> ✅ Each practical is **modular**, **well-documented**, and structured for easy understanding and college lab submissions.
