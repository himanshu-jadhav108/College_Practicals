USE customer_order_db;

INSERT INTO customers (first_name, last_name, email, phone, city)
VALUES
('Himanshu', 'Jadhav', 'himanshujadhav@email.com', '9876543210', 'Mumbai'),
('Dhruv', 'Kulkarni', 'dk@email.com', '9123456780', 'Pune'),
('Onkar', 'Kharat', 'onkar@email.com', '9988776655', 'Delhi'),
('Paritosh', 'Sandhan', 'paru@email.com', '9871234567', 'Bangalore'),
('Baku', 'Madarame', 'baku@email.com', '9090909090', 'Hyderabad');

INSERT INTO orders (customer_id, order_date, total_amount, order_status)
VALUES
(1, '2026-01-10', 2500.00, 'Delivered'),
(1, '2026-01-15', 1800.50, 'Shipped'),
(2, '2026-01-20', 3200.75, 'Processing'),
(3, '2026-01-22', 4999.99, 'Delivered'),
(NULL, '2026-01-25', 1500.00, 'Guest Order');