def citireDate():
    f=open("data.in","r")
    l=[]
    for x in f.readline().split():
        l.append(int(x))
    n=int(f.readline())
    return l,n
def contor(lista,x,n):
def primaAparitie(lista, pozMinima, pozMaxima, x, n):
    try:
        return lista.index(x)
    except:
        return -1
def ultimaAparitie(lista, pozMinima, pozMaxima, x, n):
    try:
        return lista.index(x)
    except:
        return -1
lista,x=citireDate()
print(contor(lista,x,len(lista)))