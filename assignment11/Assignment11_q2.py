# Q2:-
# Write a Python function student_data () which will print the id of a student (student_id).
# If the user passes an argument student_name or student_class(use **kwargs)
# the function will print the student name and class.

def student_info(*args, **kwargs):
    if kwargs.get('info') == 'student_name':
        print(f"Student Name: {args}")
    elif kwargs.get('info') == 'student_class':
        print(f"Student Class: {args}")
    elif kwargs.get('info') == None:
        print(f"Student ID: {args}")
    else:
        print(f"Student ID: {args}")


n = input("Enter Value: ")
i = input("Enter what is the type of the value(student_info or student_class): ")
student_info(n, info=i)


