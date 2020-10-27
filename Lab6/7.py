f=open("date.in")
g=open("date.out","w")
n=int(f.readline())
a=[]
b=[]
for x in f.readline().split():
    a.append(int(x))
m=int(f.readline())
for x in f.readline().split():
    b.append(int(x))
