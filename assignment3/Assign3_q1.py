 # 1. Write a python program to print sum of tuple elements.

def add_tuple():
    elements = (10,20,30,40,50)
    print(f"tuple elements = {elements}")
    sum=0
    for index in range(len(elements)):
        sum = sum + elements[index]
    print(sum)




add_tuple()



