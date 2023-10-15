# Que2. Computation class:
# 1 - Create a Coputation class with a default constructor (without parameters) allowing to
# perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer.
# Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 +
# 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in the Calculation class to test the primality of a given
# integer. Test this method.
# 4 - Create a method called testPrims() allowing to test if two numbers are prime between
# them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given
# integer. Then create an allTablesMult() method to display all the integer multiplication tables
# 1, 2, 3, ..., 9.

class Computation:
    def __init__(self):
        pass

    def factorial(self, num):
        fact = 1
        for index in range(1,num+1):
            fact = fact*index
        print(f"Factorial of {num}: {fact}")

    def sum(self, s):
        sum = 0
        for num in range(s+1):
            sum += num
        print(f"Sum of first {s} numbers: {sum}")

    def testprime(self, num):
        isPrime = True
        for j in range(2,num):
            if num % j == 0:
                isPrime = False
                break
        if isPrime:
            print(f"{num} is prime number")
        else:
            print(f"{num} is not a prime number")

    def testprims(self, num1, num2):
        print(f"Prime numbers between {num1} and {num2}: ")
        for i in range(num1, num2):
            isPrime = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                print(i)

    def alltablemult(self):
        for i in range(1,10):
            print(f"Multiplication Table of {i}: ")
            for j in range(1,11):
                print(f"{i}*{j} = {i*j}")


c1 = Computation()
c1.factorial(5)
c1.sum(10)
c1.testprime(237)
c1.testprims(2,20)
c1.alltablemult()
