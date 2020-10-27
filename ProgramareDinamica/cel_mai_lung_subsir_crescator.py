n=int(input())
v=[]
T=[1]*n
Pred=[0]*n
for i in range(n):
    x=int(input())
    v.append(x)
for i in range(n):
    for j in range(i):
        if v[i]>v[j] and T[i]<T[j]+1:
            T[i]=T[j]+1
            Pred[i]=j
print(T)
print(Pred)