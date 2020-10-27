n=int(input("n="))
i=2
x=float(input())
y=float(input())
n-=2
dif=y-x
if dif>0:
    ok=True
    j=i
else:
    ok=False
x=y
while n!=0:
    n-=1
    i+=1
    y=float(input())
    if dif>0:
        ok=True
    if y-x>dif:
        dif=y-x
        j=i
    x=y
if ok==True:
    print(dif,j-1,j)
else:
    print("Nu s-a inregistrat nicio crestere")