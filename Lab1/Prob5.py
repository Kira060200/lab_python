n=int(input("n="))
x=int(input())
y=int(input())
n-=2
if x>y:
    maxi1=x
    maxi2=y
else:
    maxi1=y
    maxi2=x
while n!=0:
    n-=1
    x=int(input())
    if x>maxi1:
        maxi2=maxi1
        maxi1=x
    elif x>maxi2 & x!=maxi1:
        maxi2=x
if maxi1==maxi2:
    print("Imposibil")
else:
    print(maxi1,maxi2)