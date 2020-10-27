f=open("text.txt","r")
l=[]
for s in f:
    x=s.split()
    y=s.split(":")
    contor=1
    i=1
    while y[0] in s[i:]:
        contor+=1
        i+=s[i:].find(y[0])+1
    print(contor)
    i=1
    while "~" in s[i:]:
        contor+=1
        i+=s[i:].find("~")+1
    l.append((y[0],contor))
print(l)