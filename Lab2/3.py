prop=input("Dati sirul:")
old=input("Dati cuvantul care trebuie inlocuit:")
new=input("Dati cuvantul nou:")
i=0
'''while(i<len(prop)):
    if(prop.find(old,i)):
        j=prop.find(old,i)
        if(prop[j+len(old)]>='A'&prop[j+len(old)]<='z'&prop[j+len(old)-1]>='A'&prop[j+len(old)-1]<='z'):
            prop=prop[0:j]+new+prop[j+len(old):]
            i+=len(new)
        else:
            i+=1
    else:
        i+=1'''
k=len(prop)
poz=prop.find(old)
#print(poz)
while(prop.find(old)!=-1):
    if(prop.find(old)):
        prop=prop[:poz]+prop[poz:].replace(old,new,1)
    poz=prop.find(old,poz+k)
    print(poz)
print(prop)