import re
# #txt='the rain in spain'
# #o=re.findall('ai',txt)
# # print(o)
# # print(len(o))
# # i=input('enter the string')
# # o=re.findall(i,txt)
# # print(o)
# # print(len(o))
# t='xyz abc abc xyz'
# r=re.findall('t',t)
# print(r)
# s=re.search('t',t)
# print(s)
# a=re.split(' ',t,1)
# print(a)
# b=re.sub('z','1',t)
# print(b)

txt='123AbcZabcxyzz123@^*-'
a=re.findall('\d',txt)
#print(a)
b=re.findall('[a-zA-Z]',txt)
#print(b)
a.extend(b)
#print(a)
c=set(a)
b=set(txt)
#d=b.difference(c)
#print(d)
l= list(txt)
mtlist = []
for j in l:
    if j not in a:
        mtlist.append(j)
print(mtlist)

