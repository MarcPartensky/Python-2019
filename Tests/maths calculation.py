import math
from functools import reduce
from itertools import cycle

n=1.0088284e+90
print(n)
n=n*math.factorial(54)
print(n)
c=math.log(n,26)
print(c)



def partitions(n):
    parts = [1]+[0]*n
    for t in range(1, n+1):
        for i, x in enumerate(range(t, n+1)):
            parts[x] += parts[i]
    return parts[n]


def prod(l):
    return reduce(lambda x1,x2:x1*x2,l)

print(prod([1,3]))


print(partitions(1000))

def adapt(l,b):
    return [0]*(len(b)-len(l))+l


def decompose(n):
    return list(map(int,str(n)))

def compose(l):
    return int("".join(map(str,l)))

print(decompose(1432))

def addInBase(l1,l2,b):
    l=[]
    s=0
    for i in range(-1,-len(b)-1,-1):
        r=(l1[i]+l2[i]+s)%b[i]
        s=(l1[i]+l2[i]+s)//b[i]
        l.append(r)
    return list(reversed(l))

def getInBase10(l,b):
    return l[-1]+sum([l[i]*prod(b[i+1:]) for i in range(-2,-len(l)-1,-1)])


def getInBase10(l,b):
    l=adapt(l,b)
    s=l[0]
    l.reverse()
    b.reverse()
    p=1
    for i in range(1,len(b)-1):
        p*=b[i]
        s+=l[i]*p
    return s

def getFromBase10(n,b):
    b.reverse()
    l=[]
    for i in range(len(b)):
        r=n%b[i]
        n=n//b[i]
        l.append(r)
    l.reverse()
    return l


def convert(l,b1,b2):
    l.reverse()
    b1.reverse()
    b2.reverse()
    nl=[]
    i=0
    n1=0
    n2=0
    while l.count(0)!=len(l):
        if b1[n1]>b2[n2]:
            r=l[i]%b2[n2]
            s=l[i]//b2[n2]
            nl.append(r)
            i+=1


def convertEasy(l,b1,b2):
    n=getInBase10(l,b1)
    l=getFromBase10(n,b2)
    return l



#[1,0,0,0] [10,10,10,10]
#[0,16,40]           [24,60,60]

c=10

hms=[24,60,60]
binary=[2]*c
decimal=[2]*c

t1=[12,12,30]
t2=[5,0,30]

r=addInBase(t1,t2,hms)
print(r)

print(compose([10,5,5]))

print(getInBase10([2,16,40],hms))
print(getFromBase10(1000,hms))

t1d=convertEasy(t1,hms,decimal)
print(t1d)
t1b=convertEasy(t1d,decimal,binary)
print(t1b)
t1=convertEasy(t1b,binary,hms)

print(t1)

print(convertEasy([1,0,0],decimal,hms))

print(getInBase10([1,0],decimal))


print(adapt([1,0],decimal))
