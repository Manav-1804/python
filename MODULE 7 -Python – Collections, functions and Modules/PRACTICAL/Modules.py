#Write a Python program to import the math module and use functions like sqrt(), ceil(),floor().

import math

num = 10.6

print("Square Root:", math.sqrt(25))
print("Ceil Value:", math.ceil(num))
print("Floor Value:", math.floor(num))


#Write a Python program to generate random numbers using the random module.

print("-"*80)
import random

print("Random Integer (1 to 10):", random.randint(1, 10))
print("Random Float (0 to 1):", random.random())
print("Random Choice from list:", random.choice([10, 20, 30, 40, 50]))

