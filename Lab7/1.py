#Problema monedelor
#nr minim monede necesare + monede folosite
f=open("date.in","r")
suma=int(f.readline())
M=[]
for x in f.readline().split():
    M.append(int(x))
f.close()

nrmin=[suma+1]*(suma+1)    #nr minim monede folosite
pred=[-1]*(suma+1)     #predecesori (valoare monedei,nu indicele)

nrmin[0]=0 #maxim posibil
for i in range(1,suma+1):
    for m in M:
        if m<=i and nrmin[i] > nrmin[i-m]+1:
            nrmin[i]=nrmin[i-m]+1
            pred[i]=m
print(nrmin)
print(pred)
if pred[suma]==-1:
    print(f"Suma {suma} nu poate fi obtinuta")
else:
    print(f"Summa {suma} a fost obtinuta din {nrmin[suma]} monede \n")
    poz=suma
    while pred[poz] !=-1:
        print(pred[poz],end=" ")
        poz-=pred[poz]

