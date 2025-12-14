'''
Write a Python program to open a file in write mode, write some text, and then close it.
'''

file=open("write.txt","w")

file.write("This is my first Opening and closing file program.\n")
file.write("Thank you for visit in my write.txt file.")

file.close()

print("Data added successfully...!!!")
