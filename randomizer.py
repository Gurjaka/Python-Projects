import random

pass_str = input("Choose the password level, Low, Medium, or High : ")

set1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
set2 = "1234567890"
set3 = "!@#$%&*-=_+`"
charset = ""

while True:
    if pass_str == "Low" or pass_str == "low":
        charset = set1
        break
    elif pass_str == "Medium" or pass_str == "medium":
        charset = set1 + set2
        break
    elif pass_str == "High" or pass_str == "high":
        charset = set1 + set2 + set3
        break
    else:
        pass_str = input("Incorrect option. Choose the password level, Low, Medium, or High : ")

while True:
    pass_len = input("Choose password length (minimum len = 8) : ")
    if pass_len.isdigit() and int(pass_len) < 8:
        print("Password length can not be less than 8")
    elif pass_len.isdigit() and int(pass_len) >= 8:
        pass_len = int(pass_len)
        break
    else:
        print("Please choose in numbers, no letters!")

back = ""
while pass_len > 0:
    chars = random.randint(0,len(charset))
    back = back + charset[chars]
    pass_len = pass_len - 1

password = back

print(password)
