

"""
x| |o
 | |x
 | |x
"""

class Morpion:
    def __init__(self):
        self.grille=[[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        self.symboles=[" ","x","o"]

    def aff(self):
        for y in range(3):
            a="|".join(map(lambda x:self.symboles[x],self.grille[y]))
            print(a)
    m.aff()
