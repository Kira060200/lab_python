f=open("data2.txt")
s=set(int(x) for x in f.readline().split())
fs=frozenset(int(x) for x in f.readline().split())
print(s)
print(fs)
print(s.isdisjoint(fs)) #verifica daca sunt disjuncte
s.discard(5)
print(s.isdisjoint(fs))