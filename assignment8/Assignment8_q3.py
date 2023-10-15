# Que 3
# Person class and child Student class Create a class Person with attributes: name and age of type
# string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student which inherits from the Person class and which also has a section
# attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via
# the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"---Student's Attributes---")
        print(f"name = {self.name}")
        print(f"age = {self.age}")

class Student(Person):
    def __init__(self,name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        Person.display_person(self)
        print(f"Section of Student = {self.section}")


p = Person('Vishnu', 25)
p.display_person()

print()

s = Student('Vishnu', 25 ,'B')
s.displayStudent()




