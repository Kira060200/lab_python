f=open("test.in","r")
g=open("test.out","w")
count=1
for x in f:
    i=0
    while x[i]!='*':
        i+=1
    y=int(x[:i])
    j=i+1;
    while x[i]!="=":
        i+=1
    z=int(x[j:i])
    w=int(x[i+1:len(x)-1])
    if y*z==w:
        g.write(x[:len(x)-1]+" Corect"+'\n')
        count+=1
    else:
        g.write(x[:len(x)-1]+" Gresit "+str(y*z)+'\n')
    g.write("Nota "+str(count))
f.close()
g.close()


