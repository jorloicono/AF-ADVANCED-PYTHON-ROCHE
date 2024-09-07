# # Introduction to Databases with Python

# Python provides various ways to interact with databases, including SQL (relational) and NoSQL (non-relational) databases.
# This notebook will cover the basics of connecting to both types, executing queries, and handling transactions.

# ## 1. Connecting to SQL Databases

# SQL databases are relational databases where data is structured in tables.
# Common SQL databases include SQLite, MySQL, and PostgreSQL.
# We'll use SQLite in this example for simplicity as it comes built-in with Python.

import sqlite3

# Establish a connection to an SQLite database
connection = sqlite3.connect('example.db')

# Create a cursor object using the connection
cursor = connection.cursor()

# ## 2. Basic SQL Queries

# ### Creating a Table

# Create a table named 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# ### Inserting Data

# Insert a new user into the 'users' table
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

# ### Querying Data

# Select all users from the 'users' table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

# ### Updating Data

# Update a user's age
cursor.execute('''
    UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))

# ### Deleting Data

# Delete a user
cursor.execute('DELETE FROM users WHERE name = ?', ('Alice',))

# ## 3. Transaction Handling

# Transactions ensure that a series of database operations are executed as a single unit.
# If an error occurs, the transaction can be rolled back to maintain data integrity.

# Start a transaction
connection.execute('BEGIN')

try:
    # Perform some operations
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Charlie', 35))

    # Commit the transaction
    connection.commit()
    print("Transaction committed successfully.")
except Exception as e:
    # Rollback in case of error
    connection.rollback()
    print(f"Transaction rolled back due to: {e}")

# ## 4. Connecting to NoSQL Databases

# NoSQL databases are non-relational and include document stores, key-value stores, and column-family stores.
# We'll use MongoDB as an example of a document-based NoSQL database.

from pymongo import MongoClient

# Connect to a MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Select a database
db = client['example_db']

# Select a collection (similar to a table in SQL)
collection = db['users']

# ## 5. Basic NoSQL Queries

# ### Inserting Data

# Insert a new document into the 'users' collection
collection.insert_one({'name': 'Alice', 'age': 30})

# ### Querying Data

# Find all documents in the 'users' collection
documents = collection.find()

print("Users in MongoDB:")
for doc in documents:
    print(doc)

# ### Updating Data

# Update a user's age
collection.update_one({'name': 'Alice'}, {'$set': {'age': 31}})

# ### Deleting Data

# Delete a user
collection.delete_one({'name': 'Alice'})

# ## 6. Closing Connections

# It's important to close connections to free up resources.

# Close SQLite connection
connection.close()

# Close MongoDB connection
client.close()
