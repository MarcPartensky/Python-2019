"""mots=[]

determinants=["le","la","un","une"]

determinants={"avant":[],
              "apres":[],
              "masculin":None,
              "singulier":None}

#print(determinants)"""

words=[]

articles=["a","an","the"]
a=["I","you","he","she","it","we","they"]

class List(list):
    def __init__(self,object):
        super().__init__(object)

    def removeall(self,element):
        while element in self:
            self.remove(element)

    def purge(self,elements):
        for element in elements:
            self.removeall(element)

    def keep(self,elements):
        for element in self[:]:
            if not (element in elements):
                self.removeall(element)






class Str(str):
    def __init__(self,object):
        super().__init__()
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        self.consonants="bcdfghjklmnpqrstvwxyz"
        self.vowels="aeiouy"
        self.numbers="0123456789"

    def remove(self,element):
        self.replace(element,"")


    def removeall(self,element):
        while element in self:
            self.replace(element,"")


    def purge(self,elements):
        a=Str("")
        l=List(self)
        l.purge(elements)
        return Str(a.join(l))

    def keep(self,elements):
        a=Str("")
        l=List(self)
        l.keep(elements)
        return Str(a.join(l))


    def reverse(self):
        self=[l for l in self[-1:]]
        #for i in range(len(self)//2):
        #    self[i]=self[-i-1]

    def append(self,element):
        self+=element


    def apphead(self,element):
        self.reverse()
        self.append(element)
        self.reverse()

    def __sub__(self,element):
        return self.replace(element,"")

    def __isub__(self,element):
        self.replace(element,"")

    def __truediv__(self,element):
        self.replace(element,"")

    def __floordiv__(self,element):
        while element in self:
            self.replace(element,"")





class Sentence(Str):
    def __init__(self,object):
        super().__init__(object)
        self.words=self.wordsplit()

    def wordsplit(self):
        text=self[:]
        text=text.lower()
        text=Str(text.replace("'"," "))
        text=text.keep(" "+self.alphabet)
        words=List(text.split(" "))
        words.removeall('')
        words=[Word(word) for word in words]
        return words




class Word(Str):
    def __init__(self,object):
        super().__init__(object)
        self.syllables=self.syllablesplit()

    def syllablesplit(self):
        syllables=[]
        word=self[:]
        while word!="":
            syllable=self.firstsyllable(word)
            syllables.append(syllable)
            word=word[len(syllable):]
        return syllables

    def firstsyllable(self,word):
        vowelfound=False
        for i in range(len(word)-1):
            if word[i] in self.vowels: vowelfound=True
            if (word[i] in self.consonants) and (word[i+1] in self.vowels):
                if i>0 and vowelfound: return word[:i]
        return word


class MutableString(object):
    def __init__(self, data):
        self.data = list(data)
    def __str__(self):
        return "".join(self.data)
    def append(self,element):
        self.data+=list(element)
    def appstart(self,element):
        self.data.reverse()
        element.reverse()
        self.data.append(element)
        self.data.reverse()

    def __repr__(self):
        return "".join(self.data)
    def __setitem__(self, index, value):
        self.data[index] = value
    def __getitem__(self, index):
        if type(index) == slice:
            return "".join(self.data[index])
        return self.data[index]
    def __delitem__(self, index):
        del self.data[index]
    def __add__(self, other):
        self.data.extend(list(other))
    def __len__(self):
        return len(self.data)
    def __reverse__(self):
	       self.data.reverse()



noun={"nature":None,
      "singular":None,
      "synonyms":[]}







if __name__=="__main__":

    sentence=Sentence("you're a fucking asshole you dumbass, you are a scrotumbag")
    b=Str([1,2])
    #a=a.remove(".")
    #print(a)
    print(sentence.words)
    print([word.syllables for word in sentence.words])
    print(sentence-"fucking ")
    sentence=MutableString(sentence)
    print(sentence)
    print(sentence.append("Wesh negro"))
    #print(list(a))
    #print(a.remove("s"))
    #print(b.remove(1))


    #def decomposeSentence(Str):

        #return words

    #decomposeSentence(a)
