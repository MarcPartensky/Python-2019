from polynomial import Polynomial


def getInteger(message):
    number=0
    for i,character in enumerate(message):
        c=int(character)
        number+=c*2**i
    return number

class TByte(int):
    def __init__(self,other):
        """Create somekind of a byte value using integers at its core."""
        super().__init__()
        self.correct()

    def correct(self):
        """Correct the byte."""
        self%=369

    def __add__(self,other):
        """Add two bytes."""
        result=other+self
        result.correct()
        return result

    __sub__=__add__

    def __str__(self):
        """Return the string representation of the byte."""
        conversion=lambda n:[(n//(2**i))%2 for i in range(7,-1,-1)]
        return str(conversion(self))


    def __call__(self):
        pass







class ReedSolomon:
    def N(message):
        """Return the number 'n' of characters of the message."""
        return len(message)

    def StrToAscii(message):
        """Return the ascii code for each letter of the message."""
        ascii_code=[]
        for character in message:
            ascii_character=ord(character)
            ascii_code.append(ascii_character)
        return ascii_code

    def AsciiToList(ascii_code):
        """Return the list code for the ascii characters by converting in binary
        each ascii character and concatenating the results."""
        conversion=lambda n:[(n//(2**i))%2 for i in range(7,-1,-1)]
        list_code=[]
        for ascii_character in ascii_code:
            list_character=conversion(ascii_character)
            list_code+=list_character
        return list_code

    def __init__(self,alpha=1,k=256):
        """Create a Reed Solomon encoder and decoder"""
        sefl.alpha=alpha
        self.k=k

    def StrToByte(self,message,k):
        """Convert a str message in byte."""
        if k==256:
            return ReedSolomon.StrToAscii(message)

    def StrToList(self,message,k=256):
        """Convert the message in list code."""
        byte_code=self.StrToByte(message,k)
        list_code=self.ByteToList(ascii_code)
        return list_code

    def encode(self,message):
        """Encode the message."""
        self.n=ReedSolomon.N(message)
        list_code=self.StrToList(message,k)
        A=Polynomial(list_code)


if __name__=="__main__":
    message="salut comment ca va"
    #coder=ReedSolomon()
    #code=coder.encode(message)
    #message=coder.decode(code)
    message="100011101"
    n=getInteger(message)
    print(n)
    b=TByte(256)
    print(b)
    print(512%369)
    conversion=lambda n:[(n//(2**i))%2 for i in range(7,-1,-1)]
    print(conversion(143))
