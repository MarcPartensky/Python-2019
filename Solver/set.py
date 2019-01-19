def intersection(list1,list2):
    list1=set(list1)
    list2=set(list2)
    elements=inBoth(list1,list2)
    return set(elements)

def union(list1,lis2):
    elements=inOne(list1,list2)
    return set(elements)

def inOne(list1,list2):
    return list1+list2

def inBoth(list1,list2):
    in_both=[]
    for e1 in list1:
        for e2 in list2:
            if e1 is e2:
                in_both.append(e1)
    return in_both
