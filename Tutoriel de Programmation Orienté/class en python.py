class human:
    def __init__(self,nom):
        self.pieds=2
        self.nom=nom
    def marcher(self):
        print("Yes je marche avec mes "+self.nom+" pieds")

valentin=human("valentin")
valentin.marcher()
