from person import Person


class Staff(Person):

    def __init__(self, name, address, age, staff_id):
        
        super().__init__(name, address, age)
        self.staff_id = staff_id
        self.tax_num = None

    def get_details(self):
        return "Staff(name={}, id={}, tax_num={})".format(self.name, self.staff_id, self.tax_num)


class Lecturer(Staff):
    # Academic staff with publications

    def __init__(self, name, address, age, staff_id, publications=None, tax_num=None):
        super().__init__(name, address, age, staff_id)
        self.tax_num = tax_num
        self.publications = publications or []

    def add_publication(self, title):
        self.publications.append(title)

    def num_publications(self):
        return len(self.publications)

    def display_publications(self):
        count = self.num_publications()

        # Display the number of publications
        print(f"{self.name} has {count} publication{'s' if count != 1 else ''}.")

        # Display the list of publications
        for pub in self.publications:
            print(" - " + pub)


class GeneralStaff(Staff):
    # General staff with pay calculation

    def __init__(self, name, address, age, staff_id, hourly_wage, hours_worked=0, tax_num=None):
        super().__init__(name, address, age, staff_id)
        self.tax_num = tax_num
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_pay_rate(self):
        return self.hourly_wage 

    def monthly_pay(self):
        return self.calculate_pay_rate() * self.hours_worked

if __name__ == "__main__":
    # Lecturer publications

    lec = Lecturer("Mr. Mohammad", "30, Mt Eden, Auckland", 42, "LS-1001", publications=["Programming Paper", "Blockchain Paper"], tax_num="TRN-00123") 

    lec.display_publications()

    # General staff pay rate
    gs = GeneralStaff("Amman", "12, Remeura, Auckland", 35, "GS-2001", hourly_wage=25.0, hours_worked=160, tax_num="TRN-00456")

    pay_rate = gs.calculate_pay_rate()

    # Display the effective hourly pay rate and monthly pay
    print(f"{gs.name}'s effective hourly pay rate : ${pay_rate:.2f}")

    # Display the monthly pay based on hours worked
    print(f"{gs.name}'s monthly pay based on : {gs.hours_worked} hours --> ${gs.monthly_pay():.2f}")
