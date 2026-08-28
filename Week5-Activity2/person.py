class Person:
   
   def __init__(self, name, address, age):
       self.name = name
       self.address = address
       self.age = age

   def describe(self):
       return "Person({}, {})".format(self.name, self.age)
   
   def greet(self):
       print("Greetings and felicitations from the maestro " + self.name)

person1 = Person("Bilal", "123 Main St", 29)

print(person1.describe())