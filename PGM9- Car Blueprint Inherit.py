class Car:
    @staticmethod
    def start():
        print("Car Started....")
    
    @staticmethod
    def stop():
        print("Car Stop....")

class ToyotoCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotoCar):
    def __init__(self,type,color):
        self.type=type
        self.color=color

Car1=Fortuner("Petrol","Black")
print(Car1.type,Car1.color)
Car1.start()
Car1.stop()