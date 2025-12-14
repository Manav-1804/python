#Write a Python program to read a name and age from the user and print a formatted output.

name = input("Enter Your Name : ")

age = int(input("Enter Your Age : "))
print("-"*80)
print(f"Name : {name}")
print(f"Age : {age}")
print("-"*80)
print(f"{name} is {age} years old.")
