distribute = ["Apple",
            "Banana",
            "Orange",
            "Mango", 
            "Grape", 
            "Watermelon", 
            "Strawberry", 
            "Pineapple", 
            "Blueberry", 
            "Kiwi",
            "Peach", 
            "Pear", 
            "Coconut", 
            "Avocado", 
            "Dragonfruit", 
            "Durian", 
            "Fig", 
            "Lemon", 
            "Cherry", 
            "Grapefruit"]

# goods = {}

# for i in distribute:
#     print(i)
#     price = float(input("Input price for fruit: "))
#     goods.update({i:price})
# print(goods)

goods_dict = {'apple': 5.0, 
            'banana': 2.0, 
            'orange': 3.4, 
            'mango': 8.6, 
            'grape': 3.0, 
            'watermelon': 6.6, 
            'strawberry': 5.0, 
            'pineapple': 9.0, 
            'blueberry': 12.0, 
            'kiwi': 6.0, 
            'peach': 7.0, 
            'pear': 8.6, 
            'coconut': 23.0, 
            'avocado': 15.0, 
            'dragonfruit': 40.0, 
            'durian': 54.0, 
            'fig': 32.0, 
            'lemon': 12.0, 
            'cherry': 1.0, 
            'grapefruit': 2.5}

MENU_ITEMS = {
    "1)": "Add goods to basket", 
    "2)": "Edit your basket",
    "3)": "Get total and proceed to checkout",
    "4)": "Exit"
    }

basket = []
    
total = 0

def menu_goods():
    print("\n----- Available Goods -----\n")
    for name,price in goods_dict.items():
        print(f"{name.capitalize()}: {price} GEL")

def display_basket():
    print("\n----- Your Basket -----\n")
    for item in basket:
        print(f"{item[0]} - {item[2]} x {item[1]} GEL")

def add_to_basket():
    global basket
    while True:
        display_basket()
        good = input("\nType name of good to add to basket (type 0 to exit): ")
        if good == "0":
            break
        elif good != "0" and good.lower() in goods_dict:
            quantity = int(input("\nChoose the quantity: "))
            found = False  # Flag to track if item found in basket
            for i in basket:
                if i[0] == good.capitalize():
                    i[2] += quantity  # Update quantity if item already exists
                    found = True
                    break
            if not found:
                basket.append([good.capitalize(), goods_dict[good], quantity])
        else:
            print("\nGood not available")

def edit_basket():
    global basket
    while True:
        display_basket()
        name = input("\nenter name (type 0 to exit): ").lower()
        if name == "0":
            break
        else:
            for item in basket:
                if item[0] == name.capitalize():
                    quantity = int(input("\nChoose quantity (0 to fully remove the item): "))
                    if quantity == 0:
                        basket.remove(item)
                        print("good removed")
                    else:
                        item[2] = quantity
                    break

def checkout():
    global total
    for item in basket:
        total += item[1] * int(item[2])
    pay_method = input(f"\nYour total is - {total}. Will you pay in cash or credit card? ")
    if pay_method.lower() == "cash":
        print("\nHere is your check.")
        print(check())
        print("see you another time.")
    elif pay_method.lower() == "credit card":
        print("\nPlease tap on the terminal.")
        import time
        time.sleep(2)
        print("Your pay was succesful.")
        print(check())
        print("see you another time.")

def check():
    print("----- Your check -----")
    for item in basket:
        print(f"{item[0]} - {item[2]} x {item[1]} GEL")

print("\n----- Hello welcome to our store! -----\n")


while True:
    for key,value in MENU_ITEMS.items():
        print("\n",key,value)
    operation = input("\nChoose your operation: ")
    if operation.lower() in ("1" or "add goods to your basket"):
        menu_goods()
        add_to_basket()
        display_basket()
    elif operation.lower() in ("2" or "edit your basket"):
        display_basket()
        edit_basket()
    elif operation.lower() in ("3" or "get total and proceed to checkout"):
        checkout()
        break
    elif operation.lower() in ("4" or "exit"):
        print("\nSee you another time!")
        break
    else:
        print("\nOperation not found!")
        continue