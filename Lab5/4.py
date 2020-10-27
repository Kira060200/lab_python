f=open("bani.txt","r")
g=open("plata.txt","w")
l=[int(x) for x in f.readline().split()]
#print(l)
suma=int(f.readline())
#print(suma)
f.close()
l.sort(reverse=True)
#print(l)
g.write(str(suma)+" = ")
for x in l:
    nr=0
    while x<=suma:
        nr+=1
        suma-=x
    if nr>0:
        g.write(str(x)+"*"+str(nr)+(" + " if suma!=0 else ""))
g.close()