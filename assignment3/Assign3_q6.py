# 6. Write a function filter_long_words() that takes a list of words and
#    an integer len and returns the list of words that are longer than len.

def filter_long_words():
    words_list = ['Amey', 'Ajay', 'Ashish', 'Aman', 'Akshay']
    list1 = []

    length = int(input(f"Enter a number: "))

    for value in words_list:
        if len(value) > length:
            print(f"words that are loger than length: {value}")
            list1.append(value)


    return list1

list2 = []
list2 = filter_long_words()
print(f"list of words that are longer than length = {list2}")
