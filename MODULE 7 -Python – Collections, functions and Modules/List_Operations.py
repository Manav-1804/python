#Write a Python program to add elements to a list using insert() and append().

my_list = [10, 20, 30]

my_list.append(40)


my_list.insert(1, 15)

print("List after adding elements:", my_list)


#Write a Python program to remove elements from a list using pop() and remove().

my_list1 = [10, 20, 30, 40, 50]

# pop() removes element at a specific index (default last)
removed_item = my_list1.pop(2)  # removes item at index 2
print("Popped element:", removed_item)

# remove() removes the first occurrence of the given value
my_list1.remove(40)

print("List after removing elements:", my_list1)

