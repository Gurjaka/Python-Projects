CURRENCY = "GEL"

goods = {
    "1": {"Banana": 6},
    "2": {"Apple": 5},
    "3": {"Strawberry": 3.8},
    "4": {"Peach": 4.3},
    "5": {"Grapes": 32},
    "6": {"Tomato": 1.4},
    "7": {"Cucumber": 1.34},
    "8": {"Pepper": 0.4},
}

cart = []

price_list = 0

def menu():
    for num, elem in goods.items():
        for name, infos in elem.items():
            print(f"{num}. {name} - {infos} {CURRENCY}")

def shopping_cart():
    global price_list
    item = input("Choose your product using their index: ")
    quantity = int(input("Choose quantity: "))
    price = str(list(goods[item].keys())[0]) + ": " + str((list(goods[item].values())[0]) * quantity)
    price_list_calc = (list(goods[item].values())[0]) * quantity
    cart.append(price)
    price_list = price_list + price_list_calc

while True:
    menu()
    shopping_cart()
    exit = input("Have you finished shopping? (yes/no): ")
    while exit.lower() not in ("yes", "no"):
        exit = input("Have you finished shopping? (yes/no): ")
    if exit.lower() in ("yes"):
        print("You can now proceed to checkout!")
        break
    elif exit.lower() in ("no"):
        continue

print("Here is your check:")

for i in cart:
    print(i)

print(f"Your total is: {price_list}\n")
