import csv
f=open("emp.csv",'r')
r=csv.reader(f)
data=list(r)
print(data)
#each list value how to get
for line in data:
    #print(line)
   for word in line:
      print(word,end=' ')




