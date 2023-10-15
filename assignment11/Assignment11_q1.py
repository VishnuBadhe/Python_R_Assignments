# Q1:--
# Create a short program that prompts the user for a list of grades separated by commas.
# Split the string into individual grades and use a list comprehension
# to convert each string to an integer.
# Use a “try” statement to inform the user when the values they entered cannot be converted.

def function():
    list1 = []
    str1 = input("Enter grades separated by commas: ")



    list2 = str1.strip(" ").split(',')
    print(list2)
    try:
        list_comp = [int(index) for index in list2]
    except ValueError:
        print("Values Entered Cannot be converted to integer")

    else:
        print(list_comp)

    finally:
        print("Program Executed Successfully")

function()
