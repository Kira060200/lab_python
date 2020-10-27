import operator
g=open("rime.txt","w")
s=input("Dati numele fisierului de intrare:")
f=open(s,"r")
d={}
x=f.readline()
x=x.split()
for y in x:
        key=y[len(y)-2:len(y)]
        d.setdefault(key,[])
        d[key].append(y)
        d[key].sort()
g.write(str(d))
