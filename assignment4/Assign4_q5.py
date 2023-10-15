# 5. Define a procedure histogram() that takes a list of integers and prints a
#    histogram to the screen.
#    For example, histogram([4, 9, 7]) should print the following:
#    ****
#    *********
#    *******

def histogram():
    list1 = []
    for index in range(6):
            num = int(input(f"Enter the integer: "))
            list1.append(num)
    for j in range(len(list1)):
         print("*" * list1[j])

histogram()
