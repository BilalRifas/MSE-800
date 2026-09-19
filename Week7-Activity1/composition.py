class Engine:
    def start(self):
        print("Engine is starting")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start_car(self):
        self.engine.start()
        print("Car is moving")

car = Car()
car.start_car()



