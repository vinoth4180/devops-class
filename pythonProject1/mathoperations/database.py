import sqlite3
con=sqlite3.connect('mathop.db')
cur=con.cursor()
cur.execute('create table addition(num1 int,num2 int,result int)')
cur.execute('create table subtraction(num1 int,num2 int,result int)')
cur.execute('create table multiplication(num1 int,num2 int,result int)')
cur.execute('create table division(num1 int,num2 int,result int)')
cur.close()
con.commit()