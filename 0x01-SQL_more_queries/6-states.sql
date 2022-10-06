-- Create a new table states on new db hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE AUTOINCREMENT NOT NULL PRIMARY KEY, 
    name VARCHAR(256) NOT NULL
);
