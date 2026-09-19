from abc import ABC, abstractmethod


class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self, pin):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass



class BankATM(ATM):


    def __init__(self, account_holder, balance=1000):
        self.account_holder = account_holder
        self.balance = balance
        self.card_inserted = False
        self.pin_verified = False
        self.valid_pin = "1234"

    def insert_card(self):
        self.card_inserted = True
        print(f"Card inserted for {self.account_holder}")

    def enter_pin(self, pin):
        if not self.card_inserted:
            print("Please insert your card first.")
            return False

        if pin == self.valid_pin:
            self.pin_verified = True
            print("PIN number successfully verified")
            return True

        print("Invalid PIN. Please try again")
        self.pin_verified = False
        return False

    def check_balance(self):
        if not self.card_inserted:
            print("Please insert your card first")
            return None

        if not self.pin_verified:
            print("Please verify your PIN first")
            return None

        print(f"Current balance ---> ${self.balance:.2f}")
        return self.balance

    def withdraw(self, amount):
        if not self.card_inserted:
            print("Please insert your card first")
            return None

        if not self.pin_verified:
            print("Please verify your PIN first")
            return None

        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
            return None

        if amount > self.balance:
            print("Insufficient balance")
            return None

        self.balance -= amount
        print(f"Withdrawn  ---> ${amount:.2f}." )
        print(f"Remaining balance ---> ${self.balance:.2f}")
        return self.balance


if __name__ == "__main__":

    atm = BankATM("Bilal", 5000)
    atm2 = BankATM("Sam", 5000)

    atm.insert_card()
    atm.enter_pin("1234")
    atm.check_balance()
    atm.withdraw(200)

    atm2.insert_card()
    atm2.enter_pin("1234")
    atm2.check_balance()
    atm2.withdraw(200)
    

