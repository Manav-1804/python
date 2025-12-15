#Write Python programs to demonstrate method overloading and method overriding.

class Calculator:
    def add(self, a, b=0, c=0):
        print("Sum:", a + b + c)

obj = Calculator()
obj.add(5)
obj.add(5, 10)
obj.add(5, 10, 15)

print("-"*80)

class Vehicle:
    def run(self):
        print("Vehicle is running")

class Bike(Vehicle):
    def run(self):
        super().run()
        print("Bike is running fast")

b = Bike()
b.run()
