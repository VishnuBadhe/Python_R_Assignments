# 1. Write a method in python to display the elements of list thrice if it is a number and display
#    the element terminated with ‘#’ if it is not a number.
#    Hint-: Use InBuilt Function isdigit()
#    Refer below as a input:-
#    mylist = ['41','DROND','Sunbeam', '13','ZARA']


def function():
    mylist = ['41', 'DROND', 'Sunbeam', '13', 'ZARA']

    for index in (mylist):
        if index.isdigit():
            print(index * 3)
        else:
            index =  index+'#'
            print(index)
function()


