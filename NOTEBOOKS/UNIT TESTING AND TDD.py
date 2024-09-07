# # Unit Testing and Test Driven Development (TDD) in Python

# Unit testing is a software testing technique where individual units or components of a software are tested.
# Test Driven Development (TDD) is a methodology where tests are written before the code that needs to be tested.

# ## 1. Basics of Unit Testing

# Unit testing involves writing tests to check the functionality of small, isolated pieces of code, usually functions or methods.
# Python's `unittest` module is a built-in framework that supports test case creation, test execution, and test result reporting.

# ### Example:

import unittest

# Function to be tested
def add(a, b):
    return a + b

# Unit test class
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # Test cases for the add function
        self.assertEqual(add(1, 2), 3)  # Check if 1 + 2 equals 3
        self.assertEqual(add(-1, -1), -2)  # Check if -1 + -1 equals -2
        self.assertEqual(add(0, 0), 0)  # Check if 0 + 0 equals 0

    def test_add_floats(self):
        # Additional test case for floating point numbers
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)  # Check if 1.5 + 2.5 equals 4.0

# To run the tests, use the following command in the terminal or command prompt:
# python -m unittest <name_of_this_file>.py

# The test results will show if the tests passed or failed, and if any errors occurred.

# ## 2. Creating and Running Tests

# To create tests, define a class inheriting from `unittest.TestCase`, and write methods with names starting with `test_`.
# Each method represents a separate test case. Use assertion methods like `assertEqual`, `assertTrue`, `assertFalse` to verify expected outcomes.

# ### Example:

# Function to be tested
def multiply(a, b):
    return a * b

# Unit test class
class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)  # Check if 3 * 4 equals 12
        self.assertEqual(multiply(-1, 5), -5)  # Check if -1 * 5 equals -5
        self.assertEqual(multiply(0, 100), 0)  # Check if 0 * 100 equals 0

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)  # Check if 2.5 * 4.0 equals 10.0

# Running the tests
if __name__ == '__main__':
    unittest.main()

# Running this script will execute all test cases in the TestMathOperations class.

# ## 3. Test Driven Development (TDD) as a Development Methodology

# TDD is a development methodology where you write tests before writing the actual code. The typical TDD cycle involves:
# 1. **Write a Test**: Create a test for a new feature or bug fix.
# 2. **Run the Test**: Run the test and see it fail (since the feature or fix isn't implemented yet).
# 3. **Write the Code**: Implement the code to make the test pass.
# 4. **Run the Test Again**: Ensure the test passes with the new code.
# 5. **Refactor**: Clean up the code while ensuring that all tests still pass.
# 6. **Repeat**: Continue this cycle for each new feature or bug fix.

# ### Example of TDD:

import unittest

# Define the BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_balance(self):
        return self.balance

# Define a unit test class for BankAccount
class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)  # Initial balance should be 0

    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)  # Balance should be 100 after deposit

    def test_withdrawal(self):
        account = BankAccount()
        account.deposit(200)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 150)  # Balance should be 150 after withdrawal

    def test_withdrawal_exceeds_balance(self):
        account = BankAccount()
        account.deposit(100)
        with self.assertRaises(ValueError):  # Should raise an error if withdrawing more than balance
            account.withdraw(150)

    def test_deposit_negative_amount(self):
        account = BankAccount()
        with self.assertRaises(ValueError):  # Should raise an error for negative deposit amount
            account.deposit(-50)

    def test_withdrawal_negative_amount(self):
        account = BankAccount()
        account.deposit(100)
        with self.assertRaises(ValueError):  # Should raise an error for negative withdrawal amount
            account.withdraw(-30)

if __name__ == '__main__':
    unittest.main()

