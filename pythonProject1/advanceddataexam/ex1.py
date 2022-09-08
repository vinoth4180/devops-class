# Python code to demonstrate namedtuple()


from collections import namedtuple

# Declaring namedtuple()

Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values

S = Student('Nandini', '19', '2541997')

# Access using index

print("The Student age using index is : ", end="")

print(S[1])

# Access using name

print("The Student name using keyname is : ", end="")

print(S.name)

# Python code to demonstrate namedtuple() and

# Access by name, index and getattr()


# importing "collections" for namedtuple()

import collections

# Declaring namedtuple()

Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values

S = Student('Nandini', '19', '2541997')

# Access using index

print("The Student age using index is : ", end="")

print(S[1])

# Access using name

print("The Student name using keyname is : ", end="")

print(S.name)

# Access using getattr()

print("The Student DOB using getattr() is : ", end="")

print(getattr(S, 'DOB'))

# Python code to demonstrate namedtuple() and

# _make(), _asdict() and "**" operator


# importing "collections" for namedtuple()

import collections

# Declaring namedtuple()

Student = collections.namedtuple('Student',

                                 ['name', 'age', 'DOB'])

# Adding values

S = Student('Nandini', '19', '2541997')

# initializing iterable

li = ['Manjeet', '19', '411997']

# initializing dict

di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()

print("The namedtuple instance using iterable is : ")

print(Student._make(li))

# using _asdict() to return an OrderedDict()

print("The OrderedDict instance using namedtuple is : ")

print(S._asdict())

# using ** operator to return namedtuple from dictionary

print("The namedtuple instance from dict is : ")

print(Student(**di))

# Python code to demonstrate namedtuple() and

# _fields and _replace()


# importing "collections" for namedtuple()

import collections

# Declaring namedtuple()

Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values

S = Student('Nandini', '19', '2541997')

# using _fields to display all the keynames of namedtuple()

print("All the fields of students are : ")

print(S._fields)

# ._replace returns a new namedtuple, it does not modify the original

print("returns a new namedtuple : ")

print(S._replace(name='Manjeet'))

# original namedtuple

print(S)

# Python code to demonstrate deque


from collections import deque

# Declaring deque

queue = deque(['name', 'age', 'DOB'])

print(queue)

# Python code to demonstrate working of

# append(), appendleft(), pop(), and popleft()


# importing "collections" for deque operations

import collections

# initializing deque

de = collections.deque([1, 2, 3])

# using append() to insert element at right end

# inserts 4 at the end of deque

de.append(4)

# printing modified deque

print("The deque after appending at right is : ")

print(de)

# using appendleft() to insert element at left end

# inserts 6 at the beginning of deque

de.appendleft(6)

# printing modified deque

print("The deque after appending at left is : ")

print(de)

# using pop() to delete element from right end

# deletes 4 from the right end of deque

de.pop()

# printing modified deque

print("The deque after deleting from right is : ")

print(de)

# using popleft() to delete element from left end

# deletes 6 from the left end of deque

de.popleft()

# printing modified deque

print("The deque after deleting from left is : ")

print(de)

# Python code to demonstrate working of

# insert(), index(), remove(), count()


# importing "collections" for deque operations

import collections

# initializing deque

de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4

print("The number 4 first occurs at a position : ")

print(de.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position

de.insert(4, 3)

# printing modified deque

print("The deque after inserting 3 at 5th position is : ")

print(de)

# using count() to count the occurrences of 3

print("The count of 3 in deque is : ")

print(de.count(3))

# using remove() to remove the first occurrence of 3

de.remove(3)

# printing modified deque

print("The deque after deleting first occurrence of 3 is : ")

print(de)

# Python code to demonstrate working of

# extend(), extendleft(), rotate(), reverse()


# importing "collections" for deque operations

import collections

# initializing deque

de = collections.deque([1, 2, 3, ])

# using extend() to add numbers to right end

# adds 4,5,6 to right end

de.extend([4, 5, 6])

# printing modified deque

print("The deque after extending deque at end is : ")

print(de)

# using extendleft() to add numbers to left end

# adds 7,8,9 to left end

de.extendleft([7, 8, 9])

# printing modified deque

print("The deque after extending deque at beginning is : ")

print(de)

# using rotate() to rotate the deque

# rotates by 3 to left

de.rotate(-3)

# printing modified deque

print("The deque after rotating deque is : ")

print(de)

# using reverse() to reverse the deque

de.reverse()

# printing modified deque

print("The deque after reversing deque is : ")

print(de)

# Python code to demonstrate working of

# heapify(), heappush() and heappop()


# importing "heapq" to implement heap queue

import heapq

# initializing list

li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap

heapq.heapify(li)

# printing created heap

print("The created heap is : ", end="")

print(list(li))

# using heappush() to push elements into heap

# pushes 4

heapq.heappush(li, 4)

# printing modified heap

print("The modified heap after push is : ", end="")

print(list(li))

# using heappop() to pop smallest element

print("The popped and smallest element is : ", end="")

print(heapq.heappop(li))

# Python code to demonstrate working of

# heappushpop() and heapreplce()


# importing "heapq" to implement heap queue

import heapq

# initializing list 1

li1 = [5, 1, 9, 4, 3]

# initializing list 2

li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap

heapq.heapify(li1)

heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously

# pops 2

print("The popped item using heappushpop() is : ", end="")

print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously

# pops 3

print("The popped item using heapreplace() is : ", end="")

print(heapq.heapreplace(li2, 2))

# Python code to demonstrate working of

# nlargest() and nsmallest()


# importing "heapq" to implement heap queue

import heapq

# initializing list

li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap

heapq.heapify(li1)

# using nlargest to print 3 largest numbers

# prints 10, 9 and 8

print("The 3 largest numbers in list are : ", end="")

print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers

# prints 1, 3 and 4

print("The 3 smallest numbers in list are : ", end="")

print(heapq.nsmallest(3, li1))