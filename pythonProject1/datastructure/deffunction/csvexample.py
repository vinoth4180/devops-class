import csv
# with open('samplefile.csv','w',newline='') as f:
#     w=csv.writer(f)
#     w.writerow(['Sno','name','m1','m2','m3'])
#     w.writerow([1,'babu','89','91','94'])

import os.path
sno=int(input('enter the no'))
na=input("enter the name")
m1=int(input('enter the m1'))
m2=int(input('enter the m2'))
m3=int(input('enter the m3'))
total=m1+m2+m3
average=total/3
filecheck=os.path.isfile('samplefile2.csv')
if filecheck:
    with open('samplefile2.csv','a',newline='') as f:
        w=csv.writer(f)
        w.writerow([sno,na,m1,m2,m3,total,average])
else:
    with open('samplefile2.csv','a',newline='') as f:
        w=csv.writer(f)
        w.writerow(['sno','name','m1','m2','m3','total','average'])
        w.writerow([sno,na,m1,m2,m3,total,average])