'''class branch:
    def get_branch_data(self):
        self.bcode=int(input("enter branch code:"))
        self.bname=input("enter branch name:")
        self.baddress=input("enter branch address")
    def display_branch_data(self):
        print("branch code is:",self.bcode)
        print("branch name is:",self.bname)
        print("branch address is:",self.baddress)
b=branch()
b.get_branch_data()
b.display_branch_data()

class branch:
    def get_branch_data(self):
        self.bcode=int(input("enter branch code:"))
        self.bname=input("enter branch name:")
        self.baddress=input("enter branch address")
    def display_branch_data(self):
        print("branch code is:",self.bcode)
        print("branch name is:",self.bname)
        print("branch address is:",self.baddress)
class employee:
    def get_emp_data(self):
        self.empid=int(input("enter empid:"))
        self.ename=input("enter ename:")
        self.eaddress=input("enter eaddress")
    def display_emp_data(self):
        print("emp id is:",self.empid)
        print("emp name is:",self.ename)
        print("emp address is:",self.eaddress)

b=branch()
b.get_branch_data()
b.display_branch_data()
e=employee()
e.get_emp_data()
e.display_emp_data()

#which employee belongs to which branch? so we do inheritance
#single inheritance
class branch:
    def get_branch_data(self):
        self.bcode=int(input("enter branch code:"))
        self.bname=input("enter branch name:")
        self.baddress=input("enter branch address")
    def display_branch_data(self):
        print("branch code is:",self.bcode)
        print("branch name is:",self.bname)
        print("branch address is:",self.baddress)
class employee(branch):
    def get_emp_data(self):
        self.empid=int(input("enter empid:"))
        self.ename=input("enter ename:")
        self.eaddress=input("enter eaddress")
    def display_emp_data(self):
        print("emp id is:",self.empid)
        print("emp name is:",self.ename)
        print("emp address is:",self.eaddress)
e=employee()
e.get_branch_data()
e.get_emp_data()
e.display_branch_data()
e.display_emp_data()

#multilevel inheritance
class branch:
    def get_branch_data(self):
        self.bcode=int(input("enter branch code:"))
        self.bname=input("enter branch name:")
        self.baddress=input("enter branch address")
    def display_branch_data(self):
        print("branch code is:",self.bcode)
        print("branch name is:",self.bname)
        print("branch address is:",self.baddress)
class employee(branch):
    def get_emp_data(self):
        self.empid=int(input("enter empid:"))
        self.ename=input("enter ename:")
        self.eaddress=input("enter eaddress")
    def display_emp_data(self):
        print("emp id is:",self.empid)
        print("emp name is:",self.ename)
        print("emp address is:",self.eaddress)
class empsalary(employee)
    def get_sal(self):
        self.basic=int(input("enter basic salary"))
    def calculate(self):
        self.DA=self.basic*0.03
        self.HRA=self.basic*0.4
        self.gross=self.basic+self.DA+self.HRA
    def displaysal(self):
        print("basic is:",self.basic)
        print("DA is:",self.DA)
        print("HRA is:",self.HRA)
        print("gross is:",self.gross)
e=empsalary()
e.get_branch_data()
e.get_emp_data()
e.get_sal()
e.calculate()
e.display_branch_data()
e.display_emp_data()
e.displaysal()

#heirarchical inheritance
class parent:
    def p1(self):
        print("parent class function")
class child1(parent):
    def c1(self):
        print("child1 class function")
class child2(parent):
    def c2(self):
        print("child2 class function")
obj1=child1
obj1.p1()
obj1.c1()
obj2=child2
obj2.p1()
obj2.c2()

#isinstance()
class parent:
    def p1(self):
        print("parent class function")
class child1(parent):
    def c1(self):
        print("child1 class function")
class child2(parent):
    def c2(self):
        print("child2 class function")
obj1=child1
obj2=child2
print(isinstance(obj1,child1))
#issubclass

#multiple inheritance
class A:
    def f1(self):
        print("f1 function of class A")


class B:
    def f2(self):
        print("f2 function of class B")


class C(A,B):
    def f3(self):
        print("f3 function of class C")
c=C()
c.f1()
c.f2()
c.f3()

#if there is a same function in class A and class B
class A:
    def f1(self):
        print("f1 function of class A")


class B:
    def f1(self):
        print("f1 function of class B")


class C(A,B):
#class C(B,A):#if we change class B and A then 1st priority given to class B
    def f3(self):
       # B.f1(self)#if we want B also
        #A.f1(self)# if we want A also if C(B,A)
        print("f3 function of class C")
c=C()
c.f1()
c.f3()'''

#hybrid inheritance
class A:
    def f1(self):
        print("f1 function of class A")


class B:
    def f1(self):
        print("f1 function of class B")


class C(A,B):
    def f3(self):
        print("f3 function of class C")

class D(C):
    def f4(self):
        print("f4 function of class D")

d=D()
d.f1()
d.f3()
d.f4()





