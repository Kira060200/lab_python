f=open("data1.txt")
def comp(x):
    return x%2
s=f.readline()
print(s)
l=[int(x) for x in s.split()]
ll=l.copy()
print(l)
l.sort(reverse=True)
print(l)
ll=sorted(ll,reverse=True)
print(ll)
l.sort(key=comp,reverse=True)
print(l)
