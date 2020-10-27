x=int(input("x="))
n=int(input("n="))
p=int(input("p="))
m=int(input("m="))
d=0
while m>n:
    m-=n
    d+=x*n
    x=x-x*p/100
d+=x*m
print("Distanta parcursa este:",d)