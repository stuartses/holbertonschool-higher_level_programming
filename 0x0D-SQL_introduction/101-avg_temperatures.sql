-- Temperatures #0
-- List Average Temperatures order by temperature and city
SELECT city, AVG(value) AS "avg_temp" FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
