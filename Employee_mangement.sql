CREATE DATABASE IF NOT EXISTS staff_records;


USE staff_records;


CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    position VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);

INSERT INTO employees (name, email, position, salary) VALUES 
('Aarav Sharma', 'aarav.sharma@example.com', 'Software Developer', 65000.00),
('Isha Singh', 'isha.singh@example.com', 'Marketing Manager', 72000.00),
('Rajesh Kumar', 'rajesh.kumar@example.com', 'Data Scientist', 80000.00),
('Sneha Patel', 'sneha.patel@example.com', 'HR Executive', 54000.00),
('Vikram Joshi', 'vikram.joshi@example.com', 'Operations Manager', 90000.00);

select * from employee;
