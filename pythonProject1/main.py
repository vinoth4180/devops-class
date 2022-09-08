l=[1,2,33,0]
b=[]
c=[]
for i in l:
    a=i*i
    b.append(a)
while b:
    min = b[0]
    for x in b:
        if x < min:
            min = x
    c.append(min)
    b.remove(min)

print(c)
