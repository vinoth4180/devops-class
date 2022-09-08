#l=[1,2,3,4,5]
# print(l)
# print(type(l))
#l1=[[1,2,3],[4,5,6],[7,8,9]]
# print(l1)
# print(type(l1))
#l2=[[[1,2],[3,4]],[[5,6],[7,8]]]
# print(l2)
# print(type(l2))

# import numpy as np
# a=np.array(l)
# print(a)
# b=np.array(l1)
# print(b)
# c=np.array(l2)
# print(c)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# o=[]

# for a in range(len(l)):
#     for b in range(len(l[a])):
#         print(l[a][b],end=' ')
#     print()
#     print('-------')
# for a in range(len(l)):
#     o1=[]
#     for b in range(len(l[a])):
#         o1.append(l[a][b]+2)
#         print(o1)
#     o.append(o1)
#     print(o)
# print(o)

import numpy as np
# a=np.array(l)
# print(a+2)
# a=np.arange(10)
# b=np.arange(15)
# c=np.arange(12)
# print(a)
# print(b)
# print(c)
# a=np.linspace(0,1,5)
# print(a)
# b=np.linspace(1,10,5)
# print(b)
# c=np.linspace(1,0,7)
# print(c)

# print(np.zeros(2))
# print(np.zeros((4,2)))
# print(np.zeros((2,3,4)))

# print(np.ones(2))
# print(np.ones((4,2)))
# print(np.ones((2,3,4)))
#
# print(np.full((2,3),17))
# print(np.full((3,3),7))

# l=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
# o=[]
# for i in l:
#     o1=[]
#     for j in i:
#         o2=[]
#         for k in j:
#             k+=2
#             o2.append(k)
#         o1.append(o2)
#     o.append(o1)
# print(o)
# import numpy as np
# m=[]
# n1=[]
# for i in range(0,3):
#     t=[]
#     for j in range(0,3):
#         n=int(input(f'enter the {i} row and {j} column:'))
#         t.append(n)
#     m.append(t)
# for i in range(0,3):
#     t=[]
#     for j in range(0,3):
#         n=int(input(f"enter the {i} row and {j} column :"))
#         t.append(n)
#     n1.append(t)
# print(m)
# print(n1)
# m1=np.array(m)
# m2=np.array(n)
# print(m1+m2)

import numpy as np
m=[]
n1=[]
for i in range(0,2):
    t=[]
    for j in range(0,2):
        o=[]
        for k in range(0,2):
            n=int(input(f'enter the {i} row and {j} column:'))
            o.append(n)
        t.append(o)
    m.append(t)
for i in range(0,2):
    t=[]
    for j in range(0,2):
        o1=[]
        for k in range(0,2):
            n=int(input(f"enter the {i} row and {j} column :"))
            o1.append(n)
        t.append(o1)
    n1.append(t)

print(m)
print(n1)
m1=np.array(m)
m2=np.array(n1)
print(m1+m2)

