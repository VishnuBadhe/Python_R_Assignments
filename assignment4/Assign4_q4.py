# 4. Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an
#    occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def function():
    str = "this is fun"
    str2 = ""
    for char in str:
        if char in "aeiou ":
            str2 = str2 + char
        else:
            str2 = str2 + (char+'o'+char)
    print(str2)

function()    