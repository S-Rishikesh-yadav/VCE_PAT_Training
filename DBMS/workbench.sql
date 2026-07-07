CREATE DATABASE pythoncompanydb;
USE pythoncompanydb;
CREATE TABLE employee(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2)
);
DESC employee;
Select * from employee;