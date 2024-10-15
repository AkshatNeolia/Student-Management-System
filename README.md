
# Student Management System

## Overview

The **Student Management System** is a Python application designed to manage student records using a graphical user interface (GUI) built with **Tkinter** and a **MySQL** database. This project allows users to register students, display records, and delete entries seamlessly.

## Features

- Register new students with their details (name, contact, email, roll number, branch, teacher ID, and course ID).
- View all registered students in a structured table format.
- Delete student records with a confirmation prompt.
- User-friendly interface with full-screen mode and organized layout.

## Technologies Used

- **Python**: The primary programming language used for the application.
- **Tkinter**: A standard GUI toolkit for Python that provides an easy way to create windows, buttons, and other UI elements.
- **MySQL**: A relational database management system used to store and manage student records.
- **mysql-connector-python**: A Python library to connect to MySQL databases and execute SQL queries.

## Installation

To set up and run the Student Management System, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed. Then, install the required packages using pip:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set Up MySQL Database**:
   - Ensure that you have MySQL installed and running on your machine.
   - Create a database named `student_registration_db` using the following command in the MySQL shell:
     ```sql
     CREATE DATABASE student_registration_db;
     ```
   - Update the database connection details in the code if necessary (host, user, password).

4. **Run the Application**:
   Execute the following command to start the application:
   ```bash
   python your_script_name.py
   ```
   Replace `your_script_name.py` with the name of your main Python file.

## How It Works

- The application connects to the MySQL database using `mysql.connector` to perform operations such as inserting, retrieving, and deleting student records.
- The GUI is created using Tkinter, allowing users to interact with the application visually. Users can input data into various fields, which will be saved to the database upon submission.
- The application features a tree view to display student records dynamically, and actions can be performed using buttons provided in the interface.

 ## Screenshots

 ![Sms](https://github.com/user-attachments/assets/aac91b36-03a0-474a-9bcc-e7a213060802)
 ![Sms2](https://github.com/user-attachments/assets/6f77c167-95e6-436e-b022-e25c36a0807e)


 

 

