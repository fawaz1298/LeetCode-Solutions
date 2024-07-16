# Time:  O(n)
# Space: O(n)

SELECT a.product_id, 
       ifnull(ROUND(SUM(b.units * a.price) / SUM(b.units), 2),0) AS average_price 
FROM   prices AS a
       left JOIN UnitsSold  AS b
               ON a.product_id = b.product_id 
WHERE  (b.purchase_date BETWEEN a.start_date AND a.end_date ) or b.purchase_date is null
GROUP  BY product_id; 
