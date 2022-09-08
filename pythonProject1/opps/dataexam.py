import sqlite3


class mains():
    def __init__(self):
        self.con = sqlite3.connect(r'company.db')
        self.database = self.con.cursor()
        self.database.execute(''' CREATE TABLE IF NOT EXISTS company(
                            ID INTEGER        PRIMARY KEY         NOT NULL,
                            NAME              TEXT                NOT NULL,
                            AGE               TEXT                NOT NULL,
                            DOB               TEXT                NOT NULL,
                            EMAIL             TEXT                NOT NULL,
                            GENDER            TEXT                NOT NULL,
                            CONTECT           TECT                NOT NULL,
                            ADDRESS           TEXT                NOT NULL  
                            ) ''')
        self.con.commit()

    def insert_data(self, id, name, age, dob, email, gender, contact, address):
        self.database.execute("INSERT INTO company  VALUES (?,?,?,?,?,?,?,?)",
                              (id, name, age, dob, email, gender, contact, address))
        self.con.commit()

    def fetchrec(self):
        self.con = sqlite3.connect(r'company.db')
        self.database = self.con.cursor()
        self.database.execute("select * from company")
        fetching = self.database.fetchall()
        # print(fetching)
        for a in fetching:
            print(a)

    def remove(self, id):
        self.database.execute("delete from company where id=?", (id,))
        self.con.commit()

    def update(self, id, name, age, dob, email, gender, contect, address):
        self.database.execute("update company set name=?,age=?,dob=?,email=?,gender=?,contect=?,address=? where id=?",
                              (name, age, dob, email, gender, contect, address, id))

        self.con.commit()


obj = mains()
obj.insert_data(41,'nantha','24','21,04,1995','nantha@gamil.com','male','1234567890','dharmapuritamilnadu')
# obj.remove(8)
# obj.update(2,'kumar123','23','21,4,1996','kumar@gamil.com','male','0987654321','salem,tamilnadu')
obj.fetchrec()
