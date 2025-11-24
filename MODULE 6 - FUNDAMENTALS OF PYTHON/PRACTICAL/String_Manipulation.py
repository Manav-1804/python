'''
Write a Python program to demonstrate string slicing.
'''

def string_slicing():
    s = "Manav Prajapati 123"

    print("Original String:", s)
    print("First 6 characters:", s[:6])
    print("From index 3 onwards:", s[3:])
    print("Middle part (3 to 10):", s[3:10])
    print("Every 2nd character:", s[::2])
    print("Reverse string:", s[::-1])

string_slicing()

print("*"*40)

'''
Write a Python program that manipulates and prints strings using various string methods.
'''

def string_methods():
    s = "manav prajapati 123"

    print("Original String:", s)
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    print("Title case:", s.title())
    print("Capitalize:", s.capitalize())
    print("Replace '123' with '1808':", s.replace("123", "1808"))
    print("Count of 'o':", s.count('o'))
    print("Find 'py':", s.find('py'))
    print("Is alphabetic:", s.isalpha())
    print("Is alphanumeric:", s.isalnum())
    print("Split string:", s.split())

string_methods()
