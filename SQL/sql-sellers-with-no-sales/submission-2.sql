-- Write your query below
-- Write a query to find the names of all sellers who did not make any sales in the year 2020.
SELECT s.seller_name
FROM seller s
WHERE s.seller_id NOT IN (
    SELECT DISTINCT(o.seller_id)
    FROM orders o
    WHERE extract(year from o.sale_date) = '2020'
)
ORDER BY s.seller_name ASC
