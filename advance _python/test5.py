'''class test:
    def __init__(self):
        self.a=10
    def m1(self):
        self.b=20
t=test()
t.c=30
print(t.__dict__)

class test:
    def __init__(self):
        self.a=10
    def m1(self):
        self.b=20
t=test()
t.m1()
t.c=30
print(t.__dict__)

#how to access instance variable
class test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        print(self.a)
        print(self.b)
t=test()
print(t.a)
print(t.b)

# how to delete instance variable
class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        del self.a
#t=test()
#print(t.__dict__)
t1=test()
t2=test()
t1.m1()
del t2.b
t1.c=99
#t2.m1()
print(t1.__dict__)
print(t2.__dict__)

#staic variable
class test:
    a=10#static or class level variable
    def __init__(self):
        self.b=20#instance variable
t1=test()
t2=test()
print(t1.a,t1.b)
print(t2.a,t2.b)

#test.a=99
#print(t1.a,t1.b)
#print(t2.a,t2.b)
t1.b=25
print(t1.a,t1.b)
print(t2.a,t2.b)'''

#local variable

class test:
    def m1(self):
        #a=10
        #print(a)
        self.a=10
        print(self.a)
    def m2(self):
        b=20
        print(b)
        print(self.a)
t=test()
t.m1()
t.m2()
