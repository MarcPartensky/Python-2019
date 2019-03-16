class Variable:
    def __init__(self,name="Unknown",content=[None]):
        self.name=name
        self.content=content
    def __add__(self,other):
        if type(other)==int:
            name=self.name+"+"+str(other)
            content=self.content+Variable(other,[other]).content
            return Variable(name,content)
        if type(other)==Variable:
            name=self.name+"+"+other.name
            content=self.content+other.content
        return Variable(name,content)
    def __repr__(self):
        return self.name



x=Variable("x")
y=Variable("y")
z=Variable("z")
print(x+z+1*4*23+1)

#print(1.__name__)
