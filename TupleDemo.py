t=(1,2,1.1,2.2,"tops",True,[100,200,300],"python",False,"Java",10,20)

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)

print(1.1 in t)
print(t[6])
t[6].pop()
print(t)
print(list(t))
