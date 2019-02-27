import random
import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(10000)

print(sys.getrecursionlimit())

"""1"""

def belong(element,list):
    if len(list)==1:
        if [element]==list: return True
        else: return False
    else:
        return (belong(element,list[:1])+belong(element,list[1:])>0)



def union(l1,l2):
    if l1==[]: return l2
    if not belong(l1[0],l2): return [l1[0]]+union(l1[1:],l2)
    else: return union(l1[1:],l2)

def intersection(l1,l2):
    if l1==[]: return []
    if not belong(l1[0],l2): return intersection(l1[1:],l2)
    else: return [l1[0]]+intersection(l1[1:],l2)

#union = lambda l1,l2:list(set(l1+l2))

l1=list(range(100))
l2=list(range(6,16,2))
random.shuffle(l1)

#print(intersection(l1,l2))

"""2"""

def insert(e,l):
    if l==[]: return [e]
    if e>l[0]: return [l[0]]+insert(e,l[1:])
    else: return [e]+l

def sort(l):
    if l==[]: return l
    return insert(l[0],sort(l[1:]))


#print(sort(l1))

"""3"""


#sort1= lambda l:[min(l)]+sort1(l.remove(min(l)))

def sort1(l):
    if l==[]: return l
    t=min(l)
    l.remove(t)
    return [t]+sort1(l)

def factorial(n):
    if n<=1: return 1
    return n*factorial(n-1)

def shuffle(l):
    if l==[]: return l
    e=random.choice(l)
    l.remove(e)
    return [e]+shuffle(l)

#l3=[1,2,1,4,5,1,1,7]

def fusion(l1,l2):
    if l1==[]: return l1
    if l1[0]
    return


#print(l1)
#print(sort1(l1))

#print(factorial(10))
