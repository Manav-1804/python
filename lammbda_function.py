x=lambda a:a*a
print(x(5))

print("-"*80)

def cube(a):
    return a*a*a

print("Cube Of " ,5," IS  : ",cube(5))

print("-"*80)

x=lambda a:a*a*a
print("Cube Of " ,5," IS  : ",cube(5))

print("-"*80)

x= lambda a,b:a+b
print(x(10,20))

print("-"*80)

def oddeven(n):
    if n%2==0:
        print("even")
    else:
        print("odd")

oddeven(10)

print("-"*80)

result = lambda num : "even" if num%2==0 else "odd"


