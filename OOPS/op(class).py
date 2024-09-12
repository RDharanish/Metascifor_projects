class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("name is:",self.name,"age is:",self.age)
class Char(Person):
    def __init__(self, name, age,id,):
        super().__init__(name, age)
        self.id=id
    def add(self):
        print("NAME 1",self.name,"AGE IS ",self.age,"id: ",self.id)
class Emp(Char):
    def __init__(self, name, age, id,dep):
        super().__init__(name, age, id)
        self.dep=dep
    def employee(self):
        print("NAME2:",self.name,"age:",self.age,"id=",self.id,"dep",self.dep)

#run=Person(input("name: "),input("age:"))
#run.details()
ob1=Char(input("name:"),input("age:"),input("id:"))
ob1.add()
ob2=Emp(input("emp_name:"),input("emp_age:"),input("emp_id"),input("emp_dep:"))
ob2.employee()

        