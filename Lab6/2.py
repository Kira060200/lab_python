f=open("copaci.in","r")
g=open("copaci.out","w")
#x=f.readline()
#n,m=x.split()
#Ctrl+q arata definitia functiei pe care vrem sa o folosim
#parametrul trebuie sa fie mutabil ca sa putem sa il modificam in arg functiei(list,set,dict)
xst,yst=f.readline().split()
xdr,ydr=f.readline().split()
xst,yst,xdr,ydr=int(xst),int(yst),int(xdr),int(ydr)
gauri=[tuple(x.split()) for x in f.readlines()]
coord=()
f.close()
def dreptunghiArieMaxima(left,up,right,down):
    ok=True
    global maxS,coord
    for g in gauri:
        if up<int(g[0]) and int(g[0])<down and int(g[1])>left and int(g[1])<right:
            ok=False
            dreptunghiArieMaxima(left,up,int(g[1]),down)
            dreptunghiArieMaxima(int(g[1]),up,right,down)
            dreptunghiArieMaxima(left,up,right,int(g[0]))
            dreptunghiArieMaxima(left,int(g[0]),right,down)
    if ok:
        sup=(right-left)*(down-up)
        if maxS<sup:
            maxS=sup
            coord=(up,left,down,right)
maxS=0
dreptunghiArieMaxima(yst,xst,ydr,xdr)
g.write(str(maxS)+"\n")
g.write(str(coord))
g.close()