# Q3:-
# Write a Python program to square and cube every number in a given list of integers using
# Lambda,map.
# Input:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output-----Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ------Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

def function():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    sq = lambda x: x ** 2

    square = list(map(sq, list1))
    print(f"Square of List: {square}")

    cb = lambda y: y ** 3

    cube = list(map(cb, list1))
    print(f"Cube of List: {cube}")

function()

