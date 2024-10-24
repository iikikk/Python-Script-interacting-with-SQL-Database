# SQL Database Interaction with Python

## Description

A Python script that connects to an SQLite database and performs CRUD operations, including custom SQL queries.

## CI/CD Pipeline
The project uses GitHub Actions to automate testing of database operations on every push. The pipeline:

Loads the existing example.db file into the environment.
Runs the script, which uses the existing database.
Verifies that each CRUD operation works correctly using assertions.
Prints the results of each operation to the pipeline logs for review.

[![Python application](https://github.com/iikikk/Python-Script-interacting-with-SQL-Database/actions/workflows/python-app.yml/badge.svg)](https://github.com/iikikk/Python-Script-interacting-with-SQL-Database/actions/workflows/python-app.yml)

### loading the .db file
![ci](./ci.png)
## Requirements

- Python 3.x

## Usage

1. Clone the repository.
2. Run the script:

   ```bash
   python test.py
## Database connection
Python script has successfully connected to sqlite database.

![connection](./connection.png)
## CRUD Operations
### Create Operation
After inserting the initial data into the employees table, the data is as follows:

![create](./create.png)
### Read Operation
Retrieving all data from the employees table:

![create](./read.png)
### Update Operation
After updating Charlie's department to Sales, the data is:

![update](./update.png)
### Delete Operation
After deleting Bob's record, the data is:

![delete](./delete.png)
## SQL Queries
### Query 1: Employee Count by Department
Counting the number of employees in each department:

![q1](./q1.png)
### Query 2: Employees Whose Names Start with 'A'
Selecting employees whose names start with 'A':

![q2](./q2.png)

