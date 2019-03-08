import math

def puissancede2(number):
    a=1
    while a*2<number:
        a*=2
    return a

print(puissancede2(513))


puissance=lambda x:2**int(math.log(x)/math.log(2))

print(puissance(513))
