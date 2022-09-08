# sq=[]
# cu=[]
# def square(Threadname,endpoint,delay):
#     for i in range(1,endpoint+1):
#         sq.append(i*i)
#         print("Tread name was=",Threadname,"and sq value is =",sq)
#
# def cube(Threadname,endpoint,delay):
#     for i in range(1,endpoint+1):
#         cu.append(i**3)
#         print("Tread name was=",Threadname,"and cu value is =",cu)
#
#
# square("thread1",10,2)
# print("---------------------------------------------")
# cube("thread2",10,2)

# import _thread
# import time
#
# sq=[]
# cu=[]
#
# def square(Threadname,endpoint,delay):
#     for i in range(1,endpoint+1):
#         sq.append(i*i)
#         print("Tread name was=",Threadname,"and sq value is =",sq)
#         time.sleep(delay)
#
# def cube(Threadname,endpoint,delay):
#     for i in range(1,endpoint+1):
#         cu.append(i**3)
#         print("Tread name was=",Threadname,"and cu value is =",cu)
#         time.sleep(delay)
#
# try:
#     _thread.start_new_thread(square,("thread-1",10,5))
#     _thread.start_new_thread(cube, ("thread-2",10,4))
#     _thread.start_new_thread(square, ("thread-3", 5, 3))
#     _thread.start_new_thread(cube, ("thread-4", 5, 2))
#
# except:
#     print("Error:enable start to thread")
#
#
# while 1:
#     pass


import _thread
import time
import datetime

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print(threadName,datetime.datetime.now())

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print("Error: unable to start thread")

while 1:
   pass