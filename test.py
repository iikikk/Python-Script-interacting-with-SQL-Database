import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )
''')

# Insert data into the table (Create)
cursor.execute('''
    INSERT INTO employees (name, department)
    VALUES ('Alice', 'HR'), ('Bob', 'Engineering'), ('Charlie', 'Marketing')
''')
conn.commit()

# Print the data after insertion (Create)
print("Data after insertion (Create):")
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Read data from the table (Read)
print("\nData retrieved (Read):")
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update a record
cursor.execute('''
    UPDATE employees
    SET department = 'Sales'
    WHERE name = 'Charlie'
''')
conn.commit()

# Print the data after update (Update)
print("\nData after update (Update):")
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Delete a record
cursor.execute('''
    DELETE FROM employees
    WHERE name = 'Bob'
''')
conn.commit()

# Print the data after deletion (Delete)
print("\nData after deletion (Delete):")
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

# First custom SQL query: Count the number of employees in each department
print("\nEmployee count by department:")
cursor.execute('''
    SELECT department, COUNT(*) FROM employees GROUP BY department
''')
dept_counts = cursor.fetchall()
for dept in dept_counts:
    print(dept)

# Second custom SQL query: Select employees whose names start with 'A'
print("\nEmployees whose names start with 'A':")
cursor.execute('''
    SELECT * FROM employees WHERE name LIKE 'A%'
''')
a_names = cursor.fetchall()
for employee in a_names:
    print(employee)

# Close the connection
conn.close()
