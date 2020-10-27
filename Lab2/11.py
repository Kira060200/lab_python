s=input("Dati textul:")
i=0
j=0
while i<len(s):
    if s[i]=='.' and ord(s[i+1])>=ord('A') and ord(s[i+1])<=ord('Z'):
        print(s[j:i+1])
        j=i+1
    i+=1