def myfun():
    global name
    print("1st", name)
    name="Python Langugae"
    print("2nd ", name)

name="Python"

myfun()

print("3rd",name)
