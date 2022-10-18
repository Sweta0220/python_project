'''class A:
    def __init__(self):
        print("A class constructor")
class B(A):
    def __init__(self):
        print("B class constructor")
class C(B):
    def __init__(self):
        print("C class constructor")
c=C()

class A:
    def __init__(self):
        print("A class constructor")
class B():
    def __init__(self):
        print("B class constructor")
class C(A,B):
   def __init__(self):
        print("C class constructor")
c=C()

#polymorphism
#operator overloading
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1=book(10)
b2=book(20)
print(b1+b2)

#method overriding
class parent:
    def asset(self):
        print("cash+gold+lands")
    def car(self):
        print("alto car")
class child(parent):
    #pass
    def car(self):
       # super().car()
        print("benz car")
c=child()
c.asset()
c.car()

#constructor over riding
class parent:
    def __init__(self):
        print("parent class constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("child class constructor")
c=child()'''

#abstract class

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def wheel(self):
        pass
    def enginetype(self):
        print("bs-6 engine")
class car(vehicle):
    def wheel(self):
        print("car:4wheels")
    def color(self):
        print("color:red")
class bike(vehicle):
    def wheel(self):
        print("bike:2wheels")
    def color(self):
        print("color:blue")
c=car()
c.wheel()
c.color()
b=bike()
b.wheel()
b.enginetype()
b.color()