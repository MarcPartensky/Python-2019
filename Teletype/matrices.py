import numpy as np
from math import sqrt
import random
from copy import deepcopy



def pgcd(a,b):
	t = b
	b = a % b
	if b == 0:
		return t
	else:
		return pgcd(t,b)

def ppcm(a, b):
    return a * b // pgcd(a, b)

def transvection(a,i,j):
    """Anciennement appelee la sainte transvection"""
    if a[j][i]!=0:
        p = ppcm(a[i][i],a[j][i])
        k1 = p//a[i][i]
        k2 = p//a[j][i]
        a[i] *= k1
        a[j] *= k2
        a[j] = a[i]-a[j]
    return a

def transpose(a):
    """Echange l'abscisse et l'ordonnee pour chaque case"""
    b=np.array([[a[i][j] for i in range(a.shape[1])] for j in range(a.shape[0])])
    return b

def exchange(a,j1,j2):
    """Li1 <-> Li2"""
    l = deepcopy(a[j1])
    a[j1] = deepcopy(a[j2])
    a[j2] = l
    return a

def index_pivot(a, i,jmin):
    """Renvoie un pivot"""
    for j in range(jmin,len(a)):
        if a[j][i] != 0:
            return j

def triangular(a):
    """Renvoie la matrice triangularise"""
    for i in range(len(a[0])-1):
        jmin=i+1
        jp = index_pivot(a,i,jmin)
        if a[i][i]==0:
            a = exchange(a,i,jp)
        for j in range(jmin,len(a)):
            a = transvection(a,i,j)
    for j in range(len(a)):
        a[j]=a[j]/pgcdl(a[j])
    return a

def identity(a):
    pass

def pgcdl(l):
    """Renvoie le pgcd d'une liste"""
    p=l[0]
    for i in range(1,len(l)):
        p=pgcd(p,l[i])
    return p


if __name__=="__main__":
    c=6 #taille de la matrice carre de depart
    a=np.array([[random.randint(0,10) for i in range(c)] for j in range(c)])
    print(a)
    b=triangular(a)
    print(b)
    #c=transpose(b)
    #print(c)
