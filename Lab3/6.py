a={}
key = "somekey"
x = "unu"
y = "doi"
a.setdefault(key, [])
a[key].append(x)
print(a)
key = "somerandomkey"
a.setdefault(key, [])
a[key].append(y)
print(a)