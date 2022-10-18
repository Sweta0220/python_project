try:
    f=open("xyz.txt",'x')
    f.write("hello\n")
    f.write("hyderabad\n")
    print("data written to the file")
    f.close()
except FileNotFoundError as msg:
    print(msg)
