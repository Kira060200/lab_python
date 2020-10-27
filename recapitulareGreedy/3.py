f=open("cuburi.txt","r")
g=open("turn.txt","w")
n=int(f.readline())
l=[tuple(x.split()) for x in f.readlines()]
l.sort(key=lambda x:int(x[0]),reverse=True)
color=l[0][1]
h=int(l[0][0])
g.write("{} {}\n".format(*l[0]))
for x in l:
    if x[1]!=color:
        g.write("{} {}\n".format(*x))
        color=x[1]
        h+=int(x[0])
g.write("Inaltimea totala:"+str(h))