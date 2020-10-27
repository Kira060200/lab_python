l1=int(input("L1="))
l2=int(input("L2="))
a=l1
b=l2
while l1!=l2:
    if l1>l2:
        l1-=l2
    else:
        l2-=l1
print("Dimensiunea placilor este:",l1)
print("Numarul placilor este:",int(a*b/l1/l1))