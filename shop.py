# define currency
CURRENCY = "GEL"
# Define menu options
MENU = {
    1: "Add item",
    2: "List items",
    3: "Total price",
    4: "Modify item",
    5: "Exit",
}
#define goods
GOODS = {
    "apple" :2,
    "banana" : 3,
    "orange" : 2.5,
    "mustard" : 0.4,
    "coke" : 2,
    "milk" : 3,
    "bread" : 1.5,
    "cheese" : 15,
    "mineral water" : 1.2,
    "chocolate" : 6
}
basket = []
# Function to display the menu
def display_menu():
    print("\n--- Shopping Basket ---")
    for option, name in MENU.items():
        print(f"{option}. {name}")

# Function to display available goods
def display_goods():
    print("\n--- Available goods ---")
    for name, price in GOODS.items():
        print(f"{name} - {price} {CURRENCY}.")
        
# Function to add goods to your basket
def add_to_basket():
    name = input("enter name: ").lower()
    if name in GOODS:
        quantity = int(input("enter quantity: "))
        if basket !=[]:
            for i in basket:
                if i[0] == name:
                    i[2] += quantity
                else:
                    basket.append([name, GOODS[name], quantity])
        else:
            basket.append([name, GOODS[name], quantity])
        display_basket()
    else:
        print("this good is not in the shop")
        
# Function to display basket
def display_basket():
    print("\n--- Your basket ---")
    for item in basket:
        print(f"{item[0]} - {item[2]} x {item[1]} {CURRENCY}")


# print(GOODS.items())

# Loop for
while True:
    display_menu()
    menu_choise = int(input("choise an option:"))
    if menu_choise == 1:
        display_goods()
        add_to_basket()
        
    elif menu_choise == 2:
        display_basket()
    elif menu_choise == 3:
        total = 0
        for item in basket:
            total += item[1] * int(item[2])
        display_basket()    
        print(f"Total price: {total} {CURRENCY}")
    elif menu_choise == 4:
        display_basket()
        name = input("enter name: ").lower()
        for item in basket:
            if item[0] == name:
                quantity = int(input("Choose quantity (0 to fully remove the item): "))
                if quantity == 0:
                    basket.remove(item)
                    print("good removed")
                else:
                    item[2] = quantity
                break
        display_basket()
    elif menu_choise == 5:
        break
