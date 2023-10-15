# 1. Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as
# "Go hanga salami I'm a lasagna hog.", \
# "Was it a rat I saw?", \
# "Step on no pets",\
# "Siton a potato pan,Otis", \
# "Lisa Bonet ate no basil", \
# "Satan, oscillate my metallic sonatas", \
# "I roamed under it as a tired nude Maori",
# "Rise to vote sir",
# or the exclamation "Dammit, I'm mad!".
# Note that punctuation, capitalization, and spacing are usually ignored.


def palindrome_recognizer():
    str1 = input("Enter the string: ")
    str_new = str1.lower().replace("\'","").replace(" ","").replace("\"","").replace(".","").replace(",","").replace("!","").replace("?","")
    l = list(str_new)
    p = []
    for i in range (len(l)):
        p.append(l[len(l)-1-i])

    if p == l:
        print(f"{str1}\nIs a Palindrome")
    else:
        print(f"{str}\nNot a Palindrome")


palindrome_recognizer()
