from database import create_connection

# connect database, insert original data, query data, show results

def insert_sample_data():
   connection = create_connection()
   cursor = connection.cursor()

   # insert customers x5
   if not record_exists(cursor, "Customer", "customer_id", 1):
     cursor.execute("""
       INSERT INTO Customer
       VALUES
       (1,'Richard','Xiahou','0211234567')
     """) 
   
   if not record_exists(cursor, "Customer", "customer_id", 2):
     cursor.execute("""
       INSERT INTO Customer
       VALUES
       (2,'Tom','Smith','0212222222')
     """)

   if not record_exists(cursor, "Customer", "customer_id", 3):
     cursor.execute("""
       INSERT INTO Customer
       VALUES
       (3,'Lucy','Brown','0213333333')
     """)

   if not record_exists(cursor, "Customer", "customer_id", 4):
     cursor.execute("""
       INSERT INTO Customer
       VALUES
       (4,'Jack','Lee','0214444444')
     """)

   if not record_exists(cursor, "Customer", "customer_id", 5):
     cursor.execute("""
       INSERT INTO Customer
       VALUES
       (5,'Emma','Wilson','0215555555')
     """)

   # insert 3 currencies
   if not record_exists(cursor,"Currency","currency_id",1):
     cursor.execute("""
       INSERT INTO Currency
       VALUES
       (1,'NZD','New Zealand Dollar')
     """)

   if not record_exists(cursor,"Currency","currency_id",2):
     cursor.execute("""
       INSERT INTO Currency
       VALUES
       (2,'USD','US Dollar')
     """)
   if not record_exists(cursor,"Currency","currency_id",3):
     cursor.execute("""
       INSERT INTO Currency
       VALUES
       (3,'CNY','Chinese Yuan')
     """)

   # insert 3 exchange rates
   if not record_exists(cursor,"ExchangeRate","rate_id",1):
     cursor.execute("""
       INSERT INTO ExchangeRate
       VALUES
       (1,1,2,0.60)
     """)

   if not record_exists(cursor,"ExchangeRate","rate_id",2):
     cursor.execute("""
       INSERT INTO ExchangeRate
       VALUES
       (2,1,3,4.30)
     """)
   if not record_exists(cursor,"ExchangeRate","rate_id",3):
     cursor.execute("""
       INSERT INTO ExchangeRate
       VALUES
       (3,2,3,7.20)
     """)

   # insert 3  TransactionHistory
   # e.g. Richard - NZD > USD 1000,  Richard do exchange action: 2 times 
   if not record_exists(cursor,"TransactionHistory","transaction_id",1):
     cursor.execute("""
       INSERT INTO TransactionHistory
       VALUES
       (1,1,1,2,1000,0.60)
     """)
   if not record_exists(cursor,"TransactionHistory","transaction_id",2):
     cursor.execute("""
       INSERT INTO TransactionHistory
       VALUES
       (2,2,1,3,500,4.30)
     """)

   if not record_exists(cursor,"TransactionHistory","transaction_id",3):
     cursor.execute("""
       INSERT INTO TransactionHistory
       VALUES
       (3,1,2,3,200,7.20)
     """)

   print("Sample data all inserted.")
   connection.commit()
   connection.close()

# counting transactionHistory numbers
def show_transaction_count():
   connection = create_connection()
   cursor = connection.cursor()

   cursor.execute("""
   SELECT COUNT(*)
   FROM TransactionHistory
   """)

   result = cursor.fetchone()
   print()

   print("Total transactions:", result[0])
   connection.close()

# show all transaction records
def show_customer_transactions():
   connection = create_connection()
   cursor = connection.cursor()

   cursor.execute("""
   SELECT *
   FROM TransactionHistory
   """)

   result = cursor.fetchall()
   print()
   print("Transaction History")

   for row in result:
       print(row)

   connection.close()

def record_exists(cursor, table, field, value):
   sql = "SELECT * FROM " + table + " WHERE " + field + "=?"
   cursor.execute(sql, (value,))
   result = cursor.fetchone()
   if result:
       return True
   return False