class human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def work(self):
        if self.occupation=="Football player":
            print(self.name,"plays Football")
        elif self.occupation=="Actor":
            print("Hi i'm ",self.name)
    def speaks(self):
        print(self.name,"How are you")
aakash=human("Aakash","Football player")
aakash.work()
aakash.speaks()

