s=input("Dati sirul:")
op=int(input("Dati numarul operatiei(criptare:0,decriptare:1): "))
k=int(input("Dati cheia:"))
if(op==0):
    i=0
    while(i<len(s)):
        if(ord(s[i])>=ord("A")&ord(s[i])<=ord("z")):
            while(ord(s[i])+k>ord('a')+26):
                k-=26
            s=s[:i]+s[i:].replace(s[i],chr(ord(s[i])+k),1)
        i-=-1

elif(op==1):
    i=0
    while(i<len(s)):
        if(ord(s[i])>=ord("A")&ord(s[i])<=ord("z")):
            while(ord(s[i])+k>ord('a')+26):
                k-=26
            s=s[:i]+s[i:].replace(s[i],chr(ord(s[i])-k),1)
        i-=-1
print(s)