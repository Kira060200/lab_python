def ipotenuza(a,b):
    import math
    return math.sqrt(a**2+b**2)
#a=int(input())
#b=int(input())
#print(ipotenuza(a,b))
g=open("triplete_pitagorice","w")
b=int(input())
for a in range(1,b):
    c=ipotenuza(a,b)
    if c==int(c):
        g.write(str(a)+" "+str(b)+" "+str(int(c))+'\n')
