 # 7:- Write a program that accepts a list from user and print the alternate element of list

def function():
    list = []
    for index in range(5):
        element = input(f"Enter the elements: ")
        list.append(element)
    print(list)

    for num in range(0, len(list), 2):
        print(list[num])


function()

