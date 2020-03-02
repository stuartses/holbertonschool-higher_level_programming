-- Full creation
-- Query to creates a second table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- Insert id=1, name=Jhon, score=10
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, 'John', 10);
-- Insert id=2, name=Alex, score=3
INSERT INTO second_table (`id`, `name`, `score`) VALUES (2, 'Alex', 3);
-- Insert id=3, name=Bob, score=14
INSERT INTO second_table (`id`, `name`, `score`) VALUES (3, 'Bob', 14);
-- Insert id=4, name=George, score=8
INSERT INTO second_table (`id`, `name`, `score`) VALUES (4, 'George', 8);
