f=open("bani.txt","r")
g=open("plata.txt","w")
l=[int(x) for x in f.readline().split()]
s=int(f.readline())
f.close()
l.sort(reverse=True)
g.write(str(s)+" = ")
for x in l:
    count=0
    while s>=x:
        count+=1
        s-=x
    if count:
        g.write(str(x)+"*"+str(count)+(" + " if s!=0 else ""))
g.close()