# 2:- Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers
# using Lambda.
# Input:-
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Output:-
# [19, 65, 57, 39, 152, 190]


def function():
    numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
    is_divisible = lambda x : x % 13 == 0 or x % 19 == 0
    divisibility = list(filter(is_divisible, numbers))
    print(f"Numbers which are divisible by 19 or 13: {divisibility}")

function()