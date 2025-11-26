import random

data=open("data.txt", "w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt", "w")
l=data.read().split(",")[:-1]

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

for i in l:
    num = int(i)
    if num%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

    if is_prime(num):
        prime.write(i + ",")
        
even.close()
odd.close()
prime.close()
data.close()

print("Data File Content")
data=open("data.txt","r")
print(data.read())
data.close()

print("Even File Content")
data=open("even.txt","r")
print(data.read())
data.close()

print("Odd File Content")
data=open("odd.txt","r")
print(data.read())
data.close()

print("Prime File Content")
data=open("prime.txt","r")
print(data.read())
data.close()

    

