class Test:
    v=1
    def __init__(self):
        self.v=1

    @staticmethod
    def test(cls,self):
        print(cls.v,self.v)

t=Test()
print(t.test())
