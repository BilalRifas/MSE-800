class Observer:
    def update(self, price):
        pass

class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(self.name, "received a new stock price:", price)

class Subject:
    # Subject
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, price):
        for observer in self.observers:
            observer.update(price)

# Concrete Subject
class StockPriceMonitoringSystem(Subject):

    def upload_stock_price(self, title):
        print("New stock price released:", title)
        self.notify(title)

# Create Subject
stock = StockPriceMonitoringSystem()

# Create Observers
investor1 = Investor("Bilal")
investor2 = Investor("Lahiru")
investor3 = Investor("Rithika")

# Subscribe Investors
stock.attach(investor1)
stock.attach(investor2)
stock.attach(investor3)

# Upload video
stock.upload_stock_price("Stock Price for Google released - $105")
