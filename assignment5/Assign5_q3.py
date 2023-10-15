# 3. Write a program that contains a function that has one parameter, n, representing an integer
#    greater than 0. The function should return n! (n factorial).
#    Then write a main function that calls this function with the values 1 through 20, one at a time, printing the returned
#    results.
#    This is what your output should look like:
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880
# 36288002.

def factorial(num):
    fact = 1
    for index in range(1,num+1):
        fact *= index
    print(fact)


def fun1():

    l1 = list(range(1, 21))
    print(l1)
    for j in l1:
        factorial(l1[j-1])

fun1()


