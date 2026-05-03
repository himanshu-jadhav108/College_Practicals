-- Backup and Dumping 
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS borrow_records, books, members, authors;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    country VARCHAR(100)
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    join_date DATE NOT NULL,
    membership_type VARCHAR(50) NOT NULL
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    isbn VARCHAR(20) NOT NULL UNIQUE,
    publication_year YEAR,
    author_id INT NOT NULL,
    available_copies INT DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE borrow_records (
    borrow_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- indexes
CREATE INDEX idx_book_author ON books(author_id);
CREATE INDEX idx_borrow_member ON borrow_records(member_id);
CREATE INDEX idx_borrow_book ON borrow_records(book_id);

-- seed
INSERT INTO authors (full_name, country) VALUES
('Masashi Kishimoto','Japan'),
('Kentaro Miura','Japan'),
('Akira Toriyama','Japan'),
('Tite Kubo','Japan'),
('Eiichiro Oda','Japan'),
('Hajime Isayama','Japan'),
('Yoshihiro Togashi','Japan');

INSERT INTO members (full_name, email, join_date, membership_type) VALUES
('Naruto Uzumaki','naruto@dattebayo.com','2025-01-10','Premium'),
('Goku Son','goku@kamehameha.com','2025-03-15','Standard'),
('Monkey D. Luffy','luffy@onepiece.com','2025-06-05','Premium'),
('Ichigo Kurosaki','ichigo@bleach.com','2025-07-20','Standard'),
('Eren Yeager','eren@aot.com','2025-08-12','Premium'),
('Guts','guts@berserk.com','2025-09-01','Standard'),
('Gon Freecss','gon@hxh.com','2025-10-10','Premium');

INSERT INTO books (title, isbn, publication_year, author_id, available_copies) VALUES
('Naruto','9784088725093',1999,1,10),
('Berserk','9784592132290',1989,2,6),
('Dragon Ball','9784088518312',1984,3,12),
('Bleach','9784088732138',2001,4,8),
('One Piece','9784088725094',1997,5,15),
('Attack on Titan','9784063842760',2009,6,7),
('Hunter x Hunter','9784088725095',1998,7,9);

INSERT INTO borrow_records (member_id, book_id, borrow_date, return_date) VALUES
(1,2,'2026-01-05','2026-01-15'),
(2,5,'2026-02-01',NULL),
(3,3,'2026-02-10',NULL),
(4,1,'2026-02-15',NULL),
(5,4,'2026-02-20',NULL),
(6,6,'2026-02-25',NULL),
(7,7,'2026-03-01',NULL);

-- queries
SELECT COUNT(*) AS total_books,
SUM(available_copies) AS total_copies_available
FROM books;

SELECT m.full_name AS member,
b.title AS book,
br.borrow_date,
COALESCE(br.return_date,'Not Returned') AS return_status
FROM borrow_records br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
ORDER BY br.borrow_date DESC;

SELECT a.full_name AS author,
COUNT(b.book_id) AS total_books_written,
MIN(b.publication_year) AS earliest_work,
MAX(b.publication_year) AS latest_work
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
GROUP BY a.full_name
ORDER BY total_books_written DESC;

SELECT br.borrow_id,
m.full_name AS member,
b.title AS book,
br.borrow_date
FROM borrow_records br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
WHERE br.return_date IS NULL
ORDER BY br.borrow_date;

EXPLAIN SELECT * FROM books WHERE author_id = 1;

SELECT m.full_name AS member,
COUNT(br.book_id) AS total_borrowed
FROM members m
LEFT JOIN borrow_records br ON m.member_id = br.member_id
GROUP BY m.full_name
ORDER BY total_borrowed DESC;

SELECT b.title AS book,
COUNT(br.member_id) AS times_borrowed
FROM books b
LEFT JOIN borrow_records br ON b.book_id = br.book_id
GROUP BY b.title
ORDER BY times_borrowed DESC;