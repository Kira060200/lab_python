f=open("activitati.txt","r")
n=int(f.readline())
l=[tuple(x.split()) for x in f.readlines()]
l.sort(key=lambda x:int(x[1]))
print(l)
h1=0
s=0
for x in l:
    late=int(x[0])+s-int(x[1])
    if late>h1:
        h1=late
    s+=int(x[0])
print(h1)