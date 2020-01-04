class Machin:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return str("".join(map(str,self.args)))


if __name__ == "__main__":
    machin = Machin(1,2,341)
    print(machin)
    print("do stuff")
