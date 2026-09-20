class Car:
     def price(self):
         return 25000
     def description(self):
         return "Basic Car"
     
class CarDecorator:
    def __init__ (self, coffee):
        self.car = car
    def price(self):
        return self.car.price()
    
class GPSDecorator(CarDecorator):
    def price(self):
        return self.car.price() + 500

class SunroofDecorator(CarDecorator): 
      def price(self):
        return self.car.price() + 1000
      
class LeatherSeatDecorator(CarDecorator): 
     def price(self):
        return self.car.price() + 1500
     
class PremiumSoundSystemDecorator(CarDecorator): 
     def price(self):
        return self.car.price() + 800
     
car = Car()
car = GPSDecorator(car)
car = SunroofDecorator(car)
car = LeatherSeatDecorator(car)
car = PremiumSoundSystemDecorator(car)


car = GPSDecorator(SunroofDecorator(LeatherSeatDecorator(PremiumSoundSystemDecorator(Car())))) 
print("Car Price is $",car.price())