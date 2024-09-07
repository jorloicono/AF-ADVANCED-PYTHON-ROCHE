# # Object-Oriented Programming (OOP) Concepts in Python

# ## 1. Inheritance
# Inheritance is the process by which one class can acquire the properties and methods of another class.
# The new class is called a derived class or child class, and the existing class is called a base class or parent class.
# It allows for code reusability.

# ### Example:

# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (Child)
class Dog(Animal):
    def __init__(self, name, breed):
        # Use super() to call the parent class constructor
        super().__init__(name)
        self.breed = breed

    # Override the speak method
    def speak(self):
        return f"{self.name}, the {self.breed}, barks."

# Derived class (Child)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # Override the speak method
    def speak(self):
        return f"{self.name}, the {self.color} cat, meows."

# Creating objects of the derived classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "white")

# Calling the overridden methods
print(dog.speak())  # Output: Buddy, the Golden Retriever, barks.
print(cat.speak())  # Output: Whiskers, the white cat, meows.

# Notice that both Dog and Cat classes inherited properties from the Animal class

# ## 2. Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common base class.
# It provides the ability to define a method in the base class and override it in the derived class, 
# with the same interface but different functionality.

# ### Example:

# Let's create a function that accepts any object derived from the Animal class and calls the speak method.

def animal_speak(animal):
    # This will call the speak method defined in the corresponding class (Dog or Cat)
    print(animal.speak())

# Even though both dog and cat are from different classes (Dog, Cat), we can use them interchangeably
animal_speak(dog)  # Output: Buddy, the Golden Retriever, barks.
animal_speak(cat)  # Output: Whiskers, the white cat, meows.

# Here, dog and cat objects have different implementations of the speak method,
# yet the same function (animal_speak) can handle both, which is an example of polymorphism.

# ## 3. Abstraction
# Abstraction is the concept of hiding the internal details and showing only the necessary features of an object.
# In Python, abstraction can be achieved by using abstract base classes (ABC module).
# An abstract class cannot be instantiated and requires subclasses to implement its abstract methods.

from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Abstract method
    @abstractmethod
    def start_engine(self):
        pass

# Concrete subclass 1
class Car(Vehicle):
    def start_engine(self):
        return f"The engine of the car {self.make} {self.model} starts with a key."

# Concrete subclass 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return f"The engine of the motorcycle {self.make} {self.model} starts with a button."

# Now let's instantiate the subclasses
car = Car("Toyota", "Corolla")
motorcycle = Motorcycle("Harley-Davidson", "Street 750")

# Call the start_engine method for both vehicles
print(car.start_engine())        # Output: The engine of the car Toyota Corolla starts with a key.
print(motorcycle.start_engine()) # Output: The engine of the motorcycle Harley-Davidson Street 750 starts with a button.

# Note: We cannot instantiate the Vehicle class directly
# vehicle = Vehicle("Generic", "Model")  # This will throw an error because Vehicle is abstract
