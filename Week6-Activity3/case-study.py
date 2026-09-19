logged_in = False

def login_required(func):
   def wrapper(*args, **kwargs):
       print("Before the function is called.")
       if logged_in:
           return func(*args, **kwargs)
           print("After the function is called.")
       else:
           print("Access Denied")           
           return None
   return wrapper


@login_required
def view_salary(salary):
    print(f"Salary - ${salary} per month")
Z
@login_required
def view_personal_details():
   print("Personal Details:")
   print("Name: Bilal")
   print("Employee ID: EMP001")

@login_required
def download_report():
   print("Report downloaded successfully")
   print(" - Employee Access Management System -")
   print("\n--- Employee NOT Logged In ---")

view_salary(5000)
view_personal_details()
download_report()
print("\n--- Employee Going to Login ---")
logged_in = True
print("Employee logged in successfully.")

print("\n--- Accessing Employee Functions ---")
view_salary(5000)
view_personal_details()
download_report()

print("\n--- Employee is Logging out ---")
logged_in = False
print("Employee logged out")
print("\n--- Attempting Access After Logout ---")
view_salary(5000)