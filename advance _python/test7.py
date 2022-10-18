#Encapsulation
'''class test:
    x=10
    _y=20
    __z=30
    def __init__(self):
        print(self.x)
        print(self._y)
        print(self.__z)
t=test()
print(t.x)
print(t._y)
print(t.__z)

class parent:
    x=20
    _y=30
    __z=50
class child(parent):
    print(parent.x)
    print(parent._y)
    print(parent.__z)
class car:
     def __init__(self):
         pass
     def __updatesoftware(self):
         print("updating car software")
c=car()'''

class car:
    __name=""
    __maxspeed=0
    def __init__(self):
        self.__name="figo"
        self.__maxspeed=100
    def drive(self):
        print("car name:",self.__name)
        print("car drive with a speed:",self.__maxspeed)
c=car()
c.drive()
c.__maxspeed=200
c.drive()