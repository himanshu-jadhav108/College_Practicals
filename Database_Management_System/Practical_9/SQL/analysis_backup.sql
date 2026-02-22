USE library_backup_system;

-- Verify data integrity after restore
SELECT COUNT(*) AS total_books,
       SUM(available_copies) AS total_copies_available
FROM books;

-- Join validation: show who borrowed what and when
SELECT m.full_name AS member,
       b.title AS book,
       br.borrow_date,
       COALESCE(br.return_date, 'Not Returned') AS return_status
FROM borrow_records br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
ORDER BY br.borrow_date DESC;

-- Aggregation check: how many books each author wrote
SELECT a.full_name AS author,
       COUNT(b.book_id) AS total_books_written,
       MIN(b.publication_year) AS earliest_work,
       MAX(b.publication_year) AS latest_work
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.full_name
ORDER BY total_books_written DESC;

-- Active borrow records (still checked out)
SELECT br.borrow_id,
       m.full_name AS member,
       b.title AS book,
       br.borrow_date
FROM borrow_records br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
WHERE br.return_date IS NULL
ORDER BY br.borrow_date;

-- Performance check: index usage
EXPLAIN SELECT * FROM books WHERE author_id = 1;

-- Borrow frequency per member
SELECT m.full_name AS member,
       COUNT(br.book_id) AS total_borrowed
FROM members m
LEFT JOIN borrow_records br ON m.member_id = br.member_id
GROUP BY m.full_name
ORDER BY total_borrowed DESC;

-- Extra: Most borrowed books
SELECT b.title AS book,
       COUNT(br.member_id) AS times_borrowed
FROM books b
LEFT JOIN borrow_records br ON b.book_id = br.book_id
GROUP BY b.title
ORDER BY times_borrowed DESC;