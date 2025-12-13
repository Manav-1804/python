#Write a Python program to iterate over a list using a for loop.

my_list = ["apple", "banana", "mango", "orange"]

print("Iterating over the list:")
for item in my_list:
    print(item)

print("-"*70)


#Write a Python program to sort a list using both sort() and sorted().

numbers = [20, 5, 15, 40, 10]

numbers.sort()
print("List after sort():", numbers)

numbers2 = [20, 5, 15, 40, 10]
sorted_list = sorted(numbers2)
print("Original list (numbers2):", numbers2)
print("List after sorted():", sorted_list)
