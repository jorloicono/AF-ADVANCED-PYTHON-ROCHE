# # Advanced Functional Programming in Python

# Python provides several powerful functional programming features, such as higher-order functions,
# decorators, generators, and lambda functions. These are useful for creating concise, reusable code.

# ## 1. Decorators
# Decorators are a design pattern that allows you to modify the behavior of a function or method.
# A decorator is a higher-order function that takes another function and extends its behavior without explicitly modifying it.

# Here's a basic example to illustrate how decorators work:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# ### Example 2: A simple decorator that logs the execution time of a function.

import time

# Define a decorator that logs the execution time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

# Use the decorator to wrap a function
@timer_decorator
def slow_function():
    time.sleep(2)  # Simulate a slow function
    print("Slow function completed.")

# Call the decorated function
slow_function()

# The `@timer_decorator` syntax is equivalent to calling:
# slow_function = timer_decorator(slow_function)

# The decorator adds the extra functionality of logging the time without changing the original `slow_function`.

# ## 2. Generators
# Generators are a special kind of iterator in Python that allow you to iterate over data without storing it in memory.
# They are defined using functions and the `yield` keyword.

# ### Example: A simple generator that yields squares of numbers

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i  # This generates squares lazily

# Create a generator
squares = square_generator(5)

# Iterate over the generator
for square in squares:
    print(square)

# Note: A generator doesn't store values in memory; instead, it produces them one by one on demand.
# This is useful for handling large datasets.

# Generators can also be used to model infinite sequences:

# ### Example: An infinite generator for Fibonacci numbers

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a  # Yield the current value of `a`
        a, b = b, a + b  # Update `a` and `b` for the next iteration

# Create a generator
fib_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

# The `fibonacci_generator` function generates an infinite sequence of Fibonacci numbers.
# You can control how many numbers to generate by calling `next()` on the generator.

# ## 3. Advanced Lambda Functions

# Lambda functions in Python are anonymous (i.e., they don't have a name).
# They are often used when a short, throwaway function is needed.

# ### Basic Example:
# A lambda function for adding two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# ### Advanced Example: Sorting with a lambda function
# Lambda functions are often used as key functions in sorting.

# List of tuples (name, score)
students = [("Alice", 85), ("Bob", 75), ("Charlie", 95)]

# Sort by the second element (score) using a lambda function
students_sorted = sorted(students, key=lambda student: student[1])

print(students_sorted)  # Output: [('Bob', 75), ('Alice', 85), ('Charlie', 95)]

# ### Example: Using lambda with `map`, `filter`, and `reduce`

# 1. `map` applies a function to all items in an iterable

numbers = [1, 2, 3, 4, 5]

# Using map to square each number
squared_numbers = list(map(lambda x: x * x, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 2. `filter` selects items from an iterable based on a condition

# Using filter to select only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4]

# 3. `reduce` (from `functools`) is used to apply a function cumulatively to items in an iterable, reducing it to a single value

from functools import reduce

# Using reduce to find the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120

# Lambda functions are particularly useful for writing small functions in-line, making the code more concise and readable.
