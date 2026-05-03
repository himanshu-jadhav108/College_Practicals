-- Multi Table Joins
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS orders, customers;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    CONSTRAINT fk_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
    ON DELETE SET NULL
);

CREATE INDEX idx_orders_customer_id ON orders(customer_id);

-- seed
INSERT INTO customers (first_name, last_name, email, phone, city) VALUES
('Himanshu','Jadhav','himanshujadhav@email.com','9876543210','Mumbai'),
('Dhruv','Kulkarni','dk@email.com','9123456780','Pune'),
('Onkar','Kharat','onkar@email.com','9988776655','Delhi'),
('Paritosh','Sandhan','paru@email.com','9871234567','Bangalore'),
('Baku','Madarame','baku@email.com','9090909090','Hyderabad');

INSERT INTO orders (customer_id, order_date, total_amount, order_status) VALUES
(1,'2026-01-10',2500.00,'Delivered'),
(1,'2026-01-15',1800.50,'Shipped'),
(2,'2026-01-20',3200.75,'Processing'),
(3,'2026-01-22',4999.99,'Delivered'),
(NULL,'2026-01-25',1500.00,'Guest Order');

-- queries
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY o.order_date DESC;

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
ORDER BY c.customer_id;

SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_id,
    c.first_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

EXPLAIN
SELECT * FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;