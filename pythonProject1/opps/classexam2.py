# class classme:
#     @classmethod
#     def printclassmethod(self):
#         print('no need object')
#         print('call me with class name itself')
#     def printnonclassmethod(self):
#         print('i need object')
#
# classme.printclassmethod()
# #c=classme()
# classme.printnonclassmethod=classmethod(classme.printnonclassmethod)###second type for creating classmethod
# #c.printnonclassmethod()
# classme.printnonclassmethod()

# class classEx:
#     print('hello')
#     print('xyz')
#     print('hello world')
#     n='babu'
#     def prints(self):
#         print(self.n)
#
# c=classEx()
# c.prints()
#
# ####empty class
# class emptyclass:
#     pass
# ####empty function
# class emptyfunction:
#
#     def fun(self):
#         pass


# Python program to understand the classmethod


class Student:
    # create a variable

    name = "Geeksforgeeks"

    # create a function

    def print_name(obj):
        print("The name is : ", obj.name)

    # create print_name classmethod


# before creating this line print_name()
# It can be called only with object not with class

Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()


class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()

# Python
# program
# to
# understand
# the
# classmethod


class Student:
    # create a variable

    name = "Geeksforgeeks"

    # create a function

    def print_name(obj):
        print("The name is : ", obj.name)

    # create print_name classmethod


# before creating this line print_name()
# It can be called only with object not with class

Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()

#Python
#program
#to
#demonstrate
# use of a class method and static method.

from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name

        self.age = age

        # a class method to create a

    # Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person = Person('mayank', 21)
person.display()
a=person.fromBirthYear('vino',1996)
print(vars(a))


class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Puchase course : ", obj.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()

# Python program to demonstrate
# use of a class method and static method.

from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name

        self.age = age

        # a class method to create a

    # Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person = Person('mayank', 21)
person.display()