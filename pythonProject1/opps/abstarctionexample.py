# Python program demonstrate
# abstract base class work
from abc import ABC,abstractmethod
# class Car(ABC):
#     def mileage(self):
#         pass
# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph ")
# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 24kmph ")
# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph ")
#  # Driver code
# t = Tesla()
# t.mileage()
# r = Renault()
# r.mileage()
# s = Suzuki()
# s.mileage()
# d = Duster()
# d.mileage()
@abstractmethod
class shape(ABC):
    def area(self):
        pass
class circle(shape):
    def area(self,r):
        self.r=r
        print(3.14*self.r*self.r)
class square(shape):
    def area(self,a):
        self.a=a
        print(self.a*self.a)
class rectangle(shape):
    def area(self,l,b):
        self.l=l
        self.b=b
        print(self.l*self.b)

a=circle()
a.area(2)
b=rectangle()
b.area(2,3)
c=square()
c.area(9)