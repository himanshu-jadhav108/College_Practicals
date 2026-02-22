USE sales_management;

INSERT INTO customers (full_name, email, phone, city) VALUES
('Kiyotaka Aayanokoji', 'kiyoayo@example.com', '9876543210', 'Mumbai'),
('Sung JinWoo', 'shadowmoarch@example.com', '9123456780', 'Pune'),
('Lyoid Fronterra', 'lyoid@example.com', '9988776655', 'Delhi');

INSERT INTO products (product_name, category, unit_price, stock_quantity) VALUES
('Wireless Mouse', 'Electronics', 799.00, 150),
('Bluetooth Speaker', 'Electronics', 2499.00, 80),
('Office Chair', 'Furniture', 5999.00, 40);

INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2026-02-10', 'Delivered'),
(2, '2026-02-12', 'Processing');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 2, 799.00),
(1, 2, 1, 2499.00),
(2, 3, 1, 5999.00);