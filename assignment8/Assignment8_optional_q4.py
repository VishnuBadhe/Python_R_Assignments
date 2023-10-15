# 4:- Write a program that reads a string from keyboard and display:
#   * The number of uppercase letters in the string
#   * The number of lowercase letters in the string
#   * The number of digits in the string
#   * The number of whitespace characters in the string


def function():
    string = input(f"Enter a string: ")

    print(f"String before converted to uppercase: ", {string})
    print(f"String after converted to uppercase: ", {string.upper()})

    print()

    print(f"String before converted to lowercase: ", {string})
    print(f"String after converted to lowercase: ", {string.lower()})

    print()

    print(f"Number of digits in string: ", {len(string)})

    print()

    space_count = 0
    for index in range(0, len(string)):
        if string[index] == " ":
            space_count = space_count + 1
    print(f"Number of whitespace characters in the string: ", {space_count})


function()

