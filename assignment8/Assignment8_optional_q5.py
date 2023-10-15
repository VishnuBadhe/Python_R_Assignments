# 5:- Write a program in python that accepts a string to setup a passwords. Your entered password
#     must meet the following requirements:
# * The password must be at least eight characters long.
# * It must contain at least one uppercase letter.
# * It must contain at least one lowercase letter.
# * It must contain at least one numeric digit.

def function():
    password = input(f"Enter a Password: ")
    lower = upper = digit = False
    l1 = list()

    for index in password:
        l1.append(index)
    # print(l1)
    if len(password) >= 8:
        for character in password:
            if character.isupper():
                upper = True
            if character.islower():
                lower = True
            if character.isnumeric():
                digit = True
    else:
        print("Password must be at least 8 characters.")

    if upper and lower and digit:
        print("Valid Password.")
    else:
        print("Invalid Password.")


function()
