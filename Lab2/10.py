s=input("Dati numele si prenumele:")
i=0
ok=True
while i<len(s) and ok:
    while s[i]!=' ' and s[i]!='-':
        if ((ord(s[i])<ord('A') or ord(s[i])>ord('Z')) and (ord(s[i])<ord('a') or ord(s[i])>ord('z'))):
            ok=False
print(ok)
