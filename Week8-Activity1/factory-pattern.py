class Pizza:
     def prepare(self):
         print("Cheese Pizza!")
class Burger:
     def prepare(self):
         print("Crispy Chicken Burger!")
class Pasta:
     def prepare(self):
         print("Cheese Pasta!")

class FoodFactory:
     @staticmethod
     def create_food(food_type):
         if food_type == "pizza":
             return Pizza()
         elif food_type == "burger":
             return Burger()
         elif food_type == "pasta":
             return Pasta()
         else:
             raise ValueError("Unknown food")
                              
food = FoodFactory.create_food("pizza")
food.prepare()

food = FoodFactory.create_food("burger")
food.prepare()

food = FoodFactory.create_food("pasta")
food.prepare()