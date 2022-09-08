s='The article of the artic was arresting'
w='te'
a=s.split(' ')
exisit=False
for i in a:
    exisit=False
    for j in w:
        if j in i.lower():
            exisit=True

        else:
            exisit=False
            break
    if exisit:
        print(i)

# s = "The article of the arctic was arresting"
# w = 'at'
# l = s.split()
# flag=0
# for x in l:
#     for b in w:
#         if b in x.lower():
#             flag+=1
#             if flag==len(w):
#                 print(x)
#     flag=0
