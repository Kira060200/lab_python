f=open("tis.txt","r")
l=[int (i) for i in f.read().split()]
s=0
count=len(l)
timp=0
for a in l:
    s+=a
    timp+=s
print(timp)
print(round(timp/count,2))
print(l)
l.sort()
print(l)
s=0
timp=0
for a in l:
    s+=a
    timp+=s
print(round(timp / count, 2))