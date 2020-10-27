s=input()
l=[int(x) for x in s.split()]
a=l[0]
k=1
while a==l[k] and k<len(l):
    k+=1
if k==len(l):
    print("Nu exista 2 numere maxime distincte")
else:
    if(a>l[k]):
        maxi1=a
        maxi2=l[k]
    else:
        maxi1=l[k]
        maxi2=a
    for i in l[k+1:]:
        if i>maxi1:
            maxi2=maxi1
            maxi1=i
        elif i>maxi2:
            maxi2=i
    print(maxi1,maxi2)