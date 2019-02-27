from classes import Str,List,Sentence,Word

def test(arg1,arg2):
    #do something with args
    a = arg1 + arg2
    return a



keywords=["assert","break","class","continue","def","del","elif","else","except","finally","for",
          "from","global","if","import","in","pass","print","raise","return","try","while","yield"]

conversion = {"assert":"ASSERT",
              "break":"SORTIR DE LA BOUCLE"
              "class":"CLASSE",
              "continue":"CONTINER",
              "def":"DONNEES",
              "del":"SUPPRIMER",
              "elif":["SINON SI","FAIRE"],
              "else":["SINON","FAIRE"],
              "except":"EXCEPTE",
              "finally":"FINALLEMENT",
              "for":["POUR","FAIRE"],
              "from":"DEPUIS",
              "global":"GLOBAL",
              "if":"SI",
              "import":"IMPORTER",
              "in":"DANS",
              "pass":"PASSER",
              "print":"AFFICHER",
              "raise":"RELEVER",
              "return":"AFFICHER",
              "try":"ESSAYER",
              "while":["TANT QUE","FAIRE"],
              "yield":"PASSER AU TOUR SUIVANT",
              "==":"=",
              "=":"<-"}

def convert(name):
    import inspect
    lines = inspect.getsource(foo)
    lines=Str(lines)
    output=[]
    for line in lines:
        output.append(convert(line)
    return "".join(output)

def convert(line):
    pass
