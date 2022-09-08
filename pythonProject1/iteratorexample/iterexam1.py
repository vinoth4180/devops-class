stri = 'tutorialbesantt'

for x in stri:
    print(x, end='  ')

stng = 'tutorialbesantt'

for x in stng:
    print(x, end='  ')

print("\n**** Output *****")
itr = iter(stng)

print(next(itr))

sting = 'tutorialbesantt'

for x in sting:
    print(x, end='  ')

print("\n**** Example *****")
itr = iter(sting)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

numbers = [10, 20, 30, 40, 50]

itr = iter(numbers)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

numbers = [10, 20, 30, 40, 50]

itr = iter(numbers)

print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

mySet = {1, 2, 3, 4, 5}

ittr = iter(mySet)

print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())


fruits = ('Apple', 'Orange', 'Grape', 'Banana', 'Kiwi')

fruit_itr = iter(fruits)

print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))


class Counter:

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        number = self.number

        if number > self.maximum:
            raise StopIteration
        else:
            self.number = number + 1
            return number


numbers = Counter(10)
a = iter(numbers)

print(next(a))
print(next(a))
print(next(a))


class Counter:

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        number = self.number

        if number > self.maximum:
            raise StopIteration
        else:
            self.number = number + 1
            return number


for t in Counter(10):
    print(t)
