class BankAccount:

    def __init__(self, account_number: str, customer_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = float(balance)

    def display_details(self) -> None:

        print("Account Details:")
        print("----------------")
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name:  {self.customer_name}")
        print(f"Balance:        ${self.balance:,.2f}")
        # print(f"Interest Rate: {self.interest_rate}%")
        print("----------------")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        
        self.balance += amount

        print(f"Deposited ${amount:,.2f}. New balance: ${self.balance:,.2f}")



    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        
        if amount > self.balance:
            print("Insufficient funds. Cannot do Withdrawal -- cancelled")
            return
        
        self.balance -= amount

        print(f"Withdrew ${amount:,.2f}. New balance: ${self.balance:,.2f}")


class SavingsAccount(BankAccount):

    def __init__(self, account_number: str, customer_name: str, balance: float = 0.0):
        super().__init__(account_number, customer_name, balance)

    def calculate_interest(self, rate_percent: float) -> float:

        if rate_percent < 0:
            raise ValueError("Interest rate cannot be negative")
        interest = self.balance * (rate_percent / 100.0)

        print(f"Interest at {rate_percent}% on ${self.balance:,.2f} = ${interest:,.2f}")
        return interest

    def display_details(self):

        print("Account Type:   Savings Account")
        super().display_details()

class CheckingAccount(BankAccount):

    def __init__(self, account_number: str, customer_name: str, balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(account_number, customer_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > (self.balance + self.overdraft_limit):
            print("Insufficient funds including overdraft limit. Cannot do Withdrawal -- cancelled")
            return
        
        self.balance -= amount
        print(f"Withdrew ${amount:,.2f}. New balance: ${self.balance:,.2f}")

    def display_details(self):
        print("Account Type:   Checking Account")
        super().display_details()
        print(f"Overdraft Limit: ${self.overdraft_limit:,.2f}")

class BankLoan():

    def __init__(self, loan_id: str, customer_name: str, loan_amount: float, interest_rate: float):
        self.loan_id = loan_id
        self.customer_name = customer_name
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate

    def calculate_loan_interest(self) -> float:
        interest = self.loan_amount * (self.interest_rate / 100.0)
        print(f"Loan Interest at {self.interest_rate}% on ${self.loan_amount:,.2f} = ${interest:,.2f}")
        return interest

    def display_loan_details(self):
        print("Loan Details:")
        print("----------------")
        print(f"Loan ID:         {self.loan_id}")
        print(f"Customer Name:   {self.customer_name}")
        print(f"Loan Amount:     ${self.loan_amount:,.2f}")
        print(f"Interest Rate:   {self.interest_rate}%")
        print("----------------")

if __name__ == "__main__":
    acct = SavingsAccount("SA0001", "John", 5000)

    acct.display_details()

    acct.deposit(1000)
    acct.withdraw(500)

    acct.calculate_interest(5)

    print("\n------")
    acct.loan = BankLoan("LN0001", "John", 10000, 7)
    acct.loan.display_loan_details()
    acct.loan.calculate_loan_interest()

    