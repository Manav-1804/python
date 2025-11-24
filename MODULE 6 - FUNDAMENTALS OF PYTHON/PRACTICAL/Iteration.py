# Write a Python program that uses a custom iterator to iterate over a list of integers.

def iterate_list(nums):
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 1


numbers = [10, 20, 30, 40, 50]
iterate_list(numbers)
