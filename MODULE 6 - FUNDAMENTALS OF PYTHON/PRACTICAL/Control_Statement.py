'''
Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']
'''
fruits = ['apple', 'banana', 'mango']

for i in fruits:
    if i == 'banana':
        continue
    print(i)

'''
Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.
'''
print("*"*40)

fruits = ['apple', 'banana', 'mango']

for i in fruits:
    if i == 'banana':
        break
    print(i)
