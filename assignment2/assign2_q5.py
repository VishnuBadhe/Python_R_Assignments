#  5.  Using for loop, write and run a Python program to find factorial from 0 to
#      10.

def function():
    factorial = 1
    for i in range(0,11):
        if i == 0:
            print(f"The factorial of 0 is 1")
        else:
            factorial = factorial * i
            print(f"The factorial of {i} is {factorial}")


function()








