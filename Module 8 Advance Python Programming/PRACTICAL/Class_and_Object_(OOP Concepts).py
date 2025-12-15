#Write a Python program to create a class and access its properties using an object.

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


s1 = Student("Manav", 20, "Ahmedabad")


print("Name:", s1.name)
print("Age:", s1.age)
print("City:",s1.city)

