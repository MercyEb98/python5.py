# Polymorphism with Inheritance Example

class Mover:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Mover):
    def move(self):
        print("Driving 🚗")

class Plane(Mover):
    def move(self):
        print("Flying ✈️")

class Dog(Mover):
    def move(self):
        print("Running 🐕")

class Fish(Mover):
    def move(self):
        print("Swimming 🐟")

# Test polymorphism
objects = [Car(), Plane(), Dog(), Fish()]

for obj in objects:
    obj.move()
