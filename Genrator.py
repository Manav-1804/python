"""
yield : Instead of returning a value , the yeild statment pauses the function
and send a value back to the caller.

when the generator is resumed, execution fro the point where yeild was called.

"""

def count_up_to(n):
    count =  1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)


for i in counter:
    print(i)

print("-"*50)

def simple_generator():
    yield 1*10
    yield 2*20
    yield 3*30

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))
