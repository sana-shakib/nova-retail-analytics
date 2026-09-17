-- ==========================================
-- PRODUCT ANALYSIS
-- Nova Retail Group
-- ==========================================

-- 1. Total Products
SELECT
    COUNT(*) AS total_products
FROM products;

-- 2. Active & Inactive Products
SELECT
    status,
    COUNT(*) AS total_products
FROM products
GROUP BY status
ORDER BY total_products DESC;

-- 3. Top 10 Best Selling Products
SELECT
    p.product_id,
    p.product_name,
    SUM(s.quantity) AS total_quantity_sold,
    SUM(s.total_amount) AS total_revenue
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_revenue DESC
LIMIT 10;

-- 4. Lowest Selling Products
SELECT
    p.product_id,
    p.product_name,
    SUM(s.quantity) AS total_quantity_sold
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_quantity_sold ASC
LIMIT 10;

-- 5. Average Product Price
SELECT
    AVG(price) AS average_price
FROM products;

-- 6. Most Expensive Products
SELECT
    product_name,
    price
FROM products
ORDER BY price DESC
LIMIT 10;

-- 7. Cheapest Products
SELECT
    product_name,
    price
FROM products
ORDER BY price ASC
LIMIT 10;

-- 8. Gross Profit Per Product
SELECT
    product_name,
    price,
    cost,
    (price - cost) AS profit_per_unit
FROM products
ORDER BY profit_per_unit DESC;

-- 9. Inventory Status
SELECT
    p.product_name,
    i.stock_quantity,
    i.reorder_level
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
ORDER BY i.stock_quantity ASC;

-- 10. Products That Need Reordering
SELECT
    p.product_name,
    i.stock_quantity,
    i.reorder_level
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
WHERE i.stock_quantity <= i.reorder_level
ORDER BY i.stock_quantity;