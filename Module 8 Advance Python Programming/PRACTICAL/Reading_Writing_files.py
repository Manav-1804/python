"""
Write a Python program to read the contents of a file and print them on the console.
Write a Python program to write multiple strings into a file.
"""


file = open("sample.txt", "w")
file.write("Hello\n")
file.write("Welcome to Python\n")
file.write("File handling example")
file.close()

file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()


print("Multiple strings written to file.")


