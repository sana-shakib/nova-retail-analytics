SELECT 
    SUM(total_amount) AS total_revenue
FROM sales;
SELECT 
    COUNT(*) AS total_sales
FROM sales;
SELECT 
    AVG(total_amount) AS average_sale_value
FROM sales;
SELECT
    EXTRACT(YEAR FROM sale_date) AS year,
    SUM(total_amount) AS revenue
FROM sales
GROUP BY year
ORDER BY year;
SELECT
    DATE_TRUNC('month', sale_date) AS month,
    SUM(total_amount) AS revenue
FROM sales
GROUP BY month
ORDER BY month;
SELECT
    b.branch_name,
    SUM(s.total_amount) AS revenue
FROM sales s

JOIN branches b
ON s.branch_id = b.branch_id

GROUP BY b.branch_name

ORDER BY revenue DESC;
SELECT
    b.branch_name,
    SUM(s.total_amount) AS revenue
FROM sales s

JOIN branches b
ON s.branch_id = b.branch_id

GROUP BY b.branch_name

ORDER BY revenue DESC;
SELECT
    p.product_name,
    SUM(s.quantity) AS total_quantity,
    SUM(s.total_amount) AS revenue

FROM sales s

JOIN products p
ON s.product_id = p.product_id

GROUP BY p.product_name

ORDER BY revenue DESC

LIMIT 10;