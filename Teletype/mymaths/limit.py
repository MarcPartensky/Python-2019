from mymaths.infinity import Infinity

def lim(function,value):
    if type(value)==int:
        return function(value)
    if type(value)==Infinity:
        if value>=0:
            value=10e10
        else:
            value=-10e10
        if function(value)>10e5:
            return Infinity()
        elif function(value)<-10e5:
            return -Infinity()
        else:
            return function(value)
