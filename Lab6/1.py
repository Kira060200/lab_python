f=open("rucsac.in","r")
g=open("rucsac.out","w")
G=int(f.readline())
l=[tuple(x.split()) for x in f.readlines()]
f.close()
L=sorted(l,key=lambda x:int(x[1])/int(x[0]),reverse=True)
for x in L:
    if G-int(x[0])>=0:
        g.write(str(1+l.index(x))+" "+str(x)+" "+str(int(x[1])/int(x[0]))+" 1"+"\n")
        G-=int(x[0])
    else:
        if G==0:
            break
        else:
            proc=G/int(x[0])
            g.write(str(1+l.index(x)) + " " + str(x) + " " + str(int(x[1]) / int(x[0])) + " "+str(round(proc,3)))
            G=0
g.close()