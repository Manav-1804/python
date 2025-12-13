#Write a Python program to create a function that takes a string as input and prints it.

def print_string(s):

    print("Your Name : ",s)

print_string("Manav Prajapati")

#Write a Python program to create a calculator using functions.
print("-"*90)
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

x=int(input("Enter the number of X : "))
y=int(input("Enter the number of y : "))

print("-"*90)
print("Addition : ",add(x,y))
print("-"*90)
print("Subtraction : ",sub(x,y))
print("-"*90)
print("Multiplication : ",mul(x,y))
print("-"*90)
print("Division : ",div(x,y))
