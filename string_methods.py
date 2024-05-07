def davaleba1():
    name = input("Type your name: ")
    surname = input("Type your surname: ")

    print(name[:1].capitalize()+".", surname.capitalize())
def davaleba2():
    identity = input("Type your name and surname: ")
    print(identity[:1].capitalize() + ".", identity[int(identity.find(" ")) + 1:].capitalize())
davaleba2()