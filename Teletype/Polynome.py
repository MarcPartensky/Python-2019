"""
Features:
1:COMPLETED: print #renvoie str
2:COMPLETED: addition #renvoie Polynomial
3:COMPLETED: multiplication #renvoie Polynomial
4:COMPLETED: derive #renvoie un Polynomial
5:COMPLETED: division #renvoie couple de Polynomial
6:COMPLETED: pgcd #renvoie Polynomial
7: ppcm #renvoie Polynomial
8: taylor #renvoie str ou liste "je sais pas encore"
9: factoriser #renvoie str ou liste de liste des coefficients "pareil"
10: racines reelles #renvoie liste des racines reelles
11: racines complexes #renvoie liste des racines complexes
12: show #Affiche le polynome sur une fenetre pygame, pyglet ou matplotlib
"""

from copy import deepcopy


class Polynomial:
    def __init__(self, coefficients):
        """Create a polynomial using its coefficients."""
        self.coefficients = coefficients
    def __repr__(self):
        """Return the usual representation of a polynomial."""
        if self.coefficients==[]:
            return "0"
        liste = []
        if self.coefficients[0]!=0:
            liste.append(str(self.coefficients[0]))
        for degre,coefficient in enumerate(self.coefficients[1:],1):
            if coefficient!=0:
                liste.append(str(coefficient) + "X^" + str(degre))
        liste.reverse()
        text = "+".join(liste)
        text = text.replace("^1","").replace("+-","-").replace("1X","X")
        return text

    def adapt(self,coefficients,size):
        """Add zeros to the coefficients using coefficients and size."""
        coefficients += [0]*(size-len(coefficients))
        return coefficients

    def __add__(self, other):
        """Add 2 polynomials together by adding their coefficients."""
        maxdegree = max(self.degree(),other.degree())
        cA = self.adapt(self.coefficients,maxdegree)
        cB = self.adapt(other.coefficients,maxdegree)
        newcoefficients = [a+b for (a,b) in zip(cA, cB)]
        return Polynomial(newcoefficients)

    def __sub__(self, other):
        """Substract 2 polynomials together by multiplying the second polynomial by -1 and adding it to the first using add method."""
        return self+other*Polynomial([-1])

    def __mul__(self, other):
        """Multiply 2 polynomials together using the formula for the coefficients."""
        degree = len(self.coefficients) + len(other.coefficients)
        A = self.coefficients + [0]*(degree-len(self.coefficients)+1)
        B = other.coefficients + [0]*(degree-len(other.coefficients)+1)
        newcoefficients = []
        for k in range(degree + 1):
            coeff = 0
            for i in range(k + 1):
                coeff += A[i] * B[k - i]
            newcoefficients.append(coeff)
        C = Polynomial(newcoefficients)
        C.correct()
        return C

    def correct(self):
        """Correct the coefficients of the polynomial by deleting useless zeros at the end,"""
        while len(self.coefficients)>1:
            if self.coefficients[-1] == 0:
                del self.coefficients[-1]
            else:
                break
        if self.coefficients==[0]:
            self.coefficients=[]
        """and then replace float coefficients by int coefficients if possible."""
        for i in range(len(self.coefficients)):
            if self.coefficients[i]==int(self.coefficients[i]):
                self.coefficients[i]=int(self.coefficients[i])

    def __len__(self):
        """Return the number of coefficients.
        It is important to notice that it is not the degree due to the fact that
        the polynomial might have a degree of -inf and the len method must have positive values.
        In such a case this method will raise an error.
        It is why it is better to use the degree method in the general case."""
        A=deepcopy(self)
        A.correct()
        return len(A.coefficients)-1

    def degree(self):
        """Return the degree of a polynomial.
        It will return -1 if the degree is -inf to be computer friendly."""
        A=deepcopy(self)
        A.correct()
        return len(A.coefficients)-1

    def __getitem__(self,index):
        """Return a coefficient of the polynomial."""
        return self.coefficients[index]

    def __setitem__(self,index,value):
        """Change a coefficient of the polynomial."""
        self.coefficients[index] = value

    def __delitem__(self,index):
        """Delete a coefficient of the polynomial."""
        del self.coefficients[index]

    def derivate(self):
        """Derivate the polynomial."""
        self.coefficients = [i*c for (i,c) in enumerate(self.coefficients)]
        del self.coefficients[0]

    def derivative(self):
        """Return the derivative polynomial."""
        newcoefficients = [i*c for (i,c) in enumerate(self.coefficients)]
        del newcoefficients[0]
        return Polynomial(newcoefficients)

    def unit(self):
        """Return the polynomial unit form."""
        k=self.coefficients[-1]
        newcoefficients=[]
        for i in range(len(self.coefficients)):
            newcoefficients.append(self.coefficients[i]/k)
        A=Polynomial(newcoefficients)
        A.correct()
        return A

    def unitarize(self):
        """Convert the polynomial into its unit form."""
        self=self.unit()

    def __xor__(self,other):
        """Return the HCF (PGCD  en francais) of self and other by Euclide algorithm. Make use of "^" operator."""
        R0 = deepcopy(self)
        R1 = deepcopy(other)
        R0.correct()
        R1.correct()
        listR=[R0,R1]
        R2,Q2=R0/R1
        listR.append(R2)
        while listR[-1].degree()>0:
            R,Q=listR[-2]/listR[-1]
            listR.append(R)
        return listR[-2]

        #Resultat d'une enorme galere de 2h...
        #Algorithme d'Euclide:
        #a=b*q0+r0
        #b=r*q1+r1
        #r=r1*q2+r2
        #r1=r2*q3+r3
        #...
        #ri=r(i-1)*q(i-1)+1+0

    def __or__(self,other):
        """Return the LCM (PPCM en francais) using "i have absolutely no clue how to do this so figure it out!" Make use of "|" operator."""
        #On sent la (tres) grosse fatigue apres minuit.
        return "Figure it out!"

    def __truediv__(self, other):
        """Return the division of 2 polynomials."""
        R = deepcopy(self)
        B = deepcopy(other)
        R.correct()
        B.correct()
        Q = Polynomial([])
        while R.degree()>=B.degree():
            d = R.degree()-B.degree()+1
            C = Polynomial([0 for i in range(d)])
            C[-1] = R[-1]/B[-1]
            R = R-B*C
            Q = Q+C
            Q.correct()
            R.correct()
        return [R,Q]

        #Ce que j'ai du faire pour trouver l'implementation...
        #On a: A=BQ+R
        #[3,2,4,5,1]/[1,4,1]
        #[3,2,3,1,0]=[3,2,4,5,1]-[0,0,1]*[1,4,1] #[0,0,1,4,1]
        #[3,1,-1,0]=[3,2,3,1]-[0,1]*[1,4,1] #[0,1,4,1]
        #[4,5,0]=[3,1,-1]-[-1]*[1,4,1] #[-1,-4,-1]
        #[4,5]

        #5=8*0+5 cas particulier de la division euclidienne


if __name__ == "__main__":
    suite1 = [3,2,4,5,1]
    suite2 = [1,4,1]
    suite3 = [4,5]
    A = Polynomial(suite1)
    B = Polynomial(suite2)
    C = Polynomial(suite3)
    print("A =",A)
    print("B =",B)
    print("C =",C)
    print("A+B =",A+B)
    print("A*B =",A*B)
    print("Derivative of A =",A.derivative())
    print("A/B :",A/B)
    print("Unit polynomial of C =",A.unit())
    print("HCF (PGCD en francais) of A and B (written A^B) =",A^B)
    print("LCM (PPCM en francais) of A and B (written A|B) =",A|B)
