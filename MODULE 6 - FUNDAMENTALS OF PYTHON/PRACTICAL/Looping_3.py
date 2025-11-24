'''
Write a Python program to find a specific string in the list using a simple
for loop and if condition.
'''

l=["Manav","Meet","Shubham","Pratik","Khushi","Deven"]

find = input("Enter The String : ")

found=False

for i in l:
    if i==find:
        found=True

if found==True:
       print("Found")
else:
        print("Not Found")
