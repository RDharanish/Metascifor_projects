class rec:
    def __init__(self):
        self.length=0
        self.breadth=0
    def setlength(self,length):
        self.length=length
    def setbreadth(self,breadth):
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class square(rec):
    def setlength(self, length):
        self.length=length
        self.breadth=length
    def setbreadth(self, breadth):
        self.breadth=breadth
        self.breadth=breadth
sq=square()
sq.setlength(7)
print(sq.area())
sq.setbreadth(9)
print(sq.area())