# 2. Write a program that display following output:
#    SHIFT
#    HIFTS
#    IFTSH
#    FTSHI
#    TSHIF
#    SHIFT

def function():
    str1 = 'SHIFT'
    for index in range(len(str1)+1):
       slice = str1[index:] + str1[:index]
       print(slice)

function()


