import itertools

#print(list(itertools.combinations(list(range(2)),2)))

#print([(i,j) for i in range(2) for j in range(2)])


print(list(itertools.product(list(range(2)),repeat=2)))
