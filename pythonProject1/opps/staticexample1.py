# class Employee:
#
#     def func_message(self):
#         print('Welcome to The World')
#
#     def func_addition(a, b):
#         return a + b
#
#
# Employee.func_addition = staticmethod(Employee.func_addition)
# print('Total = ', Employee.func_addition(25, 50))
#
# emp = Employee()
# emp.func_message()
#
#
# class Employee:
#
#     def func_message(self):
#         print('Welcome to this World')
#
#     def func_addition(a, b):
#         return a + b
#
#     def func_multiply(a, b):
#         return a * b
#
#
# emp = Employee()
# emp.func_message()
#
# Employee.func_addition = staticmethod(Employee.func_addition)
# print('Total = ', Employee.func_addition(25, 50))
#
# Employee.func_multiply = staticmethod(Employee.func_multiply)
# print('Multiplication = ', Employee.func_multiply(25, 50))

class Employee:

    def func_message(self):
        print('Welcome to Programming')

    @staticmethod
    def func_msg():
        print("Welcome to Tutorial Gateway")

    @staticmethod
    def split_string(message):
        return message.split(",")

Employee.func_msg()
countries = 'India, China, Japan, USA, UK, Australia, Canada'
print(Employee.split_string(countries))