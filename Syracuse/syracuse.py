from mywindow import *
from mycolors import *

from GrapherV3 import *

class Tree:
    def __init__(self,position=(-10,0),size=(20,20)):
        self.position=position
        self.size=size
        self.coordonnates=size+position
        self.color=WHITE

    def draw(self,plan,window):
        self.trace(plan,window)
        for i in range(len(self.trunk)):
            value,start,end=self.trunk[i]
            pygame.draw.line(window.screen, self.color, start, end, 1)



class Syracuse(Tree):
    def __init__(self):
        Tree.__init__(self)
        tx,ty=self.position
        self.trunk=[(1,(0,0),(0,0))]
        try:
            self.grow(self.trunk)
            #print(self.trunk)
        finally:
            print(self.trunk)

    def grow(self,trunk):
        tx,ty=self.position
        sx,sy=self.size
        new_trunk=[]
        #print(position)
        for branch in trunk:
            #print(branch)
            value,old_position,position=branch
            x,y=position
            #print(position)
            if tx<=x<sx and ty<=y<sy:
                #print(position)
                new_trunk.append((2*value,(x,y),(x-1,y+1)))
                if (value-1)%3==0 and value!=1:
                    new_trunk.append(((value-1)//3,(x,y),(x+1,y+1)))
        self.trunk+=new_trunk
        self.grow(new_trunk)


if __name__=="__main__":
    window=Window()
    arbre=Syracuse()
    print(arbre.trunk)
