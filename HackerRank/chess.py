import random

def queensAttack(n, k, r_q, c_q, obstacles):
    f=lambda o:(1<=o[0]<=n and 1<=o[1]<=n)
    obstacles=list(filter(f,obstacles))
    nob=[[x-r_q,y-c_q] for [x,y] in obstacles]
    obstacles=[[x,y] for (x,y) in list(set([(x,y) for (x,y) in obstacles]))]
    def polar(x,y):
        n=math.sqrt(x**2+y**2)



    directions=[[x,y] for x in [-1,0,1] for y in [-1,0,1] if (x,y)!=(0,0)]
    a=0
    for direction in directions:
        dx,dy=direction
        x,y=r_q+dx,c_q+dy
        while f([x,y]):
            if [x,y] in obstacles:
                break
            x+=dx
            y+=dy
            a+=1
    return a



print(queensAttack(100,50,6,7,[[random.randint(1,100),random.randint(1,100)] for i in range(50)]))
