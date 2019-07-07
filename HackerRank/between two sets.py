def pgcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    a=abs(a)
    b=abs(b)
    mi=min(a,b)
    ma=max(a,b)
    if ma%mi==0:
        return mi
    else:
        return pgcd(ma-mi,mi)

def pgcds(l):
    a=float("inf")
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            na=pgcd(l[i],l[j])
            if na<a:
                a=na
    return na

def ppcm(a,b):
    a=abs(a)
    b=abs(b)
    p=max(a,b)
    while not (p%a==0 and p%b==0):
        if not p%a==0:
            p+=b
        if not p%b==0:
            p+=a
    return p

def ppcms(l):
    a=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            na=ppcm(l[i],l[j])
            if na>a:
                a=na
    return na


a=[2,4]
b=[16,32,96]

def divideAll(d,l):
    for e in l:
        if e%d!=0:
            return False
    return True

def multipleOfAll(m,l):
    for e in l:
        if m%e!=0:
            return False
    return True


"""l=[]
pa=pab=ppcms(a)
pb=pgcds(b)
print(pa)
print(pb)
while pa<=min(b):
    if divideAll(pa,b):
        l.append(pa)
    pa+=pab
    print(pa,divideAll(pa,b))"""



l=list(range(max(a),min(b)+1))

fl=[]
for e in l:
    if divideAll(e,b) and multipleOfAll(e,a):
        fl.append(e)

print(len(fl))
