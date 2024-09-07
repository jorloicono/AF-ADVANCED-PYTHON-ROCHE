# # Web Development with Python

# Python offers several frameworks for web development, with Flask and Django being two of the most popular.
# In this notebook, we will introduce Flask and Django, build a basic web application, and demonstrate how to use templates and forms.

# ## 1. Introduction to Flask and Django

# **Flask** and **Django** are both powerful web frameworks for Python. Flask is lightweight and flexible, while Django is a full-featured framework with built-in components.

# ### Flask
# Flask is a micro web framework for Python. It is designed to be simple and easy to use, allowing developers to add components as needed.

# **Key Features of Flask:**
# - Minimalistic and simple
# - Flexible, allowing you to choose your components
# - Good for small to medium-sized applications

# ### Django
# Django is a high-level web framework that encourages rapid development and clean, pragmatic design. It comes with many built-in features.

# **Key Features of Django:**
# - Includes built-in admin interface
# - ORM (Object-Relational Mapping) for database operations
# - Comes with many built-in features, like authentication and form handling

# ## 2. Building a Basic Web Application with Flask

# Let's build a basic web application using Flask. This application will have a simple homepage and a form to collect user input.

# Install Flask (if not already installed)
# !pip install Flask

from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"Hello, {name}!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
  
# index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to the Flask Web Application!</h1>
    <form action="/submit" method="POST">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# ## 3. Building a Basic Web Application with Django

# Django requires more setup compared to Flask. Here’s how to create a basic Django project and app.

# **Step 1: Install Django**
# !pip install Django

# **Step 2: Create a new Django project**
# Open a terminal and run:
# django-admin startproject myproject

# **Step 3: Create a new app within the project**
# cd myproject
# python manage.py startapp myapp

# **Step 4: Set up the app**

# In `myproject/settings.py`, add `'myapp'` to the `INSTALLED_APPS` list.

# **Step 5: Define a simple view and template**

# Create a view in `myapp/views.py`
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Hello, {name}!")
    return render(request, 'index.html')

# **Step 6: Set up URLs**

# In `myapp/urls.py`, define the URL patterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
]

# Include `myapp` URLs in the project URLs (`myproject/urls.py`)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# **Step 7: Create a template**

# Create a file named `index.html` in `myapp/templates/`

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django App</title>
</head>
<body>
    <h1>Welcome to the Django Web Application!</h1>
    <form action="/submit/" method="POST">
        {% csrf_token %}
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# **Step 8: Run the server**
# python manage.py runserver
# # Handling Forms in Flask and Django

# Forms are an essential part of web applications for collecting user input. 
# Both Flask and Django provide tools to handle forms effectively.

# ## 1. Handling Forms in Flask

# Flask does not include form handling features by default, but it can be done using libraries like WTForms.
# For simplicity, we'll use Flask's built-in functionality to demonstrate form handling.

# ### Example: Basic Form Handling in Flask

# The following example demonstrates a basic form handling process using Flask.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for displaying the form
@app.route('/')
def home():
    return render_template('form.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Name: {name}, Email: {email}"

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)

# form.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Form</title>
</head>
<body>
    <h1>Submit Your Information</h1>
    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# ## 2. Handling Forms in Django

# Django provides a more robust system for handling forms through its forms framework. It includes form validation and easy integration with models.

# ### Example: Basic Form Handling in Django

# **Step 1: Create a Form Class**

# Create a file named `forms.py` in your Django app directory (`myapp/forms.py`).

from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')

# **Step 2: Create Views to Handle the Form**

# In `views.py` of your Django app (`myapp/views.py`), add:

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return HttpResponse(f"Name: {name}, Email: {email}")
    else:
        form = UserForm()

    return render(request, 'form.html', {'form': form})

# **Step 3: Update URL Configuration**

# In `urls.py` of your Django app (`myapp/urls.py`), update:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# **Step 4: Create a Template**

# Create a file named `form.html` in `myapp/templates/`.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Form</title>
</head>
<body>
    <h1>Submit Your Information</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>

