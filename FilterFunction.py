l1=[23,34,45,67,23,98]

def checkEven(num):
     if num%2==0:
         return num

l2=list(filter(checkEven,l1))

print(l2)

print("-"*100)

l1=[23,34,45,67,23,98,234]

l2=list(filter(lambda  num : num%2==0 , l1))

print(l2)


print("-"*100)

l1=["anjali","priyanshi","oman","ashvi"]
def findvowels(name):
    if name[0] in "aeiou":
        return name

l2=list(filter(findvowels,l1))
print(l2)

print("-"*100)

number=[1,2,3,4,5,6,7,8,9,10]
odd_number=filter(lambda x : x%2!=0, number)
print(list(odd_number))

print("-"*100)

words=["anjali","priyanshi","om","ashvi","ram"]
long_words=filter(lambda word: len(word)>=4,words)
print(list(long_words))

print("-"*100)

strings=["hello","","world","","python",""]
non_empty_string=filter(lambda x: x != "",strings)
print(list(non_empty_string))




print("-"*100)
        
