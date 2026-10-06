# Student Management System

A simple Student Management System built with raw Python, Object-Oriented Programming, MVC architecture, MySQL, HTML, and CSS.

This project is developed without using web frameworks such as Flask, Django, or FastAPI. The main purpose is to understand how a basic web application works internally, including HTTP requests, routing, controllers, models, database operations, HTML rendering, and CRUD operations.

## Features

- Student listing
- View student details
- Add new student
- Edit student information
- Delete student
- MySQL database integration
- Object-Oriented Programming
- MVC architecture
- Basic HTML template rendering
- Static CSS file serving
- Basic HTTP routing
- Form handling using GET and POST requests

## Technologies

- Python 3
- MySQL
- HTML5
- CSS3
- mysql-connector-python
- Python http.server
- Object-Oriented Programming
- MVC Architecture

## Project Structure

```text
student_management/
├── App.py
├── Config.py
│
├── Controller/
│   ├── __init__.py
│   └── StudentManagement.py
│
├── Model/
│   ├── __init__.py
│   └── Student.py
│
├── Public/
│   ├── Style/
│   │   └── style.css
│   └── Images/
│
└── View/
    ├── Layout/
    │   └── App.html
    ├── Index.html
    ├── Show.html
    ├── Create.html
    └── Edit.html
```

## Requirements

Before running the project, make sure you have:

- Python 3 installed
- MySQL Server installed and running
- A MySQL database
- mysql-connector-python installed

## Installation

1. Clone or download the project.
2. Open your terminal and move into the project directory.

```bash
cd student_management
```

3. Install the Python dependency.

```bash
pip install mysql-connector-python
```

4. Create the database.

Open MySQL and run:

```sql
CREATE DATABASE student_management;

USE student_management;
```

5. Create the students table.

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    age INT NOT NULL,
    department VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

6. Add test data.

You can insert some sample students:

```sql
INSERT INTO students
(name, email, age, department)
VALUES
('Nayan', 'nayan@example.com', 26, 'AI & ML'),
('Rahim', 'rahim@example.com', 24, 'Computer Science'),
('Karim', 'karim@example.com', 25, 'Software Engineering');
```

## Database Configuration

Open `Config.py` and configure your MySQL connection:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "student_management"
}
```

Change the username, password, host, or database name according to your MySQL configuration.

## Run the Application

From the project root directory:

```bash
python App.py
```

If everything is configured correctly, you should see:

```text
=================================
Student Management System
Server running at:
http://localhost:8000
=================================
```

Open the following URL in your browser:

`http://localhost:8000`