from math import sin
from sympy import Symbol,sin,sqrt
from sympy import *

x=Symbol('x')


#f=sin(x)/x
f=sqrt(sin(x)/(2*x))

a=5

print(f)

#x=2

print(f)

print("\n".join(map(str,Symbol.__dict__.items())))

a=(1/x)~(1/x**2)

print(a)
