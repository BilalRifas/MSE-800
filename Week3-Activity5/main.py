from database import create_tables

from exchangeManager import insert_sample_data
from exchangeManager import show_transaction_count
from exchangeManager import show_customer_transactions


def menu():
   print()
   print("==============================")
   print(" Money Exchange System")
   print("==============================")
   print("1. Show Total Transactions")
   print("2. Show Transaction History")
   print("0. Exit")


def main():
   while True:
       create_tables()
       insert_sample_data()

       menu()

       choice = input("Please choose: ")
       if choice == "1":
           show_transaction_count()

       elif choice == "2":
           show_customer_transactions()

       elif choice == "0":
           print("Goodbye!")
           break

       else:
           print("Invalid choice.")


if __name__ == "__main__":
   main()