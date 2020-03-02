-- Temperatures #0
-- Import from sql file
source temperatures.sql;
-- List AVG temperatures GRUOP by city for 7 and 8 months. Order By Top temperatures and show the first Three
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
