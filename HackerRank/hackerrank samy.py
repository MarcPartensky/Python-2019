import functools

binary=lambda x,m:list(reversed([int((x%2**(i+1))//2**i) for i in range(m)]))
xor=lambda l:list(map(lambda x:1-x,l))
decimal=lambda l:sum([v*2**i for (i,v) in enumerate(list(reversed(l)))])
prod=lambda l:functools.reduce(lambda a,b:a*b,l)

n=5
a=prod(list(range(1,n+1)))
print(a)

a=binary(a,32)
a=xor(a)
a=decimal(a)
