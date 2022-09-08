#
# #####single inheritance
class parent:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
    def parentdetails(self):
        print(f'parent_details = {self.name},{self.age},{self.location}')
class children(parent):
    def __init__(self,name,age,location,cname,cage,clocation):
        parent.__init__(self,name,age,location)
        parent.parentdetails(self)
        self.cname=cname
        self.cage=cage
        self.clocation=clocation
    def child(self):
        print(f'children details = {self.cname},{self.cage},{self.clocation}')

a=children('vinoth',26,'chennai','sri',2,'chennai')
a.child()




#####multilevel inheritance
# class grandfather:
#     def __init__(self,name,age,location):
#         self.name=name
#         self.age=age
#         self.location=location
#     def grandfatherdetails(self):
#         print(f'grandfather_details = {self.name},{self.age},{self.location}')
# class father(grandfather):
#     def __init__(self,name,age,location,fname,fage,flocation):
#         grandfather.__init__(self,name,age,location)
#         grandfather.grandfatherdetails(self)
#         self.fname=fname
#         self.fage=fage
#         self.flocation=flocation
#     def fatherdetails(self):
#         print(f'father details = {self.fname},{self.fage},{self.flocation}')
#
# class son(father):
#     def __init__(self,name,age,location,fname,fage,flocation,sname,sage,slocation):
#         father.__init__(self,name,age,location,fname,fage,flocation)
#         father.fatherdetails(self)
#         self.sname=sname
#         self.sage=sage
#         self.slocation=slocation
#     def sondetails(self):
#         print(f'son details = {self.sname},{self.sage},{self.slocation}')
# a=son('a',85,'chennai','b',30,'chennai','c',10,'chennai')
# a.sondetails()

#####multiple
# class father:
#     def __init__(self,name,age,location):
#         self.name=name
#         self.age=age
#         self.location=location
#     def fatherdetails(self):
#         print(f'father_details = {self.name},{self.age},{self.location}')
#
# class mother:
#     def __init__(self,mname,mage,mlocation):
#         self.mname=mname
#         self.mage=mage
#         self.mlocation=mlocation
#     def motherdetails(self):
#         print(f'mother_details = {self.mname},{self.mage},{self.mlocation}')
#
# class children(father,mother):
#     def __init__(self,name,age,location,mname,mage,mlocation,cname,cage,clocation):
#         father.__init__(self,name,age,location)
#         father.fatherdetails(self)
#         mother.__init__(self,mname,mage,mlocation)
#         mother.motherdetails(self)
#         self.cname=cname
#         self.cage=cage
#         self.clocation=clocation
#     def childdetails(self):
#         print(f'child_details = {self.cname},{self.cage},{self.clocation}')
#
# a=children('a',30,'ch','b',29,'ch','c',4,'ch')
# a.childdetails()

####Hierarchical Inheritance
# class School:
#     def __init__(self,sname, slocation):
#         self.sname = sname
#         self.slocation = slocation
#     def printschool(self):
#         print("Name of the school:",self.sname)
#         print("Location:", self.slocation)
# class student1(School):
#     def __init__(self,sname,slocation,s1name,s1age,s1class):
#         School.__init__(self,sname,slocation)
#         School.printschool(self)
#         self.s1name=s1name
#         self.s1age=s1age
#         self.s1class=s1class
#     def printstudent1(self):
#         print("Name:",self.s1name)
#         print("Age:", self.s1age)
#         print("Studing class:",self.s1class)
#
# class student2(School):
#     def __init__(self,sname,slocation,s2name,s2age,s2class):
#         School.__init__(self,sname,slocation)
#         School.printschool(self)
#         self.s2name=s2name
#         self.s2age=s2age
#         self.s2class=s2class
#     def printstudent2(self):
#         print("Name:",self.s2name)
#         print("Age:", self.s2age)
#         print("Studing class:",self.s2class)
#
#
#
# s1=student1("Mcc campus","Tambaram","Hagiolin",7,"1st standered")
# # s1.printschool()
# s1.printstudent1()
# print("***************")
# s2=student2("Mcc campus","Tambaram","Ewalds Castro",15,"9Th standered")
# # s2.printschool()
# s2.printstudent2()

