# # Advanced Exception Handling in Python

# Python allows us to handle runtime errors using the try-except block.
# In advanced scenarios, we may need to handle multiple exceptions, raise custom exceptions, 
# or use context managers for better resource management.

# ## 1. Creating Custom Exceptions

# Sometimes the built-in exceptions (like ValueError, TypeError) are not sufficient for specific cases,
# so we can create our own custom exception classes by subclassing from Python's built-in `Exception` class.

# ### Example:

# Define a custom exception for invalid age
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} -> {self.message}"

# Function that checks if the given age is valid
def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return f"Age {age} is valid."

# Let's test the custom exception
try:
    print(check_age(150))  # This will raise the custom exception
except InvalidAgeError as e:
    print(e)  # Output: 150 -> Age must be between 0 and 120

# ## 2. Handling Multiple Exceptions

# We can catch and handle multiple exceptions in a single try block using a tuple of exceptions
# or by chaining multiple except blocks.

# ### Example:

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of division: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e} (You cannot divide by zero!)")
    except TypeError as e:
        print(f"Error: {e} (Both inputs must be numbers!)")
    except Exception as e:  # Catch any other exception that may arise
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution finished.")

# Test cases
divide_numbers(10, 2)  # This will work fine
divide_numbers(10, 0)  # This will raise a ZeroDivisionError
divide_numbers(10, "five")  # This will raise a TypeError

# ## 3. Context Managers

# A context manager is a mechanism for resource management.
# For example, it is used to manage file streams and ensure that they are properly closed after use.
# We use the `with` statement in Python to work with context managers.

# ### Example with a file:

# Open a file, write to it, and ensure it is closed automatically
with open("example.txt", "w") as file:
    file.write("This is an example of using context managers.\n")

# At this point, the file is automatically closed, even if an error occurred while working with it.

# ### Custom Context Manager
# We can create a custom context manager using the `__enter__` and `__exit__` methods or using the `contextlib` module.

# Custom context manager using __enter__ and __exit__ methods:

class CustomResource:
    def __enter__(self):
        print("Resource acquired.")
        return self
    
    def do_something(self):
        print("Resource is being used.")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released.")
        # You can handle exceptions here if needed

# Use the custom context manager
with CustomResource() as resource:
    resource.do_something()

# In this example, `__enter__` is called when the `with` block is entered,
# and `__exit__` is called when it is exited, ensuring that resources are properly managed.

# Note: You can handle exceptions inside the __exit__ method as well.

# Here you have one more example: 
# We’ll create a context manager that handles opening and closing two files at the same time and ensures that both files are properly closed, even if an exception occurs during their usage.


class MultiFileHandler:
    def __init__(self, file1_name, file2_name):
        self.file1_name = file1_name
        self.file2_name = file2_name
        self.file1 = None
        self.file2 = None

    def __enter__(self):
        # Trying to open both files
        try:
            self.file1 = open(self.file1_name, 'w')
            print(f"{self.file1_name} opened.")
            self.file2 = open(self.file2_name, 'w')
            print(f"{self.file2_name} opened.")
        except Exception as e:
            # If any file fails to open, we release already opened files
            if self.file1:
                self.file1.close()
                print(f"{self.file1_name} closed due to error.")
            raise e  # Re-raise the exception to be handled outside
        return self

    def write_to_both_files(self, text):
        if self.file1 and self.file2:
            self.file1.write(f"File 1: {text}\n")
            self.file2.write(f"File 2: {text}\n")
        else:
            raise RuntimeError("Files are not open!")

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure both files are properly closed
        if self.file1:
            self.file1.close()
            print(f"{self.file1_name} closed.")
        if self.file2:
            self.file2.close()
            print(f"{self.file2_name} closed.")
        
        # Handle exceptions if any occur
        if exc_type:
            print(f"An exception occurred: {exc_type}, {exc_value}")
            return False  # Propagate exception
        return True  # No exception, normal exit

# Example usage
try:
    with MultiFileHandler("file1.txt", "file2.txt") as handler:
        handler.write_to_both_files("This is some test content.")
        handler.write_to_both_files("Writing more content.")
        # Simulating an error
        raise ValueError("Simulated exception during file operations.")
except Exception as e:
    print(f"Handled exception: {e}")
