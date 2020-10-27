f=open("data2.txt")
s=set(int(x) for x in f.readline().split()) #dictionar care nu repeta elementele
print(s)
fs=frozenset(int(x) for x in f.readline().split())
print(fs)
s.add(11)
s.add(11)
print(s)