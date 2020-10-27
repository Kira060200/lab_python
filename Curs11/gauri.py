f=open("gauri.txt")
g=open("out_gauri.txt","w")
x=f.readline()
n,m=x.split()
gauri=[tuple(x.split()) for x in f.readlines()]
f.close()
def s_f_g(left,up,right,down):
    ok=True
    global maxS,coord
    for g in gauri:
        if up<=int(g[0]) and int(g[0])<=down and int(g[1])>=left and int(g[1])<=right:
            ok=False
            s_f_g(left,up,int(g[1])-1,down)
            s_f_g(int(g[1])+1,up,right,down)
            s_f_g(left,up,right,int(g[0])-1)
            s_f_g(left,int(g[0])+1,right,down)
    if ok:
        sup=(right-left+1)*(down-up+1)
        if maxS<sup:
            maxS=sup
            coord=(up,left,down,right)
maxS=0
s_f_g(1,1,int(n),int(n))
g.write(str(maxS))
g.close()