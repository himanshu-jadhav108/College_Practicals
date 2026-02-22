# Practical 9: Database Backup and Recovery

## Overview

This practical demonstrates the process of backing up and restoring a MySQL database using the `mysqldump` utility. The focus is on logical backups, which export the database structure and data as SQL statements that can be re-executed to recreate the database.

### Objectives
- Create a sample database and populate it with data.
- Perform a logical backup using `mysqldump`.
- Simulate data loss by dropping the database.
- Restore the database from the backup file.
- Verify the integrity of the restored data.

### Prerequisites
- MySQL server running (either locally or in a Docker container).
- Access to MySQL client tools (`mysql` and `mysqldump`).
- Schema, seed, and analysis SQL files from this practical.
- Basic knowledge of SQL and command-line operations.

**Note:** This guide assumes you are using a Docker container named `mysql-dbms` with MySQL running. Adjust commands accordingly for your setup.

---

## Step-by-Step Execution Guide

### Step 1: Set Up the Database and Insert Sample Data

1. **Connect to MySQL:**
   - If using Docker:
     ```bash
     docker exec -it mysql-dbms mysql -u root -p
     ```
     Enter the password when prompted (e.g., `Himanshu@09` or your configured password).

   - If using local MySQL:
     ```bash
     mysql -u root -p
     ```

2. **Create and Populate the Database:**
   ```sql
   CREATE DATABASE IF NOT EXISTS library_backup_system;
   USE library_backup_system;

   -- Source the schema file (adjust path as needed)
   SOURCE /mnt/d/College Practicals/Database_Management_System/Practical_9/SQL/schema.sql;

   -- Source the seed file to insert sample data
   SOURCE /mnt/d/College Practicals/Database_Management_System/Practical_9/SQL/seed.sql;
   ```

3. **Verify Data Insertion:**
   ```sql
   SELECT COUNT(*) AS total_books FROM books;
   SELECT COUNT(*) AS total_members FROM members;
   SELECT COUNT(*) AS total_borrow_records FROM borrow_records;
   ```
   - Expected: Non-zero counts indicating data is present.
   - Take a screenshot of the results for your practical record.

4. **Exit MySQL Shell:**
   ```sql
   EXIT;
   ```

---

### Step 2: Create a Database Backup

1. **Run mysqldump Command:**
   - From the terminal (outside MySQL shell).
   - If using Docker:
     ```bash
     docker exec mysql-dbms mysqldump -u root -p library_backup_system > library_backup_system_backup.sql
     ```
   - If using local MySQL:
     ```bash
     mysqldump -u root -p library_backup_system > library_backup_system_backup.sql
     ```
   - Enter the password when prompted.

2. **Verify the Backup File:**
   ```bash
   ls -la library_backup_system_backup.sql
   head -20 library_backup_system_backup.sql
   ```
   - The file should contain SQL statements like `CREATE TABLE`, `INSERT INTO`, etc.
   - File size should be reasonable (not empty).
   - Take a screenshot of the command and file listing.

**Note:** This is a logical backup. It exports the database as SQL commands that can recreate the structure and data.

---

### Step 3: Simulate Data Loss

1. **Connect to MySQL Again:**
   ```bash
   docker exec -it mysql-dbms mysql -u root -p
   ```

2. **Drop the Database:**
   ```sql
   DROP DATABASE library_backup_system;
   ```

3. **Verify Deletion:**
   ```sql
   SHOW DATABASES;
   ```
   - The `library_backup_system` database should no longer appear in the list.
   - Take a screenshot showing the databases list without the dropped database.

4. **Exit MySQL Shell:**
   ```sql
   EXIT;
   ```

This step simulates scenarios like accidental deletion, hardware failure, or corruption.

---

### Step 4: Restore the Database from Backup

1. **Restore Using the Backup File:**
   - If using Docker:
     ```bash
     docker exec -i mysql-dbms mysql -u root -p < library_backup_system_backup.sql
     ```
   - If using local MySQL:
     ```bash
     mysql -u root -p < library_backup_system_backup.sql
     ```
   - Enter the password when prompted.

2. **Verify Restoration:**
   ```bash
   docker exec -it mysql-dbms mysql -u root -p -e "SHOW DATABASES;"
   docker exec -it mysql-dbms mysql -u root -p -e "USE library_backup_system; SELECT COUNT(*) FROM books; SELECT COUNT(*) FROM members; SELECT COUNT(*) FROM borrow_records;"
   ```
   - The database should reappear in the list.
   - Counts should match the pre-drop values.
   - Take a screenshot of the verification queries.

