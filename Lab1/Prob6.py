n=int(input("n="))
cn=n
ap=0
maxi=0
mini=0
ok=False
while n!=0:
    if n%10==0:
        ok=True
    n//=10
n=cn
i=9
while i>=0:
    while n!=0:
        if n%10==i:
            ap+=1
        n//=10
    while ap!=0:
        maxi=maxi*10+i
        ap-=1

    i-=1
    n=cn
    ap=0
print(maxi)
if ok==False:
    p=1
    y=0
    while maxi!=0:
        y=y*10+maxi%10
        maxi//=10
    print(y)
else:
    while maxi%10==0:
        ap+=1
        maxi//=10
    cif=maxi%10
    maxi//=10
    nr0=1
    y=0
    p=1
    while ap!=0:
        nr0*=10
        ap-=1
    p=1
    while maxi!=0:
        y=y*10+maxi%10
        p*=10
        maxi//=10
    print(cif*nr0*p+y)

