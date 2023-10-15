# 7. Write a program to sum all the values of a dictionary.
#    Hint
#    dict1 = {‘key 1’: 200, ‘key 2’: 300}
#    Expected output
#    Result: 500

def sum():
    dict1 = {'key1': 200,'key2': 300}
    sum1 = 0
    for i in dict1:
        sum1 = sum1 + dict1[i]
    print(sum1)

sum()


