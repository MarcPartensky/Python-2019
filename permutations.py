

#a=["a","b","c","d","e"]
#a=list(range(3))
a=[a for a in "abcdefgh"]
#print(len(a))

def permutations(l):
    if len(l)==2:
        return [(l[0],l[1]),(l[1],l[0])]
    else:
        result=[]
        for i in range(len(l)):
            b=l[:]
            del b[i]
            result+=[tuple([l[i]])+a for a in permutations(b)]
        return result

def prod(l):
    """Return the product of the list l."""
    r=1
    for a in l:
        r*=a
    return r

def facto(n):
    """Return the factorial of the number n."""
    return prod(range(1,n+1))

print(facto(10))


def getPermutation(l,n):
    """Return the permutation number n."""
    pass


print(permutations(list(range(5))))



#print(["".join(b) for b in permutations(a)])
