a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=b*b-4*a*c
if d<0:
    print("Ecuatia nu are radacini reale")
elif d==0:
    print(-b/(2*a))
else:
    print((-b+d**0.5)/(2*a))
    print((-b-d**0.5)/(2*a))

