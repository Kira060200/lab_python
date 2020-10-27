n=int(input())
m=int(input())
v=[5,2,7,9,4,3,12,10,4]
w=[5,9,2,7,10,14,3,10,19]
T=[[0]*(n) for i in range(m+1)]
for i in range(n):
    for j in range(m):
        T[0][j]=0
        T[i][0]=0
        T[i][j]=max(T[i-1][j],T[i][j-1],T[i-1][j-1]+(v[i]==w[j]))
print(T[n-1][m-1])
