import json

# JSON string representing some data
datos_JSON = """
{
    "tamano": "mediana",
    "precio": 15.67,
    "toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
    "cliente": {
        "nombre": "Jane Doe",
        "telefono": "455-344-234",
        "correo": "janedoe@email.com"
    }
}
"""

# Convert the JSON string into a Python dictionary
datos_diccionario = json.loads(datos_JSON)

# Print the values extracted from the dictionary
print("Size:", datos_diccionario["tamano"])
print("Price:", datos_diccionario["precio"])
print("Toppings:", datos_diccionario["toppings"])
print("Customer:", datos_diccionario["cliente"])

# Python dictionary representing a customer
cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}

# Convert the Python dictionary to a JSON string
cliente_JSON = json.dumps(cliente)
print("\nCustomer in JSON (no formatting):", cliente_JSON)

# Convert the dictionary to a JSON string with indentation for readability
cliente_JSON = json.dumps(cliente, indent=4)
print("\nCustomer in JSON (formatted):", cliente_JSON)

# Convert the dictionary to a JSON string with sorted keys and indentation
cliente_JSON = json.dumps(cliente, sort_keys=True, indent=4)
print("\nCustomer in JSON (sorted keys and formatted):", cliente_JSON)

# Sample JSON data for the file (you should create this file beforehand)
ordenes_json = """
{
    "ordenes": [
        {
            "tamano": "mediana",
            "precio": 15.67,
            "toppings": ["champinones", "pepperoni", "albahaca"],
            "queso_extra": false,
            "delivery": true,
            "cliente": {
                "nombre": "Jane Doe",
                "telefono": null,
                "correo": "janedoe@email.com"
            }
        },
        {
            "tamano": "pequena",
            "precio": 6.54,
            "toppings": null,
            "queso_extra": true,
            "delivery": false,
            "cliente": {
                "nombre": "Foo Jones",
                "telefono": "556-342-452",
                "correo": null
            }
        }
    ]
}
"""

# Write the JSON data to a file named "ordenes.json"
with open("ordenes.json", 'w') as file:
    file.write(ordenes_json)

# Read the JSON data from the file
with open("ordenes.json") as file:
    data = json.load(file)

# Print the number of orders in the file
print(len(data["ordenes"]))

# Print the toppings of the first order
print(data["ordenes"][0]["toppings"])

# Print the entire data read from the file
print(data)

# Modify the JSON data: Remove the "cliente" key from each order
for order in data["ordenes"]:
    del order["cliente"]

# Write the modified data back to the same file
with open("ordenes.json", 'w') as file:
    json.dump(data, file, indent=4)

# ## CSV Files

# CSV (Comma-Separated Values) files are commonly used for storing tabular data.
# Python’s `csv` module provides functionalities to read from and write to CSV files.

# ### Example: Reading a CSV file

import csv

# Sample CSV file content:
# name,age,city
# Alice,30,New York
# Bob,25,Los Angeles
# Charlie,35,Chicago

# Read CSV file
with open('sample.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Read the header row
    print(f"Headers: {headers}")
    
    for row in csv_reader:
        print(f"Row: {row}")

# ### Example: Writing to a CSV file

data = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    
print("CSV file 'output.csv' created with data.")

##Example with Pandas

# name,age,city,email
# Alice,28,New York,alice@example.com
# Bob,34,Los Angeles,bob@example.com
# Charlie,29,Chicago,charlie@example.com
# David,40,New York,david@example.com
# Eva,22,San Francisco,eva@example.com

# Import the necessary libraries
import pandas as pd

# Read a CSV file into a DataFrame
# Assuming 'data.csv' is the CSV file located in the same directory
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame to understand its structure
print("First few rows of the DataFrame:")
print(df.head())

# Show basic information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Show basic statistics of the DataFrame
print("\nBasic Statistics:")
print(df.describe())

# Filter rows based on a condition
# Example: Filtering rows where the value in the 'age' column is greater than 30
filtered_df = df[df['age'] > 30]

print("\nFiltered DataFrame (age > 30):")
print(filtered_df)

# Sort the DataFrame based on a column
# Example: Sorting by the 'name' column
sorted_df = df.sort_values(by='name')

print("\nSorted DataFrame by 'name':")
print(sorted_df)

# Add a new column to the DataFrame
# Example: Adding a 'new_column' with default value 0
df['new_column'] = 0

print("\nDataFrame with new column:")
print(df.head())

# Write the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)

print("\nModified DataFrame has been saved to 'modified_data.csv'.")

# ## Compressed Files

# Compressed files can reduce file size, and Python provides modules to handle compressed files.
# Common formats include ZIP and GZIP.

# ### Example: Working with ZIP Files

import zipfile

# Creating a ZIP file
with zipfile.ZipFile('sample.zip', 'w') as zipf:
    zipf.write('output.csv')  # Add the CSV file to the ZIP archive
    
print("ZIP file 'sample.zip' created.")

# Extracting from a ZIP file
with zipfile.ZipFile('sample.zip', 'r') as zipf:
    zipf.extractall('extracted_files')  # Extract to a directory
    
print("ZIP file 'sample.zip' extracted to 'extracted_files' directory.")
