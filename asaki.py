age = input("Input your age: ")

while True:
    if age.isdigit():
        print("You are", age, "years old")
        break
    elif age[-1:].isdigit():
        age = input("Your age must be positive: ")
    else:
        age = input("Nan, please try again: ")
