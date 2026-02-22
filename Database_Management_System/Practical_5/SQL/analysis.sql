USE sales_management;

-- View total sales
SELECT fn_total_sales() AS total_revenue;

-- Customer order history
SELECT c.full_name, o.order_id, o.order_date, o.status
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY o.order_date DESC;

-- Revenue per order
SELECT o.order_id,
       SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id
ORDER BY order_total DESC;

-- Filtering high-value orders
SELECT *
FROM orders
WHERE order_id IN (
    SELECT order_id
    FROM order_items
    GROUP BY order_id
    HAVING SUM(quantity * unit_price) > 5000
);

-- Performance check
EXPLAIN SELECT * FROM orders WHERE customer_id = 1;