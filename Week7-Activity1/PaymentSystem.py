# Polymorphism with Payment Methods
class PaymentMethod:

    def make_payment(self, amount: float):
        return "Generic payment"
    
class CreditCard(PaymentMethod):

    def make_payment(self, amount: float):
        return f"Payment of ${amount} made with Credit Card"

class Paypal(PaymentMethod):

    def make_payment(self, amount: float):
        return f"Payment of ${amount} made with PayPal"

class BankTransfer(PaymentMethod):

    def make_payment(self, amount: float):
        return f"Payment of ${amount} made with Bank Transfer"

payments = [CreditCard(), Paypal(), BankTransfer()]

for payment in payments:
    print(payment.make_payment(100.0))