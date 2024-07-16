# Time:  O(n)
# Space: O(n)

SELECT b.product_id, 
       ROUND(SUM(a.units * b.price) / SUM(a.units), 2) AS average_price 
FROM   Prices AS b 
       INNER JOIN UnitsSold AS a
               ON a.product_id = b.product_id 
WHERE  a.purchase_date BETWEEN b.start_date AND b.end_date 
GROUP  BY product_id; 
