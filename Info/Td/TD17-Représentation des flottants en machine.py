#Représentation des flottants en machine.

import math

#I) Représentation des réels

#1) Quel mot code 25? et 25.0?
#25  : 11001
#en 64 bits: 0000000000000000000000000000000000000000000000000000000000011001
#25. : 0,0*48,11001,1,000000100
#en 64 bits: 010110000000000000000000000000000000000000000000000000000000100

#2)Quel mot code le plus grand réel positif normalisé? Quel réel représente-t-il? En donner un ordre de grandeur.
#0111111111111111111111111111111111111111111111111111111111111111
#Ordre de grandeur 2**1023

#3) Quel mot code le plus petit réel positif normalisé? Quel réel représente-t-il? En donner un ordre de grandeur.
#0,0*53,1,0*10
#0000000000000000000000000000000000000000000000000000010000000000
#Ordre de grandeur 2**-1023

#4) Quel mot code le plus petit réel positif dénormalisé? Quel réel représente-t-il? En donner un ordre de grandeur.
#0000000000000000000000000000000000000000000000000000000000000000
#Représente zéro

#II) Provoquer l'erreur

#5)Donner un calcul dont le résultat produit un dépassement de capacité par valeurs inférieurs.
#print(math.log(0.))
#print(-1./2**1024)

#6) Donner un calcul dont le résultat produit -inf
print(-2 * (2.**1023))

#7) Donner un calcul dont le résultat produit à tord 0.0
print(2.**(-2**11))

#8) Donner un calcul dont le résultat ne produit pas à tord 0.0
#print(1/10-math.log(math.exp(1/10)))
print(1-(2.**-1023+1))


#III) Comprendre les erreurs

#9) Quelle précision perd-on si on diviser un nombre à virgule flottante par deux puis qu'on le multiplie à nouveau par deux?
#On perd une précision de 2**1022

#10) On considère le script Python suivant:
def Algo10():
    x=1.0
    y=x+1.0

    while y-x==1.0:
        x=x*2.0
        y=x+1.0
Algo10()

#a)Ecrire l'algorithme correspondant à ce programme. Quel problème y a t'il?
"""Algorithme:
Donnees: Rien
x <- 0
y <- x+1
TANT QUE y-x = 1:
    x <- x*2
    y <- x+1
"""
#Le problème est que cet algorithme est infini.

#b)Recopier ce programme dans un interpréterur et l'exécuter. Que constate-t-on? Quelle en est la raison?
#On constate que cet algorithme se fini.

#c) Modifier ce programme afin d'introduire un compteur qui détermine le nombre d'itérations effectuées.
def Algo10Iteration():
    x=1.0
    y=x+1.0
    i=0

    while y-x==1.0:
        i+=1
        x=x*2.0
        y=x+1.0
        print(x)
        print(i)

Algo10Iteration()
# On compte 53 itérations

#d) Interpréter précisément la différence de comportement entre l'algorithme et le programme
#A la 53e itération l'erreur a été dépassée.

#e) Que se passerait-il si on initialisait x à 1 et y a x+1
#Théoriquement: Le calcul continuerait jusqu'à atteindre le dépassement de capacité mémoire de l'ordinateur

#11) Affecter 2.0 **1023 à la variable a puis interpréter ce qu'affiche python pour chacun des calculs suivants:
a=2.0**1023

#a) 2*a
print(2*a)
#Le dépassement de capacité en valeur négatif à été atteint donc le résultat est inf

#b) b=2*a puis b/2
b=2*a
print(b/2)
#Comme le dépassement de capacité en valeur négatif à été atteint la valeur de b
#correspond à l'infini et diviser l'infini par 2 donne toujours l'infini.

#c) 3*a-3*a
print(3*a-3*a)
#Comme le résultat de 3*a est considéré comme l'infini par python la différence des 2
#correspond à une forme indéterminée, d'où le résultat.

#d) 1/(2*a)
print(1/(2*a))
#Comme le résultat de 2*a est considéré comme l'infini par python, lors du passage
#à l'inverse python fait le quotient de 1 par l'infini ce qui lui donne 0.

#IV) Les nombres dénormalisés
#12) On note x1 le plus petit réel positif normalisé représentable et x2 le plus
#petit réel strictement supérieur à x1 normalisé représentable. Déterminer x1, x2
#et (x2-x1)/(x1-0)
#
x1=2.**-1023
print(x1)
x2=2.**-1022
print(x2)
#(x2-x1)/(x1-0)=1
print((x2-x1)/(x1-0))

#13)
#y1=2**-1074
y1=2.**-1074
print(y1)
#y2=2**-1073
y2=2.**-1073
print(y2)

print((y2-y1)/(x2-x1))
#Ce résultat devrait valoir 2**-52 mais vaut 2**-51 à cause de l'erreur d'approximation lors de la division
