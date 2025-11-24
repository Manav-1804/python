#Write a generator function that generates the first 10 even numbers.

def even_numbers():
    return (i * 2 for i in range(1,11))

for n in even_numbers():
    print(n)
