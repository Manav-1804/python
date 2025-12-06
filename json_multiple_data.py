import json

users_data=[]

num_users = int(input("Enter the number of users : "))

for i in range(num_users):
    user_data={}
    user_data["name"]=input("Enter Your Name : ")
    user_data["age"]=int(input("Enter Your Age : "))
    user_data["city"]=input("Enter Your City : ")

    users_data.append(user_data)

with  open("users_data.json","w") as file:
    json.dump(users_data,file,indent=4)

print("Data Added Successfully...!!!")
