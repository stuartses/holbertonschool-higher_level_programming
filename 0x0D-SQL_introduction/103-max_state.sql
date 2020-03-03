-- Temperatures #2
-- List The MAX temperatura GROUP By State
SELECT state, MAX(value) AS 'max_temp' FROM temperatures GROUP BY state;
