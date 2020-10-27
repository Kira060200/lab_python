def min_max(*values):
    if values:
        for x in values:
            if x!=0:
                if int(x)!=x or x<0:
                    return None
        return min(values),max(values)
    else: return None
#print(min_max(3,17,10,0,11))
try:
    f=open("numere.txt","r")
    g = open("impartire.txt", "w")
    x = f.readline()
    x = x.split()
    l=[]
    for a in x:
        l.append(int(a))
    try:
        a,b=(min_max(*l))
        g.write(str(b/a))
    except: print("Eroare la parsare")
except:
    print("Eroare de citire")