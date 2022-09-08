# Python program to illustrate
# enumerate function

l1 = ["eat", "sleep", "repeat"]

s1 = "geek"

# creating enumerate objects

obj1 = enumerate(l1)

obj2 = enumerate(s1)

print("Return type:", type(obj1))

print(list(enumerate(l1)))

# changing start index to 2 from 0

print(list(enumerate(s1, 25)))
print('-----------------')
# Python program to illustrate
# enumerate function in loops

l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly

for ele in enumerate(l1):
    print(ele)

# changing index and printing separately

for count, ele in enumerate(l1, 100):
    print(count, ele)

# getting desired output from tuple

for count, ele in enumerate(l1):
    print(count)

    print(ele)
print('-------------------')
languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_prime))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
print('-----------------------')
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
print('---------------------------')
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')

for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)