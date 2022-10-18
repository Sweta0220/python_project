#how to check wheather the file is exist or not
'''import os
fname=input("Enter file name to check:")
if os.path.isfile(fname):
    print("file is exist:",fname)
else:
    print("file does not exist:",fname)

# if file exist read the content of the file
import os
fname=input("Enter file name to check:")
if os.path.isfile(fname):
    print("file is exist:",fname)
    f=open(fname,'r')
    print("content of the file")
    print(f.read())
    f.seek(0)
else:
    print("file does not exist:",fname)'''

#