
# Task 1 - Single Inheritance
from pyclbr import Class


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emily", 36)

print(p1.name)
print(p1.age)

class Mother:
    def __init__ (self, mothername):
        self.mothername= mothername

# Task 2

class Father:
    def __init__ (self, fathername):
        self.fathername= fathername
    
class Son(Mother, Father):
    def __init__(self, mothername, fathername):
        Mother.__init__(self, mothername)
        Father.__init__(self, fathername)

    def parents(self):
        print(f"Mother: {self.mothername}, Father: {self.fathername}")

son = Son("Alex", "Bob")
son.parents()

# Task 3 - Multilevel Inheritance

class GrandFather:
    def __init__ (self, grandFatherName):
        self.grandFatherName = grandFatherName


class Father(GrandFather):
    def __init__ (self, FatherName, grandFatherName):
            self.FatherName = FatherName
            super().__init__(grandFatherName)


class Son(Father):
    def __init__ (self, SonName, FatherName, grandFatherName):
         self.sonName = SonName
         super().__init__(FatherName, grandFatherName)


    def display(self):
         print(f"Son: {self.sonName}")
         print(f"Father: {self.FatherName}")
         print(f"Grand Father: {self.grandFatherName}")


s1 = Son("Jack", "Bob", "William")
s1.display()

# Task 4 - Hierarchical Inheritance

class Father():
    def __init__ (self, FatherName):
            self.FatherName = FatherName
class Son(Father):
    def __init__ (self, SonName, FatherName):
         self.sonName = SonName
         super().__init__(FatherName)
    def display(self):
         print(f"Son: {self.sonName}")
         print(f"Father: {self.FatherName}")
class Daughter(Father):
    def __init__ (self, DaughterName, FatherName):
          self.DaughterName = DaughterName
          super().__init__(FatherName)
    def display(self):
             print(f"Daughter: {self.DaughterName}")
             print(f"Father: {self.FatherName}")

s1 = Son("Jack", "Bob")
d1 = Daughter("Helen", "Bob")
s1.display()
d1.display()

# Task 5 - Hybrid Inheritance

class F:
    def show_person(self):
        print("This is a person")
class B(F):
    def study(self):
        print("Student is studying")


class G:
    def work(self):
        print("Employee is working")


class E(F, G):
    def teach(self):
        print("Teacher is teaching")


class A(B):
    def attend_class(self):
        print("Undergraduate student is attending class")


class C(B):
    def conduct_research(self):
        print("Postgraduate student is conducting research")

# Undergraduate student
student1 = A()
student1.show_person()
student1.study()
student1.attend_class()
# Postgraduate student
student2 = B()
student2.show_person()
student2.study()
student2.study()
# Teacher
teacher = E()
teacher.show_person()
teacher.work()
teacher.teach()
