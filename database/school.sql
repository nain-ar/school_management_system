CREATE DATABASE IF NOT EXISTS school_management;

USE school_management;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Admin','Teacher','Student','Parent') NOT NULL,
    status ENUM('Active','Inactive') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE students (

student_id INT AUTO_INCREMENT PRIMARY KEY,

admission_no VARCHAR(20) UNIQUE NOT NULL,

first_name VARCHAR(50) NOT NULL,

last_name VARCHAR(50),

gender ENUM('Male','Female','Other'),

dob DATE,

phone VARCHAR(15),

email VARCHAR(100),

address TEXT,

class_name VARCHAR(20),

section VARCHAR(10),

roll_no VARCHAR(10),

admission_date DATE,

photo VARCHAR(255),

qr_code VARCHAR(255),

status ENUM('Active','Inactive') DEFAULT 'Active',

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject VARCHAR(50),
    qualification VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    photo VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE parents (
    parent_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    father_name VARCHAR(100),
    mother_name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    address TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
);