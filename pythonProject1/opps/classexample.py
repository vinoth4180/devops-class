# class employee:
#     name='vino'
#     location='chennai'
#     salary='50000'
#
#     def printemployees(self):
#         print(f'employee details={self.name} and {self.location} and {self.salary}')
#
# e=employee()
# print(e.name)
# print(e.location)
# print(e.salary)
# e.printemployees()
# print(employee.name)
# print(employee.location)
# employee.printemployees()

# class student:
#     Id='6'
#     name='vinoth'
#     m1=90
#     m2=95
#     m3=91
#     def students(self):
#         return (f'student details = {self.Id} and {self.name} and {self.m1} and {self.m2} and {self.m3}')
#
#     def studentavg(self):
#         return ((self.m1+self.m2+self.m3)/3)
# a=student()
# print(a.students())
# print(a.studentavg())
####empty constructor
# class training:
#     def __init__(self):
#         print('--------')
#         print('welcome to training')
#         print('-------')
#     def printdetails(self):
#         print('hello')
#
# t=training()
# t.printdetails()

###parameterized constructor
# class Employee:
#     company = 'Tutorial Gateway'
#
#     def __init__(self, n, a, gen):
#         self.name = n
#         self.age = a
#         self.gender = gen
#
#     def func_message(self):
#         print('Welcome to Programming')
#     def printmsg(self):
#         print(f'empdetails = {self.name} and {self.age} and {self.gender} and {self.company}')
#
# emp1 = Employee('Johnson', 29, 'Male')
#
# print(emp1.company)
# emp1.func_message()
# print(emp1.name)
# print(emp1.age)
# print(emp1.gender)
# emp1.printmsg()
# emp2 = Employee('John', 24, 'Male')
# print(emp2.company)
# emp2.func_message()
# print(emp2.name)
# print(emp2.age)
# print(emp2.gender)
# emp2.printmsg()

class headerprint:
    def __init__(self):
        print('---------------------------------------')
        print("Welcome to TNEB")
        print("----------------------------------------")
class footerprint:
    def __init__(self):
        print('---------------------------------------')
        print("Please Pay the bill on time other wise sub will be disconnect please pay on time")
        print("----------------------------------------")
class elebillcal:

    def __init__(self,units):
        self.units=units
    def billcal(self):
        # program for calculating electricity bill in Python

        if (self.units <= 100):
            payAmount = self.units * 1.5
            fixedcharge = 25.00
        elif (self.units <= 200):
            payAmount = (100 * 1.5) + (self.units - 100) * 2.5
            fixedcharge = 50.00
        elif (self.units <= 300):
            payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (self.units - 200) * 4
            fixedcharge = 75.00
        elif (self.units <= 350):
            payAmount = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (self.units - 300) * 5
            fixedcharge = 100.00
        else:
            payAmount = 0
            fixedcharge = 1500.00

        Total = payAmount + fixedcharge
        print("Electicity bill=", Total)


units=int(input("please enter the number of units you consumed in a month"))
h=headerprint()
b=elebillcal(units)
b.billcal()
f=footerprint()