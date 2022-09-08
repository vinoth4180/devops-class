# f=open('output.txt','a')
# f.write('--- - --\n')
# f.write('hello\n')
# f.write('world\n')


import re
f=open("output1.txt","a")

f.write("Hi I am barath kumar\n")
f.write("HI i am ......\n")

f=open("output1.txt","r")
txt=f.read()
newtxt=re.sub('am','ant',txt)
print(newtxt)

f=open("output1.txt","w")
f.write(newtxt)
