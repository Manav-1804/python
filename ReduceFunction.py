from functools import reduce

def add(x,y):
    return x + y

numbers=[1,2,3,4,5,6,7,8,9,10]
result=reduce(add,numbers)
print(result)

sum = 0
for i in numbers:
    sum=sum+i

print(sum)
