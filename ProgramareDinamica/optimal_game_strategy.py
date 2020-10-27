n=int(input())
v=[int(input()) for i in range (n+1)]
#print(v)
T=[[0]*(n+1) for i in range(n+1)]
for i in range(1,n):
    T[i][i]=v[i]
    T[i][i+1]=max(v[i],v[i+1])
for len in range(2,n+1):
    for i in range(1,i+len):
        if i+len<=n:
            T[i][i+len]=max(v[i]+min(T[i+2][i+len],T[i+1][i+len-1]),v[i+len]+min(T[i+1][i+len-1],T[i][i+len-2]))
print(T[1][n])