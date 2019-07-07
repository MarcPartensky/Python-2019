import random

#1
A=  [[1,2,-1],
     [-2,0,3],
     [4,1,-1]]


print("Matrice:",A)

#2
#print(A[1])

#3
#print(A[1][2])

#4
#print(A[:][1])

#5a
def MatNulle(n,p):
    """Cree la matrice nulle de taille np."""
    return [[0 for j in range(p)] for i in range(n)]

#5b
print("Matrice Nulle de taille (n,p):",MatNulle(3,4))

#5c
def MatNulleBis(n,p=None):
    """Cree la matrice nulle de taille np."""
    if not p: p=n
    return [[0 for j in range(p)] for i in range(n)]


#5d
print("Matrice nulle carre:",MatNulleBis(5))

#5e
def MAlea(k,n,p=None):
    """Cree la matrice comporant n lignes, p colonnes et dont les coefficients sont des entiers aleatoires de [-k,k]."""
    if not p: p=n
    return [[random.randint(-k,k) for j in range(p)] for i in range(n)]

#6
def Pivot(M,j):
    """Renvoie l'index de la ligne i qui contient l'élément de la colonne M d'indice j qui a la plus grande valeur absolue."""
    m=abs(M[j][j])
    p=j
    for i in range(j+1,len(M)):
        t=M[i][j]
        if abs(t)>m:
            m=t
            p=i
    return p

print("pivot:",Pivot(A,0))


#7
def EchangerLigne(M,i,l):
    """Permet d'echanger la i-eme ligne et la l-eme ligne de la matrice M."""
    M[i],M[l]=M[l],M[i]


EchangerLigne(A,0,1)
print(A)

#8
def CombLigne(M,i,l,r):
    """Permet de remplacer la ligne i de la matrice M par Li-r*Ll."""
    M[i]=[M[i][j]-r*M[l][j] for j in range(len(M[i]))]

#CombLigne(A,1,0,A[Pivot(A,0)][0])
p=Pivot(A,0)
print(p)
EchangerLigne(A,0,p)
print(A)
CombLigne(A,1,0,A[1][0]/p)
print("Combine les lignes i et l:",A)


#9 Algorithme
"""Pivot Triangulaire Sup:
Donnees: M une matrice

l<-nombre de lignes de la matrice M
Pour j de 0 a l-1 FAIRE:
    p<-Pivot de la matrice m a partir de la colonne 0
    Echanger les lignes j et p de la matrice M
    Pour i de j+1 a l-1 FAIRE:
        Realise Li <- Li-r*Lj pour la matrice M
"""
        

#9
def PivotTriangulaireSup(M):
    """Permet de triangulariser la matrice."""
    l=len(M)
    for j in range(l):
        p=Pivot(M,j)
        EchangerLigne(M,j,p)
        if p!=0:
            for i in range(j+1,l):
                CombLigne(M,i,j,M[i][j]/M[j][j])

#10

            
def Afficher(B,precision=3):
    for i in range(len(B)):
        text=""
        for j in range(len(B[i])):
            text+=str(float(B[i][j]))[:precision]
            if j<len(B[i])-1:
                text+="|"
        print(text)
    
#11
B=MAlea(5,5)
PivotTriangulaireSup(B)
print("Triangularise")
Afficher(B)
#print(B)

#12
def MaxIndice(l):
    """Renvoie la liste des indices des termes de la liste dans l'ordre croissant."""
    M=[[l[i],i] for i in range(len(l))]
    indices=[]
    for i in range(len(l)):
        p=M[i].index(min(M[i]))
        indices.append(M[p][1])
        del M[p]
    return [indices[-j-1] for j in range(len(indices))]
        
    
a=[random.randint(0,100) for i in range(10)]
print(a)
print(MaxIndice(a))

#13

def TriTabCL(M,i):
    """Permet de trie un tableau selon l'ordre croissant d'une ligne."""
    indices=MaxIndice(M[i])
    n,p=len(M),len(M[0])
    nM=MatNulle(n,p)
    for i in range(n):
        for j in range(p):
            nM[i][j]=M[i][indices[j]]

print("\n13:")
C=MAlea(5,5)
Afficher(C)
print(C[2])
print(MaxIndice(C[2]))
TriTabCL(C,2)
Afficher(C)
 
    



    
