-- ==========================================
-- CUSTOMER ANALYSIS
-- Nova Retail Group
-- ==========================================

-- 1. Total Customers
SELECT
    COUNT(*) AS total_customers
FROM customers;

-- 2. Active Customers
SELECT
    COUNT(DISTINCT customer_id) AS active_customers
FROM sales;

-- 3. Total Purchases Per Customer
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(s.sale_id) AS total_purchases
FROM customers c
LEFT JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_purchases DESC;

-- 4. Customer Lifetime Value (CLV)
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(s.total_amount) AS lifetime_value
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY lifetime_value DESC;

-- 5. Average Purchase Value Per Customer
SELECT
    customer_id,
    AVG(total_amount) AS average_purchase
FROM sales
GROUP BY customer_id
ORDER BY average_purchase DESC;

-- 6. Top 10 Customers
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(s.total_amount) AS total_spent
FROM customers c
JOIN sales s
ON c.customer_id = s.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 10;

-- 7. Customers By City
SELECT
    city,
    COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;