import collections
s=input()
c=collections.Counter(s.split())
print(c.most_common(1))
print(c.most_common()[-1])