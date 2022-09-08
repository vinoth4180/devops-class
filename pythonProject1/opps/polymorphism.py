# a=5
# b=6
# print(a+b)
# a='babu'
# b='m'
# print(a+b)
#
# l='hello'
# print(len(l))
# l1=[1,2,3,4,5,6]
# print(len(l1))
# ###polymorphism with def function
# def add(num1=0,num2=0):
#     return num1+num2
#
# d=add(2,3)
# e=add(5)
# f=add()
# print(d,e,f)
####polymorphism with class
# class India:
#     def population(self):
#         print('population in india is 8M')
#     def type(self):
#         print('developing country')
# class Usa:
#     def population(self):
#         print('population in Usa is 7M')
#     def type(self):
#         print('developed country')
# class Russia:
#     def population(self):
#         print('population in Russia is 6M')
#     def type(self):
#         print('war country')
# a=India()
# b=Usa()
# c=Russia()
# for i in (a,b,c):
#     i.population()
#     i.type()
####polymorphism with inheritance
class shape:
    def __init__(self,r,a,l,b):
        self.r=r
        self.a=a
        self.l=l
        self.b=b
    def area(self):
        pass
class circle(shape):
    def area(self):
        print(3.14*self.r*self.r)
class square(shape):
    def area(self):
        print(self.a*self.a)
class rectangle(shape):
    def area(self):
        print(self.l*self.b)

a=circle(1,1,1,1)
b=square(1,2,2,1)
c=rectangle(1,1,1,1)
for i in (a,b,c):
    i.area()

