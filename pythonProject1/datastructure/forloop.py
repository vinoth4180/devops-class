# for a in range(10):
#     print(a)
# for b in range(1,10):
#     print(b)
# for c in range(1,10,2):
#     print(c)
# for d in range(10):
#     print(d,end=" ")
# print("---------")
# for e in range(1,10):
#     print(e,end=' ')
# print('------')
# for f in range(1,10,2):
#     print(f,end=' ')
# print('----')
# for x in 'ancdef':
#     print(x)
# for y in 'ancdef':
#     print(y,end=' ')
#
# for a in range(1,6):
#     print(f"student details {a}")
#     m1 = int(input('enter the m1:'))
#     m2=int(input('enter the m2:'))
#     m3=int(input('enter the m3:'))
#
#     if m1<35 or m2<35 or m3<35:
#         print('student has failed')
#         if m1<35 and m2<35 and m3<35:
#             print('failed in all subjects')
#         elif m1<35 and m2<35:
#             print('failed in m1 and m2')
#         elif m2<35 and m3<35:
#             print('failed in m2 and m3')
#         elif m1<35 and m3<35:
#             print('failed in m3 and m1')
#         elif m1<35:
#             print('failed in m1')
#         elif m2<35:
#             print('failed in m2')
#         elif m3<35:
#             print('failed in m3')
#     else:
#         total=m1+m2+m3
#         if total>280:
#             print('grade a')
#         elif total<=280 and total>=250:
#             print('grade b')
#         else:
#             print('grade c')

# s=set()
# l=[]
# d=dict()
# for a in range(1,15):
#     l.append(a**2)
#     d[a]=a**2
#     s.add(a**2)
# print(l)
# print(d)
# print(s)

#for a in range(1,11):
    #print(f'{a}*{17} = {a*17}')

# n=int(input('enter the number of rows:'))
# t=int(input('enter which table to print:'))
# for a in range(1,n+1):
#     print(f'{a}*{t} = {a*t}')
# l=[]
# for a in range(1,1000):
#     if a%2==0:
#         if a%3==0:
#             if a%4==0:
#                 if a%5==0:
#                     if a%6==0:
#                         l.append(a)
# print(l)

####if two for present o\p will be table format. first for-rows and second for -columns
# for a in range(1,11):
#     for b in range(1,11):
#         print(f'{a}*{b}={a*b}',end=' ')
#         #print(a*b,end=' ')
#     print()

# for a in range(1,6):
#     for b in range(1,a+1):
#         #print(a,end=' ')
#         #print(b,end=' ')
#         print(a*b,end=' ')
#     print()

# n=1
# for a in range(1,6):
#     for b in range(1,a+1):
#         print(n,end=' ')
#         n=n+2
#     print()

# nl=[]
# pl=[]
# for a in range(1,15):
#     n=int(input(f'enter the no{a}:'))
#     if n<0:
#         nl.append(n)
#     else:
#         pl.append(n)
# print(nl)
# print(pl)
# print(sum(nl))
# print(sum(pl))
# print(max(pl))
# print(min(pl))
# print(max(nl))
# print(min(nl))
# print(len(pl))
# print(len(nl))

# for a in range(1,8):
#     if a==4:
#         for b in range(1,5):
#             print('*',end=' ')
#         print()
#     else:
#         for b in range(1,5):
#             if b==1 or b==4:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=" ")
#         print()
#
# for a in range(1,4):
#     if (a==1 or a==2):
#         for b in range(1,4):
#             if b!=2:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
#     else:
#         for b in range(1,4):
#             if a==3 and b==2:
#                 print('*',end=' ')
#             else:
#                 print(' ', end=' ')
#
#         print()

# for a in range(1,5):
#     if a==1:
#         for b in range(1,8):
#             if b==1 or b==7:
#                 print('*',end=" ")
#             else:
#                 print(' ',end=" ")
#         print()
#     elif a==2:
#         for b in range(1, 8):
#             if b == 2 or b == 6:
#                 print('*', end=" ")
#             else:
#                 print(' ', end=" ")
#         print()
#     elif a==3:
#         for b in range(1, 8):
#             if b == 3 or b == 5:
#                 print('*', end=" ")
#             else:
#                 print(' ', end=" ")
#         print()
#     else:
#         for b in range(1, 8):
#             if b == 4:
#                 print('*', end=" ")
#             else:
#                 print(' ', end=" ")
#         print()
# for a in range(1,7):
#     if a==1 or a==5:
#         for b in range(1,6):
#             if b==2 or b==3 or b==4:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
#     if a==2 or a==3:
#         for b in range(1,6):
#             if b==1 or b==5:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
#     if a==4:
#         for b in range(1,6):
#             if b==1 or b==3 or b==5:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()
#     if a==6:
#         for b in range(1,6):
#             if b==5:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()

# string=input('enter string:')
# b=set(string)
# print(b)
# s={'0','1'}
# if s==b or b=={'0'} or b=={'1'}:
#     print('binary')
# else:
#     print('not binary')

#
# stringA=input('enter the string:')
# b = '10'
# j = 0
# for i in stringA:
#    if i not in b:
#       j = 1
#       break
#    else:
#       pass
# if j==0:
#    print("StringA is  a binary string")
# else:
#    print("StringA is not a binary string")


num1=16
num2=6
while(num1>=2):
    if(num1>num2):
        num1=num1/2
    else:
        print(num1)
        break









