f=open("inventar.txt","r")
d={}
l=[]
count=0
for x in f:
    y=x.split()
    l.append(y[0])
    d.setdefault(y[0],[])
    for i in range(1,len(y)):
        d[y[0]].append(y[i])
    count+=1
print("Intersectie:",end="")
for i in d[l[0]]:
    ok=True
    for j in range(count):
        if i not in d[l[j]]:
            ok=False
    if ok:
        print(i)
l2=[]
print("Reuniune:",end="")
for x in d.values():
    for i in x:
        if i not in l2:
            l2.append(i)
print(l2)
k=0
for x in d.values():
    print(l[k],end=" ")
    for y in x:
        ok = True
        for i in range(count):
            if y in d[l[i]] and k!=i:
                ok=False
        if ok:
            print(y,end=" ")
    print("")
    k+=1
#print(d)
#print(l)
#print(d[l[1]])