# def square(num1):
#     return num1**2
#
# def cube(num1):
#     return num1**3
#
# def addition(num1,num2):
#     return num1+num2
#
# y=lambda r:3.14*(r**2)
# z=lambda a:a**4
#
# a=square(4)
# b=square(6)
# c=square(7)
# d=square(9)
# e=cube(4)
# f=cube(6)
# g=cube(7)
# h=cube(9)
# print(a,b,c,d)
# print(e,f,g,h)
# print(y(2))
# print(y(4))
# print(y(12))
# print(z(21))
# print(z(24))
# print(z(23))
# o1=addition(4,9)
# o2=addition(2,3)
# print(o1,o2)
l1=[4,6,7,9]
# m1=list(map(square,l1))
# print(list(m1))
# m2=map(cube,l1)
# print(list(m2))
# m3=map(addition,l1,l1)
# print(list(m3))
# m4=map(y,l1)
# print(list(m4))
# m5=map(z,l1)
# print(list(m5))

# def agecheck(num1):
#     if num1<18:
#         return 'below 18'
#     elif num1>=18 and num1<=25:
#         return 'between 18 to 25'
#     elif num1>25 and num1<=50:
#         return 'between 25 to 50'
#     else:
#         return 'above 50'
# # a=agecheck(94)
# # a1=agecheck(47)
# # a2=agecheck(12)
# # a3=agecheck(24)
# # print(a,a1,a2,a3)
# # p=map(agecheck,l1)
# # print(list(p))
#
def temp(t):
    if 0>t:
        return 'cold'
    elif 0<=t<=15:
        return 'medium'
    elif 15<t<=45:
        return 'hot'
    else:
        return 'very hot'
# b=temp(-2)
# c=temp(5)
# d=temp(18)
# e=temp(50)
# #print(b,c,d,e)
#p=map(temp,l1)
#c=list(p)
#print(c)

# d={}
# for i in c:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)

# import numpy as e
# a=e.array(c)
# unique,count=e.unique(a,return_counts=True)
# print(unique)
# print(count)

# a=[[1,2,3],[4,5,6],[7,8,9],[4,5],[2]]
# for b in range(len(a)):
#     print(a[b][0:2])

