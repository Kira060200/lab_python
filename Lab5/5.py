f=open("activitati.txt","r")
g=open("intarzieri.txt","w")
n=int(f.readline())
l=[tuple(x.split()) for x in f.readlines()]
f.close()
l.sort(key=lambda x:int(x[1]))
f=0
t=0
maxi=0
for x in l:
    f+=int(x[0])
    if f>int(x[1]):
        t=f-int(x[1])
    g.write(str(f-int(x[0]))+"-->"+str(f)+"\t"+x[1]+"\t"+str(t)+"\n")
    if t>maxi:
        maxi=t
        t=0
g.write("Intarziere maxima:"+str(maxi))
g.close()