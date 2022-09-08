# try:
#     print(a)
# except:
#     print('a is not defined')
#
#
# a=10
# try:
#     print(a)
# except:
#     print('a is not defined')
#
# a=(input("Enter the number1:"))
# b=(input("Enter the number 2:"))
# c=0
# try:
#     c=int(a)/int(b)
#     print("Al are ok")
# except NameError as e:
#     print("variable is not defined")
# except ZeroDivisionError as e:
#     print("Number cannot be divisble by zero")
# except ValueError as e:
#     print("Please enter the valid symbol")
# finally:
#     print(c)

import os
try:
    a=os.chdir(r'C:\Users\vasan\Desktop\f3\4.txt.txt')
    b=os.listdir(a)
    print(b)
except NotADirectoryError:
    print('file is found')
except FileNotFoundError:
    print('file not found')
finally:
    print(os.listdir())