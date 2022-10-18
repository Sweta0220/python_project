import zipfile
from zipfile import*
f=ZipFile("files.zip",'r',zipfile.ZIP_STORED)
names=f.namelist()
for name in names:
    print("file name:",name)
    print("content of the file")
    f1=open(name,'r')
    print(f1.read())
    print()