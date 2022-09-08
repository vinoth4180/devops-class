# Memory Efficient
# A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.

# Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__())  # In Python 3, __next__()
print(x.__next__())
print(x.__next__())


# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()
print(a.__next__())
print(a.__next__())
print(a.__next__())

# Using for loop
for item in my_gen():
    print(item)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)

print(list_)
print(list(generator))

# Initialize the list
my_list = [1, 3, 6, 10]

a = (x ** 2 for x in my_list)
print(next(a))

print(next(a))

print(next(a))

print(next(a))



