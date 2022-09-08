# Python program to illustrate functions

# can be treated as objects

def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))


# Python program to illustrate functions

# can be passed as arguments to other functions

def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable

    greeting = func("""Hi, I am created by a function passed as an argument.""")

    print(greeting)


greet(shout)

greet(whisper)


# Python program to illustrate functions

# Functions can return another function


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))


# defining a decorator

def hello_decorator(func):
    # inner1 is a Wrapper function in

    # which the argument is called

    # inner function can access the outer local

    # functions like in this case "func"

    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now

        # inside the wrapper function.

        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper

def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the

# decorator to control its behaviour

a = hello_decorator(function_to_be_used)

# calling the function

a()

