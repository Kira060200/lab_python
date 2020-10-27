cuv1=input()
cuv2=input()
if(len(cuv1)!=len(cuv2)):
    print("False")
else:
    ok=True
    i=0
    while(i<len(cuv1)):
        if(cuv2.find(cuv1[i])!=-1):
            cuv2=cuv2.replace(cuv1[i],"",1)
        else:
            ok=False
        i-=-1
print(ok)


