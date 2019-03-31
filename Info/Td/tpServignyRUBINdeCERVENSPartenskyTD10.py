#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:23:27 2019

@author: hurc60248
"""

"""
I) Choisir le bon type de données
1) a) Chaîne de caractère
b) t uple
c) chaîne de caractére
d) chaîne de caractére

II)Prévoir ce que fait un script
2) Ce script affichera un message d'erreur car t=(1,2,3) est un t uple et t+4 est une opération sur les entiers
3) Ce script affichera "str"
4) Ce script affichera "isepparis"
5) Ce script affichera le crochet quand on demande a[0], et la virgule, quand on demande a[2]

III) Listes
6)a) "randint(self, a, b) method of random.Random instance
Return random integer in range [a, b], including both end points."

1er methode
b) import random
a=[]
for i in range(50):
    a.append(random.randint(0,1))

  2eme methode
a=[random.randint(0,1) for i in range(50)]

7)a) Données : liste, element
    compteur <- 0
    Pour e dans liste FAIRE
      Si e=element FAIRE
      compteur <- compteur + 1
      Fin si
    Fin pour
    Afficher compteur
    FIN

b) def compter(liste, élément):
       compteur=0
         for e in liste:
            if e==element:
               compteur+=1
       return compteur

8)a) Données : liste, element
     sortie <- []
     pour i dans (0,longueur(liste)) faire
       si liste(i)=element FAIRE
         Ajouter a sortie l'indice i
    FIN si
    Afficher(sortie)
    FIN

b)def Compter(liste, element):
    sortie=[]
    for i in range(len(liste)):
        if liste[i]==element:
            sortie.append(i)
 return sortie

9)a)Données : liste
    somme=0
    Pour element dans liste FAIRE
       somme <- element + somme
    Fin pour
    moyenne=somme/longueur(liste)
    somme2=0
    Pour element dans liste FAIRE
       somme2 <- somme2 + (element-moyenne)²
       variance=somme2/longueur(liste)
    Afficher moyenne, variance
    FIN

b)def stats(liste):
    moyenne=sum(liste)/len(liste)
    variance=sum([(x-moyenne)**2 for x in liste])/len(liste)
    return (moyenne, variance)

10)a) Données : entnat1, entnat2
    Si entnat1 divise entnat2 FAIRE
        res <- vrai
    Sinon FAIRE
        res <-faux
    fin si
    Afficher resultat

b) Divise=lambda a,b:(b%a==0)

11)a) Données : entier
    liste=[]
    Pour element dans liste qui prend toutes les valeurs entre 1 et entier Faire
        Si element divise entier Faire
           Ajouter element dans liste
        fin si
    fin pour
Afficher liste

 b) ListeDiv=lambda a:[e for e in range(1,a+1) if Divise(e,a)]

12)a) Données : liste1, liste2
    commun=[]
    pour element dans liste1 faire
        Si element dans liste2 faire
            Ajouter element a commun
        fin si
    fin pour
Afficher commun

b) ComListe=lambda a,b:list(set([e for e in a if e in b]))

13)a)


PGCDN=lambda a,b:max(ComListe(ListDiv(a),ListDiv(b)))




"""
