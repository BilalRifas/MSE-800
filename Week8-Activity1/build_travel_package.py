class Travel:

    def __init__(self, destination, hotel, transport, mealPlan, activities, insurance):
        self.destination = destination
        self.hotel = hotel
        self.transport = transport
        self.mealPlan = mealPlan
        self.activities = activities
        self.insurance = insurance

    def show_details(self):
        print("------------ TRAVEL PACKAGE -------------------")
        print("Destination:", self.destination)
        print("Hotel:", self.hotel)
        print("Transport:", self.transport)
        print("Meal Plan:", self.mealPlan)
        print("Acitvities:", self.activities)
        print("Insurance:", self.insurance)
        print("-----------------------------------------------")


class TeavelPackageBuilder:
    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.mealPlan = None
        self.activities = None
        self.insurance = None

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_hotel(self, hotel):
        self.hotel = hotel
        return hotel
    
    def set_transport(self, transport):
        self.transport = transport
        return self

    def set_mealPlan(self, mealPlan):
            self.mealPlan = mealPlan
            return self

    def set_activities(self, activities):
            self.activities = activities
            return self

    def set_insurance(self, insurance):
            self.insurance = insurance
            return self

    def build(self):
        return Travel(
            self.destination,
            self.hotel,
            self.transport,
            self.mealPlan,
            self.activities,
            self.insurance
)

class TravelDirector:

    def build_travel_package(self, builder): 
        builder.set_destination("Auckland") 
        builder.set_hotel("3 Star") 
        builder.set_transport("Flight")
        builder.set_mealPlan("Full Board")
        builder.set_activities("City Tour")
        builder.set_insurance("Yes") 

        return builder.build()

    
builder= TeavelPackageBuilder()
director = TravelDirector()
travel = director.build_travel_package(builder) 
travel.show_details()

'''
Travel = (
    TeavelPackageBuilder()
    .set_destination("Auckland")
    .set_hotel("3 Star")
    .set_transport("Flight")
    .build()
) '''