# # l1=[[10,20],[11,21],[12,25],[5,6,7]]
# l1=[[-1,5],[100],[11,22,33],[55,66,77],[-1,-2,-3]]
# print(l1)
# m=[]
# for a in range(0,len(l1)-1):
#     # print(l1[a])
#     x = l1[a]
#     y = l1[a+1]
#     n = []
#     # print(x,y)
#     for b in range(len(x)):
#         for c in range(len(y)):
#             if x[b]<y[c]:
#                 n.append(x[b])
#             break
#     m.append(n)
# print(m)


s=int(input('enter the number of students:'))
a=[]
for i in range(s):
    name = input('enter the name:')
    score = float(input('enter the mark:'))
    b=(name,score)
    c=list(b)
    a.append(c)
print(a)
f=dict(a)
print(f)
keys=f.keys()
h= sorted(keys)
print(h)
q = {}
for key in h:
  q[key] = f[key]
print(q)

d=[]
for j in a:
    for k in j:
        if type(k)==float:
            d.append(k)
            d.sort()
print(d)
for k,v in q:
    if d[1]==v:
        print(k)
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# from decimal import Decimal
# from itertools import groupby, islice
# from operator import itemgetter
#
# a = []
# for i in range(6):
#   x, y = (input(), Decimal(input()))
#   a.append((y, x))
# a.sort()
# for k, v in islice(groupby(a, key=itemgetter(0)), 1, 2):
#   for x in v:
#     print(x[1])





