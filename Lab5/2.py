f=open("spectacole.txt","r")
l=[tuple(s.replace("-"," ",1).split(" ",2)) for s in f.readlines()]
l.sort(key=lambda x:x[1])
#print(l)
print(l[0])
time=l[0][1]
for i in range(1,len(l)):
    if l[i][0]>time:
        print(l[i])
        time=l[i][1]