# Class to represent a student with personal information
class Student:
    def __init__(self, full_name: str, age: int, address: str, student_id: str):

        # full_name is a text string 
        self.full_name = full_name
        # age is an integer representing the student's age in years
        self.age = age
        # address is a text string 
        self.address = address
        # student_id is a text string because IDs can contain letters or starts with zeros
        self.student_id = student_id

    def __str__(self) -> str:
        return (
            f"Name: {self.full_name}, Age: {self.age}, "
            f"Address: {self.address}, Student ID: {self.student_id}"
        )

#Class to Manage the add student, sorting students by age & displaying the students 
class StudentManager:
    def __init__(self):
        # students is a list that stores Student objects
        self.students = []

    # Method to add a student to the list
    def add_student(self, student: Student) -> None:
        self.students.append(student)

    # Method to sort students by age
    def sort_by_age(self) -> None:
        self.students.sort(key=lambda student: student.age)

    # Method to display the sorted list of students
    def display_students(self) -> None:
        print("\nSorted students by age:\n")
        for student in self.students:
            print(student)

    # Method to collect student data from user input
    def collect_students(self) -> None:
        print("Enter student data." + "\n" + "[ Leave full name blank or Press enter to stop ]")
        while len(self.students) < 70:
            full_name = input("Full name: ")
            if not full_name:
                break

            age_text = input("Age: ")
            if not age_text.isdigit():
                print("Age must be a whole number. Try again.")
                continue
            age = int(age_text)

            address = input("Address: ")
            student_id = input("Student ID: ")

            student = Student(full_name, age, address, student_id)
            self.add_student(student)
            print(f"Added student #{len(self.students)}")

        if not self.students:
            print("No students were entered.")


def main() -> None:
    manager = StudentManager()
    manager.collect_students()

    # Sort and display students if students list is not empty
    if manager.students:
        manager.sort_by_age()
        manager.display_students()


if __name__ == "__main__":
    main()