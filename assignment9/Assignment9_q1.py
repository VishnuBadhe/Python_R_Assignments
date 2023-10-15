# Ques 1.:-
# Create a class 'Student' with rollno, studentName, course ,dictionary of marks(subjectName -
# marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data
# E. accept records of 5 students and Print it


class Student:
    def __init__(self, rollno=0 , studentname='', course='', marks=0):
        self.rollno = rollno
        self.studentname = studentname
        self.course = course
        self.marks = marks
        self.list1 = []

    def accept_student_data(self, rollno=0, studentname='', course='', marks=0):
        rollno = int(input("Enter roll no.: "))
        self.rollno = rollno
        name = input("Enter Name : ")
        self.studentname = studentname
        course = input("Enter Course :")
        self.course = course
        self.marks = {'Maths':0,
                      'Science':0,
                      'Sanskrit':0,
                      'Hindi':0,
                      'History':0
                      }
        for index in self.marks:
            m1 = input(f"Enter the Marks in {index} : ")
            self.marks[index] = m1

    def print_student_data(self):
        print(f"Roll No.: {self.rollno}")
        print(f"Student Name : {self.studentname}")
        print(f"Course : {self.course}")
        print(f"Marks : {self.marks}")


list2 = []
s = int(input(f"Enter the number of students: "))
for index in range(s):
    st = Student()
    st.accept_student_data()
    list2.append(st)

for num in list2:
    print(f"Student {list2.index(num)}: ")
    num.print_student_data()







