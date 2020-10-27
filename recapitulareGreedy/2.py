f=open("spectacole.txt","r")
l=[tuple(x.replace("-"," ").split(" ",2)) for x in f.readlines()]
l.sort(key=lambda x:x[1])
last=l[0][1]
print(l[0])
for y in l:
    if y[0]>=last:
        print(y)
        last=y[1]