# 5. Python program to find sum of n numbers using for loop.

def sum(s):
    add = 0
    for index in range(1, s+1):
        add = add + index
    return add


s = int(input("Enter a number : "))
add = sum(s)
print(f"Sum of n numbers = {add}")





