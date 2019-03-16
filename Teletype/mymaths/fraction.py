from infinity import Infinity

def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

sign=lambda x:(x>=0)

class Fraction:
    def __new__(self,*args):
        if len(args)==1:
            self.find(args)
        elif len(args)==2:
            if args[1]==0:
                if args[0]==0:
                    raise Exception("Undetermined")
                if args[0]>0:
                    return Infinity()
                if args[0]<0:
                    return -Infinity()
            else:
                return self.__init__(self,args[0],args[1])

    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        self.simplify()

    def __le__(self,other):
        if type(other):
            return False

    def sign(self):
        if sign(self.numerator)!=sign(self.denominator):
            return 0
        else:
            return 1


    def __mul__(self,other):
        if type(other)==int:
            self.numerator*=other
        if type(other)==Fraction:
            pass

    def __add__(self):
        pass

    def find(self,value):
        pass

    def simplify(self):
        a=pgcd(self.numerator,self.denominator)
        self.numerator//=a
        self.denominator//=a


    def __repr__(self):
        if abs(self.denominator==1):
            return str(sign(self))+str(self.numerator)
        return str(self.numerator)+"/"+str(self.denominator)

f=Fraction(-15,1)
print(f)
print(f.numerator,f.denominator)
#print(f)
