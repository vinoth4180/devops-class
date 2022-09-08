import os
# print(os.getcwd())
# l=os.listdir()
# print(os.listdir())
# for a in range(len(l)):
#     print(l[a])
# os.chdir(r'C:\Users\vasan\Desktop\f1')
# print(os.getcwd())
# l=os.listdir()
# print(os.listdir())
# for a in range(len(l)):
#     print(l[a])

# foldername=input("enter the folder name:")
# os.mkdir(foldername)# mkdir-make directory
# print(os.listdir())

y=[1990,1992,1993,1995,1997,2000,2021]
# c=os.getcwd()
# print(c)
# for i in y:
#      os.mkdir(str(i))
#      p=f'{c}\{str(i)}'
#      print(p)
#      os.chdir(p)
#      for j in range(1,13):
#          os.mkdir(str(j))
#      os.chdir(c)

import os.path
# filecheck=os.path.isfile(r'C:\Users\vasan\Desktop\f1\2.txt.txt')
# print(filecheck)
# foldercheck=os.path.isdir(r'C:\Users\vasan\Desktop\f1')
# print(foldercheck)


y1=[2021,1990,1991,2022]
s=set(y)
s1=set(y1)
o=s1.difference(s)
print(o)
c=os.getcwd()
for i in o:
     os.mkdir(str(i))
     p=f'{c}\{str(i)}'
     print(p)
     os.chdir(p)
     for j in range(1,13):
          os.mkdir(str(j))
     os.chdir(c)

