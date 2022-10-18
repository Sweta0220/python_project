import pickle
class employee:
    def __init__(self,eno,ename,eaddress):
        self.eno=eno
        self.ename=ename
        self.eaddress=eaddress
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.eaddress)
with open("emp.dat","wb") as f:
    e=employee(101,"sai","hyderabad")
    pickle.dump(e,f)
    print("pickling of employee object completed")
# for unpickling
with open("emp.dat","rb") as f:
    obj=pickle.load(f)
    print("printing employee information after unpickling")
    obj.display()
