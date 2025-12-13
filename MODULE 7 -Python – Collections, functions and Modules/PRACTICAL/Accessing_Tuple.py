#Write a Python program to access values between index 1 and 5 in a tuple.


t1=(10,20,30,40,50,60,70,80)

result=t1[1:5]

print("Access values between index 1 and 5 in a tuple : ",result)


#Write a Python program to access alternate values between index 1 and 5 in a tuple.

print("-"*90)

values=t1[1:5:2]

print("Access alternate values between index 1 and 5 in a tuple : ",values)
