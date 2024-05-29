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

goods_dict = {'Apple': 5.0, 
            'Banana': 2.0, 
            'Orange': 3.4, 
            'Mango': 8.6, 
            'Grape': 3.0, 
            'Watermelon': 6.6, 
            'Strawberry': 5.0, 
            'Pineapple': 9.0, 
            'Blueberry': 12.0, 
            'Kiwi': 6.0, 
            'Peach': 7.0, 
            'Pear': 8.6, 
            'Coconut': 23.0, 
            'Avocado': 15.0, 
            'Dragonfruit': 40.0, 
            'Durian': 54.0, 
            'Fig': 32.0, 
            'Lemon': 12.0, 
            'Cherry': 1.0, 
            'Grapefruit': 2.5}

MENU_ITEMS = {
    "1": "Add goods to basket", 
    "2": "Edit your basket",
    "3": "Get total and proceed to checkout",
    "4": "Exit"
    }

basket = {}
    

def menu_goods():
    for name,price in goods_dict.items():
        print(f"{name}: {price} GEL")

def add_to_basket():
    global basket
    while True:
        print(basket)
        good = input("Type name of good to add to basket (type 0 to exit): ")
        if good == "0":
            break
        else:
            quantity = int(input("Choose the quantity: "))
            basket.update({good:goods_dict[good]*quantity})
    

def edit_basket():
    global basket
    while True:
        print(basket)
        good_to_remove = input("Choose good to remove (type 0 to exit): ")
        if good_to_remove == "0":
            break
        elif good_to_remove in basket:
            basket.pop(good_to_remove)
            print(basket)
            continue
        else:
            print("Not in basket")
            continue

def total():
    print(basket.values)
        

print("Hello welcome to our store!")


while True:
    for key,value in MENU_ITEMS.items():
        print(key,value)
    operation = input("Choose your operation: ")
    if operation.lower() in ("1" or "add goods to your basket"):
        menu_goods()
        add_to_basket()
    elif operation.lower() in ("2" or "edit your basket"):
        edit_basket()
    