#  6. Define a function overlapping() that takes two lists and returns True if they
#     have at least one member in common, False otherwise.

def function():
    x = False
    list1 = [1,5,6,9,11]
    list2 = [2,3,6,12,10]

    length = len(list1)
    for i in range(length):
        for j in range(len(list2)):
           if list1[i] == list2[j]:
               x= True
    return x

a = function()
print(a)




