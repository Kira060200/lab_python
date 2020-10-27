s=input("Dati sirul:")
i=0
j=1
y=0
sum=0
while i<len(s):
    y=0
    while ord(s[i])>=ord('0') and ord(s[i])<=ord('9') and i<len(s):
        j+=1
        y=y*10+ord(s[i])-48
        i+=1
    if(j==1):
        i+=1
    j=1
    sum+=y
    y=0
print(sum)