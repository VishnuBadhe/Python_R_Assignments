# 2. Display following menu and write required function for it
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times


def sample_str():
    # str1 = " "
    str1 = input("Enter the data for the list: ")
    print(f"Original string: {str1}")
    return str1


def even_pos():
        l1 = sample_str()
        # l1.replace(" ","")
        l2 = []
        for i in range(len(l1)):
            if i % 2 == 0:
                l2.append(l1[i])
        print(f"Characters at even position: {l2}")


def odd_pos():
    l1 = sample_str()
    l2 = []
    for i in range(1,len(l1),2):
        l2.append(l1[i])
    print(f"Characters at odd position: {l2}")


def str_len():
    l1 = sample_str()
    print(f"Length of the String: {len(l1)}")
    return len(l1)
def add_to_a_string():
    l1 = sample_str()
    length_str = len(l1)
    l1 = (l1+'a'*length_str)
    print(f"New String: {l1}")

def menu():
    print("-----Welcome to My String Application-----")
    print("1. Display characters from even position")
    print("2. Display characters from odd position")
    print("3. Display length of a string")
    print("4. Add a at the end of string length times")
    print("5. Exit")
    return int(input("Enter Your Choice: "))

def exec():
    while True:
        choice = menu()
        if choice == 1:
            even_pos()
        elif choice == 2:
            odd_pos()
        elif choice == 3:
            str_len()
        elif choice == 4:
            add_to_a_string()
        else:
            break

exec()