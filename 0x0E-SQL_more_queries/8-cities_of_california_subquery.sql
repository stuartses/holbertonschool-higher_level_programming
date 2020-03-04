-- Create Database and Table
-- List cities Where state_id corresponds to California id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id;
