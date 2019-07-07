import itertools

s=list(range(6))

scy=itertools.cycle(iter(s))

def extract(it,mi,ma):
    it1,it = itertools.tee(it)
    return ([next(it1) for i in range(ma)][mi:],it)


a,scy=extract(scy,1,3)

print(a)
print(extract(scy,1,3))


print(" ".join(map(str,s)))
