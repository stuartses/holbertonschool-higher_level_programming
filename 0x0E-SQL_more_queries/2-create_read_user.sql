-- Creates a new database and user
-- Query to create a new datanbase hbtn_0d_2 and GRANTS SELECT permissions to a new user user_0d_
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
