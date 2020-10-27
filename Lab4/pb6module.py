def citire():
    n=int(input("Dati valoare lui n:"))
    v=[]
    for i in range(n):
        v.append(int(input()))
    return n,v
def afisare(v):
    print(v)
def valpoz(v):
    l=[]
    for x in v:
        if x>0:
            l.append(x)
    return l
def semn(v):
    l=[]
    for x in v:
        l.append(0-x)
    v=l
    #print(v)
    return v