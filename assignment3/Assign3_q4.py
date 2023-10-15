# 4. Print the given number in words.(eg.1234 => one two three four).
#    numbers = [" ", "one", "two", "three", "four"]

number = int(input("Input any number: "))
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
output = []

while(number > 0):
    index = number % 10
    number = number // 10
    output.append(numbers[index])
output.reverse()
print(output)

