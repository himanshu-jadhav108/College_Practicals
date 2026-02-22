USE customer_order_db;

-- INNER JOIN
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

-- LEFT JOIN
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

-- RIGHT JOIN
SELECT 
    c.customer_id,
    c.first_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o
    ON c.customer_id = o.customer_id;

-- FULL OUTER JOIN Simulation (MySQL)
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

-- Aggregation Example
SELECT 
    c.customer_id,
    c.first_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- Performance Check
EXPLAIN
SELECT *
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;