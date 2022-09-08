# i=1
# while(i<=5):
#     print(i)
#     i+=1
#
# i=1
# while(i<=21):
#     print(i,end=' ')
#     i+=1
#
# i=25
# while(i<=22):
#     print(i,end=' ')
#     i+=1
# else:
#     print('i value is bigger')

##1
# i=1
# while(i<=10):
#     if i%2==0:
#         print(i,end=' ')
#     i+=1
# print()

##2
# i=1
# while(i<=10):
#     if i%2!=0:
#         print(i,end=' ')
#     i+=1
# print()

##3
# i=1
# for a in range(1,5):
#     for b in range(1,a+1):
#         print(i,end=' ')
#         i+=1
#     print()

# i=1
# a=1
# while(a<5):
#     b=1
#     while(b<a+1):
#         print(i,end=' ')
#         i+=1
#         b+=1
#     print()
#     a+=1

# Python program to check if the number is an Armstrong number or not

num = int(input("Enter a number: "))
o=len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   print("digit value=",digit)
   sum += digit ** o
   print("sum value",sum)
   temp //= 10
   print("temp value=",temp)
   print('-----------------')

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


