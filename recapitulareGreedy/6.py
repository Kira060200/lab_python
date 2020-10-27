f=open("spectacole2.txt","r")
l=[tuple(x.replace("-"," ").split()) for x in f.readlines()]
f.close()
l.sort(key=lambda x:x[0])
nr=0
L=[]
fin=[]
L.append(str(l[0])+",")
fin.append(l[0][1])
for x in l[1:]:
    ok = False
    j = 0
    while j <= nr:
        if x[0] >= fin[j]:
            ok = True
            fin[j] = x[1]
            L[j] += (str(x) + ",")
            break
        j += 1
    if ok == False:
        nr += 1
        fin.append(x[1])
        L.append(str(x) + ",")
print(str(nr + 1) + " sali")
for x in L:
    print(x)

