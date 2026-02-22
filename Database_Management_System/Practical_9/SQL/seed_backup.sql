USE library_backup_system;

-- Authors (same as before, legendary manga creators)
INSERT INTO authors (full_name, country) VALUES
('Masashi Kishimoto', 'Japan'),       -- Naruto
('Kentaro Miura', 'Japan'),           -- Berserk
('Akira Toriyama', 'Japan'),          -- Dragon Ball
('Tite Kubo', 'Japan'),               -- Bleach
('Eiichiro Oda', 'Japan'),            -- One Piece
('Hajime Isayama', 'Japan'),          -- Attack on Titan
('Yoshihiro Togashi', 'Japan');       -- Hunter x Hunter

-- Members replaced with anime protagonists
INSERT INTO members (full_name, email, join_date, membership_type) VALUES
('Naruto Uzumaki', 'naruto@dattebayo.com', '2025-01-10', 'Premium'),
('Goku Son', 'goku@kamehameha.com', '2025-03-15', 'Standard'),
('Monkey D. Luffy', 'luffy@onepiece.com', '2025-06-05', 'Premium'),
('Ichigo Kurosaki', 'ichigo@bleach.com', '2025-07-20', 'Standard'),
('Eren Yeager', 'eren@aot.com', '2025-08-12', 'Premium'),
('Guts', 'guts@berserk.com', '2025-09-01', 'Standard'),
('Gon Freecss', 'gon@hxh.com', '2025-10-10', 'Premium');

-- Books (legendary manga titles)
INSERT INTO books (title, isbn, publication_year, author_id, available_copies) VALUES
('Naruto', '9784088725093', 1999, 1, 10),
('Berserk', '9784592132290', 1989, 2, 6),
('Dragon Ball', '9784088518312', 1984, 3, 12),
('Bleach', '9784088732138', 2001, 4, 8),
('One Piece', '9784088725094', 1997, 5, 15),
('Attack on Titan', '9784063842760', 2009, 6, 7),
('Hunter x Hunter', '9784088725095', 1998, 7, 9);

-- Borrow records (protagonists borrowing other series for fun)
INSERT INTO borrow_records (member_id, book_id, borrow_date, return_date) VALUES
(1, 2, '2026-01-05', '2026-01-15'),   -- Naruto borrowed Berserk
(2, 5, '2026-02-01', NULL),           -- Goku borrowed One Piece
(3, 3, '2026-02-10', NULL),           -- Luffy borrowed Dragon Ball
(4, 1, '2026-02-15', NULL),           -- Ichigo borrowed Naruto
(5, 4, '2026-02-20', NULL),           -- Eren borrowed Bleach
(6, 6, '2026-02-25', NULL),           -- Guts borrowed Attack on Titan
(7, 7, '2026-03-01', NULL);           -- Gon borrowed Hunter x Hunter