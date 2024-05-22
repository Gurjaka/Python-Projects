CURRENCY = "GEL"

goods ={
        "1":{"Banana":
            [7,"kg","mon",0.1]}, 
        "2":{"Apple":
            [5,"kg","mon",0.2]}, 
        "3":{"Strawberry":
            [3.8,"kg","wed",0.15]}, 
        "4":{"Peach":
             [4.3,"kg","wed",0.2]}, 
        "5":{"Grapes": 
             [32,"kg","sun",0.5]},
        "6":{"Tomato": 
             [1.4,"kg","sun",0.29]}, 
        "7":{"Cucumber": 
             [1.34,"kg","thu",0.80]}, 
        "8":{"Pepper": 
             [0.4,"kg","thu",0.15]},
        }


def print_menu():
    for num, elem in goods.items():
        for name, infos in elem.items():
            print(f"{num}. {name} - {infos[0]} {CURRENCY}.")


def count_total():
    pass

def choose_elem():
    elem = input("Choose item: ")
    quantity = int(input("Choose quantity: "))
    price = goods[elem[1]] * quantity
    return price

while True:
    print_menu()
    choose_elem()