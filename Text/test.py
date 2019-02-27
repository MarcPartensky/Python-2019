def foo(arg1,arg2):
    #do something with args
    a = arg1 + arg2
    return a



print(lines.split("\n"))



def convertir(nom):
    import inspect
    lines = inspect.getsource(foo)
    lines=Str(lines)
    output=[]
    for line in lines:
        output.append(convert(line))
    return "".join(output)

def convert(line):
    if word_split():



#import dis
#print(dis.dis(foo))

#from dill.source import getsource

#print(getsource(list.remove))
