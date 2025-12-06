import json

user_data={}

user_data["name"] = input("Enter your name : ")
user_data["age"] = int(input("Enter your age : "))
user_data["city"] = input("Enter your city : ")

with open ("user_data.json","w") as file:
    json.dump(user_data,file,indent=4)

print("Data Added....!!!!")
