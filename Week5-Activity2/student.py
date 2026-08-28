from person import Person

class Student(Person):
   
   def __init__(self, name, address, age, student_id):
       self.name = name
       self.address = address
       self.age = age
       self.student_id = student_id
       self.courses = []

   def enrol_in_course(self, course_code):
       self.courses.append(course_code)

   def display_details(self):
       print("Student(name='Bilal', id='S-1001')".format(self.name, self.student_id))