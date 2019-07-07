import random




def getNewPosition(x,y,w,h,r):
    d=min(min(w-1-x,x),min(h-1-y,y))
    while r>0 and not(h==w==0):
        r-=1
        if x==d and y!=h-1-d:
            x,y=(x,y+1)
            continue
        if y==d and x!=d:
            x,y=(x-1,y)
            continue
        if x==w-1-d and y!=d:
            x,y=(x,y-1)
            continue
        if y==h-1-d and x!=w-1-d:
            x,y=(x+1,y)
            continue
    return (x,y)

def rotate(m,r=1):
    h=len(m)
    w=len(m[0])
    if w>1 and h>1: r%=(2*(h+w-2))
    nm=[[0 for x in range(w)] for y in range(h)]
    for x in range(w):
        for y in range(h):
            nx,ny=getNewPosition(x,y,w,h,r)
            nm[ny][nx]=m[y][x]
    return nm

def toSpaceStr(m):
    t=[]
    for y in range(len(m)):
        t.append(" ".join([str(e) for e in m[y]]))
    return "\n".join(str(e) for e in t)

x1,y1=[random.randrange(2,10,2) for i in range(2)]

m=[[random.randint(1,9) for x in range(5)] for y in range(4)]
m=[[y*4+x+1 for x in range(4)] for y in range(4)]
#m=[[0]]


tm=toSpaceStr(m)
print(tm,end='\n\n')

rm=rotate(m,2)
trm=toSpaceStr(rm)
print(trm,end='')
