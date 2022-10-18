#instance method
'''class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
       # self.average()
    def average(self):
        print((self.m1+self.m2+self.m3)/3)
s1=student(10,30,50)
s2=student(50,30,80)
#s1.average()
#s2.average()

#classmethod
class student:
    inst="devi"#static variable
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        print((self.m1+self.m2+self.m3)/3)
    @classmethod
    def m1(cls):
        print(cls.inst)
s1=student(10,30,50)
s2=student(50,30,80)
s1.average()
s2.average()
student.m1()

#static method
class student:
    inst="devi"#static variable
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        print((self.m1+self.m2+self.m3)/3)
    @classmethod
    def m1(cls):
        print(cls.inst)
    @staticmethod
    def m2():
        print("hello")
s1=student(10,30,50)
s2=student(50,30,80)
s1.average()
s2.average()
student.m1()
student.m2()

#where we can access static variable
class test:
    a=200#static variable
    def __init__(self):
        print("inside the constructor")
        print(self.a)
        print(test.a)
    def m1(self):
        print("inside the instance method")
        print(self.a)
        print(test.a)
    @classmethod
    def m2(cls):
        print("inside the class method")
        print(cls.a)
        print(test.a)
    @staticmethod
    def m3():
        print("inside static method")
        print(test.a)
t=test()
t.m1()
t.m2()
t.m3()
print("outside of the class")
print(t.a)
print(test.a)


#garbage collector
import gc
print(gc.isenabled())
print(gc.disable())
print(gc.isenabled())
print(gc.enable())
print(gc.isenabled())

#destructor
import time
class test:
    def __init__(self):
        print("constructor executed")
    def __del__(self):
        print("destructor execution")
t=test()
time.sleep(3)'''

# inner and outer class
class outer:
    def __init__(self):
        print("outer class constructor")
    #def f1(self):
        #print("outer class method")
    class inner:
        def __init__(self):
            print("inner class constructor")
        def m1(self):
            print("inner class method")
#o=outer()
#i=o.inner()
#i.m1()
#OR
#i=outer().inner()
#i.m1()
#or
#outer().f1()
outer().inner().m1()