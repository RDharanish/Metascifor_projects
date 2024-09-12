class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class operations(calculator):
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x *self.y
    def div(self):
            if self.y!=0:
                return self.x/self.y
            else:
                 return "ZeroDivisionError"
    def floor(self):
         return self.x//self.y
    def exp(self):
         return self.x **self.y

op=int(input("ENTER THE OPERAATION YOU WANT TO BE PERFORM:\n 1.add 2.substraction 3.multiplication 4.division 5.floor division 6.exponent:\n"))
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
obj=operations(x,y)
if op ==1:
    print(obj.add())
elif op==2:
    print(obj.sub())
elif op==3:
    print(obj.mul())
elif op==4:
    print(obj.div())
elif op ==5:
    print(obj.floor())
elif op==6:
    print(obj.exp())
else:
    print("invlaid")