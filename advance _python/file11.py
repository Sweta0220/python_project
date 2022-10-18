import zipfile
from zipfile import*
f=ZipFile("files.zip",'w',zipfile.ZIP_DEFLATED)
f.write("abc.txt")
f.write("abcd.txt")
f.write("durga.txt")
f.write("sample.txt")
f.close()
print("zip file created successfully")