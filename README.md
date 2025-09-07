Polymorphism with Inheritance Example
📌 Overview

This project demonstrates the concept of polymorphism in Object-Oriented Programming (OOP) using Python.
Polymorphism allows different classes to define methods with the same name but with different behaviors.

In this example, multiple classes (Car, Plane, Dog, and Fish) inherit from a base class Mover and override the move() method in their own unique way.

🧑‍💻 Code Explanation

Mover (Base Class):
Defines a general method move(). If a subclass does not implement this method, a NotImplementedError will be raised.

Subclasses (Car, Plane, Dog, Fish):
Each class inherits from Mover and overrides the move() method with its own implementation.

Car.move() → "Driving 🚗"

Plane.move() → "Flying ✈️"

Dog.move() → "Running 🐕"

Fish.move() → "Swimming 🐟"

Polymorphism in Action:
A list of objects is created, and the same method move() is called on each. The correct method is executed depending on the object’s type.

▶️ How to Run

Save the code in a file, e.g., polymorphism.py.

Run the file using Python:

python polymorphism.py

✅ Expected Output
Driving 🚗
Flying ✈️
Running 🐕
Swimming 🐟

🎯 Key Concept

Polymorphism: Same method name (move()), different implementations across classes.

Inheritance: All subclasses derive from the base class Mover.

Method Overriding: Each subclass provides its own version of the move() method.
