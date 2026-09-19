class Department:
    def __init__(self, department_name, head):

        self.department_name = department_name

        self.head = head

    def show_department(self):

        print(f"Department: {self.department_name}")
        print(f"Head of Department:  {self.head}")

class University:
    def __init__(self, university_name, department_name, head):

        self.university_name = university_name

        self.department = Department(department_name, head)

    def show_university(self):

        print(f"University: {self.university_name}")

        self.department.show_department()


if __name__ == "__main__":

    university = University("Yoobee University", "Software Engineering", "Dr. Sarah Younus")

    university.show_university()
