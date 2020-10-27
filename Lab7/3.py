#cele 2 suma sa fie cat ma apropiate
f=open("date3.in")
A=[int(x) for x in f.readline().split()]
print(A)
A1=[]
A2=[]
suma=sum(A)//2
print(suma)
n=len(A)
#T[i][j] daca suma poate fi obtinuta folosind unele dintre primele elemente
T=[[None]*(suma+1) for i in range(n+1)]

for j in range(1,suma+1):
    T[0][j]=False
for i in range(0,n+1):
    T[i][0]=True

for i in range(1,n+1):
    for j in range(1,suma+1):
        if A[i-1]>j:
            T[i][j]=T[i-1][j]
        else:
            T[i][j]=T[i-1][j] or T[i-1][j-A[i-1]]
print(*T,sep="\n")

i=n
for j in range(suma,-1,-1):
    if T[i][j]:
        break
while i>0:
    if T[i-1][j]==True:
        A2.append(A[i-1])
    else:
        A1.append(A[i-1])
        j-=A[i-1]
    i-=1
print(A1)
print(A2)