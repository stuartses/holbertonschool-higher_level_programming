-- List data from two tables
-- List cities by id, name and state.name
SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id;
