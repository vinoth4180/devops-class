# import os
# print(os.getcwd())#current working directory
# os.chdir(r'C:\Users\vasan\Desktop\f1')#change directory
# l=os.listdir()
# print(l)
# os.chdir(r'C:\Users\vasan\Desktop\f2')
# l2=os.listdir()
# print(l2)
# i=set(l)
# j=set(l2)
# print(i.intersection(j))
# print(i.difference(j))

import re#regular expressions
import numpy as np
s='this is training is is training'
#print(s)
o=re.split(' ',s)
print(o)
a=np.array(o)
print(a)
unique,count=np.unique(a,return_counts=True)
print(unique)
print(count)