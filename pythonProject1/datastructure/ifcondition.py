# if -2:#false and 0 if condition not work
#     print("hello")
# if 0:
#     print("hello world")
# if True:
#     print("hello")
# if False:
#     print("hi")
# if 999:
#     print("hiiii")

# age=int(input('enter the age:'))
# # if age<18:
# #     print('below 18 years')
# # else:
# #     print("above 18 years")
# if age<18:
#     agewait=18-age
#     print(f'user has to wait for {agewait} year to cast vote')
# else:
#     print('user is allowed to vote')
#
# m1=int(input('enter the m1:'))
# m2=int(input('enter the m2:'))
# m3=int(input('enter the m3:'))
#
# if m1<35 or m2<35 or m3<35:
#     print('student has failed')
#     if m1<35 and m2<35 and m3<35:
#         print('failed in all subjects')
#     elif m1<35 and m2<35:
#         print('failed in m1 and m2')
#     elif m2<35 and m3<35:
#         print('failed in m2 and m3')
#     elif m1<35 and m3<35:
#         print('failed in m3 and m1')
#     elif m1<35:
#         print('failed in m1')
#     elif m2<35:
#         print('failed in m2')
#     elif m3<35:
#         print('failed in m3')
# else:
#     total=m1+m2+m3
#     if total>280:
#         print('grade a')
#     elif total<=280 and total>=250:
#         print('grade b')
#     else:
#         print('grade c')

# age=int(input("enter the age:"))
# country=input('enter the country:')
# if age<18 and country=='india':
#     print('below 18 india')
# elif age<18 and country!='india':
#     print('below 18 other country')
# elif age>=18 and age<=56 and country=='india':
#     print('above 18 and country is india')
# elif age>=18 and age<=56 and country!='india':
#     print('above 18 other country')
# elif age>56 and country=='india':
#     print('sr.cit india')
# else:
#     print('sr.cit other country')


# n=int(input('enter the number:'))
# if n<100:
#     print('below 100')
# elif 100<=n<1000:
#     print('100 and below 1000')
# elif 1000<=n<10000:
#     print('1000 and below 10000')
# else:
#     print('greater than 10000')

# n=int(input('enter the number:'))
# if n in range(11) and (n%2!=0):
#     print('n is odd number')
# elif n in [2,4,6,8,10]:
#     print('n is even number')
# else:
#     print('wrong input')

# n=2002
# if n%4==0:
#     print('leap year')
# else:
#     print('not leap year')
#
# n=int(input('enter the no:'))
# if n%2==0:
#     if n%3==0:
#         if n%4==0:
#             if n%5==0:
#                 print('hello')


l23=[]
l25=[]
othl=[]
n=int(input('enter the no:'))
if n%2==0 and n%3==0:
    l23.append(n)
elif n%2==0 and n%5==0:
    l25.append(n)
else:
    othl.append(n)
print(l23)
print(l25)
print(othl)