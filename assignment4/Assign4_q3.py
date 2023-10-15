# 3. A pangram is a sentence that contains all the letters of the English alphabet at least once,
#    for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

def pangram():
    str = "The quick brown fox jumps over the lazy dog"
    alphabets_str = "abcdefghijklmnopqrstuvwxyz"
    list_of_str = set(str.lower().replace(" ","").replace(".","").replace(",",""))
    list_of_alphabets = set(alphabets_str)
    for i in list_of_str:
        if list_of_str == list_of_alphabets:
            print(f"{str}\nIs a Pangram")
            break
        else:
            print(f"{str}\nNot a Pangram")
            break

pangram()