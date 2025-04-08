CREATE DATABASE IF NOT EXISTS kastro_exam_db;

USE kastro_exam_db;

CREATE TABLE IF NOT EXISTS exam_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(100),
    tool VARCHAR(50),
    score INT
);
