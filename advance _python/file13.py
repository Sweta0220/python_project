#how to store data in csv file
import csv
with open("emp.csv",'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(["eno","ename","esal","eaddress"])
    n= int(input("Enter no employees:"))
    for i in range(n):
        eno=input("enter employee no:")
        ename=input("enter employee name:")
        esal=input("enter employee sal:")
        eaddress=input("enter employee address:")
        w.writerow([eno,ename,esal,eaddress])
        print("employee data written to csv file successfully")

