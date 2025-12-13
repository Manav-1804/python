#Write a Python program to update a value in a dictionary.

student = {

    "id" : 101,
    "name" : "Manav",
    "age" : 22,
    "course" : "Python",
    "marks" : 90,
    "city" : "Ahmedabad"
    }

student["marks"]=95

print("Update Student Dictionary : \n",student)

#Write a Python program to merge two lists into one dictionary using a loop.


print("-"*90)

keys=["id","name","age","course","marks","city"]
values=[101,"Manav",22,"Python",90,"Ahmedabad"]


result={}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print("Merge Two List into One Dictionary : \n ",result)
    
