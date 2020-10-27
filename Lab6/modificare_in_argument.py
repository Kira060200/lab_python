x=3
y=7
rezz=[]
print(id(rezz))
def adunare(x,y,rez):
    rez.append(x+y)
    #rez=[x+y] asta nu merge
adunare(x,y,rezz)
print(rezz,id(rezz))