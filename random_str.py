import random
num = 8#random.randint(0,8)
string = input("Type anything: ")

if num == 0:
    print(string.count("a"))
elif num == 1:
    print(string.find("b"))
elif num == 2:
    print(string.replace("c", "*"))
elif num == 3:
    print(string.upper())
elif num == 4:
    print(string.lower())
elif num == 5:
    print(string.capitalize())
elif num == 6:
    print(string.swapcase())
elif num == 7:
    print("d" in string)
elif num == 8:
    print(string.replace("e",""))