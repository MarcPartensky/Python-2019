# coding: utf-8

sign=lambda x:(x>=0)

class Infinity:
    def __init__(self,sign=1):
        self.sign=sign
    def __ge__(self,other):
        if self.sign: return True
        else:         return False
    def __gt__(self,other):
        if self.sign: return True
        else:         return False
    def __le__(self,other):
        if self.sign: return False
        else:         return True
    def __lt__(self,other):
        if self.sign: return False
        else:         return True
    def __pos__(self):
        return self
    def __neg__(self):
        sign=(self.sign+1)%2
        return Infinity(sign)
    def __abs__(self):
        return Infinity()
    def __add__(self,other):
        return self
    def __sub__(self,other):
        return self
    def __pow__(self,other):
        if other==0:
            return 1
        if other<0:
            return 0
        if type(other)==Infinity:
            if other>0:
                return self
            else:
                return 0
        return self
    def __mul__(self,other):
        if other==0:
            raise Exception("Undetermined")
            return None
        else:
            if sign(other)!=sign(self):
                return Infinity(0)
            else:
                return Infinity(1)
    def __truediv__(self,other):
        if type(other)==Infinity:
            raise Exception("Undetermined")
            return None
        else:
            if sign(other)!=sign(self):
                return Infinity(0)
            else:
                return Infinity(1)
    def __repr__(self):
        if self.sign:
            sign="+"
        else:
            sign="-"
        #return (sign+"∞").encode("utf-8")
        return sign+"oo"
    def __invert__(self,value=10e10):
        if self>0: return value
        else:      return -value


if __name__=="__main__":
    inf=Infinity()
    print(abs(inf)/inf)
    #print(-inf*4*inf*(-inf)+inf**(-inf))
