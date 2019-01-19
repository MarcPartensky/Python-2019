from set import *
from equation import *
from expression import *

class Solver:
    def __init__(self):
        self.solved=False
        self.valid_equation=None
        self.valid_typeCheck=None
        self.comparisons=None
        self.unknowns=None
        self.resolution=[]
        self.loadVocabulary()


    def __call__(self,input):
        self.input=input
        self.type=type(self.input)
        self.output=""
        self.analyse()
        self.end()
        return self.output


    def loadVocabulary(self):
        self.lower_case_alphabet="abcdefghijklmnopqrstuvwxyz"
        self.upper_case_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.all_case_alphabet=self.lower_case_alphabet+self.upper_case_alphabet
        self.operations="+-*/!%^()"
        self.comparisons="=<>~"
        self.numbers="0123456789"
        self.valid_types=[str]

    def analyse(self):
        self.isValidType(self.input)
        if not self.valid_typeCheck:
            self.output="The type is not valid.\n"
        else:
            self.isEquation(self.input)
            if self.valid_equation:
                self.equation=self.input
                self.solveEquation(self.equation)
            else:
                self.output="The input isn't an equation."

    def isValidType(self,input):
        if self.type in self.valid_types:
            self.valid_typeCheck=True
        else:
            self.output+="Insert an input of type:\n"
            self.output+=str(self.valid_types)+"\n"
            self.valid_typeCheck=False

    def isEquation(self,input):
        valid_equation=True
        comparisons=intersection(input,self.comparisons)
        unknowns=intersection(input,self.all_case_alphabet)
        operations=intersection(input,self.operations)
        if len(comparisons)==0:
            valid_equation=False
        if len(unknowns)==0:
            valid_equation=False
        self.valid_equation=valid_equation


    def solveEquation(self,equation):
        self.equation=equation
        self.step=0
        self.max_steps=100
        while self.step<self.max_steps and not self.solved:
            self.resolution.append(self.equation)
            self.unknowns=intersection(equation,self.all_case_alphabet)
            self.comparisons=intersection(equation,self.comparisons)
            self.operations=intersection(equation,self.operations)
            self.equation=isolate(equation)
            if len(self.unknowns)==1 and self.comparisons==["="] and self.operations:
                pass
            self.output+="Resolution: \n"
            self.output+=str(self.resolution)+"\n"

    def end(self):
        if not self.solved:
            if len(self.output)==0:
                self.output+="The resolution of this problem still needs to be implemented."
            else:
                self.output+="The resolution of this problem is being implemented."

solve=Solver()

if __name__=="__main__":
    solve(input("Enter: "))
