cur = "GEL"
n = input("Your name: ")
s = input("Your last name: ")
c = input("Your balance: ")
def balance(name, surname, balance):
    info = name + " " + surname + " " + balance + cur 
    # print(info)
    return balance
balance(n, s, c)

print(balance(n, s, c))

