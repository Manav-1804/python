import re


text = input("Enter a string: ")
word = input("Enter word to search: ")


result = re.search(word, text)

if result:
    print("Word found using re.search()")
else:
    print("Word not found using re.search()")


text = input("Enter a string: ")
word = input("Enter word to match: ")


result = re.match(word, text)

if result:
    print("Word matched at the beginning using re.match()")
else:
    print("Word did not match at the beginning using re.match()")
