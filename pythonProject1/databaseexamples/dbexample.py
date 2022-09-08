from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")

        self.roll_no = StringVar()
        self.name = StringVar()
        self.father_name = StringVar()
        self.gen = StringVar()
        self.category = StringVar()
        self.branch = StringVar()
        self.year = StringVar()
        self.contact = StringVar()
        self.address= StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.totalrecord = StringVar()
        self.con = sqlite3.connect("mydb.db")
        self.database = self.con.cursor()
        sql='CREATE TABLE if not exists students1 (Roll_no text NOT NULL,Name text NOT NULL,Father_Name text NOT NULL,Gender text NOT NULL,Category text NOT NULL,Branch text NOT NULL,Year text NOT NULL,Contact_no text NOT NULL,Address text NOT NULL)'
        print(sql)
        self.database.execute(sql)
        headinglbl = Label(root, text="Student Management System", font=("arial", 24, "bold"), bg='wheat', fg='red')
        headinglbl.pack(side=TOP, fill=X)

        # ***********Frame-1***************
        entry_frame = Frame(root, bd=5, relief='ridge', bg='wheat')
        entry_frame.place(x=20, y=50, width=350, height=745)

        # Labels of frame-1
        reg_lbl = Label(entry_frame, text="Registration Form", font=("arial", 20, "bold"), bg='wheat', fg='red')
        reg_lbl.grid(row=0, columnspan=2)

        roll_lbl = Label(entry_frame, text="Roll no.", font=("", 13))
        roll_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        name_lbl = Label(entry_frame, text="Name", font=("", 13))
        name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        Fname_lbl = Label(entry_frame, text="Father's name", font=("", 13))
        Fname_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        gen_lbl = Label(entry_frame, text="Gender", font=("", 13))
        gen_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        cat_lbl = Label(entry_frame, text="Category", font=("", 13))
        cat_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        branch_lbl = Label(entry_frame, text="Branch", font=("", 13))
        branch_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        yr_lbl = Label(entry_frame, text="Year", font=("", 13))
        yr_lbl.grid(row=7, column=0, sticky='w', padx=10, pady=11)

        phn_lbl = Label(entry_frame, text="Contact no.", font=("", 13))
        phn_lbl.grid(row=8, column=0, sticky='w', padx=10, pady=11)

        add_lbl = Label(entry_frame, text="Address", font=("", 15))
        add_lbl.grid(row=9, column=0, sticky='w', padx=10, pady=11)

        # Entry box of Frame-1
        roll_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.roll_no)
        roll_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

        name_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.name)
        name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

        fname_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.father_name)
        fname_entry.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        gen_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.gen)
        gen_combo['values'] = ('Male', 'Female')
        gen_combo.current(0)
        gen_combo.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        cat_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.category)
        cat_combo['values'] = ('General', 'OBC', 'SC', 'ST')
        cat_combo.current(0)
        cat_combo.grid(row=5, column=1, sticky='w', padx=10, pady=11)

        branch_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.branch)
        branch_combo['values'] = (
        'Compter Science', 'Automobile', 'Civil', 'Mechanical', 'Production', 'Textile', 'Electronics')
        branch_combo.current(0)
        branch_combo.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        yr_combo = ttk.Combobox(entry_frame, state='readonly', width=27, textvariable=self.year)
        yr_combo['values'] = ('Year 1', 'Year 2', 'Year 3', 'Year 4')
        yr_combo.current(0)
        yr_combo.grid(row=7, column=1, sticky='w', padx=10, pady=11)

        phn_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.contact)
        phn_entry.grid(row=8, column=1, sticky='w', padx=10, pady=11)

        add_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.address)
        add_entry.grid(row=9, column=1, sticky='w', padx=10, pady=11)


root = Tk()
ob = Student(root)
root.mainloop()



