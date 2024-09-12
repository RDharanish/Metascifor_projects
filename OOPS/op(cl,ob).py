class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def detials(self):
        print("Details\n",self.name,'\n',self.age,'\n',self.gender)

obj=Person('dharanish',22,'male')
obj.detials()
