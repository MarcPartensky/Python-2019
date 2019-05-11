#Hugues de Rubin de Cervens
#Marc Partensky
#Louise De Servigny

from scipy.optimize import bisect,newton

import math

f=lambda x:x**2-2
#1)a) On définit f : x-->x^2-2. f s'annule en sqrt(2) et -sqrt(2). Or leurs valeurs décimales ne sont pas fini.
"""b)DONNEES (a,b,e)
   x<-(a+b)/2
   TANT QUE abs(x^2-2)>e FAIRE:
        SI f(a)*f(b)>0: FAIRE:
            a<-x
        SINON FAIRE:
            b<-x
        x<-(a+b)/2
    FIN TANT QUE
    AFFICHER x
"""

#c)
def ZeroD(f,a,b,e):
    x=(a+b)/2
    while abs(f(x))>e:
        if f(a)*f(x)>0:
            a=x
        else:
            b=x
        x=(a+b)/2
    return x

#d)
print("ZeroD:",ZeroD(f,1,2,e=10**(-12)))
print(math.sqrt(2))

#2)a))
print(bisect(f,1,2))
#b)
print("ZeroD:",ZeroD(f,1,2,e=10**(-12)))

#II) a)


#b)Données(f,a,b,n)
"""
   t : x-->(-f(a)*(b-a))/(f(b)-f(a))+a
   c=t(a,b)
   Pour i parcourant n
   c=t(a,b)
   Si f(a)f(c)>0
      a=c
   Sinon
      b=c
   Afficher c
"""

#c)
def ZeroL(f,a,b,n):
    t=lambda a,b:-f(a)*(b-a)/(f(b)-f(a))+a
    c=t(a,b)
    for i in range(n):
        c=t(a,b)
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    return c
#d)
print("ZeroL:",ZeroL(f,1,2,10))
print(math.sqrt(2))

#e)
def ZeroDC(f,a,b,e):
    x=(a+b)/2
    t=0
    while abs(f(x))>e:
        t+=1
        if f(a)*f(x)>0:
            a=x
        else:
            b=x
        x=(a+b)/2
    return (x,t)

#f)
print("ZeroDC:",ZeroDC(f,1,2,10**(-12)))

#4)
print(newton(f,1,maxiter=20))


#III)
#a) Figure...

#b) Algorithme
"""Données(f,a,b,n)
    fp : a-->(f(a+h)-f(a))/h
    e=10^-10
    c=b
    Pour i parcourant n
    c=c-f(c)/fp(c,e)
    Si f(a)f(c)>0
    a=c
    SINON
    b=c
    Afficher c
"""

#c)
def ZeroN(f,a,b,n):
    fp=lambda a,h:(f(a+h)-f(a))/h
    e=10**(-10)
    c=b
    for i in range(n):
        c=c-f(c)/fp(c,e)
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    return c

#d)
print("ZeroN:",ZeroN(f,1,2,20))
print(math.sqrt(2))

#6)
#a)
print(newton(f,1,maxiter=20))

#b)
print("ZeroN:",ZeroN(f,1,2,20))
