from tkinter import *
import sqlite3
import csv
import os.path
root=Tk()
root.title('same form')
root.geometry('400x700')
num1=IntVar()
num2=IntVar()
result=IntVar()
s=IntVar()
num1.set('')
num2.set('')
def sel():
    o=s.get()
    a=num1.get()
    b=num2.get()
    if o==1:
        result.set(a+b)
    elif o==2:
        result.set(a-b)
    elif o==3:
        result.set(a*b)
    else:
        result.set('invalid')
def run():
    a=num1.get()
    b=num2.get()
    o=s.get()
    fc=fchk.get()
    dc=dchk.get()
    r=sel()
    if fc==1:
        filecheck = os.path.isfile('radiobutton1.csv')
        if filecheck:
            with open('radiobutton1.csv', 'a', newline='') as f:
                w = csv.writer(f)
                w.writerow([num1.get(),num2.get(),s.get(),result.get()])
        else:
            with open('radiobutton1.csv', 'a', newline='') as f:
                w = csv.writer(f)
                w.writerow(['number1', 'number2', 'result', 'op'])
                w.writerow([num1.get(),num2.get(),s.get(),result.get()])

        print('file is selected')



    if dc==1:
        conn = sqlite3.connect(r"C:\Users\vasan\training.db")
        cur = conn.cursor()
        sql = f"insert into radiobuttonexam values({a},{b},'{o}','{result.get()}')"
        cur.execute(sql)
        conn.commit()
        cur.close()
        print('database is selected')
        root.destroy()

Label(root,text='number1').grid(row=0,column=0)
Entry(root,textvariable=num1).grid(row=0,column=1)
Label(root,text='number2').grid(row=1,column=0)
Entry(root,textvariable=num2).grid(row=1,column=1)
Radiobutton(root,text='addition',variable=s,value=1,command=sel).grid(row=2,column=0)
Radiobutton(root,text='subtraction',variable=s,value=2,command=sel).grid(row=2,column=1)
Radiobutton(root,text='multiplication',variable=s,value=3,command=sel).grid(row=2,column=2)
fchk=IntVar()
dchk=IntVar()
Checkbutton(root,text='save to file',variable=fchk).grid(row=3,column=0)
Checkbutton(root,text='save to database',variable=dchk).grid(row=3,column=1)
Label(root,text='result').grid(row=4,column=0)
Entry(root,textvariable=result).grid(row=4,column=1)
Button(root,text='submit',command=run).grid(row=5,column=1)
result.set('')
root.mainloop()
