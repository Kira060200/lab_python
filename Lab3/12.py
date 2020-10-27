f=open("departajare.txt","r")
l=[]
se=set()
d={}
i=0
for s in f:
    x=s.split()
    i+=1
    if x[0]!="-1":
        l.append((x[0],x[1]+" "+x[2],i))
        if x[0] not in se:
            se.add(int(x[0]))
        d.setdefault(int(x[0]),[])
        d[int(x[0])].append((x[1]+" "+x[2],i))
print(l)
print(se)
for key in sorted(d,reverse=True):
    print(key,d[key])