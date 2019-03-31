import random

"""Partie 1: Tri par sélection."""

def reperer(liste,n):
    """Repere la position du plus grand element parmi les n premiers elements d'une liste."""
    maximum=liste[0] #Affecte a maximum la valeur du premier élément de la liste.
    position=0 #Affecte a position la valeur de 0.
    for i in range(1,n): #Fait varier les valeurs de i de 1 à n.
        if liste[i]>maximum: #Verifie si la ie valeur de la liste est supérieur a la valeur de maximum.
            maximum=liste[i] #Si oui, affecte a maximum la valeur du ie valeur de la liste.
            position=i #Recupere la position de cet élément.
    return position #Renvoie la position de cet élément.

def echanger(liste,position1,position2):
    """Echange 2 éléments d'une liste de positions données."""
    valeur=liste[position1] #Affecte a valeur la valeur de position1e terme de la liste.
    liste[position1]=liste[position2] #Mets en position1 le position2e terme de la liste.
    liste[position2]=valeur #Affecte au position2e terme de la liste la valeur de valeur.
    return liste #Renvoie la nouvelle liste de termes échangés.

def TriParSelection(liste):
    """Tri une liste."""
    for n in range(len(liste)-1,0,-1): #Fait varier les valeurs de n de len(liste)-1 à 1.
        r=reperer(liste,n) #Recupere la position du plus grand élément parmi les n premiers.
        liste=echanger(liste,n,r) #Echange les éléments de position n et r.
    return liste #Renvoie la liste triée.

def test(a,b,taille,nombre=10):
    """Test:"""
    for i in range(nombre): #Fait nombre tests et affiche les résultats.
        liste=[random.randint(a,b) for i in range(taille)]
        print("Test:",i+1)
        print(liste)
        print(principale(liste))
        print("")

#test(0,10,100)

"""Partie 2: Tri par insertion

10)
ALGORITHME:  TRIPARINSERTION:

DONNES: L :
LT <- []
POUR i DE 0 JUSQU A LA LONGUEUR DE LA LONGUEUR DE L FAIRE
    AJOUTER A LT LA VALEUR L[i]
            k <- i
            cle <- LT[-1]
    TANT QUE cle<LT[k-1] and k>0 FAIRE
            LT[k] <- LT[k-1]
            k <- k-1
    FIN  TANT QUE
    LT[k] <- cle
FIN POUR
AFFICHER LT

11)
"""
def TriParInsertion(L):
    """Tri une liste par insertion."""
    LT=[]
    #Recupere les éléments de L et les ajoute dans LT de façon a ce que LT soit triée
    for i in range(len(L)):
        #Ajoute la valeur de L considérée et stocke la valeur de la clé
        LT.append(L[i])
        k=i
        cle=LT[-1]
        #Décale la valeur de la clé dans LT tant que la clé est supérieur a ses éléments en partant de la fin
        while cle<LT[k-1] and k>0:
            LT[k]=LT[k-1] #Réaffecte la valeur de l'élément k a la valeur de l'élément k-1.
            k-=1
        #Une fois que l'on trouve que la clé est inférieure à un élément ou que l'on a considéré tous les éléments de LT
        LT[k]=cle
    #Renvoie la liste triée
    return LT

"""
13) Justesse du tri par sélection

Algorithme: Reperer
Pas de boucle

Algorithme: Echanger
Pas de boucle

Algorithme: TriParSelection
Invariant de boucle: ...

Algorithme: Test
Invariant de boucle: ...


14) Justesse du tri par insertion

Algorithme: Tri par insertion
Invariant de boucle: ...


15)
"""

def TriParInsertionEtComplexite(L):
    complexite=0
    LT=[]
    complexite+=1
    for i in range(len(L)):
        LT.append(L[i])
        k=i
        cle=LT[-1]
        complexite+=4
        while cle<LT[k-1] and k>0:
            LT[k]=LT[k-1]
            k-=1
            complexite+=4
        complexite+=1
        LT[k]=cle
        complexite+=1
    complexite+=1
    return [LT,complexite]


#16)

L=[random.randint(0,10) for e in range(100)]

Trie,complexite=TriParInsertionEtComplexite(L)
print("Liste triee:",Trie)
print("Complexite:",complexite)
