#exception handling
#syntactical error
'''def f1()
    print("hello")

def f1:
    print(hell
# name error
a=10
print(A)

#value error
a=int(input("enter a number"))
print(a)

#type error
print(10+"sai")

#zero division error
print(10/0)

a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=a/b
print("result is:",c)

#logicl implementation
a=int(input("enter num1:"))
b=int(input("enter num2:"))

if b==0:
    print("second num can not be zero")
else:
    c = a / b
    print("result is:",c)

#try except implementattion
try:
    a = int(input("enter num1:"))
    b = int(input("enter num2:"))
    c = a / b
    print("result is:", c)
except:
    print("something went wring")

try:
    a = int(input("enter num1:"))
    b = int(input("enter num2:"))
    c = a / b
    print("result is:", c)
except ZeroDivisionError as message:
    print(message)
except:
    print("something went wrong")

try:
    print("statement-1")
    print("statement-2")
    print("statement-3")
except:
    print("statement-4")
print("statement-5")

try:
    #print(10/0)
    print("try block")
except:
    print("except block")
finally:
    print("finally block")

import os
try:
    print(10/0)
    print("try block")
    os._exit(0)
except:
    print("except block")
    os._exit(0)
finally:
    print("finally block")

#nested try except finally
try:
    print("outer try")
    try:
        print("inner try")
    except:
        print("inner except")
    finally:
        print("inner finally")
except:
    print("outer except")
finally:
    print("outer finally")

#if there is an exception in outer try
try:
    print(10/0)
    print("outer try")
    try:
        print("inner try")
    except:
        print("inner except")
    finally:
        print("inner finally")
except:
    print("outer except")
finally:
    print("outer finally")
 #if there is an exception in inner try
try:
    print("outer try")
    try:
        print(10/0)
        print("inner try")
    except:
        print("inner except")
    finally:
        print("inner finally")
except:
    print("outer except")
finally:
    print("outer finally")

#how to create your own exception class
#userdefined or customized exception
class ToooldException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooyoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input("enter your age:"))
if age>=60:
    raise ToooldException("age should not 60 or more")
elif age<=16:
    raise TooyoungException("age should not 16 or below")
else:
    print(("you are eligible to take policy"))'''

#how to handle them
class ToooldException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooyoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
try:
    age = int(input("enter your age:"))
    if age >= 60:
        raise ToooldException("age should not 60 or more")
    elif age <= 16:
        raise TooyoungException("age should not 16 or below")
    else:
        print(("you are eligible to take policy"))
#except( TooyoungException,ToooldException,ValueError) as msg:
except Exception as msg:
    print(msg)



