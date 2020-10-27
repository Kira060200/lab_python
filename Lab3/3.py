f=open("cheltuieli.txt","r")
sum=0
a=0.0
b=0.0
c=0.0
d=0.0
for x in f:
    for y in x.split():
        if (y.isdecimal()==True):
            if a!=0:
                d=int(y)
            else:
                a=int(y)
        elif ord(y[0])>=ord('0') and ord(y[0])<=ord('9'):
            if b!=0:
                c=float(y)
            else:
                b=float(y)
        if a==0 and b!=0 and c!=0:
            a=c
        if a!=0 and b==0 and d!=0:
            b=d
        if a!=0 and b!=0:
            sum+=(a*b)
            a=0.0
            b=0.0
            c=0.0
            d=0.0
print(sum)