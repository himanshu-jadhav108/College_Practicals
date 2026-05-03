-- PL/SQL Procedures and Functions
-- schema
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS order_items, orders, products, customers;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    unit_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'Processing',
    CONSTRAINT fk_customer
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    ON DELETE CASCADE
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_order
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_product
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- indexes
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_order_customer ON orders(customer_id);
CREATE INDEX idx_orderitem_order ON order_items(order_id);

-- procedure
DELIMITER //
CREATE PROCEDURE sp_add_order(
    IN p_customer_id INT,
    IN p_order_date DATE
)
BEGIN
    INSERT INTO orders(customer_id, order_date)
    VALUES (p_customer_id, p_order_date);
END //
DELIMITER ;

-- function
DELIMITER //
CREATE FUNCTION fn_total_sales()
RETURNS DECIMAL(12,2)
DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(12,2);
    SELECT SUM(quantity * unit_price)
    INTO total
    FROM order_items;
    RETURN IFNULL(total, 0);
END //
DELIMITER ;

-- seed
INSERT INTO customers (full_name, email, phone, city) VALUES
('Kiyotaka Aayanokoji','kiyoayo@example.com','9876543210','Mumbai'),
('Sung JinWoo','shadowmoarch@example.com','9123456780','Pune'),
('Lyoid Frontera','lyoid@example.com','9988776655','Delhi');

INSERT INTO products (product_name, category, unit_price, stock_quantity) VALUES
('Wireless Mouse','Electronics',799.00,150),
('Bluetooth Speaker','Electronics',2499.00,80),
('Office Chair','Furniture',5999.00,40);

INSERT INTO orders (customer_id, order_date, status) VALUES
(1,'2026-02-10','Delivered'),
(2,'2026-02-12','Processing');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1,1,2,799.00),
(1,2,1,2499.00),
(2,3,1,5999.00);

-- queries
SELECT fn_total_sales() AS total_revenue;

SELECT c.full_name, o.order_id, o.order_date, o.status
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY o.order_date DESC;

SELECT o.order_id,
SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id
ORDER BY order_total DESC;

SELECT *
FROM orders
WHERE order_id IN (
    SELECT order_id
    FROM order_items
    GROUP BY order_id
    HAVING SUM(quantity * unit_price) > 5000
);

EXPLAIN SELECT * FROM orders WHERE customer_id = 1;