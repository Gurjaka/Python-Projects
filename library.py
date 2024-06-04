#gen ID like LIB00023 where firss section "LIB" last 5 chars is numer in five chars
reg_users= {}


last_id = 0
id_string ="LIB"
menu_items ={"1":"add user","x":"exit"}

def gen_id():
    global last_id
    if last_id==99999:
        return None
    else:
        new_id = id_string+f"{last_id+1:0>{5}}"
        last_id+=1
        return new_id

def menu_list():
    for key, value in menu_items.items():
        print(f"{key}) {value} ")
    
    # pass

def collect_info():
    name = input("Input name: ")
    surname = input("Input surname: ")
    phone_number = input("Input phone number: ")
    birthday = input("Input birthday (DD/MM/YY): ")
    piradi_nomeri = input("Input your P/N: ")
    paid_membership = input('Do you want to get the paid membership?\nif "yes" - you will be able to bring the book with you, outside the library\nif "no" - you can only read the book in the library.\nChoose your answer (yes or no): ').lower()
    user_info =[name,surname,phone_number,birthday,piradi_nomeri,paid_membership]
    return user_info
   

# main_code
while True:
    menu_list()
    menu_elem = input("enter menu elem : ")
    if menu_elem.lower() == "x":
        break
    elif menu_elem == "1":
        lib_id = gen_id()
        user_info = collect_info()
        reg_users.setdefault(lib_id,user_info)
    for key, value in reg_users.items():
         print(key,value)
