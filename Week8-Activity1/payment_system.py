
# Target
class Target:
    def pay(self, amount):
        print("payment method not including old third party system")

# Adaptee -- existing third party system 
class OldPaymentSystem:
    def make_payment(self, amount):
        print("---------------------------------------------")
        print("Payment of $",amount ,"made using Old Payment System.")


# Adapter using Composition
class PaymentAdapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def pay(self, amount):
        self.adaptee.make_payment(amount)

# ----------------------------------- #

# Adapter using Multiple Inheritance
class PaymentAdapterMultipleInheritance(Target, OldPaymentSystem):
    def pay(self, amount):
        self.make_payment(amount)


# Client
if __name__ == "__main__":
    # Composition adapter
    old_system = OldPaymentSystem()
    adapter = PaymentAdapter(old_system)
    adapter.pay(500)   

    # Multiple inheritance adapter
    mi_adapter = PaymentAdapterMultipleInheritance()
    mi_adapter.pay(500)

