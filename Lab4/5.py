s=input("Dati numele fisierului de iesire:")
g=open(s+".txt","w")
def negative_pozitive(l):
    l1=[]
    l2=[]
    for x in l:
        if x<0:
            l1.append(x)
        else: l2.append(x)
    return l1,l2
g.write(str(negative_pozitive([0,9,-4,0,3,-7,-88])))