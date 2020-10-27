f=open("cuburi.txt","r")
g=open("turn.txt","w")
n=int(f.readline())
#print(n)
l=[tuple(s.split()) for s in f.readlines()]
f.close()
#print(l)
l.sort(key=lambda x:int(x[0]),reverse=True)
#print(l)
g.write("{} {}\n".format(*l[0]))
color=l[0][1]
h=int(l[0][0])
for i in l[1:]:
    if i[1]!=color:
        g.write("{} {}\n".format(*i))
        color=i[1]
        h+=int(i[0])
g.write("Inaltime totala:"+str(h))
g.close()