-- Temperatures #2
-- Import from sql file
source temperatures.sql;
-- List The MAX temperatura GROUP By State
SELECT state, MAX(value) AS 'max_temp' FROM temperatures GROUP BY state;
