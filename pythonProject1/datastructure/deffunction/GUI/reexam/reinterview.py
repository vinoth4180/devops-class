import re
# ####butterfly
# bandf=input("Enter the butterfly and flower in garden")
#
# def findingBF(bandfstr):
#     findstr = re.findall("@B|@.*B",bandfstr)
#     print(len(findstr))
# findingBF(bandf)
######length of string
# str=[]
# numofinput = int(input("Enter the Number of input"))
#
# for i in range(numofinput):
#     inputstr = input(f"Enter the string-{i}")
#     str.append(inputstr)
#
# maxlen = 0
# maxlenindex = 0
# def findlongeststring(str):
#     print(len(str))
#     print(list(str))
#     for i in range(len(str)):
#         if i == 0 :
#             maxlen = len(str[i])
#             maxlenindex = i
#         elif maxlen < len(str[i]):
#             maxlen = len(str[i])
#             maxlenindex = i
#         else:
#             continue
#     print(f"Max String is {str[maxlenindex]} and the length is {maxlen} and the index is {maxlenindex}")
# findlongeststring(str)

# rows = int(input("Enter the number of rows:"))
#Reversed loop for downward inverted pattern
#
# for i in range(5, 0, -1):
# Increment in k after each iteration
#     k = 1
#     c=i*2
#     n=c//2
#     for j in range(1,c+1):
#         if j<n:
#             print(k,end=" ")
#             k+=1
#         elif j==n:
#             print(k, end=" ")
#         else:
#             print(k,end=" ")
#             k-=1
#
#
#     print()


# Python3 Program to add two numbers
# without using arithmetic operator
# def Add(x, y):
#     # Iterate till there is no carry
#     while (y != 0):
#         carry = x & y
#         x = x ^ y
#         y = carry << 1
#
#     return x


# print(Add(5,2))

# n = int(input("Enter the Rows :"))
# for i in range(1, n):
#     for j in range(1, n-i):
#         print(j, end=" ")
#     for b in range(2, 2*i):
#         print(" ", end=" ")
#     for c in range(n-1-i,0, -1):
#         print(c, end=" ")
#     print()

###palindrome without using slice function
# num = int(input("Enter a value:"))
# temp = num
# rev = 0
# while(num > 0):
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10
# if(temp == rev):
#     print("This value is a palindrome number!")
# else:
#     print("This value is not a palindrome number!")
# n=5
# i=n+1
# for a in range(n,0,-1):
#     for b in range(1,i):
#         if b<=a:
#             print(b,end=' ')
#         else:
#             print(' ',end=' ')
#     for b in range(n,0,-1):
#         if b<=a:
#             print(b,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

####interleaved string
# from itertools import chain
# def interleaved(a,b):
#     result="".join(i+j for i, j in zip(a,b))
#     res="".join(list(chain.from_iterable(zip(a,b))))
#     return ('interleaved string:',res)
#
# print(interleaved('111111','222222'))

def find(x):
    x*=x/2
    return x
print(find(4))