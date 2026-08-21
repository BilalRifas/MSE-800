import sqlite3


def create_connection():
   connection = sqlite3.connect("moneyEcchange.db")
   print("Database ready.")
   return connection


def create_tables():
   connection = create_connection()
   cursor = connection.cursor()

   # Customer table
   cursor.execute("""
   CREATE TABLE IF NOT EXISTS Customer
   (
       customer_id INTEGER PRIMARY KEY,
       first_name TEXT,
       last_name TEXT,
       phone TEXT
   )
   """)

   cursor.execute("""
   CREATE TABLE IF NOT EXISTS Currency
   (
       currency_id INTEGER PRIMARY KEY,
       currency_code TEXT,
       currency_name TEXT
   )
   """)

   cursor.execute("""
   CREATE TABLE IF NOT EXISTS ExchangeRate
   (
       rate_id INTEGER PRIMARY KEY,
       from_currency INTEGER,
       to_currency INTEGER,
       exchange_rate REAL
   )
   """)

   cursor.execute("""
   CREATE TABLE IF NOT EXISTS TransactionHistory
   (
       transaction_id INTEGER PRIMARY KEY,
       customer_id INTEGER,
       from_currency INTEGER,
       to_currency INTEGER,
       amount REAL,
       exchange_rate REAL
   )
   """)
   

   connection.commit()
#   connection. Close()