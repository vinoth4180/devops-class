import sqlite3
from flask import Flask,render_template,url_for,flash,request
app=Flask(__name__)
@app.route('/')
def vinoth():
    return render_template('index.html')
@app.route('/add')
def add():
    return render_template('add.html')
@app.route('/sub')
def sub():
    return render_template('subtraction.html')
@app.route('/multiple')
def mul():
    return render_template('multiple.html')
@app.route('/divide')
def div():
    return render_template('division.html')

@app.route("/saveadddetails", methods=["POST", "GET"])
def saveadddetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["num1"]
            b = request.form["num2"]
            c=int(a)+int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into addition (num1, num2, result) values (?,?,?)", (a, b, c))
                con.commit()
                msg = "successfully Added"
        except:
            con.rollback()
            msg = "We can not add to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()
@app.route("/savesubdetails", methods=["POST", "GET"])
def savesubdetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["num1"]
            b = request.form["num2"]
            c=int(a)-int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into subtraction (num1, num2, result) values (?,?,?)", (a, b, c))
                con.commit()
                msg = "successfully subtracted"
        except:
            con.rollback()
            msg = "We can not subtract to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()
@app.route("/savemultipledetails", methods=["POST", "GET"])
def savemultipledetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["num1"]
            b = request.form["num2"]
            c=int(a)*int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into multiplication (num1, num2, result) values (?,?,?)", (a, b, c))
                con.commit()
                msg = "successfully multiplied"
        except:
            con.rollback()
            msg = "We can not multiplied to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()
@app.route("/savedividedetails", methods=["POST", "GET"])
def savedividedetails():
    msg = "msg"
    if request.method == "POST":
        try:
            a = request.form["num1"]
            b = request.form["num2"]
            c=int(a)/int(b)
            with sqlite3.connect("mathop.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into division (num1, num2, result) values (?,?,?)", (a, b, c))
                con.commit()
                msg = "successfully divided"
        except:
            con.rollback()
            msg = "We can not divide to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/vadd")
def viewaff():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from addition")
    rows = cur.fetchall()
    msg="Addition"
    return render_template("view.html", msg=msg,rows=rows)
@app.route("/vsub")
def viewsub():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from subtraction")
    rows = cur.fetchall()
    msg="Subtraction"
    return render_template("view.html", msg=msg,rows=rows)
@app.route("/vmultiple")
def viewmultiple():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from multiplication")
    rows = cur.fetchall()
    msg="multiplication"
    return render_template("view.html", msg=msg,rows=rows)
@app.route("/vdivide")
def viewdivide():
    con = sqlite3.connect("mathop.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from division")
    rows = cur.fetchall()
    msg='division'
    return render_template("view.html", msg=msg,rows=rows)
app.run(debug=True,port=1234)