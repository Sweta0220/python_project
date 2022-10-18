'''try:
    f=open("mohan.txt",'r')
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError as msg:
    print(msg)

try:
    f=open("abcd.txt",'r')
    data=f.read(5)
    print(data)
    f.close()
except FileNotFoundError as msg:
    print(msg)'''

#readline()
try:
    f=open("abcd.txt",'r')
    #data=f.readline()
    data=f.readlines()
    print(data)
    f.close()
except FileNotFoundError as msg:
    print(msg)