

"""
class Hanoi:
    def __init__(self,tower1,tower2,tower3):
        self.tower1=tower1
        self.tower2=tower2
        self.tower3=tower3
        self.moveTower(10,tower1,tower2,tower3)

    def moveTower(height,fromPole, toPole, withPole):
        if height >= 1:
            self.moveTower(height-1,fromPole,withPole,toPole)
            self.moveDisk(fromPole,toPole)
            self.moveTower(height-1,withPole,toPole,fromPole)

    def moveDisk(fp,tp):
        print("before moving disk from",fp,"to",tp)
        tp=[fp[0]]+tp
        del fp[0]
        print("after moving disk from",fp,"to",tp)
        self


if __name__=="__main__":
    tower1=[x for x in range(10)]
    tower2=[]
    tower3=[]
    hanoi=Hanoi()

    print(hanoi.tower1)
    print(hanoi.tower2)
    print(hanoi.tower3)
"""


number_of_disks=4

tower1=[x for x in range(number_of_disks)]
tower2=[]
tower3=[]

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
    tp.reverse()
    tp.append(fp[0])
    tp.reverse()
    del fp[0]

moveTower(number_of_disks,tower1,tower2,tower3)

print(tower1,tower2,tower3)
