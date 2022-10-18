data="my name sweta"
f=open("rrr.txt",'w')
f.write(data)
with open("rrr.txt","r+") as f:
    print("current cursor position:",f.tell())
    text=f.read()
    print(text)
    print("current cursor position:",f.tell())
    f.seek(11)
    print("current cursor position:", f.tell())
    f.write("sourav")
    f.seek(0)
    print("the data after modification")
    print(f.read())