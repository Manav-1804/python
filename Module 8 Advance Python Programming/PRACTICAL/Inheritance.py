#Write Python programs to demonstrate different types of inheritance (single, multiple,multilevel, etc.).

#1)Single Inheritance

class Mobile:
    def call(self):
        print("Calling...")

class Smartphone(Mobile):
    def internet(self):
        print("Using Internet")

obj = Smartphone()
obj.call()
obj.internet()


#2)Multiple Inheritance

print("-"*80)

class Student:
    def study(self):
        print("Studying")

class Athlete:
    def play(self):
        print("Playing Sports")

class Person(Student, Athlete):
    def info(self):
        print("Student and Athlete")

p = Person()
p.study()
p.play()
p.info()

#3)Multilevel Inheritance

print("-"*80)


class Food:
    def type(self):
        print("Food Item")

class Restaurant(Food):
    def restaurant(self):
        print("From Restaurant")

class Delivery(Restaurant):
    def deliver(self):
        print("Delivered to Home")

obj = Delivery()
obj.type()
obj.restaurant()
obj.deliver()

#4)Hierarchical Inheritance

print("-"*80)


class Teacher:
    def teach(self):
        print("Teaching")

class MathTeacher(Teacher):
    def math(self):
        print("Teaching Math")

class ScienceTeacher(Teacher):
    def science(self):
        print("Teaching Science")

m = MathTeacher()
s = ScienceTeacher()

m.teach()
m.math()

s.teach()
s.science()

#5)Hybrid Inheritance

print("-"*80)

class Character:
    def move(self):
        print("Moving")

class Fighter(Character):
    def fight(self):
        print("Fighting")

class Wizard(Character):
    def magic(self):
        print("Casting Spell")

class Hero(Fighter, Wizard):
    def hero(self):
        print("Ultimate Hero")

h = Hero()
h.move()
h.fight()
h.magic()
h.hero()


