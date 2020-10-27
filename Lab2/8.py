s=input("Dati sirul:")
i=0
while i<len(s):
    if s[i] in "AEIOUaeiou":
        s=s[:i]+s[i]+"p"+s[i]+s[i+1:]
        print(s)
        i+=2
    i+=1
print(s)
