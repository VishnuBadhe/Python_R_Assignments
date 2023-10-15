# 3. Write a function find_longest_word() that takes a list of words and
#    returns the length of the longest word and that word itself.

def find_longest_word():
    words_list = ['Yash', 'Vishnu', 'Ganesh', 'Tejas', 'Jaywardhan']
    length = 0
    for value in words_list:
        if len(value) > length:
            length = len(value)
    print(f"length = {length}")

    for value in words_list:
        if len(value) == length:
            print(f"Longest word in list = {value}")

find_longest_word()


