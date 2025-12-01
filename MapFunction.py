l1=[1,2,3,4,5,6,7,8,9,10]

def square(n):
    return n*n

l2= list(map(square,l1))

print(l2)

print("-"*100)


l1=[23,34,56,67,89,40,47,69,26]

def oddeven(num):
    if num%2==0:
        return str (num)+ " - Even"
    else:
        return str (num)+ " - Odd"

l2= list(map(oddeven,l1))

print(l2)
