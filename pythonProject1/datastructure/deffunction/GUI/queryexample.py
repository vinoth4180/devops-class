from tkinter import *
import cx_Oracle
dsn_tns=cx_Oracle.makedsn('LAPTOP-NOIBARN8','1521', service_name='XE')
conn=cx_Oracle.connect(user=r'hr',password=r'hr',dsn=dsn_tns)
cur=conn.cursor()
root=Tk()
root.title('Employee_display')
root.geometry('800x800')
emp_id_search=StringVar()
emp_id=StringVar()
first_name=StringVar()
last_name=StringVar()
salary=StringVar()
phone=StringVar()
department=StringVar()

def search():
    id=emp_id_search.get()
    sql=f"select * from employees where employee_id={id}"
    o=cur.execute(sql)
    for a in o:
        print(a)
    emp_id.set(a[0])
    first_name.set(a[1])
    last_name.set(a[2])
    salary.set(a[7])
    phone.set(a[4])
    department.set(a[10])


Label(root,text='emp_id_search').grid(row=0,column=0)
Entry(root,textvariable=emp_id_search).grid(row=0,column=1)
Button(root,text='submit',command=search).grid(row=0,column=2)
Label(root,text='emp_id').grid(row=1,column=0)
Entry(root,textvariable=emp_id).grid(row=1,column=1)
Label(root,text='first_name').grid(row=2,column=0)
Entry(root,textvariable=first_name).grid(row=2,column=1)
Label(root,text='last_name').grid(row=3,column=0)
Entry(root,textvariable=last_name).grid(row=3,column=1)
Label(root,text='salary').grid(row=4,column=0)
Entry(root,textvariable=salary).grid(row=4,column=1)
Label(root,text='phone').grid(row=5,column=0)
Entry(root,textvariable=phone).grid(row=5,column=1)
Label(root,text='department').grid(row=6,column=0)
Entry(root,textvariable=department).grid(row=6,column=1)

root.mainloop()

