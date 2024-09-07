# # Regular Expressions in Python

# Regular expressions (regex) are a powerful tool for matching patterns in text.
# Python's `re` module provides support for working with regular expressions.

import re

# ## 1. Basic Syntax

# Regular expressions consist of patterns that define sets of strings.
# Some of the most commonly used patterns are:
# - `.`: Matches any character except a newline
# - `\d`: Matches any digit (0-9)
# - `\D`: Matches any non-digit character
# - `\w`: Matches any word character (alphanumeric + underscore)
# - `\W`: Matches any non-word character
# - `\s`: Matches any whitespace character
# - `\S`: Matches any non-whitespace character
# - `*`: Matches 0 or more repetitions of the preceding character
# - `+`: Matches 1 or more repetitions of the preceding character
# - `?`: Matches 0 or 1 repetition of the preceding character
# - `{n}`: Matches exactly `n` repetitions of the preceding character
# - `^`: Anchors the match to the start of the string
# - `$`: Anchors the match to the end of the string

# ### Example of basic regex patterns:

text = "Hello, my name is John and I am 30 years old."

# Find all words in the text using \w+
words = re.findall(r'\w+', text)
print("Words:", words)

# Find all digits using \d+
digits = re.findall(r'\d+', text)
print("Digits:", digits)

# Search for a word starting with 'J'
match = re.search(r'\bJ\w+', text)  # \b denotes a word boundary
if match:
    print(f"Found word starting with 'J': {match.group()}")

# Search for the start of a sentence using ^
if re.match(r'^Hello', text):
    print("The text starts with 'Hello'.")

# ## 2. Text Search and Manipulation

# Regular expressions are often used to search for text patterns, replace them, or manipulate the text.

# ### Example 1: Searching for patterns
email_text = "Please contact us at support@example.com for more info."

# Extract the email from the text
email_match = re.search(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', email_text)
if email_match:
    print("Found email:", email_match.group())

# ### Example 2: Replacing text
sentence = "The quick brown fox jumps over the lazy dog."

# Replace all occurrences of 'dog' with 'cat'
new_sentence = re.sub(r'dog', 'cat', sentence)
print("Modified sentence:", new_sentence)

# ### Example 3: Splitting text
# Split the sentence into words using a regular expression for spaces
words = re.split(r'\s+', sentence)
print("Split words:", words)

# ## 3. Practical Applications

# Regular expressions are used in many real-world tasks such as:
# - Validating user input (email, phone numbers)
# - Extracting specific information (such as dates, URLs)
# - Cleaning text data
# - Searching through large text files

# ### Practical Example 1: Validating Email Addresses

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w{2,4}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the email validator
emails = ["user@example.com", "invalid-email", "john.doe@domain.co"]
for email in emails:
    if validate_email(email):
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")

# ### Practical Example 2: Validating Phone Numbers

def validate_phone_number(phone_number):
    # This pattern matches phone numbers in the format (123) 456-7890 or 123-456-7890
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone_number))

# Test the phone number validator
phone_numbers = ["(123) 456-7890", "123-456-7890", "456-7890", "1234567890"]
for number in phone_numbers:
    if validate_phone_number(number):
        print(f"Valid phone number: {number}")
    else:
        print(f"Invalid phone number: {number}")

# ### Practical Example 3: Extracting Dates from Text

date_text = "We have a meeting scheduled on 2024-09-07 and another one on 09/10/2024."

# Regular expression for matching dates in YYYY-MM-DD or MM/DD/YYYY format
date_pattern = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b'

dates = re.findall(date_pattern, date_text)
print("Extracted dates:", dates)

# ### Practical Example 4: Removing Special Characters from Text

dirty_text = "Hello! Welcome to @Python_101. Let's clean this #text?"

# Remove all non-alphanumeric characters (excluding spaces)
clean_text = re.sub(r'[^\w\s]', '', dirty_text)
print("Cleaned text:", clean_text)
