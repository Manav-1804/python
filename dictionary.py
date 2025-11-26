d={101:"Manav",344:"Meet",787:"Pratik"}

print(d)
print(d[344])
print(d.get(787))
#d.clear()
#print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d)
print(d.pop(344))
print(d)
d.popitem()
print(d)
d1={123:"Meet",345:"Pratik"}
d.update(d1)
print(d)

for i in d:
    print(i, " : ",d[i])
