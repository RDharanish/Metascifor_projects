#vehicles problem
class Vehicles:
    def __init__(self,name):
        self.name=name
        self.isrunning=False
    def start(self):
        self.running=True
        print(self.name,"Started")
    def stop(self):
        self.isrunning= False
        print(self.name,"Stopped")
class Car(Vehicles):
    def __init__(self, name):
        super().__init__(name)
    def honk(self):
        if self.isrunning:
            print(self.name,"honks")
        else:
            print(self.name,"is not running")
class Moto(Vehicles):
    def __init__(self, name):
        super().__init__(name)
    def pop_wheel(self):
        if self.isrunning:
            print(self.name,"pops wheelie")
        else:
            print(self.name,"is not running")
car=Car("car")
mot=Moto('Motorcycle')
car.start()
car.honk()
car.stop()
mot.start()
mot.pop_wheel()
mot.stop()


        