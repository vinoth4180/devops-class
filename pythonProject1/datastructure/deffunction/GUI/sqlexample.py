# from tkinter import *
# import sqlite3
# conn=sqlite3.connect(r"C:\Users\vasan\training.db")
# cur=conn.cursor()
#
# ## creating form
# # root = Tk()
# # root.title("Student Form")
# # root.geometry('900x480')
# #
# # root.mainloop()
#
# root = Tk()
# root.title("Student Form")
# root.geometry('900x480')
#
#
# def submitchanges():
#     sql=f"insert into student values ( {snov.get()},'{namev.get()}',{m1.get()},{m2.get()},{m3.get()})"
#     print(sql)
#     cur.execute(sql)
#     conn.commit()
#     cur.close()
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

# from tkinter import *
# import sqlite3
#
# conn=sqlite3.connect(r"C:\Users\vasan\training.db")
# root=Tk()
# root.title('checkbutton')
# root.geometry('600x400')
# var=IntVar()
# cv= IntVar()
# cv1= IntVar()
# cv2= IntVar()
# cv3= IntVar()
# ivd=IntVar()
# ivd.set("")
# def sel():
#     selection=str(var.get())
#     print(selection)
#
# def savd():
#     iv=ivd.get()
#     cvv=cv.get()
#     cp=cv1.get()
#     jv=cv2.get()
#     pv=cv3.get()
#     cur = conn.cursor()
#     strv=""
#     l=[]
#     if cvv==1:
#         l.append("C")
#     if cp==1:
#         l.append("C++")
#     if jv==1:
#         l.append("Java")
#     if pv==1:
#         l.append("Python")
#     for i in range(len(l)):
#         if i==0:
#             v=""
#             v=l[i]
#             strv+=v
#         else:
#             v=","
#             v=v+l[i]
#             strv+=v
#     print(strv)
#     cur.execute('insert into studentinterest values(?,?)',(iv,str(strv)))
#     cur.close()
#     conn.commit()
#     root.destroy()
#
#
#
# Label(root,text='Student ID : ').grid(row=0,column=0)
# Entry(root,textvariable=ivd).grid(row=0,column=1)
#
# Radiobutton(root,text="option1",variable=var,value=1,command=sel).grid(row=1,column=0)
# Radiobutton(root,text="option2",variable=var,value=2,command=sel).grid(row=1,column=1)
# Radiobutton(root,text="option3",variable=var,value=3,command=sel).grid(row=1,column=2)
# Radiobutton(root,text="option4",variable=var,value=4,command=sel).grid(row=1,column=3)
# Label(root,text='Interested in : ').grid(row=2,column=0)
# Checkbutton(root,text="C",variable= cv).grid(row=3,column=0)
# Checkbutton(root,text="C++",variable= cv1).grid(row=3,column=1)
# Checkbutton(root,text="Java",variable = cv2).grid(row=3,column=2)
# Checkbutton(root,text="Python",variable = cv3).grid(row=3,column=3)
#Button(root,text="submit",command=savd).grid(row=4,column=1)
# root.mainloop()
#
# from tkinter import *
# root=Tk()
# root.title('calci')
# root.geometry('400x400')
# number1=IntVar()
# number2=IntVar()
# operators=StringVar()
# output=IntVar()
# number1.set('')
# number2.set('')
# operators.set('')
# output.set('')
# def sol():
#     if operators.get()=='+':
#         output.set(number1.get()+number2.get())
#     elif operators.get()=='-':
#         output.set(number1.get()-number2.get())
#     elif operators.get()=='*':
#         output.set(number1.get()*number2.get())
#     elif operators.get()=='/':
#         if number2.get()==0:
#             output.set('mathematical error')
#         else:
#             output.set(number1.get()/number2.get())
#     else:
#         output.set('invalid operation')
# Label(root,text='Num1').grid(row=0,column=0)
# Entry(root,textvariable=number1).grid(row=0,column=1)
# Label(root,text='Num2').grid(row=1,column=0)
# Entry(root,textvariable=number2).grid(row=1,column=1)
# Label(root,text='Operator').grid(row=2,column=0)
# Entry(root,textvariable=operators).grid(row=2,column=1)
# Label(root,text='Output').grid(row=3,column=0)
# Entry(root,textvariable=output).grid(row=3,column=1)
# Button(root,text='Result',command=sol).grid(row=4,column=1)
#
# root.mainloop()

from tkinter import *
import sqlite3

conn=sqlite3.connect(r'C:\Users\vasan\training.db')
root=Tk()
root.title('checkbutton')
root.geometry('600x400')
var=IntVar()
cv= IntVar()
cv1= IntVar()
cv2= IntVar()
cv3= IntVar()
ivd=IntVar()
ivd.set("")
def sel():
    selection=str(var.get())
    if selection=='1':
        return "INDIA"
    elif selection=='2':
        return "UNITED STATE"
    elif selection=='3':
        return "RUSSIA"
    else:
        return "United Kingdom"

def savd():
    iv=ivd.get()
    cvv=cv.get()
    cp=cv1.get()
    jv=cv2.get()
    pv=cv3.get()
    c=sel()
    cur = conn.cursor()
    strv=""
    l=[]
    if cvv==1:
        l.append("C")
    if cp==1:
        l.append("C++")
    if jv==1:
        l.append("Java")
    if pv==1:
        l.append("Python")
    for i in range(len(l)):
        if i==0:
            v=""
            v=l[i]
            strv+=v
        else:
            v=","
            v=v+l[i]
            strv+=v
    print(strv)
    cur.execute('insert into studentinterest values(?,?,?)',(iv,str(strv),c))
    cur.close()
    conn.commit()
    root.destroy()



Label(root,text='Student ID : ').grid(row=0,column=0)
Entry(root,textvariable=ivd).grid(row=0,column=1)

Radiobutton(root,text="IND",variable=var,value=1,command=sel).grid(row=1,column=0)
Radiobutton(root,text="USA",variable=var,value=2,command=sel).grid(row=1,column=1)
Radiobutton(root,text="RUSSIA",variable=var,value=3,command=sel).grid(row=1,column=2)
Radiobutton(root,text="UK",variable=var,value=4,command=sel).grid(row=1,column=3)
Label(root,text='Interested in : ').grid(row=2,column=0)
Checkbutton(root,text="C",variable= cv).grid(row=3,column=0)
Checkbutton(root,text="C++",variable= cv1).grid(row=3,column=1)
Checkbutton(root,text="Java",variable = cv2).grid(row=3,column=2)
Checkbutton(root,text="Python",variable = cv3).grid(row=3,column=3)
Button(root,text="submit",command=savd).grid(row=4,column=1)
root.mainloop()








