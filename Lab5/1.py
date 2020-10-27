f=open("tis.txt","r")
l=[int(i) for i in f.read().split()]
L=[(i,l[i-1]) for i in range(1,len(l)+1)]
print(L)
def afisare_timpi_servire(L):
    s=0
    num=0
    #print(s)
    for i in range(0,len(L)):
        s += L[i][1]
        num+=s
        print("{}\t{}\t{}".format(*L[i],s))
    print(round(num/len(L),2))
afisare_timpi_servire(L)
L2=sorted(L,key=lambda x:x[1])
afisare_timpi_servire(L2)

# for y in x:
#     t=t+(i,y)
#     i+=1
# for x in t:
#     print(x,y)
#


