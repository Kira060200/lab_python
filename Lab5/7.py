f=open("obiecte.txt","r")
g=open("rucsac.txt","w")
n=int(f.readline())
import math
i=0
l=[]
#print(n)
while i<int(n):
    x=f.readline()
    l.append(tuple(x.split()))
    i+=1
#print(l)
G=int(f.readline())
#print(G)
f.close()
l.sort(key=lambda x:float(int(x[1])/int(x[0])))
#print(l)
g.write("greutate:"+"\n")
g.write(str(G)+"=")
i=0
cd=0
value=0
while G:
    for x in l:
        if G-int(x[1])>=0:
            g.write(x[1]+("+" if G-int(x[1])!=0 else "\n"))
            G-=int(x[1])
            i+=1
        elif G!=0:
            cd=math.gcd(G,int(x[1]))
            g.write(str(int(G/cd))+"/"+str(int(int(x[1])/cd))+"*"+x[1]+"\n")
            value=G
            i+=1
            G=0
sum=0
for j in range(i):
    if j!=i-1 or cd==0:
        g.write(l[j][0]+("+" if j!=i-1 else ""))
        sum+=int(l[j][0])
    if j==i-1 and cd !=0:
        g.write(str(int(value/cd))+"/"+str(int(int(l[j][1])/cd))+"*"+l[j][0])
        sum+=int(int(value/cd)*int(l[j][0])/int(int(l[j][1])/cd))
g.write("="+str(sum))