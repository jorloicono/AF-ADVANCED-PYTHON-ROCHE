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
