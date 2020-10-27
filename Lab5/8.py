f=open("proiecte.txt","r")
g=open("profit.txt","w")
l=[tuple(x.split()) for x in f.readlines()]
print(l)
d={}
for x in l:
    d[int(x[1])].append(int(x[2]))
print(d)