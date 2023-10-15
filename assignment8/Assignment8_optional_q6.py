# 6:- Write a definition of a method count_now(places) to find and display those place names, in
#    which there are more than 5 characters.
#    For example :
#    If the list places contains
#    ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]
#    The following should get displayed :
#    LONDON
#    NEW YORK

def function():
    list = ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]

    for index in range(len(list)):
        if len(list[index]) > 5:
            print(list[index])


function()