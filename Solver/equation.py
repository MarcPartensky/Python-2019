from expression import *

def isolate(equation):
    i=equation.index("=")
    first_member=equation[:i]
    second_member=equation[i+1:]
    equation="("+first_member+")-("+second_member+")=0"
    print(equation)
    return equation
