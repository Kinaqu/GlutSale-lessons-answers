# person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, I am {self.name}, and I am {self.age} years old.")

# student.py
from person import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hello, I am {self.name}, {self.age} years old, and my student ID is {self.student_id}.")

# file_operations.py
def write_to_file(person, student):
    with open("people_info.txt", "w") as file:
        file.write(f"Person: {person.name}, {person.age} years old.\n")
        file.write(f"Student: {student.name}, {student.age} years old, Student ID: {student.student_id}.\n")

# main_script.py
from person import Person
from student import Student
from file_operations import write_to_file

person = Person("John", 25)
student = Student("Alice", 20, "12345")

person.introduce()
student.introduce()

write_to_file(person, student)
print("Information written to 'people_info.txt'.")