---

### Step 5: Verify Data Integrity and Relationships

1. **Connect to MySQL:**
   ```bash
   docker exec -it mysql-dbms mysql -u root -p
   USE library_backup_system;
   ```

2. **Run Integrity Checks:**
   ```sql
   -- Check table structures
   DESCRIBE books;
   DESCRIBE members;
   DESCRIBE borrow_records;

   -- Verify data counts
   SELECT COUNT(*) FROM books;
   SELECT COUNT(*) FROM members;
   SELECT COUNT(*) FROM borrow_records;

   -- Test relationships (foreign keys)
   SELECT m.full_name, b.title, br.borrow_date, br.return_date
   FROM borrow_records br
   JOIN members m ON br.member_id = m.member_id
   JOIN books b ON br.book_id = b.book_id
   LIMIT 10;

   -- Check for any orphaned records
   SELECT * FROM borrow_records WHERE member_id NOT IN (SELECT member_id FROM members);
   SELECT * FROM borrow_records WHERE book_id NOT IN (SELECT book_id FROM books);
   ```

3. **Exit MySQL Shell:**
   ```sql
   EXIT;
   ```

- If all queries execute without errors and show expected data, the recovery is successful.
- Take screenshots of the relationship query results.

---

## Practical Record Documentation

### Aim
To demonstrate database backup and recovery using MySQL's `mysqldump` utility, ensuring data integrity and availability in case of failures.

### Tools Used
- MySQL Server (version 8.x or compatible)
- mysqldump utility
- Docker (for containerized MySQL) or native MySQL installation
- Terminal/Command Prompt
- SQL files: `schema.sql`, `seed.sql`, `analysis.sql`

### Procedure
1. Established a MySQL connection and created the `library_backup_system` database.
2. Executed schema and seed scripts to set up tables and insert sample data.
3. Verified data presence with SELECT queries.
4. Performed a logical backup using `mysqldump`, creating `library_backup_system_backup.sql`.
5. Simulated data loss by dropping the database.
6. Restored the database from the backup file.
7. Validated restoration through data counts and relationship queries.

### Result
The database was successfully backed up and restored, with all data and relationships intact. This demonstrates the effectiveness of logical backups for disaster recovery and data protection.

### Screenshots Required
- Pre-backup data verification
- mysqldump command execution
- Post-drop database list
- Post-restore database list and data counts
- Integrity check query results

---

## Additional Concepts (For Enhanced Understanding)

- **Logical Backup:** Exports database as SQL statements (using mysqldump).
- **Physical Backup:** Direct copy of MySQL data files and directories.
- **Full Backup:** Complete database export (as demonstrated).
- **Incremental Backup:** Only changes since last backup (requires additional tools like Percona XtraBackup).
- **Point-in-Time Recovery:** Restoring to a specific moment using binary logs.
- **Disaster Recovery Planning:** Involves regular backups, testing restores, and offsite storage.

---

## Common Issues and Troubleshooting

- **Permission Denied:** Ensure you have proper MySQL user privileges (e.g., root or user with BACKUP_ADMIN role).
- **Password Issues:** Use `--password=yourpassword` instead of `-p` for non-interactive scripts, but avoid in production.
- **Path Issues:** Ensure SQL files are accessible from the MySQL container or adjust paths.
- **Large Databases:** For big databases, consider compression: `mysqldump ... | gzip > backup.sql.gz`
- **Character Encoding:** Add `--default-character-set=utf8mb4` if using special characters.
- **Docker Volume Persistence:** Ensure Docker volumes are properly configured to persist data across container restarts.

---

## Environment-Specific Notes

- **Docker Setup:** Commands assume container name `mysql-dbms`. Check with `docker ps`.
- **Local MySQL:** Ensure MySQL service is running (`sudo systemctl start mysql` on Linux).
- **Windows/WSL:** Use WSL terminal for Docker commands; adjust paths for Windows file system.
- **Security:** Never hardcode passwords in scripts; use environment variables or secure prompts.

This guide provides a complete, demonstrable process for database backup and recovery. Follow each step carefully and document your actions for the practical submission.
