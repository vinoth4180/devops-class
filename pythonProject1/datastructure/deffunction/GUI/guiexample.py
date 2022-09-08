# from tkinter import *
# root=Tk()
# root.title('student form')
# root.geometry('400x400')
# namev=StringVar()
# Snov=IntVar()
# m1v=IntVar()
# m2v=IntVar()
# m3v=IntVar()
# Snov.set('')
# m1v.set('')
# m2v.set('')
# m3v.set('')
#
# Label(root,text='Sno').grid(row=0,column=0)
# Entry(root,textvariable=Snov).grid(row=0,column=1)
# Label(root,text='Name').grid(row=1,column=0)
# Entry(root,textvariable=namev).grid(row=1,column=1)
# Label(root,text='m1').grid(row=2,column=0)
# Entry(root,textvariable=m1v).grid(row=2,column=1)
# Label(root,text='m2').grid(row=3,column=0)
# Entry(root,textvariable=m2v).grid(row=3,column=1)
# Label(root,text='m3').grid(row=4,column=0)
# Entry(root,textvariable=m3v).grid(row=4,column=1)
#
# root.mainloop()


from tkinter import *
import os.path
import csv
## creating form
# root = Tk()
# root.title("Student Form")
# root.geometry('900x480')
#
# root.mainloop()
#
# root = Tk()
# root.title("Student Form")
# root.geometry('900x480')
#
#
# def submitchanges():
#     # print(namev.get(),snov.get(),m1.get(),m2.get(),m3.get())
#     filecheck = os.path.isfile(r"C:\Users\vasan\Desktop\f1\samplefile4.csv")
#     total = m1.get() + m2.get() + m3.get()
#     avg = total / 3
#     if filecheck:
#         with open(r"C:\Users\vasan\Desktop\f1\samplefile4.csv", "a", newline="") as f:
#             w = csv.writer(f)
#             w.writerow([snov.get(), namev.get(), m1.get() ,m2.get() ,m3.get() ,total, avg])
#
#
#     else:
#         with open(r"C:\Users\vasan\Desktop\f1\samplefile4.csv", "a", newline="") as f:
#             w = csv.writer(f)
#             w.writerow(["S.no", "Name", "M1", "M2", "M3", "Total", "Average"])
#             w.writerow([snov.get(), namev.get(), m1.get() ,m2.get() ,m3.get() ,total, avg])
#     root.destroy()
# namev = StringVar()
# snov = IntVar()
# m1 = IntVar()
# m2 = IntVar()
# m3 = IntVar()
# Label(root,text="S.No").grid(row=0,column=0)
# Entry(root,textvariable=snov).grid(row=0,column=1)
# snov.set("")
#
# Label(root,text="Name").grid(row=1,column=0)
# Entry(root,textvariable=namev).grid(row=1,column=1)
#
#
# Label(root,text="M1").grid(row=2,column=0)
# Entry(root,textvariable=m1).grid(row=2,column=1)
# m1.set("")
#
# Label(root,text="M2").grid(row=3,column=0)
# Entry(root,textvariable=m2).grid(row=3,column=1)
# m2.set("")
#
# Label(root,text="M3").grid(row=4,column=0)
# Entry(root,textvariable=m3).grid(row=4,column=1)
# m3.set("")
#
# Button(root,text="Submit",command=submitchanges).grid(row=5,column=1)
#
# root.mainloop()

n=int(input('enter the number:'))
if n>=1:
    for x in range(2,n):
        if n%x==0:
            print('not a prime')
        break
    else:
        print('prime')