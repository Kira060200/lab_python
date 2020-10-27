#matrice nepatratica
#mergem doar in jos si in dreapta
f=open("date2.in")
n,m=f.readline().split()
n=int(n)
m=int(m)
M=[]

for x in f:
    M.append([int(i) for i in x.split()])

#print(*M,sep="\n")

#smax[i][j] suma elem care se termina in i,j
smax=[[0]*m for i in range(n)]
#print(smax)

smax[0][0]=M[0][0]
for j in range(1,m):
    smax[0][j] = smax[0][j-1] + M[0][j]
for i in range(1,n):
    smax[i][0] = smax[i-1][0] + M[i][0]

for i in range(1,n):
    for j in range(1,m):
        smax[i][j] = min(smax[i-1][j],smax[i][j-1]) + M[i][j]
print(*smax, sep="\n")

print(f"Suma maxima a drumului obtinut este:{smax[-1][-1]}")
i=n-1
j=m-1
while i!=0 or j!=0:
    print(M[i][j],end=" ")
    if i==0 or (j!=0 and smax[i][j-1]>=smax[i-1][j]):
        j-=1
    else: i-=1