#####hybrid
# class fatherofson:
#     def __init__(self,gname,age,location):
#         self.gname=gname
#         self.age=age
#         self.location=location
#     def printfatherofson(self):
#         print("Name:", self.gname)
#         print("Age:", self.age)
#         print("Location:", self.location)
#
# class son1(fatherofson):
#     def __init__(self, gname, age, location,fname, fage, flocation):
#         fatherofson.__init__(self,gname, age, location)
#         #parent.printfatherofson(self)
#         self.fname = fname
#         self.fage = fage
#         self.flocation = flocation
#     def printson1(self):
#         print("....father of father.....")
#         fatherofson.printfatherofson(self)
#         print(".....son1(father).....")
#         print("Name:",self.fname)
#         print("Age:",self.fage)
#         print("Location:",self.flocation)
# class son2(fatherofson):
#     def __init__(self, gname, age, location,cname, cage, clocation):
#         fatherofson.__init__(self, gname, age, location)
#         self.cname = cname
#         self.cage = cage
#         self.clocation = clocation
#     def printson2(self):
#         print("Name:",self.cname)
#         print("Age:",self.cage)
#         print("Location:",self.clocation)
#
#
#
# class fatherofmother:
#     def __init__(self,fmname,fmage,fmlocation):
#         self.fmname=fmname
#         self.fmage=fmage
#         self.fmlocation=fmlocation
#     def printfatherofmother(self):
#         print("Name:", self.fmname)
#         print("Age:", self.fmage)
#         print("Location:", self.fmlocation)
#
# class daughter(fatherofmother):
#     def __init__(self,fmname,fmage,fmlocation,dname,dage,dlocation ):
#         fatherofmother.__init__(self,fmname,fmage,fmlocation)
#         #parent.printparent(self)
#         self.dname = dname
#         self.dage = dage
#         self.dlocation = dlocation
#     def printdaughter(self):
#         print(".....Father of mother.......")
#         fatherofmother.printfatherofmother(self)
#         print("....Mother......")
#         print("Name:",self.dname)
#         print("Age:",self.dage)
#         print("Location:",self.dlocation)
#
#
# class grandchild(son1,daughter):
#     def __init__(self,gname, age, location,fname, fage, flocation,fmname, fmage, fmlocation,dname,dage,dlocation,gcname,gcage,gclocation):
#         #fatherofson._init_(self, gname, age, location)
#         son1.__init__(self,gname, age, location,fname, fage, flocation)
#         #fatherofmother._init_(self, fmname, fmage, fmlocation)
#         daughter.__init__(self,fmname,fmage,fmlocation,dname,dage,dlocation)
#         son1.printson1(self)
#         daughter.printdaughter(self)
#         self.gcname=gcname
#         self.gcage=gcage
#         self.gclocation=gclocation
#     def printgrandchild(self):
#         print("....Me.....")
#         print("Name:", self.gcname)
#         print("Age:", self.gcage)
#         print("Location:", self.gclocation)
#
#
#
# grandc=grandchild("Thangaraj",65,"tvl","kings",36,"chennai","moses",61,"alvai","mettilda",33,"chrompet","Hagiolin",6,"chrompet chennai")
# grandc.printgrandchild()

# class University:
#   def __init__(self):
#     print("Contructor of the Base class")
#     # Initializing a class variable named univ to store university name:
#     self.univ = "MIT"
#   def display(self):  # Method to print the University Name:
#     print(f"The University name is: {self.univ}")
#
# # 1st Derived or Child Class of University Class:
# class Course(University):
#   def __init__(self):
#     # using "super" keyword to access members of the parent class having same name:
#     print("Constructor of the Child Class 1 of Class University")
#     University.__init__(self)
#     self.course = "CSE"
#   def display(self):  # Method to print the Course Name:
#     # using "super" keyword to access display method defined in the parent class:
#     print(f"The Course name is: {self.course}")
#     University.display(self)
#
# # 2nd Derived or Child Class of University Class:
# class Branch(University):
#   def __init__(self):
#     print("Constructor of the Child Class 2 of Class University")
#     self.branch = "Data Science"
#   def display(self):  # Method to print the Branch Name:
#     print(f"The Branch name is: {self.branch}")
#
# # Derived or Child Class of Class Course and Branch:
# class Student(Course, Branch):
#   def __init__(self,name):
#     print("Constructor of Child class of Course and Branch is called")
#     self.name = name
#     Branch.__init__(self)
#     Course.__init__(self)
#   def display(self):
#     print(f"The Name of the student is: {self.name}")
#     Branch.display(self)
#     Course.display(self)
#
# # Object Instantiation:
# ob = Student("Mettilda")  # Object named ob of the class Student.
# print()
# ob.display()    # Calling the display method of Student class.