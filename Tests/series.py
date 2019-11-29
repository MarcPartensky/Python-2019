import math

N=200
a1=sum([1-math.exp(1/n) for n in range(1,N)])
a1b=sum([-1/n for n in range(1,N)])
a2=sum([math.cosh(n)/math.cosh(2*n) for n in range(1,N)])
a3=sum([math.factorial(n)/n**n for n in range(1,N)])

print(a1,a1b,a2,a3)
