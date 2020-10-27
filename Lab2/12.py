s=input("Dati sirul:")
s=s.split()
if s[0][len(s[0])-1]!=s[2][0]:
    x=s[0]+s[2]
else:
    l=s[0][len(s[0])-1]
    i=len(s[0])-1
    while i>0 and l==s[0][i]:
        s[0]=s[0][:i]
        i-=1
    x=s[0]
    while l==s[2][0]:
        s[2]=s[2][1:]
    x+=s[2]
print(x)
